# ch5_Answers

# 퍼즐의 답
# myEtchASketch2 코딩클럽 : 파이썬 기초편의 myEtchASketch2 어플리케이션입니다.

from tkinter import *

canvas_height = 400
canvas_width = 600
canvas_color = "black"
p1_x=canvas_width/2
p1_y=canvas_height
p1_colour='green'
line_width=5
line_length=5

def p1_move(x, y):
    global p1_x
    global p1_y
    p1_new_x = p1_x + x
    p1_new_y = p1_y + y
    canvas.create_line(p1_x, p1_y, p1_new_x, p1_new_y, width=line_width, fill=p1_colour)
    p1_x = p1_new_x
    p1_y = p1_new_y
    
def p1_move_N(event):
    p1_move(0, -line_length)

def p1_move_S(event):
    p1_move(0, line_length)

def p1_move_E(event):
    p1_move(line_length, 0)
    
def p1_move_W(event):
    p1_move(-line_length, 0)
    
def erase_all(event):
    canvas.delete(ALL)

window = Tk()
window.title("MyEtchaSketch")
canvas = Canvas(bg=canvas_color, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("u", erase_all)

window.mainloop()
