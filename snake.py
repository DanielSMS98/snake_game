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
cuerpo = []

#alimento--------------------------------------------------------------------------
alimento = turtle.Turtle()
alimento.speed(0)
alimento.shape("circle")
alimento.color("red")
alimento.penup()
alimento.goto(0,100)


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
        
        
        #coliciones con los bordes
        if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
            time.sleep(1)
            alimento.goto(0,100)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            for c in cuerpo:
                c.hideturtle()
            cuerpo.clear()
            
        
        if cabeza.distance(alimento) < 20 :
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            alimento.goto(x,y)

            c = turtle.Turtle()
            c.speed(0)
            c.shape("square")
            c.color("grey")
            c.penup()
            cuerpo.append(c)
        
        #mover el cuerpo
        segmentos = len(cuerpo)
        for i in range(segmentos - 1, 0, -1):
            x = cuerpo[i - 1].xcor()
            y = cuerpo[i - 1].ycor()
            cuerpo[i].goto(x,y)
        if segmentos > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpo[0].goto(x,y)
        
            
        
        mov()
        time.sleep(posponer)


juego()