import pygame
import random

# Inicializa o pygame
pygame.init()

# Constantes do jogo
LARGURA_TELA = 300
ALTURA_TELA = 600
TAMANHO_BLOCO = 30
COLUNAS = LARGURA_TELA // TAMANHO_BLOCO
LINHAS = ALTURA_TELA // TAMANHO_BLOCO

# Cores
CORES = [
    (0, 255, 255),   # I
    (255, 165, 0),   # L
    (0, 0, 255),     # J
    (255, 255, 0),   # O
    (0, 255, 0),     # S
    (255, 0, 0),     # Z
    (128, 0, 128)    # T
]

# Formatos das pecas
PECAS = [
    [[1, 1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 0], [1, 1, 1]]
]

class Peca:
    def __init__(self):
        self.tipo = random.randint(0, len(PECAS) - 1)
        self.forma = PECAS[self.tipo]
        self.cor = CORES[self.tipo]
        self.x = COLUNAS // 2 - len(self.forma[0]) // 2
        self.y = 0

    def girar(self):
        self.forma = [list(linha) for linha in zip(*self.forma[::-1])]

def cria_grade(travado):
    grade = [[(0, 0, 0) for _ in range(COLUNAS)] for _ in range(LINHAS)]
    for y in range(LINHAS):
        for x in range(COLUNAS):
            if (x, y) in travado:
                grade[y][x] = travado[(x, y)]
    return grade

def desenha_tela(tela, grade):
    tela.fill((0, 0, 0))
    for y in range(LINHAS):
        for x in range(COLUNAS):
            pygame.draw.rect(
                tela,
                grade[y][x],
                (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO),
                0
            )
            pygame.draw.rect(
                tela,
                (50, 50, 50),
                (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO),
                1
            )
    pygame.display.update()

def posicao_valida(peca, grade):
    for i, linha in enumerate(peca.forma):
        for j, valor in enumerate(linha):
            if valor:
                x = peca.x + j
                y = peca.y + i
                if x < 0 or x >= COLUNAS or y >= LINHAS:
                    return False
                if y >= 0 and grade[y][x] != (0, 0, 0):
                    return False
    return True

def adicionar_peca(peca, travado):
    for i, linha in enumerate(peca.forma):
        for j, valor in enumerate(linha):
            if valor:
                x = peca.x + j
                y = peca.y + i
                if y >= 0:
                    travado[(x, y)] = peca.cor

def limpar_linhas(grade, travado):
    linhas_completas = 0
    for y in range(LINHAS - 1, -1, -1):
        if (0, 0, 0) not in grade[y]:
            linhas_completas += 1
            for x in range(COLUNAS):
                try:
                    del travado[(x, y)]
                except:
                    continue
            for k in range(y - 1, -1, -1):
                for x in range(COLUNAS):
                    if (x, k) in travado:
                        travado[(x, k + 1)] = travado.pop((x, k))
    return linhas_completas

def main():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    travado = {}
    grade = cria_grade(travado)

    peca_atual = Peca()
    tempo_queda = 0
    queda_velocidade = 500  # milissegundos

    rodando = True
    while rodando:
        tempo_queda += clock.get_rawtime()
        clock.tick()

        if tempo_queda > queda_velocidade:
            peca_atual.y += 1
            if not posicao_valida(peca_atual, grade):
                peca_atual.y -= 1
                adicionar_peca(peca_atual, travado)
                peca_atual = Peca()
                if not posicao_valida(peca_atual, grade):
                    rodando = False
            tempo_queda = 0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    peca_atual.x -= 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.x += 1
                elif evento.key == pygame.K_RIGHT:
                    peca_atual.x += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.x -= 1
                elif evento.key == pygame.K_DOWN:
                    peca_atual.y += 1
                    if not posicao_valida(peca_atual, grade):
                        peca_atual.y -= 1
                elif evento.key == pygame.K_UP:
                    peca_atual.girar()
                    if not posicao_valida(peca_atual, grade):
                        for _ in range(3):  # Desfaz rotação
                            peca_atual.girar()

        grade = cria_grade(travado)
        for i, linha in enumerate(peca_atual.forma):
            for j, valor in enumerate(linha):
                if valor:
                    x = peca_atual.x + j
                    y = peca_atual.y + i
                    if y >= 0:
                        grade[y][x] = peca_atual.cor

        limpar_linhas(grade, travado)
        desenha_tela(tela, grade)

    # Exibe Game Over
    fonte = pygame.font.SysFont("comicsans", 40)
    texto = fonte.render("Game Over", True, (255, 255, 255))
    tela.blit(texto, (LARGURA_TELA // 2 - texto.get_width() // 2, ALTURA_TELA // 2 - texto.get_height() // 2))
    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN:
                esperando = False

    pygame.quit()

if __name__ == "__main__":
    main()