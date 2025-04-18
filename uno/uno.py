import pygame
import random

# Inicializa o Pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UNO - Versão Simplificada")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

COLORS = [RED, BLUE, GREEN, YELLOW]

FONT = pygame.font.SysFont("Arial", 24)

CARD_WIDTH = 80
CARD_HEIGHT = 120

# Classe Carta
class Card:
    def __init__(self, color, number, special=None):
        self.color = color
        self.number = number
        self.special = special  # Pode ser 'skip', '+2'

    def draw(self, x, y):
        pygame.draw.rect(SCREEN, self.color, (x, y, CARD_WIDTH, CARD_HEIGHT))
        pygame.draw.rect(SCREEN, BLACK, (x, y, CARD_WIDTH, CARD_HEIGHT), 2)
        if self.special:
            text = FONT.render(self.special, True, BLACK)
        else:
            text = FONT.render(str(self.number), True, BLACK)
        SCREEN.blit(text, (x + 10, y + 45))

    def matches(self, other_card):
        return (self.color == other_card.color or
                self.number == other_card.number or
                self.special is not None and self.special == other_card.special)

# Função para gerar um baralho simplificado
def generate_deck():
    deck = []
    for color in COLORS:
        for number in range(0, 10):
            deck.append(Card(color, number))
        deck.append(Card(color, None, special='+2'))
        deck.append(Card(color, None, special='skip'))
    random.shuffle(deck)
    return deck

# Inicialização
deck = generate_deck()
player_hand = [deck.pop() for _ in range(7)]
computer_hand = [deck.pop() for _ in range(7)]
discard_pile = [deck.pop()]

selected_card_index = None
running = True
turn = "player"  # ou "computer"
skip_next = False

# Botão de comprar
buy_button = pygame.Rect(WIDTH - 150, HEIGHT - 150, 120, 50)

# Game loop
while running:
    SCREEN.fill(WHITE)

    # Desenhar carta do topo do descarte
    top_card = discard_pile[-1]
    top_card.draw(WIDTH//2 - CARD_WIDTH//2, HEIGHT//2 - CARD_HEIGHT//2)

    # Mostrar mão do jogador
    for i, card in enumerate(player_hand):
        x = 100 + i * (CARD_WIDTH + 10)
        y = HEIGHT - CARD_HEIGHT - 20
        card.draw(x, y)

    # Mostrar botão de comprar carta
    pygame.draw.rect(SCREEN, GRAY, buy_button)
    pygame.draw.rect(SCREEN, BLACK, buy_button, 2)
    buy_text = FONT.render("Comprar", True, BLACK)
    SCREEN.blit(buy_text, (buy_button.x + 10, buy_button.y + 10))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and turn == "player":
            mx, my = pygame.mouse.get_pos()

            # Clique nas cartas
            for i, card in enumerate(player_hand):
                x = 100 + i * (CARD_WIDTH + 10)
                y = HEIGHT - CARD_HEIGHT - 20
                if x < mx < x + CARD_WIDTH and y < my < y + CARD_HEIGHT:
                    if card.matches(top_card):
                        played_card = player_hand.pop(i)
                        discard_pile.append(played_card)

                        # Efeito especial
                        if played_card.special == '+2':
                            for _ in range(2):
                                if deck:
                                    computer_hand.append(deck.pop())
                        elif played_card.special == 'skip':
                            skip_next = True

                        turn = "computer"
                    break

            # Clique no botão de comprar
            if buy_button.collidepoint(mx, my):
                if deck:
                    player_hand.append(deck.pop())
                    turn = "computer"

    # Turno do computador
    if turn == "computer":
        pygame.time.delay(1000)
        if skip_next:
            skip_next = False
        else:
            for i, card in enumerate(computer_hand):
                if card.matches(top_card):
                    played_card = computer_hand.pop(i)
                    discard_pile.append(played_card)

                    # Efeito especial
                    if played_card.special == '+2':
                        for _ in range(2):
                            if deck:
                                player_hand.append(deck.pop())
                    elif played_card.special == 'skip':
                        skip_next = True

                    break
            else:
                if deck:
                    computer_hand.append(deck.pop())

        turn = "player"

    # Verifica fim de jogo
    if not player_hand:
        print("Jogador venceu!")
        running = False
    elif not computer_hand:
        print("Computador venceu!")
        running = False

    pygame.display.update()

pygame.quit()