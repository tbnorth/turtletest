import turtle

STEPS = 12
TURN = 360 / STEPS
SIZE = 200

shelly = turtle.Turtle()

for step in range(STEPS):
    shelly.forward(SIZE)
    shelly.right(90)
    shelly.forward(10)
    # shelly.back(10)
    shelly.left(90)  # 80
    shelly.back(SIZE)
    shelly.right(TURN)

raw_input()
