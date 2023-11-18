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

def addingcharacter():
    global game_character
    game_character = canvas.create_image(100, 400, image = character)
    top.update()

def leftKey(event):
    global direction
    direction = "left"
    canvas.move(game_character,-5,0)
    top.update()

def rightKey(event):
    global direction, i
    direction = "right"
    i = 1
    i +=1
    print("Right key is working")
    if i % 2 == 0:
        canvas.delete(game_character)
        game_character = canvas.create_image(105, 400, image = character)
        
    else:
        canvas.game_character.config(image = character1)
    canvas.move(game_character,5,0)
    top.update()


def upKey(event):
    global direction
    direction = "up"
    canvas.move(game_character,0,-5)
    top.update()

def downKey(event):
    global direction
    direction = "down"
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
character = PhotoImage(file = "Trial 1.png")
character1 = PhotoImage(file = "Trial 2.png")

i = 1
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






