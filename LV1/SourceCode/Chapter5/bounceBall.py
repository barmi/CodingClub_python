# base source : https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
# tkinter ref : http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
from tkinter import *
import math

canvas_width = 600
canvas_height = 400

root = Tk()
root.title = "Game"
#root.resizable(0,0)
#root.wm_attributes("-topmost", 1)

canvas = Canvas(root, width=canvas_width, height=canvas_height, bd=0, highlightthickness=0)
canvas.pack()


class Ball:
    def __init__(self, canvas, color):
        self.x = canvas_width / 2
        self.y = canvas_height / 2
        self.direction = 45.0
        self.canvas = canvas
        self.id = canvas.create_oval(-10, -10, 10, 10, fill=color)
        self.canvas.move(self.id, self.x, self.y)

        self.canvas.bind("<Button-1>", self.canvas_onclick)
        self.text_id = self.canvas.create_text(300, 200, anchor='se')
        self.canvas.itemconfig(self.text_id, text='hello')

    def canvas_onclick(self, event):
        self.canvas.itemconfig(
            self.text_id,
            text="You clicked at ({}, {})".format(event.x, event.y)
        )

    def move(self):
        self.x = 5.0 * math.cos(math.radians(self.direction))
        self.y = 5.0 * math.sin(math.radians(self.direction))

    def draw(self):
        self.move()
        #(self.canvas.coords(self.id)[0] + self.canvas.coords(self.id)[2]) / 2
        self.canvas.move(self.id, self.canvas.canvasx(self.x), self.canvas.canvasy(self.y))
        pos = self.canvas.coords(self.id)
        if pos[0] < 0:
            if self.direction < 180:
                self.direction -= 90
            else:
                self.direction += 90
        if pos[1] < 0:
            if self.direction > 270:
                self.direction -= 90
            else:
                self.direction -= 90
        if pos[2] > canvas_width:
            if self.direction > 180:
                self.direction -= 90
            else:
                self.direction += 90
        if pos[3] > canvas_height:
            if self.direction > 90:
                self.direction += 90
            else:
                self.direction = 360 - self.direction
        self.canvas.after(20, self.draw)


ball = Ball(canvas, "red")
ball.draw()  #Changed per Bryan Oakley's comment.
root.mainloop()
