# many_circles.py
import turtle
t=turtle

#set variables. 변수를 정합니다.
size=50
distance=50
angle=20

# speed things up. 속도를 조절합니다.
t.speed(0) # 1=slow, 10=fast, 0=fastest. 1=느리게, 10=빠르게, 0=최대 빠르게

# Draw the pattern. 패턴을 그립니다.
n=0
while n < 18:
    # draw a circle. 원을 그립니다.
    t.pendown()
    t.circle(size)
    t.penup()

    # move start position. 시작점으로 이동합니다.
    t.forward(distance)
    t.left(angle)
    
    n=n+1

# hide the turtle when it has finished drawing.
# 다 그렸으면 거북이를 숨깁니다.
t.hideturtle()

# end. 끝
t.done()
