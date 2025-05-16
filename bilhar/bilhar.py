import pygame
import pymunk
import pymunk.pygame_util
import math

# --- Configurações iniciais ---
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sinuca Realista com Buracos")
clock = pygame.time.Clock()
FPS = 60
FONT = pygame.font.SysFont("Arial", 24)

GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)

space = pymunk.Space()
space.damping = 0.99

draw_options = pymunk.pygame_util.DrawOptions(screen)

# --- Funções de criação ---
def create_table(space, width, height, border_thickness=20):
    static_lines = [
        pymunk.Segment(space.static_body, (border_thickness, border_thickness), (width-border_thickness, border_thickness), 1),
        pymunk.Segment(space.static_body, (width-border_thickness, border_thickness), (width-border_thickness, height-border_thickness), 1),
        pymunk.Segment(space.static_body, (width-border_thickness, height-border_thickness), (border_thickness, height-border_thickness), 1),
        pymunk.Segment(space.static_body, (border_thickness, height-border_thickness), (border_thickness, border_thickness), 1)
    ]
    for line in static_lines:
        line.elasticity = 0.95
        line.friction = 0.9
    space.add(*static_lines)

def create_holes(space):
    hole_positions = [
        (20, 20), (WIDTH//2, 20), (WIDTH-20, 20),
        (20, HEIGHT-20), (WIDTH//2, HEIGHT-20), (WIDTH-20, HEIGHT-20)
    ]
    holes = []
    for pos in hole_positions:
        shape = pymunk.Circle(space.static_body, 18, offset=pos)
        shape.sensor = True
        shape.collision_type = 1
        holes.append(shape)
        space.add(shape)
    return holes

def create_ball(space, pos, color=WHITE, radius=12, mass=5):
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.95
    shape.friction = 0.6
    shape.color = color
    shape.collision_type = 2
    space.add(body, shape)
    return shape

def apply_cue_force(ball_body, mouse_pos):
    dx = ball_body.position[0] - mouse_pos[0]
    dy = ball_body.position[1] - mouse_pos[1]
    force = math.hypot(dx, dy) * 50
    angle = math.atan2(dy, dx)
    fx = math.cos(angle) * force
    fy = math.sin(angle) * force
    ball_body.apply_impulse_at_local_point((fx, fy))

# --- Criação da mesa e bolas ---
create_table(space, WIDTH, HEIGHT)
holes = create_holes(space)
balls = [
    create_ball(space, (200, 200), WHITE),  # bola branca
    create_ball(space, (400, 200), RED),
    create_ball(space, (420, 210), YELLOW)
]

score = 0
def remove_ball(arbiter, space, data):
    global score
    shape = arbiter.shapes[1]
    if shape in space.shapes:
        score += 1
        space.remove(shape, shape.body)
    return False

# Handler de colisão buraco-bola
handler = space.add_collision_handler(1, 2)
handler.begin = remove_ball

# --- Loop principal ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if balls and balls[0].body in space.bodies:
                apply_cue_force(balls[0].body, pygame.mouse.get_pos())

    screen.fill(GREEN)
    space.step(1 / FPS)
    space.debug_draw(draw_options)

    score_text = FONT.render(f"Pontuação: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()