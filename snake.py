import turtle
import time
import random

#Constante-----------------------------------------------------------------------
posponer = 0.1


#Ventana-------------------------------------------------------------------------
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake------------------------------------------------------------------------
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"


#Funciones-----------------------------------------------------------------

#direcciones de snake
def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"


#Velocidad de movimiento
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    elif cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    elif cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    elif cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#juego -------------------------------------------------------------------------
def juego():
    #interacion del teclado
    wn.listen()
    wn.onkeypress(arriba,"Up")
    wn.onkeypress(abajo,"Down")
    wn.onkeypress(izquierda,"Left")
    wn.onkeypress(derecha,"Right")

    while True:
        wn.update()
        mov()
        time.sleep(posponer)


juego()