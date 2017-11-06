# myArtApp.py

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

background = "treescape.gif"
pen_up = False
current_line = None

#### Functions. 함수
def move(x, y):
    global x_coord
    global y_coord
    global current_line
    new_x_coord = x_coord + x
    new_y_coord = y_coord + y
    # add the pen_up code here. pen_up 코드는 여기에 입력합니다.
    if ((pen_up == False) or (current_line == None)):
        current_line = canvas.create_line(x_coord, y_coord, new_x_coord, new_y_coord,
                                          width=line_width, fill=line_colour)
    else:
        ## make sure width and colour is OK (bug fix)
        ## 색과 폭이 맞는지 확인합니다.
        canvas.itemconfigure(current_line, width=line_width, fill=line_colour)
        
        # move the current line to a new position.
        # 새 위치로 줄을 이동합니다.
        canvas.coords(current_line, x_coord, y_coord, new_x_coord, new_y_coord)

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
    canvas.create_image(0, 0, image=scene, anchor=NW)
    
def pen_lift(event):
    global pen_up
    pen_up = True

def pen_down(event):
    global pen_up
    pen_up = False

## add new functions here. 새 함수는 여기에 입력합니다.
def line_red():
    global line_colour
    line_colour = "red"

def line_green():
    global line_colour
    line_colour = "green"

def line_blue():
    global line_colour
    line_colour = "blue"

def line_yellow():
    global line_colour
    line_colour = "yellow"

def line_black():
    global line_colour
    line_colour = "black"

def line_white():
    global line_colour
    line_colour = "white"

def smaller():
    global line_width
    global line_length
    if (line_width > 5):
        line_width = line_width-5
        line_length = line_length-5

def bigger():
    global line_width
    global line_length
    if (line_width <= 50):
        line_width = line_width+5
        line_length = line_length+5

#### main. 메인
window = Tk()
window.title("MyArtApp")
canvas = Canvas(bg=canvas_colour, height=canvas_height,
                width=canvas_width, highlightthickness=0)
scene = PhotoImage(file=background)
canvas.create_image(0, 0, image=scene, anchor=NW)
canvas.pack()

# bind movement to keys. 키보드 키를 연결합니다.
window.bind("<Up>", move_N)
window.bind("<Down>", move_S)
window.bind("<Left>", move_W)
window.bind("<Right>", move_E)
window.bind("e", erase_all)
window.bind("u", pen_lift)
window.bind("d", pen_down)

## load images for top buttons. 상단 버튼 이미지를 불러옵니다.
red = PhotoImage(file="red.gif")
blue = PhotoImage(file="blue.gif")
green = PhotoImage(file="green.gif")
yellow = PhotoImage(file="yellow.gif")
black = PhotoImage(file="black.gif")
white = PhotoImage(file="white.gif")
plus = PhotoImage(file="plus.gif")
minus = PhotoImage(file="minus.gif")

## build top set of buttons. 상단 버튼을 만듭니다.
Button(window, image=red, command=line_red).pack(side=LEFT)
Button(window, image=green, command=line_green).pack(side=LEFT)
Button(window, image=blue, command=line_blue).pack(side=LEFT)
Button(window, image=yellow, command=line_yellow).pack(side=LEFT)
Button(window, image=black, command=line_black).pack(side=LEFT)
Button(window, image=white, command=line_white).pack(side=LEFT)
Button(window, image=plus, command=bigger).pack(side=LEFT)
Button(window, image=minus, command=smaller).pack(side=LEFT)

# start tkinter's main loop. tkinter의 메인 반복을 시작합니다.
window.mainloop()
