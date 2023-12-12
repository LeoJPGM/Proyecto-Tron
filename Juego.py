"""Tron, classic arcade game."""

from turtle import *
from freegames import square, vector

player1 = vector(-100, 0)
velocidad1 = vector(2, 0)
Linea1 = set()

player2 = vector(100, 0)
velocidad2 = vector(-2, 0)
Linea2 = set()

juego = False

contadorrojo = 0
contadorazul = 0

def inside(head):
    "Return True if head inside screen."
    return -200 < head.x < 200 and -200 < head.y < 200

def empezar_juego():
    global juego
    juego = True
    reset_game ()

def reset_game ():
    global juego, Linea1, Linea2, player1, player2, velocidad1, velocidad2
    Linea1.clear()
    Linea2.clear()
    juego = False
    player1 = vector(-100, 0)
    velocidad1 = vector(2, 0)
    player2= vector (100, 0)
    velocidad2 = vector(-2, 0)
    update()
    draw()

def draw_jugadores():
    
    square(player1.x, player1.y, 3, 'red')
    square(player2.x, player2.y, 3, 'blue') 

def draw_contador():
    penup()
    goto(-190, 180)
    pendown()
    write(f'Victorias rojo: {contadorrojo}', font=('Arial', 12, 'normal'))
    penup()
    goto(70, 180)
    pendown()
    write(f'Victorias azul: {contadorazul}', font=('Arial', 12, 'normal'))

def draw():
    global contadorrojo, contadorazul
    "Advance players and draw game."
    player1 .move(velocidad1)
    cabeza1 = player1 .copy()

    player2.move(velocidad2)
    cabeza2 = player2.copy()

    if not inside(cabeza1) or cabeza1 in Linea2:
        print('Player blue wins!')
        contadorazul += 1
        return

    if not inside(cabeza1) or cabeza1 in Linea1:
        print('Player blue wins!')
        contadorazul += 1
        return
    
    if not inside(cabeza2) or cabeza2 in Linea1:
        print('Player red wins!')
        contadorrojo += 1
        return

    if not inside(cabeza2) or cabeza2 in Linea2:
        print('Player red wins!')
        contadorrojo += 1
        return

    Linea1.add(cabeza1)
    Linea2.add(cabeza2)

    clear()
    for segment in Linea1:
        square(segment.x, segment.y, 3, 'red')
    for segment in Linea2:
        square(segment.x, segment.y, 3, 'blue')

    draw_contador() 
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
onkey(empezar_juego, 'space')
draw()
done()