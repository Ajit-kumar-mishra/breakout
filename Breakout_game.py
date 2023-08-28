import turtle
import time
import random

# Set up the screen
window = turtle.Screen()
window.title("Breakout Clone")
window.bgcolor("black")
window.setup(width=800, height=600)

# Create the paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Create bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):
    color = colors[y]
    for x in range(-7, 8):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(color)
        brick.penup()
        brick.goto(x * 100, 200 - y * 50)
        bricks.append(brick)

# Function to move the paddle
def move_paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

def move_paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

# Keyboard bindings
window.listen()
window.onkeypress(move_paddle_left, "Left")
window.onkeypress(move_paddle_right, "Right")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() < -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if brick.distance(ball) < 40:
            brick.goto(1000, 1000)  # Move the brick off-screen
            bricks.remove(brick)
            ball.dy *= -1

    # Check for game over
    if ball.ycor() < -290 or len(bricks) == 0:
        ball.goto(0, 0)
        ball.dy *= -1
        bricks = []  # Reset bricks
        for y in range(5):
            color = colors[y]
            for x in range(-7, 8):
                brick = turtle.Turtle()
                brick.speed(0)
                brick.shape("square")
                brick.color(color)
                brick.penup()
                brick.goto(x * 100, 200 - y * 50)
                bricks.append(brick)

    time.sleep(0.01)

turtle.done()
