import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Show do Milhão")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (10, 10, 200)
GREEN = (0, 255, 0)
RED = (200, 0, 0)

# Fonte
font = pygame.font.SysFont("arial", 28)

def draw_text(text, size, color, x, y, center=True):
    font_obj = pygame.font.SysFont("arial", size)
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Sons (usar mocks neste ambiente, mas referenciáveis no local)
def play_sound(sound_file):
    try:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    except:
        pass  # som desativado neste ambiente

# Estrutura de perguntas
questions = [
    {
        "question": "Qual a capital do Brasil?",
        "options": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "answer": 2
    },
    {
        "question": "Qual o maior planeta do sistema solar?",
        "options": ["Terra", "Júpiter", "Saturno", "Marte"],
        "answer": 1
    },
    # ... adicionar até 15 perguntas aqui
]

# Estado do jogo
current_question = 0
score = 0
helps = {
    "pular": True,
    "universitarios": True,
    "cartas": True
}

# Botões
class Button:
    def __init__(self, text, x, y, w, h, callback, color=BLUE):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        draw_text(self.text, 22, WHITE, self.rect.centerx, self.rect.centery)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

# Funções de resposta
selected = -1
def choose_option(index):
    global current_question, score, selected
    selected = index
    correct = questions[current_question]["answer"]
    if index == correct:
        score += 1
        play_sound("assets/correct.wav")
        current_question += 1
    else:
        play_sound("assets/wrong.wav")
        game_over()

def game_over():
    draw_text("Fim de jogo! Pontuação: {}".format(score), 36, RED, WIDTH//2, HEIGHT//2)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Ajuda

def usar_pular():
    global current_question
    if helps["pular"]:
        helps["pular"] = False
        current_question += 1

def usar_universitarios():
    if helps["universitarios"]:
        helps["universitarios"] = False
        correct = questions[current_question]["answer"]
        print(f"Universitários acham que a resposta certa é: {chr(65+correct)}")

def usar_cartas():
    if helps["cartas"]:
        helps["cartas"] = False
        correct = questions[current_question]["answer"]
        options = list(range(4))
        options.remove(correct)
        to_remove = random.sample(options, 2)
        for i in to_remove:
            questions[current_question]['options'][i] = "---"

# Criação dos botões das ajudas
ajuda_botoes = [
    Button("Pular", 50, 500, 100, 40, usar_pular, GREEN),
    Button("Universitários", 170, 500, 150, 40, usar_universitarios, GREEN),
    Button("Cartas", 340, 500, 100, 40, usar_cartas, GREEN)
]

def main():
    clock = pygame.time.Clock()
    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for b in ajuda_botoes:
                b.handle_event(event)
            for i, b in enumerate(option_buttons):
                b.handle_event(event)

        if current_question >= len(questions):
            draw_text("Parabéns! Você venceu o Show do Milhão!", 36, GREEN, WIDTH//2, HEIGHT//2)
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.quit()
            sys.exit()

        q = questions[current_question]
        draw_text(q['question'], 30, WHITE, WIDTH//2, 50)

        for b in ajuda_botoes:
            b.draw()
        for b in option_buttons:
            b.draw()

        pygame.display.flip()
        clock.tick(30)

# Criar botões de alternativas
option_buttons = []
def setup_option_buttons():
    global option_buttons
    option_buttons = []
    for i in range(4):
        btn = Button(f"", 150, 150 + i*70, 500, 50, lambda i=i: choose_option(i))
        option_buttons.append(btn)

setup_option_buttons()
main()