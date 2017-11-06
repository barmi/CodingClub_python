# squares.py
from turtle import *

def square(side_length):
    n=0
    while n < 4:
        forward(side_length)
        right(90)
        n = n+1

# Draw the first square with 50pixel sides.
# 한 면이 50픽셀인 첫 번째 사각형을 그립니다.
left(90)
square(50)

# move the turtle. 거북이를 움직입니다.
penup()
right(90)
forward(100)
left(90)
pendown()

# draw the second square. 두 번째 사각형을 그립니다.
square(50)

# Tell Python to stop waiting for turtle instructions.
# turtle 명령어 입력이 끝났습니다.
done()
