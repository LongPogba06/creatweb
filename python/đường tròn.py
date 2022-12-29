
import turtle
import random 
import time
t = turtle.Turtle()

t.speed(0)
colors = ["red", "blue", "green", "purple"]

for i in range(30):
    t.color(random.choice(colors))
    t.circle(100)
    t.left(12)

time.sleep(3)