# windows
import turtle
import os
import winsound

wn = turtle.Screen()
wn.title("Pong @Yxt")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# music(mac->1;Linux->2;Windows->3)
# os.system("afplay faded.wav&")
# os.system("aplay faded.wav&")
winsound.PlaySound('faded.wav', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Peddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0  Player B : 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0


# function
def paddle_a_up ():
    print("a up")
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_b_up ():
    print("b up")
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_a_down ():
    print("a down")
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_down ():
    print("b down")
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# keyboard
# without '()' while calling the function

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1