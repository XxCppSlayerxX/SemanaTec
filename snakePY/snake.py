"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
#Libraries used in the code
from random import randrange, choice
from turtle import *

from freegames import square, vector

colors = ['blue', 'green', 'yellow', 'orange', 'purple']


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():

    global food_color, snake_color

    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        food_color = choice(colors)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

#randomly wiht low chances, move food one segment in any direction each step, without going out of the screen
def moveFood():
    rand = randrange(0, 100)
    if(rand < 25 and inside(food)):
        food.x += randrange(-1, 2) * 10
        food.y += randrange(-1, 2) * 10
    ontimer(moveFood, 200)


food_color = choice(colors)
snake_color = choice([color for color in colors if color != food_color])

#randomly wiht low chances, move food one segment in any direction each step, without going out of the screen
def moveFood():
    rand = randrange(0, 100)
    if(rand < 25 and inside(food)):
        food.x += randrange(-1, 2) * 10
        food.y += randrange(-1, 2) * 10
    ontimer(moveFood, 200)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
moveFood()
move()
moveFood()
done()
