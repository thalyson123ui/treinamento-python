import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições de tela
largura = 600
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Tamanho do bloco da cobrinha
tamanho_bloco = 20
velocidade_cobra = 15

# Fonte para texto
fonte = pygame.font.SysFont(None, 30)

def exibir_mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

def desenhar_cobra(tamanho_bloco, lista_cobra):
    for x, y in lista_cobra:
        pygame.draw.rect(tela, verde, [x, y, tamanho_bloco, tamanho_bloco])

def gerar_comida(largura, altura, tamanho_bloco, lista_cobra):
    while True:
        comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
        comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
        if [comida_x, comida_y] not in lista_cobra:
            break
    return comida_x, comida_y

def jogo():
    fim_jogo = False
    fim_perdeu = False

    x1 = largura / 2
    y1 = altura / 2
    x1_muda = 0
    y1_muda = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x, comida_y = gerar_comida(largura, altura, tamanho_bloco, lista_cobra)

    relogio = pygame.time.Clock()

    while not fim_jogo:

        while fim_perdeu == True:
            tela.fill(branco)
            exibir_mensagem("Você perdeu! Pressione C-Continuar ou S-Sair", vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_c:
                        jogo()
                    if evento.key == pygame.K_s:
                        fim_jogo = True
                        fim_perdeu = False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x1_muda == 0:
                    x1_muda = -tamanho_bloco
                    y1_muda = 0
                elif evento.key == pygame.K_RIGHT and x1_muda == 0:
                    x1_muda = tamanho_bloco
                    y1_muda = 0
                elif evento.key == pygame.K_UP and y1_muda == 0:
                    y1_muda = -tamanho_bloco
                    x1_muda = 0
                elif evento.key == pygame.K_DOWN and y1_muda == 0:
                    y1_muda = tamanho_bloco
                    x1_muda = 0

        if x1 < 0 or x1 >= largura or y1 < 0 or y1 >= altura:
            fim_perdeu = True

        x1 += x1_muda
        y1 += y1_muda
        tela.fill(branco)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobra = [x1, y1]
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                fim_perdeu = True

        desenhar_cobra(tamanho_bloco, lista_cobra)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x, comida_y = gerar_comida(largura, altura, tamanho_bloco, lista_cobra)
            comprimento_cobra += 1

        relogio.tick(velocidade_cobra)

    pygame.quit()
    quit()

jogo()