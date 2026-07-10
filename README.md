# Street_of_Treta

Esse é o Street of Treta, um Pedra-Papel-Tesoura com RPG leve (níveis, ataque, poções) jogado pelo navegador. Esse jogo já foi desenvolvido em C, porém não foi publicado.

Esse jogo foi criado por Bruno Galhoto e Joabe Matos e desenvolvido por mim, Taynara Diniz.

### Como rodar

```
pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000` no navegador.

### Persistência e login

O progresso dos personagens é salvo em um banco **SQLite** (`street_of_treta.db`, criado automaticamente na primeira execução, não versionado no git). Cada usuário se cadastra com usuário/senha (senha nunca é salva em texto puro — hash com salt via `hashlib.pbkdf2_hmac`) e tem sua própria progressão dos 14 personagens, isolada da de outros usuários.

A sessão de login agora é uma sessão web de verdade, via cookie assinado do Flask (`flask.session`) — cada aba/navegador tem seu próprio usuário autenticado, sem depender de nenhum estado guardado em memória do servidor.

> Nota: `app.secret_key` usa uma chave de desenvolvimento fixa como fallback (variável de ambiente `SECRET_KEY`). Antes de qualquer deploy público, defina uma chave secreta real via variável de ambiente. Não há proteção CSRF nos formulários — aceitável para uso local, mas vale considerar antes de expor a aplicação publicamente.

### Estrutura do projeto

- [`db.py`](db.py) — toda a camada de banco de dados: cadastro/autenticação de usuários e CRUD dos personagens. Não sabe nada sobre HTML ou regras de combate.
- [`jogo.py`](jogo.py) — a lógica de combate, pura (sem banco, sem HTTP): calcula dano, bônus de combo, uso de poção e subida de nível a partir de objetos `Personagem` recebidos por parâmetro.
- [`app.py`](app.py) — a aplicação Flask: rotas HTTP, sessão do usuário logado, e a "cola" entre `db.py` e `jogo.py`.
- `templates/` — páginas HTML (Jinja2): login, cadastro, instruções, lista de personagens, batalha e resultado.
- `static/style.css` — estilo básico das páginas.
- `static/personagens/`, `static/jogadas/` — imagens dos personagens e de Pedra/Papel/Tesoura, redimensionadas (320×320 e 128×128) a partir da arte original em `image/` (pasta local, fora do git — ver `.gitignore`) para manter o carregamento das páginas rápido.

### Rotas principais

| Rota | Método | O que faz |
|---|---|---|
| `/login`, `/cadastro` | GET/POST | Autenticação e criação de conta |
| `/logout` | GET | Encerra a sessão |
| `/instrucoes` | GET | Regras do jogo (pode ser acessada a qualquer momento) |
| `/personagens` | GET | Lista os 14 personagens do usuário e permite escolher quem vai batalhar |
| `/personagens/resetar` | POST | Reseta o progresso do usuário para os valores iniciais |
| `/batalha/iniciar` | POST | Escolhe o personagem do jogador e começa uma partida contra a CPU |
| `/batalha` | GET | Mostra o estado da rodada atual e o formulário de jogada |
| `/batalha/jogar` | POST | Resolve uma rodada de Pedra/Papel/Tesoura |
| `/batalha/pocao` | POST | Usa ou não uma poção quando oferecida |
| `/batalha/resultado` | GET | Mostra quem venceu, aplica subida de nível e encerra a partida |

O estado de uma batalha em andamento (quem está lutando, contadores de combo/empate) fica só na sessão do usuário — os personagens em si (vida, nível, poções) sempre vêm do banco a cada requisição, para que dois usuários jogando ao mesmo tempo nunca compartilhem estado.

**O oponente da CPU é sempre sorteado** (`jogo.gerar_cpu`) com status próprio, independente do roster do usuário — nunca uma das 14 linhas salvas no banco. Isso evita duas inconsistências: a CPU vencer e o usuário "ganhar" um personagem mais forte, ou a CPU perder e o usuário "perder" um personagem seu. Só o personagem do jogador é salvo/sobe de nível ao fim da partida; o da CPU é descartado.

### Um pouco sobre as funções (`jogo.py`)

#### `calcular_bonus_ataque(contador)`:
* Calcula o bônus de dano por vitórias consecutivas: +1 na 2ª vitória seguida, +10 da 3ª em diante.
#### `aplicar_ataque(atacante, defensor, contador)`:
* Aplica o dano ao personagem defensor e retorna as mensagens correspondentes (bônus de ataque, vida restante).
#### `resetar_combo(personagem, contador)`:
* Zera o contador de vitórias consecutivas, retornando a mensagem de aviso quando o ataque volta ao valor normal.
#### `pode_usar_pocao(personagem, oponente)` / `usar_pocao(personagem)`:
* Verificam se a poção pode ser oferecida (vida < 25, tem poção, oponente vivo) e aplicam a cura de 15 pontos.
#### `tentar_usar_pocao_cpu(cpu, oponente)`:
* Decide automaticamente (50% de chance) se a CPU usa uma poção quando possível.
#### `jogar_rodada(jogador, cpu, jogada_jogador, contadores)`:
* Resolve uma rodada completa: sorteia a jogada da CPU, decide vitória/empate/derrota, aplica ataque e poção, e devolve um dicionário com as mensagens, o resultado e se a batalha terminou.
#### `atualizar_vida(personagens)` / `atualizar_atack(personagens)` / `atualizar_pocao(personagens)`:
* Recalculam vida/ataque/poção de acordo com o nível de cada personagem.
#### `subir_nivel(personagens)`:
* Sobe o nível de quem tiver vitórias suficientes e aplica as atualizações acima.

### Regras do jogo

* Os personagens começam no nível 1 (vida 50, ataque 5, 2 poções).
* Ganhar 2x seguidas soma +1 no ataque; ganhar 3x seguidas soma +10. Perder ou empatar reseta o bônus.
* Empatar 3x seguidas tira 5 pontos de vida de ambos.
* Poção cura 15 pontos e só pode ser usada com vida abaixo de 25.
* A cada nível, vida +5 e ataque +1; a cada 2 níveis, poção +1.
* Sobreviver a `nível + 1` batalhas avança um personagem de nível.
