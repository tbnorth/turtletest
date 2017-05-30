import turtle

STEPS = 12
TURN = 360 / STEPS
SIZE = 120
ANG = 55
ROT = 4
MIN_SIZE = 3
VEIN_RATIO = 0.25
STEM_RATIO = 0.5

shelly = turtle.Turtle()
screen = shelly.getscreen()

screen.tracer(10, 10)

shelly.penup()
shelly.setposition((-300, -300))
shelly.setheading(45)
shelly.pendown()

def vein(size):
    
    position = shelly.position()
    heading = shelly.heading()
    
    shelly.forward(STEM_RATIO*size)
    for i in range(STEPS):
        length = size * float(STEPS-i) / STEPS
        if length > MIN_SIZE:
            shelly.left(ANG-i*ROT)
            vein(length*VEIN_RATIO)
            shelly.right(ANG*2+i*ROT)
            vein(length*VEIN_RATIO)
            shelly.left(ANG+i*ROT)
        shelly.forward(length)

    shelly.penup()
    shelly.setposition(position)
    shelly.setheading(heading)
    shelly.pendown()

vein(SIZE)

screen.update()

raw_input()

