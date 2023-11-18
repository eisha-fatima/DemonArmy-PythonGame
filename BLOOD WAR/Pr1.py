##importing 
from tkinter import *
import time
import random
from math import cos, radians, sin, atan2, degrees, pi
import os
##############################defining functions start here###########################################################################

def creating_mainmenu():
    global mainmenu_canvas
    mainmenu_canvas = Canvas(top, width = 1000, height = 900)
    mainmenu_canvas.create_image(0, 0, anchor=NW, image = mainmenu_pic)
    mainmenu_canvas.place(x = 0, y = 0)
    mainmenu_canvas.create_text(500, 100, font="Aerial 30 bold", fill='dodger blue',text='Welcome to Our game')

    chose_char_button = Button(top, text="Select Character", relief='groove',width=20, bd=2, font='CourierNew 20',fg='white', bg='dark green', activebackground='Red',command = char_selection)
    chose_char_button.place(x=100, y=420)

    playgame_button = Button(top, text="Play Game", relief='groove',width=20, bd=2, font='CourierNew 20',fg='white', bg='dark green', activebackground='Red',command = playGame)
    playgame_button.place(x=100, y=520)

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




    

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def char_selection():
    global var, char_choice
    char_selection_canvas = Canvas(top, width = 1000, height = 900)
    char_selection_canvas.create_image(0, 0, anchor=NW, image = mainmenu_pic)
    char_selection_canvas.place(x = 0, y = 0)
    char_selection_canvas.create_text(500, 100, font="Aerial 30 bold", fill='blue',text='Select Your Character')

    var = IntVar()
    var.set(2)

    chose_char1_button = Radiobutton(char_selection_canvas,image = char1_pic, bg='black', activebackground='Red', variable=var, value = 1)
    chose_char1_button.place(x=100, y=120)

    chose_char2_button = Radiobutton(char_selection_canvas,image = char2_pic, bg='black', activebackground='Red', variable=var, value = 2)
    chose_char2_button.place(x=100, y=320)

    chose_char3_button = Radiobutton(char_selection_canvas,image = character, bg='black', activebackground='Red', variable=var, value = 3)
    chose_char3_button.place(x=400, y=320)

    chose_char4_button = Radiobutton(char_selection_canvas,image = character, bg='black', activebackground='Red', variable=var, value = 4)
    chose_char4_button.place(x=400, y=120)
    ok_button = Button(top,text="OK", relief='groove',width=20, bd=2, font='CourierNew 20',fg='white', bg='dark green', activebackground='Red',command = creating_mainmenu )
    ok_button.place(x=130, y=520)
    char_choice = var.get()
    print(char_choice)


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def settingbackground():
    global canvas
    #label = Label(top, image = filename)
    #label.place(x = 0, y = 0)
    canvas = Canvas(top, width = 1000, height = 900)
    
    canvas.create_image(0, 0, anchor=NW, image = filename)
    canvas.place(x = 0, y = 0)


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def addingcharacter(char_choice):
    global game_character, game_aim
    if char_choice == 1:
        character_image = char1_pic
    elif char_choice == 2:
        character_image = char2_pic
        
    elif char_choice == 3:
        character_image = char3_pic
        
    elif char_choice == 4:
        character_image = char4_pic

        
    game_character = canvas.create_image(100, 400, image = character_image)
    game_aim = canvas.create_oval(0, 0, 40, 40, fill = '#EB3C3C')
    top.update()


##----------------------------------------------------------------------------------


    

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def leftKey(event):
    global direction
    direction = "left"
    pos=canvas.bbox(game_character)

    if pos[0]>0:

        canvas.move(game_character,-5,0)

        top.update()

def rightKey(event):
    global direction
    direction = "right"
    pos=canvas.bbox(game_character)
    if pos[2]<1000:
        canvas.move(game_character,5,0)
        top.update()

def upKey(event):
    global direction
    direction = "up"
    pos=canvas.bbox(game_character)
    if pos[1]>350:
        canvas.move(game_character,0,-5)
        top.update()


def downKey(event):
    global direction
    direction = "down"
    pos=canvas.bbox(game_character)
    if pos[3]<700:
        canvas.move(game_character,0,5)
        top.update()


def right_upKey(event):
    global direction
    direction = "up_right"
    pos=canvas.bbox(game_character)
    if pos[2]<1000 and pos[1]>350:
        canvas.move(game_character, 5, -5)
        top.update()

def left_upKey(event):
    global direction
    direction = "up_left"
    pos=canvas.bbox(game_character)
    if pos[0]>0 and pos[1]>350:
        canvas.move(game_character, -5, -5)
        top.update()

def right_downKey(event):
    global direction
    direction = "down_right"
    pos=canvas.bbox(game_character)
    if pos[2]<1000 and pos[3]<700: 
        canvas.move(game_character, 5, 5)
        top.update()

def left_downKey(event):
    global direction
    direction = "down_left"
    pos=canvas.bbox(game_character)
    if pos[0]>0 and pos[3]<700:
        canvas.move(game_character, -5, 5)
        top.update()

###---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def playGame():
    char_choice = var.get()
    print(char_choice)

    settingbackground()
    addingcharacter(char_choice)
    canvas.bind_all("<space>", shoot1)
    canvas.bind_all("<ButtonPress-1>", shoot)
    canvas.bind_all("<Left>", leftKey)
    canvas.bind_all("<Right>", rightKey)
    canvas.bind_all("<Up>", upKey)
    canvas.bind_all("<Down>", downKey)
    canvas.bind_all("<Key-a>", leftKey)
    canvas.bind_all("<Key-d>", rightKey)
    canvas.bind_all("<Key-w>", upKey)
    canvas.bind_all("<Key-x>", downKey)
    canvas.bind_all("<Key-e>", right_upKey)
    canvas.bind_all("<Key-q>", left_upKey)
    canvas.bind_all("<Key-c>", right_downKey)
    canvas.bind_all("<Key-z>", left_downKey)
    canvas.bind_all('<Motion>',motion)

    #canvas.bind_all("<Left> + <Down>", leftdownKey)

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Bullets():
    pass




###------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def shoot(event):
    print("Hey I'm working perfectly")
    ox, oy  = canvas.coords(game_character)
    ex = event.x
    ey = event.y
    bullets.append(Bullet(canvas, ox, oy, ex, ey))

def shoot1(event):
    print("I am shoot 1")
    ox, oy  = canvas.coords(game_character)
    img = canvas.create_oval(ox, oy, ox + 18, oy + 6, fill='black')
    for i in range(200):
        canvas.delete(img)
        ox += 2.5 * cos(0)
        oy += 2.5 * sin(0)
        img = canvas.create_oval(ox, oy, ox + 18, oy + 6, fill='black')
        

def motion(event):
    x = event.x
    y = event.y
    canvas.coords(game_aim, x-20,y-20,x+20, y+20)

###------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def move_degrees(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    rads = atan2(dy, dx)
    rads %= 2 * pi
    #return degrees(rads)
    return rads



##--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Bullet(canvas, startx, starty, clickx, clicky):
    canvas = canvas
    x1 = startx
    y1 = starty
    x2 = clickx
    y2 = clicky
    degs = move_degrees(x1, y1, x2, y2)
    img = canvas.create_oval(x1, y1, x1 + 18, y1 + 6, fill='black')
    #time.sleep(2)
    #img = canvas.create_image(x1, y1, image = bullet_pic)
    for i in range(200):
        canvas.delete(img)
        x1 += 2.5 * cos(degs)
        y1 += 2.5 * sin(degs)
        img = canvas.create_oval(x1, y1, x1 + 18, y1 + 6, fill='black')
        #img = canvas.create_image(x1, y1, image = bullet_pic)
        top.update()
        #time.sleep(0.0001)
        #canvas.move(img, 1*cos(degs), 1*sin(degs))
    dmg = 2
    hit = False
    speed = 15

    



##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
####defining functions end here 
    
##main code##
##setting background
top = Tk()
top.geometry("1000x900")
##loading background images
filename = PhotoImage(file = "Game.png")
character = PhotoImage(file = "AlienDone1.png")
mainmenu_pic = PhotoImage(file = "Mainmenu.png")
bullet_pic = PhotoImage(file = "Bullet.png")
char1_pic = PhotoImage(file = "AlienDone.png")
char2_pic = PhotoImage(file = "AlienDone1.png")
##configuring windows
top.title("Welcome to This amazing Place")
radiovar = IntVar()
radiovar.set(1)
bullets = []
creating_mainmenu()

#if var == 1:
    #print(True)

#settingbackground()
direction = "right"

#addingcharacter()
#canvas.focus_set() 
#movingcharacter()


top.mainloop()




