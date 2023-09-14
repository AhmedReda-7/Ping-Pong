# Module imported
import turtle

# Game Window Customization
window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # stops window from updating automatically

# Game Objects

# First_Racket
First_Racket = turtle.Turtle()
First_Racket.speed(0)
First_Racket.shape("square")
First_Racket.color("blue")
First_Racket.shapesize(stretch_wid=5, stretch_len=1)
First_Racket.penup()
First_Racket.goto(-350, 0)

# Second_Racket
Second_Racket = turtle.Turtle()
Second_Racket.speed(0)
Second_Racket.shape("square")
Second_Racket.color("red")
Second_Racket.shapesize(stretch_wid=5, stretch_len=1)
Second_Racket.penup()
Second_Racket.goto(350, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.15
Ball.dy = -0.15

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: {}               Player 2: {}".format(score1, score2), align="center", font=("Retro", 24))

# Functions
def First_Racket_up():
    y = First_Racket.ycor()
    y += 40
    First_Racket.sety(y)

def First_Racket_down():
    y = First_Racket.ycor()
    y -= 40
    First_Racket.sety(y)

def Second_Racket_up():
    y = Second_Racket.ycor()
    y += 40
    Second_Racket.sety(y)

def Second_Racket_down():
    y = Second_Racket.ycor()
    y -= 40
    Second_Racket.sety(y)

# Keyboard Bindings
window.listen()    
window.onkeypress(First_Racket_up, "w")
window.onkeypress(First_Racket_down, "s")
window.onkeypress(Second_Racket_up, "Up")
window.onkeypress(Second_Racket_down, "Down")


# Game Loop
while True:
    window.update()

    # Ball Movement
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border Check
    if Ball.ycor() > 290 :
        Ball.sety(290)
        Ball.dy *=-1

    if Ball.ycor() < -290 :
        Ball.sety(-290)
        Ball.dy *=-1

    if Ball.xcor() > 390 :
        Ball.goto(0, 0)
        Ball.dx *=-1
        score1 +=1
        score.clear()
        score.write("Player 1: {}               Player 2: {}".format(score1, score2), align="center", font=("Retro", 24))

    if Ball.xcor() < -390 :
        Ball.goto(0, 0)
        Ball.dx *=-1 
        score2 +=1 
        score.clear()
        score.write("Player 1: {}               Player 2: {}".format(score1, score2), align="center", font=("Retro", 24))

    # Ball Collision
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < Second_Racket.ycor() + 40 and Ball.ycor() > Second_Racket.ycor() - 40):
        Ball.setx(340)
        Ball.dx *=-1

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < First_Racket.ycor() + 40 and Ball.ycor() > First_Racket.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *=-1

    # Score Winning
    if score1 == 10 or score2 == 10:
        score1.clear() and score2.clear()