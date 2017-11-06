# colourful.py
import turtle
t=turtle

#set variables. 변수를 정합니다.
size=50
distance=50
angle=20
t.speed(0)
t.shape("turtle")
t.bgcolor("blue")

n=0
while n < 18:
    # draw a square. 사각형을 그립니다.
    t.pendown()
    t.pensize(4)
    t.color("yellow")
    t.circle(size, steps=4)
    t.penup()

    # move start position. 시작점으로 이동합니다.
    t.forward(distance)
    t.left(angle)
    
    n=n+1

t.setposition(5,30)

size=50
distance=40

n=0
while n < 18:
    # draw a circle. 원을 그립니다.
    t.pendown()
    t.pensize(4)
    t.color("orange")
    t.circle(size)
    t.penup()

    # move start position. 시작점으로 이동합니다.
    t.forward(distance)
    t.left(angle)
    
    n=n+1

# move turtle. 거북이를 움직입니다.
t.setposition(22,144)
t.color("red")

# end. 끝
t.done()
