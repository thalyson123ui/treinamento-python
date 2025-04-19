import pygame
import random

# Inicializar o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Animação com Pygame")

# Cores
PRETO = (0, 0, 0)
CORES = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Classe para círculos animados
class Circulo:
    def __init__(self):
        self.x = random.randint(0, largura)
        self.y = random.randint(0, altura)
        self.raio = random.randint(20, 50)
        self.vel = random.randint(2, 5)
        self.cor = random.choice(CORES)

    def mover(self):
        self.x += self.vel
        if self.x - self.raio > largura:
            self.x = -self.raio
            self.y = random.randint(0, altura)
            self.vel = random.randint(2, 5)
            self.raio = random.randint(20, 50)
            self.cor = random.choice(CORES)

    def desenhar(self, superficie):
        pygame.draw.circle(superficie, self.cor, (self.x, self.y), self.raio)

# Criar uma lista de círculos
circulos = [Circulo() for _ in range(10)]

# Loop principal
rodando = True
relogio = pygame.time.Clock()

while rodando:
    tela.fill(PRETO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualiza e desenha os círculos
    for c in circulos:
        c.mover()
        c.desenhar(tela)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
