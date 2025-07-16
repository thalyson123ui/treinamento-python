import pygame
import sys

# --- Constantes e Configurações Iniciais ---

# Inicializa o Pygame e o mixer de som
pygame.init()
pygame.mixer.init()

# Configurações da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Round 6: Pular Corda")

# Cores (no padrão RGB)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE_JOGADOR = (0, 154, 88) # Cor do agasalho de Round 6
VERMELHO_CORDA = (220, 20, 60) # Cor dos uniformes dos guardas

# Relógio para controlar o FPS (Frames por Segundo)
relogio = pygame.time.Clock()
FPS = 60

# Carregar sons (coloque os arquivos .wav em uma pasta chamada 'sons')
try:
    som_pulo = pygame.mixer.Sound('sons/pulo.wav')
    som_falha = pygame.mixer.Sound('sons/falha.wav')
    som_pulo.set_volume(0.5)
except pygame.error:
    print("Aviso: Arquivos de som não encontrados na pasta 'sons'. O jogo funcionará sem som.")
    som_pulo = None
    som_falha = None

# Fontes para texto
fonte_jogo = pygame.font.Font(None, 50)
fonte_game_over = pygame.font.Font(None, 80)

# --- Classes do Jogo ---

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(VERDE_JOGADOR)
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA_TELA // 4, ALTURA_TELA - 50)
        
        # Física do jogador
        self.velocidade_y = 0
        self.gravidade = 1
        self.forca_pulo = -20
        self.esta_no_chao = True

    def pular(self):
        # Só pode pular se estiver no chão
        if self.esta_no_chao:
            self.velocidade_y = self.forca_pulo
            self.esta_no_chao = False
            if som_pulo:
                som_pulo.play()

    def update(self):
        # Aplica a gravidade
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y

        # Verifica se o jogador está no chão
        if self.rect.bottom >= ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA
            self.velocidade_y = 0
            self.esta_no_chao = True

class Corda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([LARGURA_TELA, 10])
        self.image.fill(VERMELHO_CORDA)
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA_TELA // 2, ALTURA_TELA - 25)
        
        # Movimento da corda
        self.velocidade = 5
        self.direcao = 1 # 1 para direita, -1 para esquerda
        
        # Lógica de pontuação
        self.ponto_computado = False

    def update(self):
        # Move a corda
        self.rect.x += self.velocidade * self.direcao
        
        # Inverte a direção quando atinge as bordas da tela
        if self.rect.right >= LARGURA_TELA + (LARGURA_TELA // 2) or self.rect.left <= -(LARGURA_TELA // 2):
            self.direcao *= -1
            self.ponto_computado = False # Reseta a flag de ponto quando a corda reinicia o trajeto

# --- Funções do Jogo ---

def mostrar_tela_game_over(pontuacao):
    """Exibe a tela de 'ELIMINADO'."""
    TELA.fill(PRETO)
    
    texto_eliminado = fonte_game_over.render("ELIMINADO", True, VERMELHO_CORDA)
    texto_pontuacao = fonte_jogo.render(f"Pontuação Final: {pontuacao}", True, BRANCO)
    texto_instrucao = fonte_jogo.render("Pressione 'R' para reiniciar", True, BRANCO)

    TELA.blit(texto_eliminado, (LARGURA_TELA/2 - texto_eliminado.get_width()/2, ALTURA_TELA/3))
    TELA.blit(texto_pontuacao, (LARGURA_TELA/2 - texto_pontuacao.get_width()/2, ALTURA_TELA/2))
    TELA.blit(texto_instrucao, (LARGURA_TELA/2 - texto_instrucao.get_width()/2, ALTURA_TELA/2 + 100))
    
    pygame.display.flip()

    # Espera o jogador pressionar 'R' para recomeçar
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    esperando = False

def loop_principal():
    """Loop principal do jogo."""
    
    # Cria os sprites
    todos_os_sprites = pygame.sprite.Group()
    grupo_corda = pygame.sprite.Group()

    jogador = Jogador()
    corda = Corda()

    todos_os_sprites.add(jogador)
    grupo_corda.add(corda) # A corda não é adicionada ao grupo principal de desenho
    
    pontuacao = 0
    eliminado = False
    
    # Loop do jogo
    rodando = True
    while rodando:
        # Controla o FPS
        relogio.tick(FPS)

        # --- Processamento de Eventos ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    jogador.pular()

        if not eliminado:
            # --- Atualização da Lógica ---
            todos_os_sprites.update()
            corda.update() # Atualiza a corda separadamente

            # Lógica de pontuação: ganha um ponto quando a corda passa pelo jogador
            if not corda.ponto_computado and corda.rect.centerx < jogador.rect.centerx:
                pontuacao += 1
                corda.ponto_computado = True
                
                # Aumenta a dificuldade a cada 5 pontos
                if pontuacao % 5 == 0:
                    corda.velocidade += 1

            # --- Verificação de Colisão ---
            # Verifica se o jogador (que não está pulando alto) colide com a corda
            if pygame.sprite.spritecollide(jogador, grupo_corda, False):
                # A colisão só conta se o jogador estiver perto do chão
                if jogador.rect.bottom > ALTURA_TELA - 40:
                    if som_falha:
                        som_falha.play()
                    eliminado = True

            # --- Desenho na Tela ---
            TELA.fill(PRETO)
            todos_os_sprites.draw(TELA)
            TELA.blit(corda.image, corda.rect) # Desenha a corda

            # Mostra a pontuação
            texto_pontuacao = fonte_jogo.render(f"Pontos: {pontuacao}", True, BRANCO)
            TELA.blit(texto_pontuacao, (10, 10))
        
        else: # Se foi eliminado
            mostrar_tela_game_over(pontuacao)
            # Após a tela de game over, o loop recomeça do zero
            loop_principal()

        # Atualiza a tela inteira
        pygame.display.flip()

# Inicia o jogo
if __name__ == "__main__":
    loop_principal()