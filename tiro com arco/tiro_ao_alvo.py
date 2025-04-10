
import pygame
import random
import math
import time

# Inicialização
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tiro ao Alvo 🎯")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Fonte
font = pygame.font.SysFont("Arial", 28)

# Sons (mock, sem som real no ambiente offline)
def play_shoot_sound():
    pass  # placeholder

def play_hit_sound():
    pass  # placeholder

# Alvo
class Target:
    def __init__(self):
        self.radius = 30
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.color = RED
        self.speed = 2

    def move(self):
        self.x += random.choice([-1, 1]) * self.speed
        self.y += random.choice([-1, 1]) * self.speed

        # Manter na tela
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# Partícula de tiro
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 10

    def update(self):
        self.life -= 1

    def draw(self, win):
        if self.life > 0:
            pygame.draw.circle(win, YELLOW, (self.x, self.y), 5)

# Funções auxiliares
def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

# Jogo
def run_game():
    clock = pygame.time.Clock()
    target = Target()
    bullets = []
    score = 0
    lives = 5
    game_time = 30  # segundos
    start_time = time.time()

    running = True
    while running:
        clock.tick(60)
        elapsed = time.time() - start_time
        win.fill(WHITE)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Disparo
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                bullets.append(Bullet(mx, my))
                play_shoot_sound()
                if distance(mx, my, target.x, target.y) < target.radius:
                    score += 1
                    play_hit_sound()
                    target = Target()
                else:
                    lives -= 1

        # Atualizações
        target.move()
        target.speed = 2 + score * 0.2  # dificuldade aumenta

        for b in bullets:
            b.update()
        bullets = [b for b in bullets if b.life > 0]

        # Desenho
        target.draw(win)
        for b in bullets:
            b.draw(win)

        # HUD
        time_left = max(0, int(game_time - elapsed))
        hud = font.render(f"Pontos: {score}  Vidas: {lives}  Tempo: {time_left}s", True, BLACK)
        win.blit(hud, (20, 20))

        pygame.display.update()

        # Fim do jogo
        if lives <= 0 or elapsed >= game_time:
            running = False

    # Tela final
    win.fill(WHITE)
    msg = font.render(f"Fim de jogo! Pontuação final: {score}", True, GREEN)
    win.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(4000)

    pygame.quit()

run_game()
