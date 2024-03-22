"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""
#Libraries used in the code
from random import *
from turtle import *

from freegames import path

#Variables used in the code
car = path('car.gif')
tiles = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456") * 2
state = {'mark': None}
hide = [True] * 64

#Count Taps
tapCount = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    #Draws a square with the given coordinates
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    global tapCount #Global variable to count taps
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    #If the mark is None or the mark is the same as the spot or the tiles in the mark and the spot are different, the mark will be the spot
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        tapCount += 1 #Count taps


def draw():
    """Draw image and tiles."""
    global tapCount #Global variable to count taps
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    #If the mark is not None and the hide in the mark is True, the x and y will be the coordinates of the mark and the tiles in the mark will be written in the screen  
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 14, y - 3)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Display tap count
    up()
    goto(-180, 180)  # Adjust coordinates as needed
    color('black')
    write(f'Tap Count: {tapCount}', font=('Arial', 16, 'normal'))
    
    # Check if all tiles are revealed
    if all(h == False for h in hide):
        up()
        goto(-50, 0)  # Adjust coordinates as needed
        color('black')
        write("¡Todos los cuadros se han destapado!", font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
