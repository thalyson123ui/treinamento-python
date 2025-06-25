import turtle
import os # Para tocar som no Windows/Mac/Linux

# --- Configuração da Tela ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Meu Jogo de Pong")
screen.tracer(0) # Desliga a atualização automática para controle manual (mais suave)

# --- Raquete A ---
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Velocidade máxima de animação
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Estica para ser uma raquete
paddle_a.penup() # Não desenha ao mover
paddle_a.goto(-350, 0)

# --- Raquete B ---
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# --- Bola ---
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 # Velocidade da bola no eixo X (delta x)
ball.dy = 2 # Velocidade da bola no eixo Y (delta y)

# --- Placar ---
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# --- Funções de Movimento da Raquete ---
def paddle_a_up():
    y = paddle_a.ycor() # Pega a coordenada Y atual
    y += 20 # Move 20 pixels para cima
    paddle_a.sety(y) # Atualiza a coordenada Y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# --- Tocar Som (Opcional) ---
def play_sound(sound_file):
    if os.name == 'posix': # Para Mac/Linux
        os.system(f"afplay {sound_file}&")
    elif os.name == 'nt': # Para Windows
        import winsound
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)

# --- Controle do Teclado ---
screen.listen() # Fica ouvindo por eventos do teclado
screen.onkeypress(paddle_a_up, "w") # Quando "w" é pressionado, chama paddle_a_up
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up") # Seta para cima
screen.onkeypress(paddle_b_down, "Down") # Seta para baixo

# --- Loop Principal do Jogo ---
while True:
    screen.update() # Atualiza a tela a cada iteração

    # Mover a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Detecção de Borda (Cima/Baixo)
    if ball.ycor() > 290: # Borda superior
        ball.sety(290)
        ball.dy *= -1 # Inverte a direção Y
        #play_sound("bounce.wav") # Descomente para tocar som

    if ball.ycor() < -290: # Borda inferior
        ball.sety(-290)
        ball.dy *= -1
        #play_sound("bounce.wav")

    # Detecção de Borda (Esquerda/Direita)
    if ball.xcor() > 390: # Borda direita (passou da raquete B)
        ball.goto(0, 0) # Volta para o centro
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        #play_sound("score.wav") # Descomente para tocar som

    if ball.xcor() < -390: # Borda esquerda (passou da raquete A)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        #play_sound("score.wav")

    # Colisão da Bola com as Raquetes
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        #play_sound("bounce.wav")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        #play_sound("bounce.wav")