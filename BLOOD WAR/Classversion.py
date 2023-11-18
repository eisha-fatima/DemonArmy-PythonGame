##importing 
from tkinter import *
import time
import random
from math import cos, radians, sin, atan2, degrees, pi, sqrt
import os
#############################defining functions start here###########################################################################

def creating_mainmenu():
    global mainmenu_canvas, score, enemies
    score = 0
    enemies = []
    mainmenu_canvas = Canvas(top, width = 1000, height = 900)
    mainmenu_canvas.create_image(0, 0, anchor=NW, image = mainmenu_pic)
    mainmenu_canvas.place(x = 0, y = 0)
    mainmenu_canvas.create_text(500, 100, font="Aerial 30 bold", fill='dodger blue',text='Welcome to Our game')

    chose_char_button = Button(top, text="Select Character", relief='groove',width=20, bd=2, font='CourierNew 20',fg='white', bg='dark green', activebackground='Red',command = char_selection)
    chose_char_button.place(x=100, y=420)

    playgame_button = Button(top, text="Play Game", relief='groove',width=20, bd=2, font='CourierNew 20',fg='white', bg='dark green', activebackground='Red',command = playGame)
    playgame_button.place(x=100, y=520)

    quit_button = Button(top, text="Quit Game", relief='groove',width=20, bd=2, font='CourierNew 20',fg='white', bg='dark green', activebackground='Red',command = quitGame)
    quit_button.place(x = 100, y = 620)


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
enemies=[]
max_enemies = 6



###----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def quitGame():
    top.destroy()
   

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

score = 0
id = None
def settingbackground():
    global canvas, score, id, game
    game = False
    #label = Label(top, image = filename)
    #label.place(x = 0, y = 0)
    canvas = Canvas(top, width = 1000, height = 900)
    #id = canvas.create_text(0,0 , text = f'Score = {score}', font = 'Aerial 20' )
    canvas.create_image(0, 0, anchor=NW, image = filename)
    id = canvas.create_text(500,30 , text = f'Score = {score}', font = 'Aerial 20' )
    canvas.place(x = 0, y = 0)


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

char_choice = 2
def addingcharacter(char_choice, x = 100, y = 500):
    global game_character, game_aim
    if char_choice == 1:
        character_image = char1_pic
    elif char_choice == 2:
        character_image = char2_pic
        
    elif char_choice == 3:
        character_image = char3_pic
        
    elif char_choice == 4:
        character_image = char4_pic

        
    game_character = canvas.create_image(x, y, image = character_image)
    #game_aim = canvas.create_oval(0, 0, 40, 40, fill = '#EB3C3C')
    game_aim = canvas.create_image(0,0, image = aim_pic)
    top.update()


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def adding_hostiles(val=-1 , list_coords = -1):
    global enemies
    enemies = []
    global max_enemies
    if val == -1 and list_coords == -1:
        for i in range(max_enemies):
            enemies.append(canvas.create_image(random.randint(300, 900), random.randint(0, 800), image=enemy))
    else:
        #max_enemies -= 1
        for i in range(val):
            x , y = list_coords[i]
            enemies.append(canvas.create_image(x, y, image=enemy))
            

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def hostile_movement():
    global enemies, counter, game

    while game == False:
        for i in range(len(enemies)):
            try:
                enemy_position = canvas.coords(enemies[i])
            except:
                continue
            try:
                movements = tracking(enemy_position)
            except:
                continue
            '''if movements[0] == 0 and movements[1] == 0:
                print("COLLISION")
                canvas.delete(enemies[i])
                break'''
            canvas.move(enemies[i], movements[0], movements[1])
            time.sleep(0.01)
            top.update()
        if counter == max_enemies:
                break



###--------------------------------------------------------------------------------------------------------------------------------------------------------------
def tracking(position):
    global game_character
    player_position = canvas.coords(game_character)
    enemy_position = position
    y_distance = abs(player_position[1]-enemy_position[1])
    x_distance = abs(player_position[0] - enemy_position[0])
    total_distance = sqrt(pow(y_distance, 2) + pow(x_distance, 2))
    if total_distance != 0:
        x_move =max_enemies * (x_distance/total_distance)
        y_move =max_enemies * (y_distance/total_distance)
        if player_position[0] < enemy_position[0] and player_position[1] > enemy_position[1]:
            return -x_move, y_move
        if player_position[0] < enemy_position[0] and player_position[1] < enemy_position[1]:
            return -x_move, -y_move
        if player_position[0] > enemy_position[0] and player_position[1] < enemy_position[1]:
            return x_move, -y_move
        if player_position[0] > enemy_position[0] and player_position[1] > enemy_position[1]:
            return x_move, y_move
        if player_position[0] == enemy_position[0] and player_position[1] > enemy_position[1]:
            return 0, y_move
        if player_position[0] == enemy_position[0] and player_position[1] < enemy_position[1]:
            return 0, -y_move
        if player_position[0] > enemy_position[0] and player_position[1] == enemy_position[1]:
            return x_move, 0
        if player_position[0] < enemy_position[0] and player_position[1] == enemy_position[1]:
            return -x_move, 0
    else:
        return 0, 0




##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def leftKey(event):
    global direction, animation_counter
    direction = "left"
    pos=canvas.bbox(game_character)

    if pos[0]>0:
        if animation_counter % 2 == 0:
            canvas.move(game_character,-5,0)
            canvas.itemconfig(game_character, image=char1_pic)
            top.update()
            animation_counter +=1
        else:
            canvas.move(game_character,-5,0)
            canvas.itemconfig(game_character, image=char2_pic)
            top.update()
            animation_counter +=1
        time.sleep(0.000001)


        
def rightKey(event):
    global direction, animation_counter
    direction = "right"
    pos=canvas.bbox(game_character)
    if pos[2]<1000:
        if animation_counter % 2 == 0:
            canvas.move(game_character,5,0)
            canvas.itemconfig(game_character, image=char1_pic)
            top.update()
            animation_counter +=1
        else:
            canvas.move(game_character,5,0)
            canvas.itemconfig(game_character, image=char2_pic)
            top.update()
            animation_counter +=1


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
    global direction, animation_counter
    direction = "up_right"
    pos=canvas.bbox(game_character)
    if pos[2]<1000 and pos[1]>350:
        if animation_counter % 2 == 0:
            canvas.move(game_character,5,-5)
            canvas.itemconfig(game_character, image=char1_pic)
            top.update()
            animation_counter +=1
        else:
            canvas.move(game_character,5,-5)
            canvas.itemconfig(game_character, image=char2_pic)
            top.update()
            animation_counter +=1

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
    global counter
    counter = 0
    try:
        char_choice = var.get()
    except:
        char_choice = 2
    print(char_choice)

    settingbackground()
    addingcharacter(char_choice)
    adding_hostiles()
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
    canvas.bind_all('<Motion>', motion)
    canvas.bind_all("<Key-p>", change_pause)
    if len(enemies) != 0:
        hostile_movement()
    #canvas.bind_all("<Left> + <Down>", leftdownKey)

##------------------------------------------------------------------------------------------------------------------------------------------------------------------------
counter_pause = 0
pause_gamecoords_x = 0
pause_gamecoords_y = 0
enemies_coords = []
game = False
def change_pause(event):
    global game, enemies_coords, change_pause, enemies, game_character, counter_pause,pause_gamecoords_x, pause_gamecoords_y, counter, max_enemies, canvas, pause_pic
    pause_pic = PhotoImage(file = 'pause.png')
    if counter_pause % 2 == 0:
        game = True
        print("I am active boss")
        pause_gamecoords_x, pause_gamecoords_y  = canvas.coords(game_character)
        enemies_coords = []
        counter_pause += 1
        print(counter_pause)
        for i in range (len(enemies)):
            try:
                (x,y) = canvas.coords(enemies[i])
            except:
                continue
            enemies_coords.append((x, y))
        canvas.delete(game_character)
        pause_bg = canvas.create_image(500,400 , image = pause_pic)
        back_menu = Button(top, text="Back to main menu", relief='groove',width=20, bd=2, font='CourierNew 20',fg='black', activebackground='Red',command = creating_mainmenu)
        back_menu.place(x = 0 , y = 0)
        top.update()
        print(enemies_coords)
        canvas.unbind_all("<space>")
        canvas.unbind_all("<ButtonPress-1>")
        canvas.unbind_all("<Left>")
        canvas.unbind_all("<Right>")
        canvas.unbind_all("<Up>")
        canvas.unbind_all("<Down>")
        canvas.unbind_all("<Key-a>")
        canvas.unbind_all("<Key-d>")
        canvas.unbind_all("<Key-w>")
        canvas.unbind_all("<Key-x>")
        canvas.unbind_all("<Key-e>")
        canvas.unbind_all("<Key-q>")
        canvas.unbind_all("<Key-c>")
        canvas.unbind_all("<Key-z>")
        canvas.unbind_all('<Motion>')
        print("Length of enemies while pausing : ", len(enemies))

            
    else:
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
        canvas.bind_all('<Motion>', motion)

        game = False
        print("I am resuming")
        settingbackground()
        addingcharacter(char_choice, pause_gamecoords_x, pause_gamecoords_y )
        adding_hostiles(max_enemies-counter, enemies_coords)
        counter_pause += 1
        if max_enemies-counter != 0:
            #print("Mistake")
            hostile_movement()
        print("Length of enemies while pausing : ", len(enemies))
            
    
    




##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Bullets():
    pass


###------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def shoot(event):
    #print("Hey I'm working perfectly")
    ox, oy  = canvas.coords(game_character)
    ex = event.x
    ey = event.y
    bullets.append(Bullet(canvas, ox, oy, ex, ey))

def shoot1(event):
    #print("I am shoot 1")
    ox, oy  = canvas.coords(game_character)
    #img = canvas.create_oval(ox, oy, ox + 18, oy + 6, fill='black')
    bullets.append(Bullet(canvas, ox, oy, ox, oy))
    '''for i in range(200):
        canvas.delete(img)
        ox += 2.5 * cos(0)
        oy += 2.5 * sin(0)
5        img = canvas.create_oval(ox, oy, ox + 18, oy + 6, fill='black')
        collision(ox, oy)'''
            
###---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def motion(event):
    x = event.x
    y = event.y
    canvas.coords(game_aim, x,y)

###------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def move_degrees(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    rads = atan2(dy, dx)
    rads %= 2 * pi
    #return degrees(rads)
    return rads



##--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Bullet(canvas, startx, starty, clickx , clicky):
    global counter, score, id
    canvas = canvas
    x1 = startx
    y1 = starty
    x2 = clickx
    y2 = clicky
    degs = move_degrees(x1, y1, x2, y2)
    img = canvas.create_oval(x1, y1, x1 + 18, y1 + 6, fill='black')
    shooted = False
    #time.sleep(2)
    #img = canvas.create_image(x1, y1, image = bullet_pic)
    for i in range(100):
        canvas.delete(img)
        x1 += 5 * cos(degs)
        y1 += 5 * sin(degs)
        img = canvas.create_oval(x1, y1, x1 + 18, y1 + 6, fill='black')
        #img = canvas.create_image(x1, y1, image = bullet_pic)
        top.update()
        for i in range(len(enemies)):
            if collision(x1, y1, enemies[i]):
                canvas.delete(img)
                canvas.delete(enemies[i])
                enemies.pop(i)
                counter += 1
                score += 10
                canvas.delete(id)
                id = canvas.create_text(500,30 , text = f'Score = {score}', font = 'Aerial 20' )
                top.update()
                print("Shot down = ", counter)
                top.update()
                shooted = True
                break
        if shooted:
            shooted = False
            break
    img = canvas.delete(img)
    top.update()
        #time.sleep(0.0001)
'''#canvas.move(img, 1*cos(degs), 1*sin(degs))
dmg = 2
hit = False
speed = 15
'''
####------------------------------------------------------------------------------------------------------------------------

def collision(bulletx, bullety, enemies):
    position = canvas.bbox(enemies)
    try:
        if (((bulletx +18) >= position[0]) and ((bulletx +18) <= position[2])) or ((bulletx >= position[0]) and (bulletx <= position[2])):
            if (((bullety + 6) >= position[1]) and ((bullety + 6) <= position[3])) or ((bullety >= position[1]) and (bullety <= position[3])):
                #print("Collided")
                return True
            else:
                return False
        else:
            return False
    except:
        return False
    





    ##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
####defining functions end here 
    
##main code##
##setting background
counter = 0
animation_counter = 0
top = Tk()
top.geometry("1000x900")
##loading background images
filename = PhotoImage(file = "Game.png")
character = PhotoImage(file = "AlienDone1.png")
aim_pic = PhotoImage(file = "Aimfina.png")
mainmenu_pic = PhotoImage(file = "Mainmenu.png")
bullet_pic = PhotoImage(file = "Bullet.png")
char1_pic = PhotoImage(file = "Trial 1.png")
char2_pic = PhotoImage(file = "Trial 2.png")
enemy = PhotoImage(file ="trial11.png")
pause_pic = PhotoImage(file = 'pause.png')
##configuring windows
top.title("Welcome to This amazing Place")
#radiovar = IntVar()
#radiovar.set(1)
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




