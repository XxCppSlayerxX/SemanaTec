"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

#Libraries used in the code
from random import randrange
from turtle import *

from freegames import vector

#Variables used in the code, ball is the projectile, speed is the speed of the projectile, targets is the list of targets
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball): #If the ball is not inside the screen, the ball will be placed at the position of the tap
        ball.x = -199
        ball.y = -199
        speed.x = (x + 600) / 25 #made faster the movemnt of the ball
        speed.y = (y + 600) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200 #Returns True if the xy is inside the screen, False if it is not


def draw():
    """Draw ball and targets."""
    clear()
    
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2 #The targets will move to the left at a faster pace

    if inside(ball):
        #The speed of the ball wont be reduced
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 35)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
