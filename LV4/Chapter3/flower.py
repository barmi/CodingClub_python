# flower.py
# this is a really cool little program slightly adapted from:
# http://docs.python.org/3.3/library/turtle.html
# 이 프로그램은 http://docs.python.org/3.3/library/turtle.html 프로그램을 약간 수정한 프로그램입니다.

import turtle
t=turtle

t.speed(8)

# set the colour and fill values in one go. 색을 정하고 입력합니다.
t.color("green", "purple")

# draw the star. 별 모양의 꽃을 그립니다.
t.begin_fill()
while True:
    t.forward(150)
    t.left(170)
    if t.distance(0,0)<1:
        break
t.end_fill()

# hide the turtle when it has finished drawing. 다 그렸으면 거북이를 숨깁니다.
t.hideturtle()

# end. 끝
t.done()
