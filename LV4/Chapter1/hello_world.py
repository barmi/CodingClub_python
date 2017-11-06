# hello_world.py introduces the turtle module.
# hello _ world.py 프로그램은 turtle 모듈을 소개합니다.
from turtle import *

# change line width. 선의 너비를 조절합니다. 
pensize(5)

# change to an actual turtle. 모양을 거북이(turtle)로 바꿉니다.
shape("turtle")

# draw the letter H. H를 그립니다. H를 어떻게 그릴지 상상해보세요.
left(90)
forward(100)
back(50)
right(90)
forward(40)
left(90)
forward(50)
back(100)

# Move to start of next letter.
# 다음 글자를 그릴 시작 위치로 거북이를 이동합니다. 
penup()
right(90)
forward(40)
left(90)
pendown()

# Draw the letter i. Hello World를 다 그리려면 시간이 걸리니 Hi만 그리도록 하겠습니다. 이번엔 i를 그립니다.
forward(50)
penup()
forward(25)

# tell tkinter to stop waiting for turtle instructions.
# turtle 명령어 입력이 끝났습니다.
done()
