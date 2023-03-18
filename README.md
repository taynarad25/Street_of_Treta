# Street_of_Treta

Esse é o Street of Treta em Python. Esse jogo já foi desenvolvido em C, porém não foi publicado.

Esse jogo foi criado por Bruno Galhoto e Joabe Matos e Desenvolvido por mim, Taynara Diniz.

Busco fazer uma interface gráfica ainda. Então aguarde por mudanças :)


### Um pouco sobre as funções:

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
#### `SOT()`:
* Aqui é onde a mágica acontece:
    * O primeiro laço de repetição *(linha 115)*, pergunta se o usuário irá continuar um jogo anterior. Se sim, ele contiua. Se não, ele atualiza os dados dos jogadores e salva.
    * O segundo laço de repetição *(linha 130)*, inicia o jogo, inicializando as váriaveis necessárias, chama a função `Escolha_personagem`.
    * Temos um segundo laço de repetições, que é necessário para contar as rodadas, esse laço para quando um dos personagens morre *(`vida <= 0`)*.
    * Em outro laço, temos as escolhas das opções. Após temos a aleatorização da escolha das opções do outro personagem.
    * Então chegamos nas condições para saber quando o usuário ganhou ou perdeu. Aqui também são definidas as regras, como, quantas vezes seguidas o personagem já ganhou, se o ataque dele foi resetado, ou se ele teve seus bônus por ganhar algumas vezes consecutivas.
    * Nas linhas 197 e  260, temos o início do uso das funções, onde nas linhas 197 à 215, é a poção do usuário. Ele pode usar a poção quando a vida está menor que 25. E tem uma quantidade certa de poção por nível. E nas linhas 260 à 269, é a aleatorização da escolha do personagem 2, ele também só pode usar a poção quando a vida está menor que 25 e tem 50% de chance dele escolher usar a poção.
    * Após um personagem morrer, o laço de repetição se encerra e mostra qual personagem morreu. Então ele chama a função *`Subir_nivel`*
    * Entra em um novo laço, para saber se o usuário deseja salvar o jogo. Se sim, ele chama a função.
    * Entra em outro laço, para saber se o usuário deseja jogar novamente. Se sim, ele continua, se não ele encerra o jogo.
#### `def Main()`:
* Função "menu", chama as funções `Inicio`, `Criar_personagens` e `SOT`.
#### `def Novo()`:
* Abre o arquivo que contem os valores iniciais e atualiza todos os personagens, substituindo os dados anteriores.
#### `def Salvar()`:
* Abre o arquivo e que contem todos os personagens e atualiza os dados.
#### `def Criar_personagens()`:
* Abre o arquivo e pega todas as informações que contem nele.
#### `def Subir_nivel()`:
* Atualiza o nível do personagem, de acordo com suas vitórias. Chama as funções de atualização do personagem.