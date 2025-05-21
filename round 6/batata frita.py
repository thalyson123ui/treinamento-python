import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Round 6: Batatinha Frita 1, 2, 3")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Fontes
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Variáveis do jogo
player_x = 100
player_y = SCREEN_HEIGHT - 100
player_speed = 5
player_size = 30
player_color = GREEN

doll_state = "RUN"  # Pode ser "RUN" (correr) ou "STOP" (parar)
game_over = False
win = False

# Temporizadores para a boneca
run_time = random.uniform(2, 5)  # Tempo para correr
stop_time = random.uniform(1, 3) # Tempo para parar
timer_start = pygame.time.get_ticks()

# Posição da linha de chegada
finish_line_x = SCREEN_WIDTH - 150

# Sons (se você tiver arquivos .wav)
# pygame.mixer.music.load('batatinha_frita.wav') # Exemplo de música de fundo
# move_sound = pygame.mixer.Sound('move_detected.wav') # Exemplo de som de detecção

def draw_player(x, y):
    pygame.draw.circle(screen, player_color, (x, y), player_size)

def draw_doll():
    # Desenha uma representação simples da boneca
    pygame.draw.rect(screen, RED, (SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 - 50, 50, 100)) # Corpo
    pygame.draw.circle(screen, BLACK, (SCREEN_WIDTH - 75, SCREEN_HEIGHT // 2 - 70), 20) # Cabeça

def display_message(message, color=WHITE, size=74):
    text_surface = pygame.font.Font(None, size).render(message, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text_surface, text_rect)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r: # Reiniciar o jogo
                # Resetar variáveis
                player_x = 100
                game_over = False
                win = False
                doll_state = "RUN"
                run_time = random.uniform(2, 5)
                stop_time = random.uniform(1, 3)
                timer_start = pygame.time.get_ticks()

    if not game_over:
        keys = pygame.key.get_pressed()

        # Lógica de movimento do jogador
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_LEFT]:
            player_x -= player_speed

        # Limitar o movimento do jogador
        if player_x < player_size:
            player_x = player_size
        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size

        # Lógica da boneca (mudar de RUN para STOP e vice-versa)
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - timer_start) / 1000 # Convertendo para segundos

        if doll_state == "RUN":
            if elapsed_time >= run_time:
                doll_state = "STOP"
                timer_start = current_time
                stop_time = random.uniform(1, 3) # Define um novo tempo para parar
                # pygame.mixer.music.stop() # Parar a música "Batatinha frita"
        elif doll_state == "STOP":
            if elapsed_time >= stop_time:
                doll_state = "RUN"
                timer_start = current_time
                run_time = random.uniform(2, 5) # Define um novo tempo para correr
                # pygame.mixer.music.play(-1) # Recomeçar a música

        # Detecção de movimento quando a boneca está "STOP"
        if doll_state == "STOP" and (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            game_over = True
            win = False
            player_color = RED # Mudar cor do jogador para indicar derrota
            # if move_sound: move_sound.play()

        # Condição de vitória
        if player_x >= finish_line_x:
            game_over = True
            win = True

    # Desenha tudo
    screen.fill(BLACK) # Limpa a tela

    pygame.draw.line(screen, WHITE, (finish_line_x, 0), (finish_line_x, SCREEN_HEIGHT), 5) # Linha de chegada

    draw_player(player_x, player_y)
    draw_doll()

    # Exibe mensagens de estado do jogo
    if game_over:
        if win:
            display_message("VOCÊ VENCEU!", GREEN)
        else:
            display_message("GAME OVER!", RED)
        display_message("Pressione 'R' para Reiniciar", WHITE, 30) # Mensagem de reiniciar
    else:
        if doll_state == "RUN":
            display_message("CORRA!", GREEN, 40)
        else:
            display_message("PARE!", RED, 40)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros (FPS)
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()