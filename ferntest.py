# import the turtle library
import turtle

# number of steps along stem
STEPS = 12
# basic size
SIZE = 120
# angle between stem and branches
ANG = 55
# extra curl angle
ROT = 5
# minimum branch size
MIN_SIZE = 3
# length of branches vs stem
BRANCH_RATIO = 0.25
# length of blank stem
STEM_RATIO = 0.5

# make our turtle, called shelly, from the Turtle class in the turtle library
shelly = turtle.Turtle()
# get the screen that shelly lives on
screen = shelly.getscreen()
# control how fast the screen updates
screen.tracer(100, 500)

# move shelly the bottom left corner, facing north-east
# put the pen up while moving to avoid leaving a trail
shelly.penup()
shelly.setposition((-300, -300))
shelly.setheading(45)
shelly.pendown()

# make a function
def branch(size):
    """Draw a branch `size` units long."""

    # remember where we started
    position = shelly.position()
    heading = shelly.heading()

    shelly.forward(STEM_RATIO*size)  # make the stem

    for i in range(STEPS):  # go through this STEPS times, from zero
        length = size * float(STEPS-i) / STEPS  # length of this step
        if length > MIN_SIZE:           # if long enough, make branches here
            shelly.left(ANG-i*ROT)      # turn for left branch
            branch(length*BRANCH_RATIO) # call this function to make the branch
            shelly.right(ANG*2+i*ROT)   # turn for right branch
            branch(length*BRANCH_RATIO) # call this function to make the branch
            shelly.left(ANG+i*ROT)      # turn back to original direction
        shelly.forward(length)  # finally move down the branch

    # go back where we started, with the pen up
    shelly.penup()
    shelly.setposition(position)
    shelly.setheading(heading)
    shelly.pendown()

# make the main branch
branch(SIZE)

# show what we've done
screen.update()

# wait for user to press a key
raw_input()

