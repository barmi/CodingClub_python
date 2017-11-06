# myScaryArtApp.py

from tkinter import *

#### Set variables:
canvas_height = 400
canvas_width = 680
canvas_colour = "black"
x_coord = canvas_width/2
y_coord = canvas_height/2
line_colour = "red"
line_width = 5
line_length = 5

background = "haunted_house.gif"
pen_up = True
current_line = None

#### Functions:
def move(x, y):
    global x_coord
    global y_coord
    global current_line
    new_x_coord = x_coord + x
    new_y_coord = y_coord + y
    if ((pen_up == False) or (current_line == None)):
        current_line = canvas.create_line(x_coord, y_coord, new_x_coord, new_y_coord,
                                          width=line_width, fill=line_colour)
    else:
        canvas.itemconfigure(current_line, width=line_width, fill=line_colour)
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

def line_violet():
    global line_colour
    line_colour = "dark violet"

def line_navy():
    global line_colour
    line_colour = "midnight blue"

def line_yellow():
    global line_colour
    line_colour = "yellow"

def line_aquamarine():
    global line_colour
    line_colour = "aquamarine2"

def line_dusk():
    global line_colour
    line_colour = "aquamarine4"

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

## add new functions here:
def add_bat():
    canvas.create_image(x_coord, y_coord, image=bat)

def add_campbell():
    canvas.create_image(x_coord, y_coord, image=campbell, anchor=S)

def add_ayesha():
    canvas.create_image(x_coord, y_coord, image=ayesha, anchor=S)

def add_jeff():
    canvas.create_image(x_coord, y_coord, image=jeff, anchor=S)

def add_krysta():
    canvas.create_image(x_coord, y_coord, image=krysta, anchor=S)

def add_hana():
    canvas.create_image(x_coord, y_coord, image=hana, anchor=S)

def add_jose():
    canvas.create_image(x_coord, y_coord, image=jose, anchor=S)

def add_leela():
    canvas.create_image(x_coord, y_coord, image=leela, anchor=S)

def paint(event):
    width = line_width/2
    x1 = event.x - width
    y1 = event.y - width
    x2 = event.x + width
    y2 = event.y + width
    canvas.create_oval(x1, y1, x2, y2, fill=line_colour, outline="")

#### main:
window = Tk()
window.title("MyScaryArtApp")
canvas = Canvas(bg=canvas_colour, height=canvas_height,
                width=canvas_width, highlightthickness=0)
scene = PhotoImage(file=background)
canvas.create_image(0, 0, image=scene, anchor = NW)
canvas.pack()

# bind movement to keys
window.bind("<Up>", move_N)
window.bind("<Down>", move_S)
window.bind("<Left>", move_W)
window.bind("<Right>", move_E)
window.bind("e", erase_all)
window.bind("u", pen_lift)
window.bind("d", pen_down)

## load images for top buttons:
violet = PhotoImage(file="violet.gif")
navy = PhotoImage(file="navy_blue.gif")
yellow = PhotoImage(file="yellow.gif")
aquamarine = PhotoImage(file="aquamarine.gif")
dusk = PhotoImage(file="dusk_green.gif")
black = PhotoImage(file="black.gif")
white = PhotoImage(file="white.gif")
plus = PhotoImage(file="plus.gif")
minus = PhotoImage(file="minus.gif")

## create top frame:
topframe = Frame(window)
topframe.pack()

## build top set of buttons
Button(topframe, image=violet, command=line_violet).pack(side=LEFT)
Button(topframe, image=navy, command=line_navy).pack(side=LEFT)
Button(topframe, image=yellow, command=line_yellow).pack(side=LEFT)
Button(topframe, image=aquamarine, command=line_aquamarine).pack(side=LEFT)
Button(topframe, image=dusk, command=line_dusk).pack(side=LEFT)
Button(topframe, image=black, command=line_black).pack(side=LEFT)
Button(topframe, image=white, command=line_white).pack(side=LEFT)
Button(topframe, image=plus, command=bigger).pack(side=LEFT)
Button(topframe, image=minus, command=smaller).pack(side=LEFT)

## load images for bottom buttons:
bat = PhotoImage(file="bat.gif")
campbell = PhotoImage(file="campbell.gif")
ayesha = PhotoImage(file="ayesha.gif")
jeff = PhotoImage(file="jeff.gif")
krysta = PhotoImage(file="krysta.gif")
hana = PhotoImage(file="hana.gif")
jose = PhotoImage(file="jose.gif")
leela = PhotoImage(file="leela.gif")

## create bottom frame:
bottomframe = Frame(window)
bottomframe.pack()

## build bottom set of buttons:
Button(bottomframe, image=campbell, command=add_campbell).pack(side=LEFT)
Button(bottomframe, image=ayesha, command=add_ayesha).pack(side=LEFT)
Button(bottomframe, image=jeff, command=add_jeff).pack(side=LEFT)
Button(bottomframe, image=krysta, command=add_krysta).pack(side=LEFT)
Button(bottomframe, image=hana, command=add_hana).pack(side=LEFT)
Button(bottomframe, image=jose, command=add_jose).pack(side=LEFT)
Button(bottomframe, image=leela, command=add_leela).pack(side=LEFT)
Button(bottomframe, image=bat, command=add_bat).pack(side=LEFT)

## bind mouse movement to a function:
canvas.bind("<B1-Motion>", paint)

# start tkinter's main loop
window.mainloop()
