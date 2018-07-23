# MonChefDoeuvre1171.py
#
# Description: Creates a drawing (using Turtle) representing a night time city scene.
#              The drawing contains three buildings, windows for each building,
#              A flag, the moon, and fifteen stars. 
#
# Peter Tran
#
# March 2017

# Import modules necessary for program:
# We will use the random module to draw the stars in random locations.
# We will use turtle to draw
import random
import turtle as t


# Build function to make squares/rectangles (To make buildings)
def createBuilding(length, height, x, y, colour) :
    """ Draws rectangles which represent buildings.
        parameters: length and height of rectangle, x and y
        coordinates, and colour of rectangle.
        Return: none
    """
    t.up()
    t.setpos(x, y)
    t.down()
    t.begin_fill()
    for index in range(2) :
        t.fd(length)
        t.lt(90)
        t.fd(height)
        t.lt(90)
    t.color(colour)
    t.end_fill()
    return

# Build function to make smaller rows and columns of squares (Windows for buildings)
def windows(row, column, x, y, colour) :
    """ Draws 'x' rows and 'y' columns of small squares, representing
        windows for the buildings.
        Parameters: Rows of windows, columns of windows, x and y
        coordinates, and what colour.
        Return: none
    """
    t.color(colour)
    t.up()
    t.setpos(x,y)
    for index in range(row):
        for i in range(column):
            t.begin_fill()
            t.down()
            for win in range(4):
                t.forward(20)
                t.right(90)
            t.up()
            t.end_fill()
            t.forward(30)
        t.backward(30 * column)
        t.right(90)
        t.forward(30)
        t.left(90)
    return

# Build function that makes a circle (The moon)
def moon(x, y, colour) :
    """ Creates a circle, representing the moon.
        Parameters: x and y coordinates, colour.
        Return: none.
    """
    t.up()
    t.color(colour)
    t.setpos(x,y)
    t.down()
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    return

# Build function that makes a straight green line (The grass)
def grass(thickness) :
    """ Makes a straight line. Represents the grass.
        Parameters: thickness represents pensize.
        Return: none
    """
    t.pensize(thickness)
    t.up()
    t.setpos(-350,-100)
    t.color("green")
    t.down()
    t.setpos(350,-100)
    return

# Build function that makes a bunch of stars.
def stars() :
    """ Makes star shapes to represent stars.
        Parameters: none
        Return: none
    """
    x = random.randint(-300,300)
    y = random.randint(100,180)
    t.up()
    t.color("yellow")
    t.setpos(x,y)
    t.down()
    for index in range(5) :        
        t.fd(15)
        t.rt(144)
    return

# Build function to create a flagpole and a flag
def flagPole(cPole, cFlag):
    """ Makes a flag and flagpole (a squate attached to a line)
        Parameters: colour of the pole, colour of the flag
        Return: none
    """
    t.color(cPole)
    t.up()
    t.setpos(150,-100)
    t.down()
    t.lt(90)
    t.fd(150)
    t.color(cFlag)
    t.begin_fill()
    for index in range(4):        
        t.lt(90)
        t.fd(40)
    t.end_fill()
    return

# Build a function that makes the SFU logo for the flag
def sfu() :
    """ Draws a white 'SFU' logo onto the flag.
        Parameters: none
        Return: none
    """
    t.color("white")
    t.up()
    t.setpos(117, 40)
    t.down()
    # Draw 'S'
    for s in range(3) :
        t.lt(90)
        t.fd(5)
    for s in range(2) :
        t.rt(90)
        t.fd(5)
    t.up()
    
    # Draw 'F'  
    t.setpos(122, 40)
    t.down()
    t.back(5)
    t.fd(5)
    t.lt(90)
    t.fd(5)
    t.rt(90)
    t.back(5)
    t.fd(5) 
    t.lt(90)
    t.fd(5)
    t.up()
    
    # Draw 'U'   
    t.setpos(135, 40)
    t.down()
    t.fd(10)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(10)
        
### Main part of the program - top level (of execution) ###

# Set background to black
window = t.Screen()
window.bgcolor("black")

# Draw the moon at given coordinates (x,y) and paint it white
moon(250, 180, "white")

# Create building of given length and width, at given coordinates and colour
createBuilding(100, 100, 0, -100, "grey")

# Create second building, similar conditions.
createBuilding(125, 185, -200, -100, "dim grey")

# Create third building, similar conditions.
createBuilding(100, 175, 200, -100, "silver")

# Windows for the first building: (Rows, columns, x, y coordinates, colour)
windows(2,3,10,-20,"royal blue")

# Windows for the second building, similar conditions
windows(4,3,-180,65,"navy")

# Windows for the third building, similar conditions.
windows(5,2,225,55, "midnight blue")

# Change pensize
t.pensize(2)

# Create a flag (Pole colour, flag colour)
flagPole("grey", "red")

# Change pensize
t.pensize(1)

# Draw 'SFU' logo on the flag
sfu()

# Draw 15 Stars
for i in range(0, 15) :
    stars()

# Draw grass, with 5 pensize for extra thickness.
grass(5)
