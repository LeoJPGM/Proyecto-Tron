"""Juego TRON"""

from turtle import *
from freegames import square, vector

player1 = vector(-100, 0)
velocidad1 = vector(4, 0)
Linea1 = set()

player2 = vector(100, 0)
velocidad2 = vector(-4, 0)
Linea2 = set()

def inside(head):
    "SI no esta dentro del rango no se puede jugar."
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    "Movimiento del jugador y rastro."
    player1 .move(velocidad1)
    cabeza1 = player1 .copy()

    player2.move(velocidad2)
    cabeza2 = player2.copy()

    if not inside(cabeza1) or cabeza1 in Linea2:
        print('Jugador azul gana!')
        return

    if not inside(cabeza2) or cabeza2 in Linea1:
        print('Jugador rojo gana!')
        return
    
    if not inside(cabeza1) or cabeza2 in Linea2:
        print('Jugador rojo gana!')
        return

    if not inside(cabeza2) or cabeza1 in Linea1:
        print('Jugador azul gana!')
        return
    
    Linea1.add(cabeza1)
    Linea2.add(cabeza2)

    square(player1 .x, player1 .y, 3, 'red')
    square(player2.x, player2.y, 3, 'blue')
    update()
    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: velocidad1.rotate(90), 'a')
onkey(lambda: velocidad1.rotate(-90), 'd')
onkey(lambda: velocidad2.rotate(90), 'Left')
onkey(lambda: velocidad2.rotate(-90), 'Right')
draw()
done()