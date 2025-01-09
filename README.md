Pahtum - read.me

Descrição: Pahtum é um jogo de estratégia para dois jogadores, representado num tabuleiro. O objetivo do jogo é criar linhas conectadas de peças na horizontal ou na vertical e marcar mais pontos que o adversário.

Funcionalidades:
● Suporte para três tipos de jogo: Utilizador 1 vs Utilizador 2, Utilizador vs Computador e Computador vs Computador.
● Três níveis de dificuldade para jogos Utilizador vs Computador: Fácil, Médio e Difícil.
● Três níveis de dificuldade para jogos Computador VS Computador : Expert vs Average , Expert vs Beginner e Beginner vs Average
● Interfacegráfica,usandoabibliotecaPygame.
● Regras do jogo implementadas para garantir que os movimentos cumprem as regras e que o vencedor seja determinado corretamente.
● Sistema de pontos para calcular o vencedor com base nas sequências horizontais e verticais das peças brancas e pretas no final do jogo.
● O tabuleiro é gerado aleatoriamente com buracos negros que impedem a colocação de pedras.

Requisitos:
● Python 3.x
● Pygame (instalável via pip install pygame)
Como Jogar
Instruções para Executar o Jogo Pygame:
    
1. Certifique-se de que o Python e o Pygame estão instalados.
2. Instale o Python: https://www.python.org/downloads/ Instale o Pygame via pip:
''bash
pip install pygame
3. Descompacte o arquivo zip em uma pasta à escolha.
4. Para que a interface_principal_user_vs_user funcione corretamente é necessário que altere os caminhos das Fonts, telas e música. Neste sentido basta substituir estes caminhos dos diretórios pelos seus:
   
tela_ajuda =
pygame.image.load("/Users/catarinadias/Desktop/trabalho_PATHUM/tela_ajuda.jpg"
)
tela1 =
pygame.image.load("/Users/catarinadias/Desktop/trabalho_PATHUM/tela1.jpg")
tela2 =
pygame.image.load("/Users/catarinadias/Desktop/trabalho_PATHUM/tela2.jpg")
tela3 =
pygame.image.load("/Users/catarinadias/Desktop/trabalho_PATHUM/tela3.jpg")
music_file_path =
"/Users/catarinadias/Desktop/trabalho_PATHUM/Subway-Surfers-Theme-Sound-Effect
.mp3"
font_path =
pygame.font.Font("/Users/catarinadias/Desktop/trabalho_PATHUM/PermanentMarker-
Regular.ttf", 40)
custom_font =
pygame.font.Font("/Users/catarinadias/Desktop/trabalho_PATHUM/PermanentMarker-
Regular.ttf",40)

 Para isso, basta carregar em cima dos ficheiros que estão dentro da pasta com o botão esquerdo do mouse e selecionar a opção copiar como caminho (ou apenas copiar).
4. Navegue até o diretório onde o script 'nome_do_jogo.py' está localizado.
5. Execute o script: python3 (nome da interface pretendida).py para iniciar o jogo. 6. Na tela inicial, clique em "Play" para iniciar o jogo.
7. Escolha o tipo de jogo entre "User1 Vs User2", "Computer Vs User" e "Computer Vs Computer”.
8. Caso escolha o tipo de jogo "User1 Vs User2”, pode começar a jogar. Se selecionar "Computer Vs User", é possível escolher o nível de dificuldade : Fácil, Médio ou Difícil.

Se escolher jogar "Computer Vs Computer”, então pode ainda escolher o nível de dificuldade : Expert vs Average , Expert vs Beginner ou Beginner vs Average
9. Durante o jogo, os jogadores alternam fazendo movimentos clicando nas casas vazias do tabuleiro.
10. O jogo termina quando o tabuleiro está completamente preenchido.
11. O jogador com mais pontos, conforme determinado pelas linhas conectadas de pedras, é declarado vencedor.

Notas:
1. Para mudar as dimensões do tabuleiro basta alterar a constante BOARD_SIZE para o valor desejado e o número de buracos negros também é possível alterar na variável NUM_BLACK_HOLES.
2. Devido à sobrecarga no sistema, optamos por dividir a nossa interface em três partes distintas:
-User 1 vs User2 (interface_principal_user_vs_user)
-User vs Computer (interface2_user_vs_computer)
-Computer vs Computer (interface3_computer_vs_computer)
Neste sentido, os seguintes botões da interface principal não funcionam: Expert vs Average, Expert vs Beginner, Average vs Beginner, Easy, Medium e Hard.
3. Para conseguir avançar nas diversas fases do jogo, o utilizador deve fazer double click nos botões disponíveis.
4. Caso o utilizador tenha dúvidas nas regras/pontuação do jogo, existe um botão “ajuda”, representado por um “?”, na interface_principal_user_vs_user.
