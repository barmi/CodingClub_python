# BonusArtApp2.py
# all keyboard control removed except "e" is still used to erase the canvas.
# 화면을 지우는 'e' 키를 제외한 다른 키보드 명령은 전부 삭제했습니다. 
from tkinter import *
import random

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
current_line = None
current_image = None

#### Functions. 함수
def move(x, y):
    global x_coord
    global y_coord
    global current_line
    new_x_coord = x_coord + x
    new_y_coord = y_coord + y
    if (current_line == None):
        current_line = canvas.create_line(x_coord, y_coord, new_x_coord, new_y_coord, width=line_width, fill=line_colour)
    else:
        canvas.coords(current_line, x_coord, y_coord, new_x_coord, new_y_coord)

    x_coord = new_x_coord
    y_coord = new_y_coord
    
def erase_all(event):
    canvas.delete(ALL)
    canvas.create_image(0, 0, image=scene, anchor=NW)

def line_red():
    global line_colour
    global current_image
    current_image = None
    line_colour = "red"

def line_green():
    global line_colour
    global current_image
    current_image = None
    line_colour = "green"

def line_blue():
    global line_colour
    global current_image
    current_image = None
    line_colour = "blue"

def line_yellow():
    global line_colour
    global current_image
    current_image = None
    line_colour = "yellow"

def line_black():
    global line_colour
    global current_image
    current_image = None
    line_colour = "black"

def line_white():
    global line_colour
    global current_image
    current_image = None
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
    
def use_tree():
    paint_with_image(tree)

def use_campbell():
    paint_with_image(campbell)

def use_ayesha():
    paint_with_image(ayesha)

def use_jeff():
    paint_with_image(jeff)

def use_krysta():
    paint_with_image(krysta)

def use_hana():
    paint_with_image(hana)

def use_jose():
    paint_with_image(jose)

def use_leela():
    paint_with_image(leela)

def paint(event):
    if (current_image != None):
        canvas.create_image(event.x, event.y, image=current_image, anchor=S)
    else:
        width = line_width/2
        x1 = event.x - width
        y1 = event.y - width
        x2 = event.x + width
        y2 = event.y + width
        canvas.create_oval(x1, y1, x2, y2, fill=line_colour, outline="")

def paint_with_image(img):
    global current_image
    current_image = img

def make_crowd():
    n=0
    while n < 150:
        choice = random.randint(1, 7)
        x = random.randint (0, canvas_width+20)
        y = random.randint (70, canvas_height+50)
        if choice == 1:
            canvas.create_image(x, y, image = ayesha, anchor=S)
        elif choice == 2:
            canvas.create_image(x, y, image = campbell, anchor=S)
        elif choice == 3:
            canvas.create_image(x, y, image = jeff, anchor=S)
        elif choice == 4:
            canvas.create_image(x, y, image = krysta, anchor=S)
        elif choice == 5:
            canvas.create_image(x, y, image = hana, anchor=S)
        elif choice == 6:
            canvas.create_image(x, y, image = jose, anchor=S)
        else:
            canvas.create_image(x, y, image = leela, anchor=S)
        n=n+1

#### main. 메인
window = Tk()
window.title("MyArtApp")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
scene = PhotoImage(file=background)
canvas.create_image(0, 0, image=scene, anchor=NW)
canvas.pack()

# bind movement to keys. 키보드 키를 연결합니다.
window.bind("e", erase_all)

# call images for top buttons. 상단 버튼 이미지를 불러옵니다.
red = PhotoImage(file="red.gif")
blue = PhotoImage(file="blue.gif")
green = PhotoImage(file="green.gif")
yellow = PhotoImage(file="yellow.gif")
black = PhotoImage(file="black.gif")
white = PhotoImage(file="white.gif")
plus = PhotoImage(file="plus.gif")
minus = PhotoImage(file="minus.gif")

# create top frame. 상단 프레임을 만듭니다.
topframe = Frame(window)
topframe.pack()

# build top set of buttons. 상단 버튼을 만듭니다.
Button(topframe, image=red, command=line_red).pack(side=LEFT)
Button(topframe, image=green, command=line_green).pack(side=LEFT)
Button(topframe, image=blue, command=line_blue).pack(side=LEFT)
Button(topframe, image=yellow, command=line_yellow).pack(side=LEFT)
Button(topframe, image=black, command=line_black).pack(side=LEFT)
Button(topframe, image=white, command=line_white).pack(side=LEFT)
Button(topframe, image=plus, command=bigger).pack(side=LEFT)
Button(topframe, image=minus, command=smaller).pack(side=LEFT)

# call images for bottom buttons. 하단 버튼 이미지를 불러옵니다.
tree = PhotoImage(file="tree.gif")
campbell = PhotoImage(file="campbell.gif")
ayesha = PhotoImage(file="ayesha.gif")
jeff = PhotoImage(file="jeff.gif")
krysta = PhotoImage(file="krysta.gif")
hana = PhotoImage(file="hana.gif")
jose = PhotoImage(file="jose.gif")
leela = PhotoImage(file="leela.gif")

# create middle frame. 중간 프레임을 만듭니다.
middleframe = Frame(window)
middleframe.pack()

# build middle set of buttons. 중간 버튼을 만듭니다.
Button(middleframe, image=campbell, command=use_campbell).pack(side=LEFT)
Button(middleframe, image=ayesha, command=use_ayesha).pack(side=LEFT)
Button(middleframe, image=jeff, command=use_jeff).pack(side=LEFT)
Button(middleframe, image=krysta, command=use_krysta).pack(side=LEFT)
Button(middleframe, image=hana, command=use_hana).pack(side=LEFT)
Button(middleframe, image=jose, command=use_jose).pack(side=LEFT)
Button(middleframe, image=leela, command=use_leela).pack(side=LEFT)
Button(middleframe, image=tree, command=use_tree).pack(side=LEFT)

# bind mouse movement to a function. 함수에 마우스 움직임을 연결합니다.
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", paint)

# create bottom frame. 하단 프레임을 만듭니다.
bottomframe = Frame(window)
bottomframe.pack()

# build bottom button. 하단 버튼을 만듭니다.
Button(bottomframe, text="make a crowd", command=make_crowd).pack()

# start tkinter's main loop. tkinter의 메인 반복을 시작합니다.
window.mainloop()
