import turtle
import time
import copy

# game vars
in_progress = True
score_a = 0
score_b = 0

# view setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle setup
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = paddle_a.clone()
paddle_b.goto(350, 0)

# ball setup
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# ball movement
ball.dx = .20
ball.dy = .20


def paddle_up(paddle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)

def paddle_down(paddle):
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)

def paddle_up_a():
    paddle_up(paddle_a)

def paddle_up_b():
    paddle_up(paddle_b)

def paddle_down_a():
    paddle_down(paddle_a)

def paddle_down_b():
    paddle_down(paddle_b)

def update_score():
    score = "Score: A - {0} B - {1}".format(score_a, score_b)
    wn.title("Pong ({0})".format(score))

def player_score():
    update_score()
    ball.goto(0, 0)
    time.sleep(1)
    ball.dx *= -1

# Key bindings
wn.listen()
wn.onkeypress(paddle_up_a, "w")
wn.onkeypress(paddle_down_a, "s")
wn.onkeypress(paddle_up_b, "Up")
wn.onkeypress(paddle_down_b, "Down")

# Main game loop
while in_progress:
    wn.update()

    # Ball movement
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
        score_a += 1
        player_score()

    if ball.xcor() < -390:
        score_b += 1
        player_score()

    # detect paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
