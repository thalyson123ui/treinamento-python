import pygame
import math
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonte
FONT = pygame.font.SysFont("arial", 24)

# FPS
FPS = 60

# Nave
class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.radius = 10

    def draw(self, win):
        angle_rad = math.radians(self.angle)
        tip = (self.x + math.cos(angle_rad) * 15, self.y - math.sin(angle_rad) * 15)
        left = (self.x + math.cos(angle_rad + math.radians(140)) * 15,
                self.y - math.sin(angle_rad + math.radians(140)) * 15)
        right = (self.x + math.cos(angle_rad - math.radians(140)) * 15,
                 self.y - math.sin(angle_rad - math.radians(140)) * 15)
        pygame.draw.polygon(win, WHITE, [tip, left, right])

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.x %= WIDTH
        self.y %= HEIGHT

    def accelerate(self):
        angle_rad = math.radians(self.angle)
        self.velocity_x += math.cos(angle_rad) * 0.2
        self.velocity_y -= math.sin(angle_rad) * 0.2

# Tiro
class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 7
        self.radius = 3

    def update(self):
        angle_rad = math.radians(self.angle)
        self.x += math.cos(angle_rad) * self.speed
        self.y -= math.sin(angle_rad) * self.speed
        self.x %= WIDTH
        self.y %= HEIGHT

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (int(self.x), int(self.y)), self.radius)

# Asteroide
class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(15, 40)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 3)

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.x %= WIDTH
        self.y %= HEIGHT

    def draw(self, win):
        pygame.draw.circle(win, WHITE, (int(self.x), int(self.y)), self.radius)

def draw_hud(win, score):
    text = FONT.render(f"Pontuação: {score}", True, WHITE)
    win.blit(text, (10, 10))

def main():
    run = True
    clock = pygame.time.Clock()

    ship = Ship(WIDTH // 2, HEIGHT // 2)
    bullets = []
    asteroids = [Asteroid() for _ in range(5)]
    score = 0

    while run:
        clock.tick(FPS)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ship.angle += 5
        if keys[pygame.K_RIGHT]:
            ship.angle -= 5
        if keys[pygame.K_UP]:
            ship.accelerate()
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullets.append(Bullet(ship.x, ship.y, ship.angle))

        ship.update()
        ship.draw(WIN)

        for bullet in bullets[:]:
            bullet.update()
            bullet.draw(WIN)

        for asteroid in asteroids:
            asteroid.update()
            asteroid.draw(WIN)

        # Colisões
        for bullet in bullets[:]:
            for asteroid in asteroids[:]:
                dist = math.hypot(bullet.x - asteroid.x, bullet.y - asteroid.y)
                if dist < bullet.radius + asteroid.radius:
                    bullets.remove(bullet)
                    asteroids.remove(asteroid)
                    score += 10
                    break

        draw_hud(WIN, score)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()