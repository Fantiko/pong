import turtle

#   config iniciais
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#   barra A
barra_a = turtle.Turtle()
barra_a.speed(0)
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=5, stretch_len=1)
barra_a.penup()
barra_a.goto(-350, 0)

#   barra b
barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=5, stretch_len=1)
barra_b.penup()
barra_b.goto(350, 0)

#   Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.dx = 0.3
bola.dy = .3



#   funçoes
def barra_a_up():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)


def barra_a_down():
    y = barra_a.ycor()
    y -= 20
    barra_a.sety(y)


def barra_b_up():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)


def barra_b_down():
    y = barra_b.ycor()
    y -= 20
    barra_b.sety(y)


#   teclado

wn.listen()
wn.onkeypress(barra_a_up, "w")
wn.onkeypress(barra_a_down, "s")
wn.onkeypress(barra_b_up, "8")
wn.onkeypress(barra_b_down, "5")

#   main game loop
while True:
    wn.update()
    #   Move a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0)

    if bola.xcor() < -390:
        bola.goto(0)
