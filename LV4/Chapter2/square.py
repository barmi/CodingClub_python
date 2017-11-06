# square.py
from turtle import *

# set up some variables. 변수를 정합니다.
side_length=50
n=0

while n < 4:
    forward(side_length)
    right(90)
    n = n+1

# Tell Python to stop waiting for turtle instructions.
# turtle 명령어 입력이 끝났습니다.
done()
