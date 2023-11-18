##importing 
from tkinter import *
import time
import random
##defining functions start here

def creating_mainmenu():
    global mainmenu_canvas
    top = Tk()
    mainmenu_canvas = Canvas(top, width = 600, height = 500)
    mainmenu_canvas.create_image(30, 30, anchor=NW, image = mainmenu_pic)
    mainmenu_canvas.place(x = 0, y = 0)
    mainmenu_canvas.create_text(40, 100, font="Aerial 10 bold", fill='dodger blue',text='Welcome to Our game')


mainmenu_pic = PhotoImage(file = "Mainmenu.png")
creating_mainmenu()
