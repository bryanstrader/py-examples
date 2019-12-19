import turtle
import time


#view setup
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle setup
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
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
    score = "Score: A - " + str(score_a) + " B - " + str(score_b)
    wn.title("Pong (" + score + ")")


# Key bindings
wn.listen()
wn.onkeypress(paddle_up_a, "w")
wn.onkeypress(paddle_down_a, "s")

wn.onkeypress(paddle_up_b, "Up")
wn.onkeypress(paddle_down_b, "Down")


# Main game loop
in_progress = True
score_a = 0
score_b = 0

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
        update_score()
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        time.sleep(1)
        ball.dx *= -1

    # detect paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1        