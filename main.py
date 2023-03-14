import turtle
import time
from tkinter import *

def mode (x, y, z):
    while True:
        t = turtle.Turtle ()
        t.hideturtle()
        t.penup ()
        t.setpos (0, 170)
        t.pendown()
        t.pensize(150)
        t.pencolor('red')
        t.forward(0)

        t.penup ()
        t.setpos(0, 0)
        t.pendown()
        t.pencolor ('grey')
        t.forward(0)

        t.penup ()
        t.setpos(0, -170)
        t.pendown()
        t.pencolor ('grey')
        t.forward(0)

        time.sleep (x)

        t.penup ()
        t.setpos (0, 170)
        t.pendown()
        t.pensize(150)
        t.pencolor('grey')
        t.right (90)
        t.forward(0)

        t.penup ()
        t.setpos(0, 0)
        t.pendown()
        t.pencolor ('yellow')
        t.forward(0)

        time.sleep(y)

        t.penup ()
        t.setpos(0, 0)
        t.pendown()
        t.pencolor ('grey')
        t.forward(0)

        t.penup ()
        t.setpos(0, -170)
        t.pendown()
        t.pencolor ('green')
        t.forward(0)

        time.sleep (z)

        t.penup ()
        t.setpos(0, -170)
        t.pendown()
        t.pencolor ('grey')
        t.forward(0)

def mode1 ():
    mode(10, 2, 5)
    print ('mode1')

def mode2 ():
    mode (0.5,0.5,0.5)
    print (mode2)

root = Tk ()
root ['bg'] = 'white'
root.title ('trafic lights')
root.wm_attributes('-alpha')
root.geometry ('500x500')
root.resizable (width=False, height=False)
img = PhotoImage (file='./img/img.png')
smaller_img = img.subsample(4, 4)
label_img = Label(image = smaller_img)
label_img.place(x=135, y=20)
btn_mode1 = Button (root, text='mode1',
                    bg= 'white',
                    font= 'Arial 20',
                    command=mode1)
btn_mode1.place (x= 120 ,y= 375)

btn_mode2 = Button (root, text='mode2',
                    bg='white',
                    font= 'Arial 20',
                    command=mode2)
btn_mode2.place (x=260, y=375)

root.mainloop ()
