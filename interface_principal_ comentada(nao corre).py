import pygame # Importa a biblioteca Pygame para criar a interface do jogo
import sys # Importa a biblioteca sys para lidar com a saída do programa
import random # Importa a biblioteca random para gerar números aleatórios


# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # Define as dimensões da tela
BG_COLOR = (0, 0, 0) # Define a cor de fundo da tela como preto
BUTTON_COLOR = (235, 26, 235) # Define a cor dos botões
TEXT_COLOR = (255, 255, 255) # Define a cor do texto
BOARD_COLOR = (245, 222, 179) # Define a cor do tabuleiro
BLACK_HOLE_COLOR = (0, 0, 0) # Define a cor dos buracos negros
PIECE_COLOR_WHITE = (255, 255, 255) # Define a cor das peças brancas
PIECE_COLOR_BLACK = (0, 0, 0) # Define a cor das peças pretas
BOARD_SIZE = 7 # Define o tamanho do tabuleiro
SQUARE_SIZE = 60 # Define o tamanho de cada quadrado do tabuleiro
FPS = 30 # Define a taxa de quadros por segundo
NUM_BLACK_HOLES = 5 # Define o número de buracos negros

# Definição de cores baseada na imagem fornecida
DARK_SQUARE_COLOR = (139, 69, 19) # Marron Escuro
LIGHT_SQUARE_COLOR = (245, 222, 179) # Bege Claro
BLACK_HOLE_COLOR = (0, 0, 0) # Preto para os buracos negros
WHITE_PIECE_COLOR = (255, 255, 255) # Branco para as peças brancas
BLACK_PIECE_COLOR = (0, 0, 0) # Preto para as peças pretas
SQUARE_SIZE = 60 # Tamanho de cada quadrado do tabuleiro
PIECE_RADIUS = SQUARE_SIZE // 2 - 10 # Raio da peça, um pouco menos que metade do tamanho do quadrado
 # Margem para que o buraco negro não ocupe o quadrado inteiro
BLACK_HOLE_SIZE = SQUARE_SIZE 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Cria a janela do jogo com as dimensões especificadas
pygame.display.set_caption("Pathum Game-Computer vs Computer") # Define o título da janela do jogo

# Define as fontes para o texto na tela
font_path = pygame.font.Font(None, 60)
font_button = pygame.font.Font(None, 40)

class PathumGame: # Classe que representa o jogo
 def __init__(self):
 self.board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
 self.current_turn = 'black'
 self.add_black_holes(NUM_BLACK_HOLES)
 self.move_log = []

 def undo_move(self):
 if self.move_log:
 last_move, last_player = self.move_log.pop()
 x, y = last_move
 self.board[y][x] = '' # Limpa o movimento
 self.current_turn = last_player # Restaura o turno
 def winner(self):
 if self.is_game_over():
 points_white = self.calculate_points("White")
 points_black = self.calculate_points("Black")
 if points_white > points_black:
 return "White"
 elif points_white < points_black:
 return "Black"
 else:
 return 'draw'
 return None

 def calculate_points(self, player):
 # Calcula os pontos para o jogador fornecido
 points = 0
 for y in range(BOARD_SIZE):
 for x in range(BOARD_SIZE):
 if self.board[y][x] == player.lower(): # Assegure que a comparação de strings está correta
 line_points = self.points_for_line(x, y)
 points += line_points

 return points

 def points_for_line(self, x, y):
 # Calcula os pontos para uma linha a partir de uma posição dada
 points_table = {1: 0, 2: 0, 3: 3, 4: 10, 5: 25, 6: 56, 7: 119}
 horizontal_count = 1
 for i in range(1, BOARD_SIZE - x):
 if self.board[y][x + i] == self.board[y][x]:
 horizontal_count += 1
 else:
 break
 for i in range(1, x + 1):
 if x - i >= 0 and self.board[y][x - i] == self.board[y][x]:
 horizontal_count += 1
 else:
 break
 
 vertical_count = 1
 for i in range(1, BOARD_SIZE - y):
 if self.board[y+i][x] == self.board[y][x]:
 vertical_count += 1
 else:
 break
 for i in range(1, y + 1):
 if y - i >= 0 and self.board[y - i][x] == self.board[y][x]:
 vertical_count += 1
 else:
 break
 points = points_table.get(horizontal_count,0) + points_table.get(vertical_count,0)
 return points


 def add_black_holes(self, num_black_holes):
 added = 0
 while added < num_black_holes:
 x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
 if self.board[y][x] == '':
 self.board[y][x] = 'BH'
 added += 1

 def get_legal_moves(self):
 return [(x, y) for y in range(BOARD_SIZE) for x in range(BOARD_SIZE) if self.board[y][x] == '']

 def make_move(self, move):
 x, y = move
 if self.board[y][x] == '':
 self.board[y][x] = self.current_turn
 self.current_turn = 'black' if self.current_turn == 'white' else 'white'
 # Adicionar a jogada ao log de movimentos, se você estiver mantendo um
 self.move_log.append((move, self.current_turn))

 def is_game_over(self):
 # Exemplo básico: o jogo termina se não houver movimentos legais
 return not self.get_legal_moves()

 def draw(self, screen):
 # Calcula o ponto inicial para centralizar o tabuleiro horizontalmente
 board_width = BOARD_SIZE * SQUARE_SIZE
 start_x = (SCREEN_WIDTH - board_width) // 2

 # Calcula o ponto inicial para centralizar o tabuleiro verticalmente
 board_height = BOARD_SIZE * SQUARE_SIZE
 start_y = (SCREEN_HEIGHT - board_height) // 2

 for y in range(BOARD_SIZE):
 for x in range(BOARD_SIZE):
 # Alternar entre cores claras e escuras para o tabuleiro
 color = LIGHT_SQUARE_COLOR if (x + y) % 2 == 0 else DARK_SQUARE_COLOR
 rect_x = start_x + x * SQUARE_SIZE
 rect_y = start_y + y * SQUARE_SIZE
 pygame.draw.rect(screen, color, pygame.Rect(rect_x, rect_y, SQUARE_SIZE, SQUARE_SIZE))
 
 # Desenhar as peças e os buracos negros
 center_x = rect_x + SQUARE_SIZE // 2
 center_y = rect_y + SQUARE_SIZE // 2
 if self.board[y][x] == 'white':
 pygame.draw.circle(screen, WHITE_PIECE_COLOR, (center_x, center_y), PIECE_RADIUS)
 elif self.board[y][x] == 'black':
 pygame.draw.circle(screen, BLACK_PIECE_COLOR, (center_x, center_y), PIECE_RADIUS)
 elif self.board[y][x] == 'BH':
 pygame.draw.rect(screen, BLACK_HOLE_COLOR, (rect_x, rect_y, BLACK_HOLE_SIZE, BLACK_HOLE_SIZE))

 
 def _init_(self):
 self.board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
 self.current_turn = 'white'
 self.move_log = [] # Log de movimentos para facilitar o undo
 self.add_black_holes(NUM_BLACK_HOLES)

def minimax(game, depth, alpha, beta, maximizing_player): # Esta função implementa o algoritmo minimax com poda alfa-beta para determinar o melhor movimento para um jogador em um dado estado do jogo.
 
 if depth == 0 or game.is_game_over():
 return evaluate_board(game, game.current_turn), None

 if maximizing_player:
 max_eval = float('-inf')
 best_move = None
 for move in game.get_legal_moves():
 game.make_move(move)
 eval = minimax(game, depth - 1, alpha, beta, False)[0]
 game.undo_move()
 if eval > max_eval:
 max_eval = eval
 best_move = move
 alpha = max(alpha, eval)
 if beta <= alpha:
 break
 return max_eval, best_move
 else:
 min_eval = float('inf')
 best_move = None
 for move in game.get_legal_moves():
 game.make_move(move)
 eval = minimax(game, depth - 1, alpha, beta, True)[0]
 game.undo_move()
 if eval < min_eval:
 min_eval = eval
 best_move = move
 beta = min(beta, eval)
 if beta <= alpha:
 break
 return min_eval, best_move
def clone_game(game): #Esta função cria uma cópia profunda (deep copy) do estado atual do jogo.
 import copy
 # Clona o estado do jogo usando deepcopy para copiar o tabuleiro e outros atributos
 cloned_game = copy.deepcopy(game)
 return cloned_game

def evaluate_board(game, player): #Esta função avalia o tabuleiro atual e atribui uma pontuação ao jogador com base nas regras e heurísticas do jogo.
 # Pontuação baseada nas regras oficiais do jogo
 points = game.calculate_points(player)

 # Heurísticas para adicionar à avaliação
 center_bonus = 3 # Pontos extras para peças no centro
 block_bonus = 2 # Pontos extras por bloqueio
 victory_threshold = 100 # Limite de pontuação para considerar estar "próximo da vitória"

 for y in range(BOARD_SIZE):
 for x in range(BOARD_SIZE):
 if game.board[y][x] == player:
 line_points = game.points_for_line(x, y)
 points += line_points
 # Heurística de controle do centro
 if x == BOARD_SIZE // 2 or y == BOARD_SIZE // 2:
 points += center_bonus
 # Heurística de bloqueio (simplificada para exemplo)
 if (x > 0 and game.board[y][x-1] != player and game.board[y][x-1] != '') or \
 (x < BOARD_SIZE - 1 and game.board[y][x+1] != player and game.board[y][x+1] != ''):
 points += block_bonus

 # Heurística de Avaliação Dinâmica
 if points >= victory_threshold:
 points *= 1.1 # Aumentar a pontuação em 10% se estiver muito próximo da vitória

 return points

def monte_carlo(game, simulations): #Esta função implementa o método de Monte Carlo para simular vários jogos e avaliar os movimentos possíveis.
 game.current_turn = "white"
 best_move = None
 best_score = float('-inf')

 legal_moves = game.get_legal_moves()
 for move in legal_moves:
 total_score = 0
 for _ in range(simulations):
 cloned_game = clone_game(game)
 cloned_game.make_move(move)
 while not cloned_game.is_game_over():
 cloned_game.make_move(random.choice(cloned_game.get_legal_moves()))
 total_score += evaluate_board(cloned_game, cloned_game.current_turn)
 average_score = total_score / simulations
 if average_score > best_score:
 best_score = average_score
 best_move = move
 return best_move

def play_turn(game, game_type): #Esta função decide o próximo movimento com base no tipo de jogo e no jogador atual.
 if game.current_turn == 'white':
 if game_type == "Expert vs Average" or game_type == "Expert vs Beginner":
 move = monte_carlo(game, 10) 
 else: # Average vs Beginner
 move = minimax(game, depth=4, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)[1]
 else: # turn is black
 if game_type == "Expert vs Beginner" or game_type == "Average vs Beginner":
 move = random_move(game)
 else: # Expert vs Average
 move = minimax(game, depth=4, alpha=float('-inf'), beta=float('inf'), maximizing_player=False)[1]

 if move is not None:
 game.make_move(move)

def random_move(game): #Esta função retorna um movimento aleatório válido.
 return random.choice(game.get_legal_moves()) if game.get_legal_moves() else None

def display_winner_and_scores(winner, white_points, black_points): #Esta função exibe o vencedor e os pontos na tela após o término do jogo.
 # Configura a fonte
 font = pygame.font.Font(None, 36)

 # Cria o texto
 winner_text = font.render(f"Winner: {winner}", True, TEXT_COLOR)
 scores_text = font.render(f"Scores - White: {white_points}, Black: {black_points}", True, TEXT_COLOR)

 # Posição do texto
 winner_rect = winner_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
 scores_rect = scores_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))

 # Desenha um fundo para o texto
 pygame.draw.rect(screen, BG_COLOR, winner_rect.inflate(20, 10)) # Infla um pouco para o fundo
 pygame.draw.rect(screen, BG_COLOR, scores_rect.inflate(20, 10)) # Infla um pouco para o fundo

 # Desenha o texto na tela
 screen.blit(winner_text, winner_rect)
 screen.blit(scores_text, scores_rect)

 # Atualiza a tela para mostrar o texto
 pygame.display.flip()

 # Espera para que o jogador possa ver os resultados
 pygame.time.delay(5000)
def game_loop(game_type): #Esta função representa o loop principal do jogo, onde o jogo é atualizado, desenhado na tela e verificado se terminou.
 game = PathumGame()
 running = True
 clock = pygame.time.Clock() # Para controlar a taxa de atualização
 white_turn = True # Inicialmente, é a vez das peças brancas
 while running:
 for event in pygame.event.get():
 if event.type == pygame.QUIT:
 running = False

 if game.current_turn == 'white':
 if game_type == "Average vs Beginner":
 move = minimax(game, depth=4, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)[1]
 elif game_type == "Expert vs Average":
 move = monte_carlo(game, 100)
 elif game_type == "Expert vs Beginner":
 move = monte_carlo(game, 100)
 else: # turn is black
 if game_type == "Average vs Beginner":
 move = random_move(game)
 elif game_type == "Expert vs Average":
 move = minimax(game, depth=4, alpha=float('-inf'), beta=float('inf'), maximizing_player=False)[1]
 elif game_type == "Expert vs Beginner":
 move = random_move(game)
 if move:
 game.make_move(move)
 

 screen.fill((255, 255, 255)) # Limpa a tela com cor branca
 game.draw(screen) # Desenha o estado atual do jogo
 pygame.display.flip() # Atualiza a tela

 if game.is_game_over(): 
 winning_player = game.winner()
 white_points = game.calculate_points("White")
 black_points = game.calculate_points("Black")

 # Exibir os resultados
 print(f"Winner: {winning_player} - White: {white_points}, Black: {black_points}")

 # Aqui você pode chamar a função para exibir o texto na tela usando pygame, 
 # semelhante à função display_winner_and_scores() que foi fornecida anteriormente.
 display_winner_and_scores(winning_player, white_points, black_points)# Verifica se o jogo terminou
 running = False

 clock.tick(60) # Mantém o jogo rodando a 60 quadros por segundo

 pygame.quit()
 sys.exit()


def main_menu(): #Esta função exibe o menu principal do jogo, onde o jogador pode escolher o tipo de jogo.
 running = True
 while running:
 screen.fill(BG_COLOR)
 title_text = font_path.render("Pathum Game-Computer vs Computer", True, TEXT_COLOR)
 screen.blit(title_text, (SCREEN_WIDTH / 2 - title_text.get_width() / 2, 50))

 mouse_x, mouse_y = pygame.mouse.get_pos()
 buttons = ['Expert vs Average', 'Expert vs Beginner', 'Average vs Beginner']
 y_offset = 150
 for index, button_text in enumerate(buttons):
 button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, y_offset, 300, 50)
 if button_rect.collidepoint(mouse_x, mouse_y):
 pygame.draw.rect(screen, BUTTON_COLOR, button_rect) # Preencher botão se o mouse estiver sobre ele
 else:
 pygame.draw.rect(screen, BUTTON_COLOR, button_rect, 2) # Desenhar borda do botão se o mouse não estiver sobre ele

 text_surface = font_button.render(button_text, True, TEXT_COLOR)
 screen.blit(text_surface, (button_rect.x + (button_rect.width - text_surface.get_width()) / 2,
 button_rect.y + (button_rect.height - text_surface.get_height()) / 2))
 y_offset += 100

 for event in pygame.event.get():
 if event.type == pygame.QUIT:
 running = False
 elif event.type == pygame.MOUSEBUTTONDOWN:
 for i, button_text in enumerate(buttons):
 button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, 150 + i * 100, 300, 50)
 if button_rect.collidepoint(event.pos):
 game_loop(button_text) # Chamar game_loop com o texto do botão como argumento

 pygame.display.flip()

if __name__ == "__main__": #Esta linha chama a função main_menu() quando o script é executado diretamente.
 main_menu()