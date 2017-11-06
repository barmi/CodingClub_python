# fractal_tree.py
import turtle
t=turtle

# set variables. 변수를 정합니다.
detail=12 #decrease for more branches. 나뭇가지의 숫자를 감소시킵니다.
length=80 # increase for larger tree. 더 많은 나무를 만듭니다.
thickness=20 # vary to see effect. 더 많은 변이를 만듭니다.
angle=20 # vary to see effect. 더 많은 변이를 만듭니다.

t.speed(0) # 1=slow, 10=fast, 0=fastest 1=느리게, 10=빠르게, 0=최대 빠르게

def draw_tree(branch_thickness, branch_length):
    if branch_length > 5:
        if branch_length < 20:
            t.color("green")
        else:
            t.color("brown")
        t.pensize(branch_thickness)
        t.forward(branch_length)
        t.right(angle)
        draw_tree(branch_thickness/1.5, branch_length-detail)
        t.left(2*angle)
        draw_tree(branch_thickness/1.5, branch_length-detail)
        t.right(angle)
        t.back(branch_length)
        t.color("brown")

# move turtle down the screen and turn to face up.
# 얼굴을 위로 오게 돌린 후 거북이를 화면 아래로 움직입니다.
t.left(90)
t.penup()
t.back(100)
t.pendown()

# set pen color and call the main function. 펜 색을 정하고 메인 함수를 부릅니다.
t.color("brown")
draw_tree(thickness, length)
t.done()
