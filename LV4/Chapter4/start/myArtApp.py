# myArtApp.py
# based on the code from myEtchASketch.py in Python Basics.
# 『코딩 클럽 LV1. 모두를 위한 파이썬 기초』의 myEtchASketch.py

from tkinter import *

#### Set variables. 변수를 정합니다.
canvas_height = 400
canvas_width = 600
canvas_colour = "black"
x_coord = canvas_width/2
y_coord = canvas_height
line_colour = "red"
line_width = 5
line_length = 5

## new variables go here. 새 변수는 여기에 입력합니다.


#### Functions. 함수
def move(x, y):
    global x_coord
    global y_coord
    new_x_coord = x_coord + x
    new_y_coord = y_coord + y
    ## add the pen_up code here. pen_up 코드는 여기에 입력합니다.

    
    canvas.create_line(x_coord, y_coord, new_x_coord, new_y_coord,
                       width=line_width, fill=line_colour)
    x_coord = new_x_coord
    y_coord = new_y_coord
    
def move_N(event):
    move(0, -line_length)

def move_S(event):
    move(0, line_length)

def move_E(event):
    move(line_length, 0)
    
def move_W(event):
    move(-line_length, 0)
    
def erase_all(event):
    canvas.delete(ALL)

## add new functions here. 새 함수는 여기에 입력합니다.

#### main. 메인
window = Tk()
window.title("MyArtApp")
canvas = Canvas(bg=canvas_colour, height=canvas_height,
                width=canvas_width, highlightthickness=0)

## background image code goes here. 배경화면 코드는 여기에 입력합니다.

canvas.pack()

# bind movement to keys. 키보드 키를 연결합니다.
window.bind("<Up>", move_N)
window.bind("<Down>", move_S)
window.bind("<Left>", move_W)
window.bind("<Right>", move_E)
window.bind("e", erase_all)

# start tkinter's main loop. tkinter의 메인 반복을 시작합니다.
window.mainloop()
