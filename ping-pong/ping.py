import pygame
import sys
import random

# Initialize Pygame
pygame.init()

WIDTH, HEIGTH = 880, 600
screnn = pygame .display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Ping Pong")

# Colors

CornflowerBlue = (100,149,237)
Lime = 	(0,255,0)

def ramdom_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

ball_speed = [3, 3]
paddle_speed = 5
boll = pygame.rect(WIDTH // 2, HEIGTH // 2, 20, 20)
player = pygame.rect(WIDTH - 20, HEIGTH // 2 - 70, 10, 140)
opponent = pygame.rect(10, HEIGTH // 2 - 70, 10, 140)
ball_color = ramdom_color()

player_score = 0
opponent_score = 0

clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

def reset_ball():
    global ball_color
    boll.x = WIDTH // 2
    boll.y = HEIGTH // 2
    ball_color = ramdom_color()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= paddle_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGTH:
        player.y += paddle_speed

    if opponent.top < boll.y:
        opponent.y += paddle_speed
    if opponent.bottom > boll.y:
        opponent.y -= paddle_speed

    boll.x += ball_speed[0]
    boll.y += ball_speed[1]

    if boll.top <= 0 or boll.bottom >= HEIGTH:
        ball_speed[1] = -ball_speed[1]

    if boll.colliderect(player) or boll.colliderect(opponent):
        ball_speed[0] = -ball_speed[0]

    if boll.left <= 0:

        player_score += 1
        reset_ball()

    if boll.right >= WIDTH:

        opponent_score += 1
        reset_ball()

    import pygame
import sys
import random

# Inicializando o pygame
pygame.init()

# Configuração da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def random_color():
    """Gera uma cor aleatória."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Variáveis do jogo
ball_speed = [3, 3]
paddle_speed = 5
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)
ball_color = random_color()

player_score = 0
opponent_score = 0

# FPS do jogo
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

def reset_ball():
    """Reseta a bola para o centro e muda sua direção e cor."""
    global ball_color
    ball.x = WIDTH // 2
    ball.y = HEIGHT // 2
    ball_color = random_color()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentos dos jogadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= paddle_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += paddle_speed

    # Movimentos do oponente (IA simples)
    if opponent.top < ball.y:
        opponent.y += paddle_speed
    if opponent.bottom > ball.y:
        opponent.y -= paddle_speed

    # Movimentos da bola
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Colisão com paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Colisão com os paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed[0] = -ball_speed[0]

    # Condições de pontuação
    if ball.left <= 0:  # Jogador marca ponto
        player_score += 1
        reset_ball()

    if ball.right >= WIDTH:  # Oponente marca ponto
        opponent_score += 1
        reset_ball()

    # Desenhar na tela
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

     # Mostrar o placar
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 2 + 20, 10))
    screen.blit(opponent_text, (WIDTH // 2 - 60, 10))

    pygame.display.flip()
    clock.tick(60)
