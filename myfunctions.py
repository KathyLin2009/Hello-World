import random
import turtle
ana = turtle.Pen()
ana.shape("turtle")
ana.width(3)
ana.speed(0)
colorlist = ["violet", "cyan", "blue", "hot pink"]

def square(size):
    for i in range(4):
        ana.forward(size)
        ana.left(90)

for i in range(100):       
        x = random.randrange(-500, 500)
        y = random.randrange(-400, 400)
        ana.up()
        ana.goto(x, y)
        ana.down()
        col = random.choice(colorlist)
        ana.color(col)
        square(random.randrange(10, 200))
ana.reset()
ana.shape("turtle")
ana.width(3)
ana.speed(0)
colorlist = ["violet", "cyan", "blue", "hot pink"]
def star(size):
        ana.left(90)
        ana.circle(100)
        ana.up
        ana.forward(100)
        ana.down
        ana.circle(100)
        ana.forward(100)
        ana.left(90)
        ana.circle(100)
        ana.up
        ana.forward(100)
        ana.down
        ana.circle(100)
        ana.forward(100)
        ana.left(90)
        ana.circle(100)
        ana.up
        ana.forward(100)
        ana.down
        ana.circle(100)
        ana.forward(100)
        ana.left(90)
        ana.circle(100)
        ana.up
        ana.forward(100)
        ana.down
        ana.circle(100)
for i in range(50):       
        x = random.randrange(-500, 600)
        y = random.randrange(-400, 300)
        ana.up()
        ana.goto(x, y)
        ana.down()
        col = random.choice(colorlist)
        ana.color(col)
        star(random.randrange(10, 200))