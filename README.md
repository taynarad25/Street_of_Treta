# Street_of_Treta

Esse é o Street of Treta em Python. Esse jogo já foi desenvolvido em C, porém não foi publicado.

Esse jogo foi criado por Bruno Galhoto e Joabe Matos e Desenvolvido por mim, Taynara Diniz.

Busco fazer uma interface gráfica ainda. Então aguarde por mudanças :)

### Persistência e login

O progresso dos personagens é salvo em um banco **SQLite** (`street_of_treta.db`, criado automaticamente na primeira execução, não versionado no git). Cada usuário se cadastra com usuário/senha (senha nunca é salva em texto puro — usa hash com salt via `hashlib.pbkdf2_hmac`) e passa a ter sua própria progressão dos 14 personagens, isolada da de outros usuários. Toda a camada de banco fica em [`db.py`](db.py); o jogo em si (`Street_of_Treta.py`) não executa SQL diretamente.

"Sessão de login" aqui significa apenas: o usuário autenticado fica ativo em memória durante aquela execução do script. Não há tokens de sessão persistentes — não faria sentido para um jogo de terminal de processo único.

### Um pouco sobre as funções:

#### `def Login()`:
* Menu inicial (Entrar / Cadastrar / Sair). Autentica ou cria um usuário via `db.py` e retorna o `usuario_id` que será usado no restante da execução.
#### `def confirmar(pergunta)`:
* Helper usado por todo o jogo para perguntas de sim/não (aceita `sim`/`s`/`não`/`nao`/`n`, em qualquer capitalização). Repete a pergunta até receber uma resposta válida.
#### `def Inicio()`:
* Apresenta as informações do jogo, instruções para melhor entendimento.
#### `def Atualizar_vida()`:
* Calcula e atualiza a vida do personagem de acordo com seu nível. Se o personagem estiver vivo e a vida for menor que **`50 + ((nivel - 1) * 5)`**.
#### `def Atualizar_atack()`:
* Calcula e atualiza o ataque do personagem de acordo com seu nível. Se o personagem estiver vivo e o ataque for menor que **`5 + (personagem[i].nivel - 1)`**.
#### `Atualizar_pocao()`:
* Calcula e atualiza a poção do personagem de acordo com seu nível. Se o personagem estiver vivo e a poção for diferente de 2 ou a poção for menor que **`2 + (personagem[i].nivel - 1) // 2`**.
#### `def Escolha_personagem(escolha)`:
* Apresenta os personagens disponíveis e possibilita a escolha de dois desses personagens. Só é possível escolher um personagem que esteja vivo e não pode escolher o mesmo personagem duas vezes.
#### `def escolher_jogada()`:
* Apresenta o menu Pedra/Papel/Tesoura/Sair e retorna a opção escolhida pelo jogador.
#### `def calcular_bonus_ataque(contador)` e `def aplicar_ataque(atacante_idx, defensor_idx, contador)`:
* Calculam o bônus de dano por vitórias consecutivas (+1 na 2ª vitória seguida, +10 da 3ª em diante) e aplicam o dano ao personagem defensor, usados tanto quando o jogador ataca quanto quando a CPU ataca.
#### `def resetar_combo(contador, idx)`:
* Zera o contador de vitórias consecutivas de um personagem, avisando quando o ataque volta ao valor normal.
#### `def tentar_usar_pocao_jogador(idx_jogador, idx_oponente)` e `def tentar_usar_pocao_cpu(idx_cpu, idx_oponente)`:
* Quando a vida está abaixo de 25 e há poções disponíveis, oferecem o uso ao jogador (pergunta) ou decidem automaticamente pela CPU (50% de chance).
#### `def jogar_rodada(escolha, contadores)`:
* Resolve uma rodada de Pedra/Papel/Tesoura: pega a jogada do jogador e sorteia a da CPU, decide quem venceu (ou empate) e aplica ataque/poção/combo de acordo com o resultado.
#### `SOT()`:
* Aqui é onde a mágica acontece:
    * Pergunta se o usuário irá continuar um jogo anterior. Se sim, ele continua. Se não, atualiza os dados dos personagens para os valores iniciais e salva.
    * O laço principal inicia uma partida, chama `Escolha_personagem` e depois roda `jogar_rodada` repetidamente até que um dos personagens morra (`vida <= 0`).
    * Após um personagem morrer, mostra qual personagem morreu, atualiza vitórias e chama `Subir_nivel`.
    * Pergunta se o usuário deseja salvar o jogo (chama `Salvar` se sim) e se deseja jogar novamente (encerra o jogo se não).
#### `def Main()`:
* Função "menu": inicializa o schema do banco, chama `Login`, depois *`Inicio`*, *`Criar_personagens`* e *`SOT`*.
#### `def Novo()`:
* Reseta os personagens do usuário logado para os valores iniciais no banco (`db.resetar_personagens`) e atualiza a lista em memória.
#### `def Salvar()`:
* Persiste o estado atual dos personagens do usuário logado no banco (`db.salvar_personagens`).
#### `def Criar_personagens(usuario_id)`:
* Carrega do banco os 14 personagens do usuário informado (`db.carregar_personagens`) e monta os objetos `Personagem` em memória.
#### `def Subir_nivel()`:
* Atualiza o nível do personagem, de acordo com suas vitórias. Chama as funções de atualização do personagem.