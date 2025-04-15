import pygame
import sys

# Inicialização do pygame
pygame.init()

# Configurações principais
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pac-Man")

# Cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurações do Pac-Man
pacman_pos = [LARGURA // 2, ALTURA // 2]
pacman_vel = 5
pacman_raio = 20

# Configurações dos fantasmas
fantasmas = [
    {"pos": [100, 100], "vel": [2, 2], "raio": 20},
    {"pos": [700, 500], "vel": [-2, -2], "raio": 20},
]

# Configurações das paredes
paredes = [
    pygame.Rect(200, 150, 400, 20),
    pygame.Rect(200, 450, 400, 20),
    pygame.Rect(350, 250, 20, 200),
]

# Loop principal
clock = pygame.time.Clock()

def desenhar_pacman(tela, pos, raio):
    pygame.draw.circle(tela, AMARELO, pos, raio)

def desenhar_fantasmas(tela, fantasmas):
    for fantasma in fantasmas:
        pygame.draw.circle(tela, VERMELHO, fantasma["pos"], fantasma["raio"])

def desenhar_paredes(tela, paredes):
    for parede in paredes:
        pygame.draw.rect(tela, AZUL, parede)

def atualizar_fantasmas(fantasmas):
    for fantasma in fantasmas:
        fantasma["pos"][0] += fantasma["vel"][0]
        fantasma["pos"][1] += fantasma["vel"][1]

        # Colisão com as bordas
        if fantasma["pos"][0] - fantasma["raio"] <= 0 or fantasma["pos"][0] + fantasma["raio"] >= LARGURA:
            fantasma["vel"][0] *= -1
        if fantasma["pos"][1] - fantasma["raio"] <= 0 or fantasma["pos"][1"] + fantasma["raio"] >= ALTURA:
            fantasma["vel"][1] *= -1

def colisao_paredes(pacman_pos, paredes):
    for parede in paredes:
        if parede.collidepoint(pacman_pos[0], pacman_pos[1]):
            return True
    return False

def main():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimentação do Pac-Man
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            pacman_pos[1] -= pacman_vel
        if keys[pygame.K_DOWN]:
            pacman_pos[1] += pacman_vel
        if keys[pygame.K_LEFT]:
            pacman_pos[0] -= pacman_vel
        if keys[pygame.K_RIGHT]:
            pacman_pos[0] += pacman_vel

        # Verificar colisão com paredes
        if colisao_paredes(pacman_pos, paredes):
            pacman_pos = [LARGURA // 2, ALTURA // 2]  # Resetar posição

        # Atualizar fantasmas
        atualizar_fantasmas(fantasmas)

        # Atualização da tela
        TELA.fill(PRETO)
        desenhar_pacman(TELA, pacman_pos, pacman_raio)
        desenhar_fantasmas(TELA, fantasmas)
        desenhar_paredes(TELA, paredes)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
