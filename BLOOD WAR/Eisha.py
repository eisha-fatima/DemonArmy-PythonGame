##importing 

from tkinter import *

import time

import random

##defining functions start here



def settingbackground():

    global canvas

    #label = Label(top, image = filename)

    #label.place(x = 0, y = 0)

    canvas = Canvas(top, width = 600, height = 500)

    

    canvas.create_image(0, 0, anchor=NW, image = filename)

    canvas.place(x = 0, y = 0)

    #pos=canvas.bbox(game_character)



def addingcharacter():

    global game_character

    game_character = canvas.create_image(100, 400, image = character)

    canvas.place(x = 0, y = 0)

    top.update()



def leftKey(event):

    global direction

    pos=canvas.bbox(game_character)

    direction = "left"

    if pos[0]>0:

        canvas.move(game_character,-5,0)

        top.update()



def rightKey(event):

    global direction

    pos=canvas.bbox(game_character)

    direction = "right"

    if pos[2]<600:

        canvas.move(game_character,5,0)

        top.update()





def upKey(event):

    global direction

    pos=canvas.bbox(game_character)

    direction = "up"

    if pos[1]>0:

        canvas.move(game_character,0,-5)

        top.update()



def downKey(event):

    global direction

    pos=canvas.bbox(game_character)

    direction = "down"

    if pos[3]<500:

        canvas.move(game_character,0,5)

        top.update()



def movingcharacter():



    positions = []

    positions.append(canvas.coords(game_character))



    #print(positions)

    while True:

        if direction == "right":

            x = 5

            y = 0

        elif direction == "left":

            x = -5

            y = 0

        elif direction == "up":

            y = -5

            x = 0

        elif direction == "down":

            y = 5

            x = 0

        

        canvas.move(game_character,x,y)

        top.update()

        time.sleep(0.05)

        #print("Zeeshan")



    

##main code##

##setting background

top = Tk()

top.geometry("600x500")

##loading background images

filename = PhotoImage(file = "Game.png")

character = PhotoImage(file = "AlienDone.png")



##configuring windows

top.title("Welcome to This amazing Place")



settingbackground()

direction = "right"



canvas.bind_all("<Left>", leftKey)

canvas.bind_all("<Right>", rightKey)

canvas.bind_all("<Up>", upKey)

canvas.bind_all("<Down>", downKey)



addingcharacter()

#movingcharacter()





top.mainloop()













