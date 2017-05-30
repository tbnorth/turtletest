import turtle

STEPS = 12           # number of steps along stem
SIZE = 120           # basic size
ANG = 55             # angle between stem and branches
ROT = 4              # extra curl angle
MIN_SIZE = 3         # minimum branch size
BRANCH_RATIO = 0.25  # length of branches vs stem
STEM_RATIO = 0.5     # length of blank stem

shelly = turtle.Turtle()
screen = shelly.getscreen()

screen.tracer(10, 10)

shelly.penup()
shelly.setposition((-300, -300))
shelly.setheading(45)
shelly.pendown()

def branch(size):

    position = shelly.position()
    heading = shelly.heading()

    shelly.forward(STEM_RATIO*size)
    for i in range(STEPS):
        length = size * float(STEPS-i) / STEPS
        if length > MIN_SIZE:
            shelly.left(ANG-i*ROT)
            branch(length*BRANCH_RATIO)
            shelly.right(ANG*2+i*ROT)
            branch(length*BRANCH_RATIO)
            shelly.left(ANG+i*ROT)
        shelly.forward(length)

    shelly.penup()
    shelly.setposition(position)
    shelly.setheading(heading)
    shelly.pendown()

branch(SIZE)

screen.update()

raw_input()

