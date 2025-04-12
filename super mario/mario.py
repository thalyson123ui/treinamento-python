import pygame
import sys

pygame.init()

LARGURA = 800
ALTURA = 600
FPS = 60

BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

JOGADOR_LARGURA = 50
JOGADOR_ALTURA = 50
GRAVIDADE = 1
FORCA_PULO = 20
VELOCIDADE = 5

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mini Mario")
clock = pygame.time.Clock()

jogador = pygame.Rect(100, ALTURA - 150, JOGADOR_LARGURA, JOGADOR_ALTURA)
vel_y = 0
no_chao = False

chao = pygame.Rect(0, ALTURA - 100, LARGURA, 100)

rodando = True
while rodando:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.x -= VELOCIDADE
    if teclas[pygame.K_RIGHT]:
        jogador.x += VELOCIDADE
    if teclas[pygame.K_SPACE] and no_chao:
        vel_y = -FORCA_PULO

    vel_y += GRAVIDADE
    jogador.y += vel_y

    if jogador.colliderect(chao):
        jogador.y = chao.top - JOGADOR_ALTURA
        vel_y = 0
        no_chao = True
    else:
        no_chao = False

    tela.fill(BRANCO)
    pygame.draw.rect(tela, VERDE, chao)
    pygame.draw.rect(tela, VERMELHO, jogador)

    pygame.display.flip()

pygame.quit()
sys.exit()
