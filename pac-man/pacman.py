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

# Configurações do Pac-Man
pacman_pos = [LARGURA // 2, ALTURA // 2]
pacman_vel = 5
pacman_raio = 20

# Loop principal
clock = pygame.time.Clock()

def desenhar_pacman(tela, pos, raio):
    pygame.draw.circle(tela, AMARELO, pos, raio)

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

        # Atualização da tela
        TELA.fill(PRETO)
        desenhar_pacman(TELA, pacman_pos, pacman_raio)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()