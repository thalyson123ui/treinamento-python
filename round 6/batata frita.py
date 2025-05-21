import pygame
import random
import sys
import os # Para lidar com caminhos de arquivos

# --- Inicialização do Pygame ---
pygame.init()
pygame.mixer.init() # Inicializa o módulo de áudio

# --- Configurações da Tela ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Round 6: Batatinha Frita 1, 2, 3")

# --- Cores ---
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# --- Fontes ---
font_large = pygame.font.Font(None, 90) # Para títulos
font_medium = pygame.font.Font(None, 60) # Para mensagens de estado
font_small = pygame.font.Font(None, 40) # Para instruções

# --- Carregamento de Recursos (Imagens e Sons) ---
# Dica: Substitua 'caminho/para/seus/arquivos/' pelo caminho real se eles não estiverem na mesma pasta.
# Exemplo: os.path.join('assets', 'images', 'player.png')
try:
    # Imagens (usando cores como fallback se as imagens não existirem)
    player_img = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.circle(player_img, GREEN, (20, 20), 20) # Cor de fallback

    doll_front_img = pygame.Surface((80, 150), pygame.SRCALPHA)
    pygame.draw.rect(doll_front_img, RED, (0, 0, 80, 150)) # Cor de fallback
    pygame.draw.circle(doll_front_img, BLACK, (40, 20), 30) # Cabeça
    
    doll_back_img = pygame.Surface((80, 150), pygame.SRCALPHA)
    pygame.draw.rect(doll_back_img, BLUE, (0, 0, 80, 150)) # Cor de fallback (azul para costas)
    pygame.draw.circle(doll_back_img, BLACK, (40, 20), 30) # Cabeça (virada)

    # Tenta carregar imagens reais se existirem
    if os.path.exists('player.png'): player_img = pygame.image.load('player.png').convert_alpha()
    if os.path.exists('doll_front.png'): doll_front_img = pygame.image.load('doll_front.png').convert_alpha()
    if os.path.exists('doll_back.png'): doll_back_img = pygame.image.load('doll_back.png').convert_alpha()
    
    # Sons
    music_song = None
    elimination_sound = None
    win_sound = None
    
    if os.path.exists('squid_game_song.ogg'): music_song = 'squid_game_song.ogg'
    elif os.path.exists('squid_game_song.wav'): music_song = 'squid_game_song.wav'
    
    if os.path.exists('elimination.wav'): elimination_sound = pygame.mixer.Sound('elimination.wav')
    if os.path.exists('win_sound.wav'): win_sound = pygame.mixer.Sound('win_sound.wav')

except pygame.error as e:
    print(f"Erro ao carregar recursos: {e}")
    print("Certifique-se de que os arquivos de imagem e som estão na mesma pasta que o script.")

# --- Variáveis do Jogo ---
player_x = 100
player_y = SCREEN_HEIGHT - 100 - player_img.get_height() // 2 # Centraliza o jogador na linha inferior
player_speed = 7

doll_x = SCREEN_WIDTH - 150 # Posição X da boneca
doll_y = SCREEN_HEIGHT // 2 - doll_front_img.get_height() // 2 # Posição Y da boneca

doll_state = "RUN"  # "RUN" (correr) ou "STOP" (parar)
game_over = False
win = False
start_screen = True # Para a tela inicial

# Temporizadores para a boneca
run_time_min = 3
run_time_max = 6
stop_time_min = 1.5
stop_time_max = 3.5

current_run_time = random.uniform(run_time_min, run_time_max)
current_stop_time = random.uniform(stop_time_min, stop_time_max)
timer_start = pygame.time.get_ticks()

# Posição da linha de chegada
finish_line_x = SCREEN_WIDTH - 200

# Variáveis para a detecção de movimento
player_moving_last_frame = False

# --- Funções de Desenho ---
def draw_player(x, y):
    screen.blit(player_img, (x - player_img.get_width() // 2, y - player_img.get_height() // 2))

def draw_doll(state):
    if state == "RUN": # Boneca de costas para os jogadores
        screen.blit(doll_back_img, (doll_x - doll_back_img.get_width() // 2, doll_y))
    else: # Boneca virada para os jogadores
        screen.blit(doll_front_img, (doll_x - doll_front_img.get_width() // 2, doll_y))

def display_message(message, color, font_obj, center_x=SCREEN_WIDTH // 2, center_y=SCREEN_HEIGHT // 2):
    text_surface = font_obj.render(message, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    screen.blit(text_surface, text_rect)

# --- Funções de Controle de Áudio ---
def play_music():
    if music_song and not pygame.mixer.music.get_busy(): # Só toca se não estiver tocando
        pygame.mixer.music.load(music_song)
        pygame.mixer.music.play(-1) # -1 para loop infinito

def stop_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

def play_sound(sound):
    if sound:
        sound.play()

# --- Loop Principal do Jogo ---
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if start_screen:
                start_screen = False
                play_music() # Começa a música ao iniciar o jogo
            elif game_over and event.key == pygame.K_r: # Reiniciar o jogo
                # Resetar variáveis
                player_x = 100
                game_over = False
                win = False
                doll_state = "RUN"
                current_run_time = random.uniform(run_time_min, run_time_max)
                current_stop_time = random.uniform(stop_time_min, stop_time_max)
                timer_start = pygame.time.get_ticks()
                player_moving_last_frame = False # Reseta a flag de movimento
                play_music() # Reinicia a música

    if start_screen:
        screen.fill(BLACK)
        display_message("ROUND 6", RED, font_large, center_y=SCREEN_HEIGHT // 2 - 50)
        display_message("BATATINHA FRITA 1, 2, 3", WHITE, font_medium, center_y=SCREEN_HEIGHT // 2 + 20)
        display_message("Pressione QUALQUER TECLA para começar", YELLOW, font_small, center_y=SCREEN_HEIGHT // 2 + 100)
        pygame.display.flip()
        continue # Pula o resto do loop até que o jogo comece

    if not game_over:
        keys = pygame.key.get_pressed()
        player_is_moving_this_frame = False

        # Lógica de movimento do jogador
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
            player_is_moving_this_frame = True
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            player_is_moving_this_frame = True

        # Limitar o movimento do jogador
        if player_x < player_img.get_width() // 2:
            player_x = player_img.get_width() // 2
        if player_x > SCREEN_WIDTH - player_img.get_width() // 2:
            player_x = SCREEN_WIDTH - player_img.get_width() // 2

        # Lógica da boneca (mudar de RUN para STOP e vice-versa)
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - timer_start) / 1000 # Convertendo para segundos

        if doll_state == "RUN":
            if elapsed_time >= current_run_time:
                doll_state = "STOP"
                timer_start = current_time
                current_stop_time = random.uniform(stop_time_min, stop_time_max)
                stop_music() # Para a música quando a boneca vira
        elif doll_state == "STOP":
            if elapsed_time >= current_stop_time:
                doll_state = "RUN"
                timer_start = current_time
                current_run_time = random.uniform(run_time_min, run_time_max)
                play_music() # Reinicia a música quando a boneca vira

        # Detecção de movimento quando a boneca está "STOP"
        if doll_state == "STOP" and player_is_moving_this_frame:
            game_over = True
            win = False
            play_sound(elimination_sound) # Toca som de eliminação
            stop_music() # Garante que a música pare
            
        # Atualiza a flag de movimento para o próximo frame
        player_moving_last_frame = player_is_moving_this_frame

        # Condição de vitória
        if player_x >= finish_line_x:
            game_over = True
            win = True
            play_sound(win_sound) # Toca som de vitória
            stop_music()

    # --- Desenha tudo ---
    screen.fill(BLACK) # Limpa a tela

    # Linha de chegada
    pygame.draw.line(screen, YELLOW, (finish_line_x, 0), (finish_line_x, SCREEN_HEIGHT), 5)

    # Desenha o jogador e a boneca
    draw_player(player_x, player_y)
    draw_doll(doll_state)

    # Exibe mensagens de estado do jogo
    if game_over:
        if win:
            display_message("VOCÊ VENCEU!", GREEN, font_large)
        else:
            display_message("GAME OVER!", RED, font_large)
        display_message("Pressione 'R' para Reiniciar", WHITE, font_small, center_y=SCREEN_HEIGHT // 2 + 70)
    else:
        if doll_state == "RUN":
            display_message("CORRA!", GREEN, font_medium, center_y=50)
        else:
            display_message("PARE!", RED, font_medium, center_y=50)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros (FPS)
    clock.tick(60)

pygame.quit()
sys.exit()