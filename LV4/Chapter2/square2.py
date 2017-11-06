# square2.py
import turtle
t=turtle

def square(side_length):
    n=0
    while n < 4:
        t.forward(side_length)
        t.right(90)
        n = n+1

# Draw a square. 사각형을 그립니다.
square(50)

# end. 끝
t.done()
