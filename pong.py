import turtle

# Create screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# Create left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Create right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Create ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Create scoreboard
left_player = 0
right_player = 0
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left Player: {}  Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

# Move left paddle up
def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

# Move left paddle down
def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

# Move right paddle up
def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)

# Move right paddle down
def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Main game loop
while True:
    sc.update()

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Border checking
    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 490:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left Player: {}  Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -490:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left Player: {}  Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (hit_ball.dx > 0) and (350 < hit_ball.xcor() < 360) and (right_pad.ycor() + 50 > hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(340)
        hit_ball.dx *= -1

    if (hit_ball.dx < 0) and (-360 < hit_ball.xcor() < -350) and (left_pad.ycor() + 50 > hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-340)
        hit_ball.dx *= -1
