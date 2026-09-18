"""Snake con colores aleatorios y comida que se mueve."""

from random import choice, sample
from turtle import *

from freegames import square, vector

# Cinco colores posibles, sin rojo.
colors = ['black', 'green', 'blue', 'purple', 'orange']
snake_color, food_color = sample(colors, 2)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Comprueba si un punto está dentro del área de juego."""
    return -200 < head.x < 190 and -200 < head.y < 190


def place_food():
    """Coloca la comida en una casilla libre."""
    available = [
        vector(x, y)
        for x in range(-190, 190, 10)
        for y in range(-190, 190, 10)
        if vector(x, y) not in snake
    ]

    if not available:
        return False

    position = choice(available)
    food.x = position.x
    food.y = position.y
    return True


def move_food():
    """Intenta mover la comida un paso al azar."""
    step = choice([
        vector(10, 0),
        vector(-10, 0),
        vector(0, 10),
        vector(0, -10),
    ])

    next_food = food.copy()
    next_food.move(step)

    if inside(next_food) and next_food not in snake:
        food.x = next_food.x
        food.y = next_food.y


def move():
    """Mueve la serpiente y la comida."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        # El rojo solo indica una colisión.
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    won = False

    if head == food:
        print('Snake:', len(snake))
        won = not place_food()
    else:
        snake.pop(0)
        move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    if not won:
        square(food.x, food.y, 9, food_color)

    update()

    if won:
        print('¡Ganaste!')
        return

    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
