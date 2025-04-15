import pygame
import random

# Inicializa o Pygame
pygame.init()

# Constantes
LARGURA, ALTURA = 600, 600
TAMANHO_BLOCO = 30
FPS = 10

# Cores
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
ROXO = (160, 32, 240)
CIANO = (0, 255, 255)

# Cria tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pac-Man")

# Fonte para pontuação
fonte = pygame.font.SysFont(None, 36)

# Labirinto simples (1 = parede, 0 = espaço livre)
labirinto = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

linhas = len(labirinto)
colunas = len(labirinto[0])

# Pac-Man e Fantasmas
pacman_pos = [1, 1]
fantasmas = [
    {'pos': [5, 18], 'cor': VERMELHO},
    {'pos': [1, 18], 'cor': VERDE},
    {'pos': [5, 1], 'cor': ROXO},
    {'pos': [3, 10], 'cor': CIANO},
]

# Pontos do jogo
pontos = set()
for y in range(linhas):
    for x in range(colunas):
        if labirinto[y][x] == 0:
            pontos.add((y, x))

pontuacao = 0

# Funções de utilidade
def desenhar_labirinto():
    for y in range(linhas):
        for x in range(colunas):
            if labirinto[y][x] == 1:
                pygame.draw.rect(tela, AZUL, (x*TAMANHO_BLOCO, y*TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))

def mover_fantasmas():
    for fantasma in fantasmas:
        direcoes = [(0,1),(1,0),(0,-1),(-1,0)]
        random.shuffle(direcoes)
        for dx, dy in direcoes:
            novo_x = fantasma['pos'][1] + dx
            novo_y = fantasma['pos'][0] + dy
            if 0 <= novo_y < linhas and 0 <= novo_x < colunas and labirinto[novo_y][novo_x] == 0:
                fantasma['pos'] = [novo_y, novo_x]
                break

def desenhar_pontuacao():
    texto = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))

# Loop principal
relogio = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentos do Pac-Man
    teclas = pygame.key.get_pressed()
    dx, dy = 0, 0
    if teclas[pygame.K_LEFT]: dx = -1
    if teclas[pygame.K_RIGHT]: dx = 1
    if teclas[pygame.K_UP]: dy = -1
    if teclas[pygame.K_DOWN]: dy = 1

    novo_x = pacman_pos[1] + dx
    novo_y = pacman_pos[0] + dy
    if 0 <= novo_y < linhas and 0 <= novo_x < colunas and labirinto[novo_y][novo_x] == 0:
        pacman_pos = [novo_y, novo_x]

    # Comer pontos
    if tuple(pacman_pos) in pontos:
        pontos.remove(tuple(pacman_pos))
        pontuacao += 10

    mover_fantasmas()

    # Checa colisão com qualquer fantasma
    for fantasma in fantasmas:
        if pacman_pos == fantasma['pos']:
            print("Você perdeu!")
            rodando = False

    tela.fill(PRETO)
    desenhar_labirinto()

    # Pontos
    for y, x in pontos:
        pygame.draw.circle(tela, (255, 255, 255), (x*TAMANHO_BLOCO+TAMANHO_BLOCO//2, y*TAMANHO_BLOCO+TAMANHO_BLOCO//2), 5)

    # Animação básica do Pac-Man (círculo piscando)
    tamanho_boca = (pygame.time.get_ticks() // 150) % TAMANHO_BLOCO // 4
    pygame.draw.circle(tela, AMARELO, (pacman_pos[1]*TAMANHO_BLOCO+TAMANHO_BLOCO//2, pacman_pos[0]*TAMANHO_BLOCO+TAMANHO_BLOCO//2), TAMANHO_BLOCO//2 - tamanho_boca)

    # Desenha fantasmas
    for fantasma in fantasmas:
        pygame.draw.circle(tela, fantasma['cor'], (fantasma['pos'][1]*TAMANHO_BLOCO+TAMANHO_BLOCO//2, fantasma['pos'][0]*TAMANHO_BLOCO+TAMANHO_BLOCO//2), TAMANHO_BLOCO//2)

    desenhar_pontuacao()
    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()