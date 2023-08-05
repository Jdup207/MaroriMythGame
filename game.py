# Simple Game of "The Battle of the Mountains" 
# By @JamesduPreez
# Part 1: Getting started.
# Starting 28 July
# TODO: Make an Maori game involving the mountians.

import turtle

wn = turtle.Screen()
wn.title("The Battle of the Mountains: by @JamesduPreez")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.bgcolor("dark green")

# Mountain A ----------------------------------------------------------------------------------------
mountain_a = turtle.Turtle()
mountain_a.speed(0)
mountain_a.shape("square")
mountain_a.color("grey")
mountain_a.shapesize(stretch_wid=1, stretch_len=1)
mountain_a.penup()
mountain_a.goto(-350, 0)
mountain_a.dy = 1
mountain_a.dx = 2

# bullet of Mounain A#
bul = turtle.Turtle()
bul.color("white")
bul.shape("square")
bul.shapesize(0.5, 1)
bul.penup()
bul.goto(0, -150)
bul.hideturtle()

def movlt():
    mountain_a.It(10)
    x = bul.xcor()
    y = bul.ycor()
    bul.It(10)
    bul.setx(x-5)
    bul.sety(y+5)

def movrt():
    mountain_a.It(10)
    x = bul.xcor()
    y = bul.ycor()
    mountain_a.rt(10)
    bul.rt(10)
    bul.setx(x-5)
    bul.sety(y-5)

def shoot(x, y):
    bul.showturtle()
    bul.fd(300)
    bul.hideturtle()
    bul.backward(300)

win = turtle.Screen()
win.listen()
win.onkeypress(movlt , 'q')
win.onkeypress(movrt , 'e') 
win.onclick(shoot , 1)

# Mountain B ------------------------------------------------------------------------------------
mountain_b = turtle.Turtle()
mountain_b.speed(0)
mountain_b.shape("square") 
mountain_b.color("light grey")
mountain_b.shapesize(stretch_wid=1, stretch_len=1)
mountain_b.penup()
mountain_b.goto(350, 0)
mountain_b.dy = 1
mountain_b.dx = 2

# bullet of Mounain B
bul = turtle.Turtle()
bul.color("white")
bul.shape("square")
bul.shapesize(0.5, 1)
bul.penup()
bul.goto(0, -150)
bul.hideturtle()

def movlt():
    mountain_b.It(10)
    x = bul.xcor()
    y = bul.ycor()
    bul.It(10)
    bul.setx(x-5)
    bul.sety(y+5)

def movrt():
    mountain_b.It(10)
    x = bul.xcor()
    y = bul.ycor()
    mountain_b.rt(10)
    bul.rt(10)
    bul.setx(x-5)
    bul.sety(y-5)

def shoot(x, y):
    bul.showturtle()
    bul.fd(300)
    bul.hideturtle()
    bul.backward(300)

win = turtle.Screen()
win.listen()
win.onkeypress(movlt , 'i')
win.onkeypress(movrt , 'o') 
win.onclick(shoot , 1)

# Pen / Score board ---------------------------------------------------------------------------------
pen = turtle.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Mountain A: 0 | Mountain B: 0", align="center", font=("Courier", 24, "normal"))

# Function y ----------------------------------------------------------------------------------------
def paddle_a_up():
    y = mountain_a.ycor()
    y += 10
    mountain_a.sety(y)

def paddle_a_down():
    y = mountain_a.ycor()
    y -= 10
    mountain_a.sety(y)

def paddle_b_up():
    y = mountain_b.ycor()
    y += 10
    mountain_b.sety(y)

def paddle_b_down():
    y = mountain_b.ycor()
    y -= 10
    mountain_b.sety(y)

# Function x ----------------------------------------------------------------------------------------

def paddle_a_left():
    x = mountain_a.xcor()
    x -= 10
    mountain_a.setx(x)

def paddle_a_right():
    x = mountain_a.xcor()
    x += 10
    mountain_a.setx(x)

def paddle_b_left():
    x = mountain_b.xcor()
    x -= 10
    mountain_b.setx(x)

def paddle_b_right():
    x = mountain_b.xcor()
    x += 10
    mountain_b.setx(x)

# Keyboard binding mountain A
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_left, "a")
wn.onkeypress(paddle_a_right, "d")

# mountain B
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")
wn.onkeypress(paddle_b_left, "j")
wn.onkeypress(paddle_b_right, "l")

# this is were I will also add in the effects, such as the selecting weapon and firing.-------------


# Main game loop -------------------------------------------------------------------------------------
while True:
    wn.update()


    # border checking moutnain_a
    if mountain_a.ycor() > 290:
        mountain_a.sety(-290)
        mountain_a.dy *= -1

    if mountain_a.ycor() < -290:
        mountain_a.sety(290)
        mountain_a.dy *= -1

    if mountain_a.xcor() > 390:
        mountain_a.goto(0, 0)
        mountain_a.dx *= -1

    if mountain_a.xcor() < -390:
        mountain_a.goto(0, 0)
        mountain_a.dx *= -1

    # border checking moutnain_b
    if mountain_b.ycor() > 290:
        mountain_b.sety(-290)
        mountain_b.dy *= -1

    if mountain_b.ycor() < -290:
        mountain_b.sety(290)
        mountain_b.dy *= -1

    if mountain_b.xcor() > 390:
        mountain_b.goto(0, 0)
        mountain_b.dx *= -1

    if mountain_b.xcor() < -390:
        mountain_b.goto(0, 0)
        mountain_b.dx *= -1
    
    # border color
    