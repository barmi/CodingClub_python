# ourEtchASketch 응용 어플리케이션

from tkinter import *

##### 변수 설정:
canvas_height=400
canvas_width=600
canvas_colour="black"
p1_x=canvas_width * (2 / 3)
p1_y=canvas_height
p1_colour='red'
p2_x=canvas_width / 3
p2_y=canvas_height
p2_colour='green'
line_width=5
line_length=5

##### 함수들:

# 사용자 콘트롤
def move(player, x, y):
    global p1_x
    global p1_y
    global p2_x
    global p2_y
    if(player == 1):
        p1_new_x = p1_x + x
        p1_new_y = p1_y + y
        canvas.create_line(p1_x, p1_y, p1_new_x, p1_new_y, width=line_width, fill=p1_colour)
        p1_x = p1_new_x
        p1_y = p1_new_y
    else:
        p2_new_x = p2_x + x
        p2_new_y = p2_y + y
        canvas.create_line(p2_x, p2_y, p2_new_x, p2_new_y, width=line_width, fill=p2_colour)
        p2_x = p2_new_x
        p2_y = p2_new_y

def p1_move_N(event):
    move(1, 0, -line_length)

def p1_move_S(event):
    move(1, 0, line_length)

def p1_move_E(event):
    move(1, line_length, 0)
    
def p1_move_W(event):
    move(1, -line_length, 0)

def p2_move_N(event):
    move(2, 0, -line_length)

def p2_move_S(event):
    move(2, 0, line_length)

def p2_move_E(event):
    move(2, line_length, 0)
    
def p2_move_W(event):
    move(2, -line_length, 0)

def erase_all(event):
    canvas.delete(ALL)

##### 메인:
window = Tk()
window.title("OurEtchaSketch")
canvas=Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

# 키를 눌렀을 때 움직임
window.bind('<Up>', p1_move_N)
window.bind('<Down>', p1_move_S)
window.bind('<Left>', p1_move_W)
window.bind('<Right>', p1_move_E)
window.bind('w', p2_move_N)
window.bind('s', p2_move_S)
window.bind('a', p2_move_W)
window.bind('d', p2_move_E)
window.bind('u', erase_all)

window.mainloop()
