##importing 
from tkinter import *
import time
import random
from math import cos, radians, sin, atan2, degrees, pi, sqrt, floor
import os
import sys
import winsound
import json
#print(sys.getrecursionlimit())
sys.setrecursionlimit(200000)

#############################defining functions start here###########################################################################
player = ''
e = ''



window_height = 675
window_width = 1200

lives_counter = 3

def entry_box():
    global e, window_width, window_height,player
    e = Entry(top, width = 50)
    e. place(x = 460, y = 520)
    ok_button = Button(top, text="Ok", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                         bg='#260707', activebackground='Red', command=creating_mainmenu)
    ok_button.place(x=460, y=580)


def creating_loginmenu():
    global loginmenu_canvas, score, enemies, window_width, window_height
    loginmenu_canvas = Canvas(top, width = window_width, height = window_height)
    loginmenu_canvas.create_image(0, 0, anchor=NW, image=mainmenu_pic)
    loginmenu_canvas.place(x=0, y=0)
    loginmenu_canvas.create_text(window_width/2, (window_height*100)/675 , font="CHILLER 70 bold", fill='DARK RED', text='DEMON ARMY : BLOOD WAR')

    chose_char_button = Button(top, text="Play as Guest", relief='groove', width=20, bd=2, font="CHILLER 30",
                               fg='white', bg='#260707', activebackground='Red', command = creating_mainmenu)
    chose_char_button.place(x=(460*window_width)/1200, y=(320*window_height)/675)

    playgame_button = Button(top, text="Sign in with Name", relief='groove', width=20, bd=2, font="CHILLER 30", fg='white',
                             bg='#260707', activebackground='Red', command=entry_box)
    playgame_button.place(x=(460*window_width)/1200, y=(420*window_height)/675)




def creating_mainmenu():
    global e, mainmenu_canvas, score, enemies, window_width, window_height,player,music_counter
    score = 0
    enemies = []
    if len(player) == 0:
        try:
            player = e.get()
        except:
            player = 'Guest'
    mainmenu_canvas = Canvas(top, width = window_width, height = window_height)
    mainmenu_canvas.create_image(0, 0, anchor=NW, image=mainmenu_pic)
    mainmenu_canvas.place(x=0, y=0)
    winsound.PlaySound("Mainmenu.wav", winsound.SND_ASYNC)
    mainmenu_canvas.create_text(window_width/2, (window_height*100)/675 , font="CHILLER 70 bold", fill='DARK RED', text='DEMON ARMY : BLOOD WAR')

    Load_button = Button(top, text="Load", relief='groove', width=20, bd=2, font="CHILLER 30",
                               fg='white', bg='#260707', activebackground='Red', command=LoadGame)
    Load_button.place(x = (100*window_width)/1200 , y = (220*window_height) /675)


    leaderboard_button = Button(top, text="Leaderboard", relief='groove', width=20, bd=2, font="CHILLER 30",
                               fg='white', bg='#260707', activebackground='Red', command=DisplayLeader)
    leaderboard_button.place(x = (100*window_width)/1200 , y = (420*window_height) /675)

    settings_button = Button(top, text="Settings", relief='groove', width=20, bd=2, font="CHILLER 30",
                               fg='white', bg='#260707', activebackground='Red', command=settings)
    settings_button.place(x=(100*window_width)/1200, y=(520*window_height) /675)

    playgame_button = Button(top, text="Play Game", relief='groove', width=20, bd=2, font="CHILLER 30", fg='white',
                             bg='#260707', activebackground='Red', command=playGame)
    playgame_button.place(x=(100*window_width)/1200, y=(320*window_height) /675)

    inst_button = Button(top, text="Instructions", relief='groove', width=20, bd=2, font="CHILLER 30", fg='white',
                         bg='#260707', activebackground='Red', command=Display_Instructions)
    inst_button.place(x=(800*window_width)/1200, y=(420*window_height) /675)

    quit_button = Button(top, text="Quit Game", relief='groove', width=20, bd=2, font="CHILLER 30", fg='white',
                         bg='#260707', activebackground='Red', command=quitGame)
    quit_button.place(x=(800*window_width)/1200, y=(520*window_height) /675)




def settings():
    global  window_width,char_choice, var,window_height,player
    print(player)

    
    settings_canvas = Canvas(top, width=window_width, height = window_height)
    settings_canvas.create_image(0, 0, anchor=NW, image=mainmenu_pic)
    settings_canvas.place(x=0, y=0)
    settings_canvas.create_text(window_width/2, (window_height * 150)/675, font="CHILLER 70 bold", fill='dark red', text='Settings')

    chose_char_button = Button(top, text="Select Character", relief='groove', width=20, bd=2, font='Chiller 30',
                               fg='white', bg='#260707', activebackground='Red', command=char_selection)
    chose_char_button.place(x=(100*window_width)/1200, y=(320*window_height)/675)

    screenres_button = Button(top, text="Screen Resolution", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                             bg='#260707', activebackground='Red', command=screen_resolution)
    screenres_button.place(x=(100*window_width)/1200, y=(420*window_height)/675)

    back_button = Button(top, text="Back", relief='groove', width=20, bd=2, font="CHILLER 30", fg='white',
                             bg='#260707', activebackground='Red', command = creating_mainmenu)
    back_button.place(x=(100*window_width)/1200, y=(520*window_height)/675)

back_button = ''
def screen_resolution():
    global back_button, settings_canvas,  window_width, window_height
    screen_res_canvas = Canvas(top, width=window_width, height = window_height)
    local_image = screen_res_canvas.create_image(0, 0, anchor=NW, image=mainmenu_pic)
    screen_res_canvas.place(x=0, y=0)
    screen_res_canvas.create_text(window_width / 2, (window_height * 100)/675, font="Chiller 70 bold", fill='dark red', text='Screen Resolution')

    # Add a grid
    mainframe = Frame(top)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.place(x=520*window_width / 1200, y=(200*window_height) / 675)

    # Create a Tkinter variable
    tkvar = StringVar(top)

    # Dictionary with options
    choices = {'1200x675', '1920x1080', '1280x720'}
    tkvar.set('1200x675')

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="Choose a resolution").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)
    '''
    window_height = top.winfo_screenheight()
    window_width = top.winfo_screenwidth()
    '''

    def resize(*args):
        global window_height, screen_res_canvas
        global window_width,back_button
        if tkvar.get() == '1200x675':
            window_height = 675
            window_width = 1200
            
        if tkvar.get() == '1280x720':
            window_height = 720
            window_width = 1280
            
        if tkvar.get() == '1920x1080':
            window_height = 1080
            window_width = 1920
            
        pictures_settings(window_width, window_height)
        top.geometry(f"{window_width}x{window_height}")
        screen_res_canvas = Canvas(top, width=window_width, height = window_height)
        local_image = screen_res_canvas.create_image(0, 0, anchor=NW, image=mainmenu_pic)
        screen_res_canvas.place(x=0, y=0)
        screen_res_canvas.create_text(window_width / 2, (window_height * 100)/675, font="Chiller 70 bold", fill='dark red', text='Screen Resolution')
        back_button.destroy()
        back_button = Button(top, text="Back", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                         bg='#260707', activebackground='Red', command = settings)
        back_button.place(x=(100*window_width)/1200, y=(470*window_height)/675)

            
        


    # link function to change dropdown
    tkvar.trace('w', resize)

    top.update()

    back_button = Button(top, text="Back", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                             bg='#260707', activebackground='Red', command = settings)
    back_button.place(x=(100*window_width)/1200, y=(470*window_height)/675)
    top.update()

    print(window_width, window_height)
    pass


def Display_Instructions():
    global instructions_pic
    instructions_canvas = Canvas(top, width = window_width, height = window_height)
    instructions = instructions_canvas.create_image(0, 0, anchor=NW, image = instructions_pic)
    instructions_canvas.place(x=0, y=0)
    ok_button = Button(top, text="OK", relief='groove', width=20, bd=2, font="CHILLER 30", fg='white',
                         bg='#260707', activebackground='Red', command=creating_mainmenu)
    
    ok_button.place(x=0, y=0)
    top.update()

 
####--------------------------------------------------------------------------
def DisplayLeader():
    global  window_width, window_height,leaderboard_pic
    #displaying leaderboard after everygame
    print("POSITION\tNAME\t\tSCORE")
    global scorelist, playerlist, mainmenu_canvas
    f=open('leaderboard.txt','a') #appending name and score in a file
    score = 0
    #print("Player and score = ",  player , "and", score)
    f.write(player+"\n"+str(score)+"\n")
    f.close()
    with open("leaderboard.txt") as f:  #storing in list
        scorelist,playerlist=list(),list()
        for line in f:
            line=line.rstrip('\n')
            try:
                line=int(line)
                scorelist.append(line)
            except: 
                playerlist.append(line)

    for i in range(1,len(scorelist)): #using bubble sort for arrranging in descending order
        for j in range(len(scorelist)-i):
            if scorelist[j]<scorelist[j+1]:
                scorelist[j],scorelist[j+1]=scorelist[j+1],scorelist[j]
                playerlist[j],playerlist[j+1]=playerlist[j+1],playerlist[j]
                

    #updating score if same user plays the game repeatedly 
    # updating technique used is storing high score and neglecting lower ones           
    x,y=list(),list()
    
    for i in playerlist:
        if i not in x:
            x.append(i)
            p = playerlist.index(i)
            y.append(scorelist[p])
    playerlist=x
    scorelist=y
    print("ENded here" , x , y)

    LeaderboardText = f'\t            LeaderBoard\n\nPosition\t\tName\t\tScore\n'
    for m in range(5):
        try:
            print((f'{m+1}\t\t{playerlist[m]}\t\t{scorelist[m]}'))
            LeaderboardText += (f'{m+1}\t\t{playerlist[m]}\t\t{scorelist[m]}\n')
        except:
            break
    LB_canvas = Canvas(top, width=window_width, height=window_height)
    LB_canvas.create_image(0, 0, anchor=NW, image=leaderboard_pic)
    LB_canvas.place(x=0, y=0)
    LB_canvas.create_text(window_width/2, (window_height*300)/675 , text = LeaderboardText, font = "CHILLER 35", fill = 'white')

    back_button = Button(LB_canvas, text="Back to Mainmenu", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                         bg='#260707', activebackground='Red', command=creating_mainmenu)
    back_button.place(x=(100*window_width)/1200, y=(580*window_height) / 675)


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
enemies = []
score = 0
id = None


###----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def quitGame():
    winsound.PlaySound("Blank.wav", winsound.SND_ASYNC)
    winsound.PlaySound("Blank.wav", winsound.SND_ASYNC)
    winsound.PlaySound("Blank.wav", winsound.SND_ASYNC)
    winsound.PlaySound("Blank.wav", winsound.SND_ASYNC)
    winsound.PlaySound("Blank.wav", winsound.SND_ASYNC)
    top.destroy()


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
var = 2
def char_selection():
    
    global var, char_choice,  window_width, window_height
    var = 2
    char_selection_canvas = Canvas(top, width=window_width, height=window_height)
    char_selection_canvas.create_image(0, 0, anchor=NW, image=mainmenu_pic)
    char_selection_canvas.place(x=0, y=0)
    char_selection_canvas.create_text(window_width/2, (window_height*50)/675, font="Chiller 50 bold", fill='dark red', text='Select Your Character')

    var = IntVar()
    var.set(2)
    '''
    chose_char1_button = Radiobutton(char_selection_canvas, image=char1_pic, bg='black', activebackground='Red',
                                     variable=var, value=1)
    chose_char1_button.place(x=(100*window_width) / 1200, y=(120*window_height)/675)
    '''
    chose_char2_button = Radiobutton(char_selection_canvas, image=char2_pic, bg='black', activebackground='Red',
                                     variable=var, value=2)
    chose_char2_button.place(x=(300*window_width) / 1200,y=(320*window_height)/675)

    chose_char3_button = Radiobutton(char_selection_canvas, image=char3_pic, bg='black', activebackground='Red',
                                     variable=var, value=3)
    chose_char3_button.place(x=(100*window_width) / 1200, y=(320*window_height)/675)

    ok_button = Button(top, text="OK", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                       bg='#260707', activebackground='Red', command=settings)
    ok_button.place(x=(130*window_width) / 1200, y=(520*window_height)/675)
    char_choice = var.get()
    animation_frames()
    print(char_choice)

frame1, frame2 =0,0
def animation_frames():
    global frame1, frame2, var, char_choice

    if char_choice == 1:
        frame1 = PhotoImage(file = 'Trial 1.png')
        frame2 = PhotoImage(file = 'Trial 2.png')
    elif char_choice == 2:
        frame1 = PhotoImage(file = 'char2_1.png')
        frame2 = PhotoImage(file = 'char2_2.png')
    elif char_choice == 3:
        frame1 = PhotoImage(file = 'char3_1.png')
        frame2 = PhotoImage(file = 'char3_2.png')


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def settingbackground():
    global canvas, score, id, game,  window_width, window_height,lives_counter, char1_pic, score_pic, game_finish
    game_finish = False
    game= False
    winsound.PlaySound("Blank.wav", winsound.SND_ASYNC)
    animation_frames()
    # label = Label(top, image = filename)
    # label.place(x = 0, y = 0)
    canvas = Canvas(top, width=window_width, height=window_height)
    # id = canvas.create_text(0,0 , text = f'Score = {score}', font = 'Aerial 20' )
    canvas.create_image(0, 0, anchor=NW, image=filename)
    score_pic = PhotoImage(file = 'Score.png')
    
    id = canvas.create_text(window_width/2, (window_height*30)/900, text=f'Score = {score}', font='Chiller 30', fill = 'white')
    canvas.place(x=0, y=0)
    x=0
    y=0
    for i in range(3):
        canvas.create_oval(x, y, x+50, y+50, fill = 'dark red')
        if i > (lives_counter - 1):
            canvas.create_oval(x, y, x+50, y+50, fill = 'white')
        x+=50
        
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
    canvas.bind_all("<Key-p>", change_pause)
    canvas.bind_all('<Motion>', motion)



##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
chr_choice = 2
def addingcharacter(char_choice, x=100, y=500):
    print("Character choice is ", char_choice)
    global window_width, window_height, var, game_aim
    
    x = x*window_width/1200
    y = y*window_height/675
    global game_character, game_aim
    if char_choice == 1:
        character_image = char1_pic
    elif char_choice == 2:
        character_image = char2_pic

    elif char_choice == 3:
        character_image = char3_pic

    game_character = canvas.create_image(x, y, image=character_image)
    # game_aim = canvas.create_oval(0, 0, 40, 40, fill = '#EB3C3C')
    game_aim = canvas.create_image(0, 0, image=aim_pic)
    animation_frames()
    top.update()

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
list_pause = []
def adding_hostiles(val=-1, list_coords=-1, z = -1):
    global enemies, pics_enemies, list_pause
    global max_enemies, window_width, window_height
    x=0
    y=0
    for i in range(3):
        canvas.create_oval(x, y, x+50, y+50, fill = 'dark red')
        if i > (lives_counter - 1):
            canvas.create_oval(x, y, x+50, y+50, fill = 'white')
        x+=50
    top.update()

    if len(enemies) < 5:
        max_enemies = floor(float(score) / 100) + 1
    else:
        max_enemies = 1
    if val == -1 and list_coords == -1:
        for i in range(max_enemies):
            n = random.randint(0,5)
            enemy = pics_enemies[n]
            list_pause.append(n)
            
            enemies.append(canvas.create_image(random.randint((900*window_width)//1200, window_width), random.randint(0, (550*window_height)//675), image=enemy))
    elif val != -1 and list_coords == -1:
        for i in range(val):
            n = random.randint(0,5)
            enemy = pics_enemies[n]
            list_pause.append(n)
            enemies.append(canvas.create_image((900*window_width)//1200, random.randint(0, (550*window_height)//675), image=enemy))   
    else:
        # max_enemies -= 1
        for i in range(val):
            try:
                x, y = list_coords[i]
                n = z[i]
                enemy = pics_enemies[n]
            except:
                continue
            enemies.append(canvas.create_image(x, y, image=enemy))


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
game_finish = False
cheat_codes = ''
cheat_counter = 0
def hostile_movement():
    global cheat_codes, game_finish, enemies, counter, game, just_resume, canvas, e, lives_counter,player, score, window_width, window_height,canvas, list_pause, canvas, gameover_pic
    local_counter = 0
    end = False
    while game == False:
        
        #print("Andar agya hun")
        for i in range(len(enemies)):
            try:
                if game_over(enemies[i]):
                    winsound.PlaySound("Hurt.wav", winsound.SND_ASYNC)
                    print("inside game over")
                    try:
                        lives_counter = lives_counter - 1
                        print("Lives are :", lives_counter)
                        time.sleep(0.75)
                        try:
                            canvas.delete(enemies[i])
                            enemies.remove(enemies[i])
                            list_pause.remove(list_pause[i])
                            print("Number of enemies now on screen :", len(enemies))

                        except:
                            print("here is problem")
                    except:
                        print("Tocheck")
                    if lives_counter <= 0:
                        game_finish = True
                        end = True
                        time.sleep(0.5)
                       
                        end_text = canvas.create_text(window_width / 2, window_height / 2, text="Game Over", font=('Aerial 20',100))
                        canvas.create_image(0, 0, anchor = NW, image = gameover_pic)
                        '''for j in range(len(enemies)):
                            canvas.delete(enemies[j])'''
                        back_button = Button(canvas, text="Back to Mainmenu", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                                             bg='#260707', activebackground='Red', command=creating_mainmenu)
                        back_button.place(x=0, y=0)

                        display_button = Button(canvas, text="Leader Board", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                                             bg='#260707', activebackground='Red', command=DisplayLeader)

                        display_button.place(x = 0, y=75)
                        
                        winsound.PlaySound("Game Over.wav", winsound.SND_ASYNC)
                        
                        break
                    else:
                        ScoreCheck()
                        break
                        continue
##------------------
                    if counter > 2000:
                        game_finish = True
                        end = True
                        time.sleep(0.5)
                       
                        end_text = canvas.create_text(window_width / 2, window_height / 2, text="Congats!!!!/nYou won", font=('Chiller 80',100))
                        back_button = Button(canvas, text="Back to Mainmenu", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                                             bg='#260707', activebackground='Red', command=creating_mainmenu)
                        back_button.place(x=0, y=0)

                        display_button = Button(canvas, text="Leader Board", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                                             bg='#260707', activebackground='Red', command=DisplayLeader)

                        display_button.place(x = 0, y=75)
                        
                        break


##_-----------------
            except:
                continue
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
            if counter <= 50:
                speed = 0.2
            elif counter >= 51:
                speed = 0.2
            elif counter >= 101:
                speed = 0.1
            if just_resume: #and counter > 54:
                speed = speed / 5

            if cheat_counter > 10:
                cheat_codes = ''

            if cheat_codes == 'Hello' and cheat_counter < 10:
                speed = speed/2

            speed = (1+((counter)//7)/8)*speed
            canvas.move(enemies[i], speed * movements[0], speed * movements[1])
            top.update()
####
        if score > 2000:
            game_finish = True
            end = True
            time.sleep(0.5)
           
            end_text = canvas.create_text(window_width / 2, window_height / 2, text="Congats!!!!\nYou won", font='Chiller 80',fill="dark red")
            back_button = Button(canvas, text="Back to Mainmenu", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                                 bg='#260707', activebackground='Red', command=creating_mainmenu)
            back_button.place(x=0, y=0)

            display_button = Button(canvas, text="Leader Board", relief='groove', width=20, bd=2, font='Chiller 30', fg='white',
                                 bg='#260707', activebackground='Red', command=DisplayLeader)

            display_button.place(x = 0, y=75)
                
    
        if end == True:
            game = True
            print("Game is end and player is ", player)
            canvas.unbind_all("<ButtonPress-1>")
            LeaderboardUpdate(player, score)
            #canvas.create_image(0, 0, anchor = NW, image = gameover_pic)
            break
        '''if just_resume and counter > 54:
            time.sleep(0.1)'''


        #if just_resume and counter > 54:
        #    time.sleep(0.1)
        '''if counter == max_enemies:
            print("Shit m break hogya")
            break'''


###-------------------------------------------------------------------------------------------------------------

def game_over(enemy):
    global game_character
    player_boundary = canvas.bbox(enemy)
    enemy_boundary = canvas.bbox(game_character)
    #print(player_boundary, enemy_boundary)
    try:
        if (enemy_boundary[0] <= player_boundary[2]) and (enemy_boundary[0] >= player_boundary[0]):
            print(enemy_boundary, player_boundary)
            if ((enemy_boundary[3] >= player_boundary[1]) and (enemy_boundary[3] <= player_boundary[3])) or ((enemy_boundary[1] >= player_boundary[1]) and (enemy_boundary[1] <= player_boundary[3])):
                return True
            else:
                return False
        else:
            return False
    except:
        print("Problem")
        return False


###-----------------------------------------------------------------------------------------

def LeaderboardUpdate(player , score):
    global scorelist, playerlist
    f=open('leaderboard.txt','a') #appending name and score in a file
    if player == '':
        player = 'Guest'
    player = player
    print("Player and score = ",  player , "and", score)
    f.write(player+"\n"+str(score)+"\n")
    f.close()
    with open("leaderboard.txt") as f:  #storing in list
        scorelist,playerlist=list(),list()
        for line in f:
            line=line.rstrip('\n')
            try:
                line=int(line)
                scorelist.append(line)
            except: 
                playerlist.append(line)

    for i in range(1,len(scorelist)): #using bubble sort for arrranging in descending order
        for j in range(len(scorelist)-i):
            if scorelist[j]<scorelist[j+1]:
                scorelist[j],scorelist[j+1]=scorelist[j+1],scorelist[j]
                playerlist[j],playerlist[j+1]=playerlist[j+1],playerlist[j]
                

    #updating score if same user plays the game repeatedly 
    # updating technique used is storing high score and neglecting lower ones           
    x,y=list(),list()
    
    for i in playerlist:
        if i not in x:
            x.append(i)
            p = playerlist.index(i)
            y.append(scorelist[p])
    playerlist=x
    scorelist=y
    print("ENded here" , x , y)
    
    


###--------------------------------------------------------------------------------------------------------------------------------------------------------------
def tracking(position):
    global game_character
    player_position = canvas.coords(game_character)
    enemy_position = position
    y_distance = abs(player_position[1] - enemy_position[1])
    x_distance = abs(player_position[0] - enemy_position[0])
    total_distance = sqrt(pow(y_distance, 2) + pow(x_distance, 2))
    if total_distance != 0:
        x_move = max_enemies * (x_distance / total_distance)
        y_move = max_enemies * (y_distance / total_distance)
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
    global frame1, frame2
    direction = "left"
    pos = canvas.bbox(game_character)

    if pos[0] > 0:
        if animation_counter % 2 == 0:
            canvas.move(game_character, -5, 0)
            canvas.itemconfig(game_character, image=frame1)
            top.update()
            animation_counter += 1
        else:
            canvas.move(game_character, -5, 0)
            canvas.itemconfig(game_character, image=frame2)
            top.update()
            animation_counter += 1
        time.sleep(0.000001)


def rightKey(event):
    global direction, animation_counter, window_width, window_height
    direction = "right"
    pos = canvas.bbox(game_character)
    if pos[2] < (550*window_width)/1200:
        if animation_counter % 2 == 0:
            canvas.move(game_character, 5, 0)
            canvas.itemconfig(game_character, image=frame1)
            top.update()
            animation_counter += 1
        else:
            canvas.move(game_character, 5, 0)
            canvas.itemconfig(game_character, image=frame2)
            top.update()
            animation_counter += 1


def upKey(event):
    global direction,window_width, window_height
    direction = "up"
    pos = canvas.bbox(game_character)
    if pos[1] > ((350 * window_height)/675):
        canvas.move(game_character, 0, -5)
        top.update()


def downKey(event):
    global direction,window_width, window_height
    direction = "down"
    pos = canvas.bbox(game_character)
    if pos[3] < ((600 * window_height)/675):
        canvas.move(game_character, 0, 5)
        top.update()


def right_upKey(event):
    global direction, animation_counter, window_width, window_height
    direction = "up_right"
    pos = canvas.bbox(game_character)
    if pos[2] < (550*window_width)/1200 and pos[1]>((350 * window_height)/675):
        if animation_counter % 2 == 0:
            canvas.move(game_character, 5, -5)
            canvas.itemconfig(game_character, image=frame1)
            top.update()
            animation_counter += 1
        else:
            canvas.move(game_character, 5, -5)
            canvas.itemconfig(game_character, image=frame2)
            top.update()
            animation_counter += 1


def left_upKey(event):
    global direction, window_width, window_height
    direction = "up_left"
    pos = canvas.bbox(game_character)
    if pos[0] > 0 and pos[1]>((350 * window_height)/675):
        canvas.move(game_character, -5, -5)
        top.update()


def right_downKey(event):
    global direction, window_width, window_height
    direction = "down_right"
    pos = canvas.bbox(game_character)
    if pos[2] < (550*window_width)/1200 and pos[3] < ((600 * window_height)/675):
        canvas.move(game_character, 5, 5)
        top.update()

def left_downKey(event):
    global direction, window_width, window_height
    direction = "down_left"
    pos = canvas.bbox(game_character)
    if pos[0] > 0 and pos[3] < ((600 * window_height)/675):
        canvas.move(game_character, -5, 5)
        top.update()


###---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def playGame():
    global counter, counter_pause, e, player, char_choice, lives_counter
    lives_counter = 3
    counter_pause = 0
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
    canvas.bind_all("<Key-b>", boss_key)
    if len(enemies) != 0:
        hostile_movement()
    # canvas.bind_all("<Left> + <Down>", leftdownKey)

####------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Cheats(cheat_code):
    global score, cheat_codes, cheat_counter
    if cheat_code == "Hello":
        cheat_codes = "Hello"
        cheat_counter = 0
    if cheat_code == "Bye":
        score = score + 100


def cheats_bar(event):
    global cheat_codes
    cheat_bar = Entry(top, width="25")
    cheat_bar.place(x=window_width-150, y=0)
    cheat_codes = cheat_bar.get()
    submit_button = Button(top, text="Submit", command=lambda: Cheats(cheat_bar.get()))
    submit_button.place(x=window_width-150, y=20)












####------------------------------------------------------
bosskey_counter = 0
flag = 0
def boss_key(event):
    global save_menu, bosskey_counter, boss_bg, counter_pause, flag, game, enemies_coords,back_menu ,just_resume, change_pause, enemies, game_character, counter_pause, pause_gamecoords_x, pause_gamecoords_y, counter, max_enemies, canvas, pause_pic

    global boss_pic
    print("Boos key : ", bosskey_counter)
    if bosskey_counter % 2 == 0:
        print("I am inside this")
        if game == False:
            flag = 0
            change_pause(event)
            back_menu.destroy()
            save_menu.destroy()
            boss_bg = canvas.create_image(window_width/2, (window_height*400)/900, image=boss_pic)
            print("I have created boos key")
        else:
            flag = 1
            back_menu.destroy()
            boss_bg = canvas.create_image(500, 400, image=boss_pic)

        bosskey_counter  += 1

    else:
        bosskey_counter += 1
        if flag == 0:
            canvas.delete(boss_bg)
            change_pause(event)
        else:
            canvas.delete(boss_bg)

            
        




##------------------------------------------------------------------------------------------------------------------------------------------------------------------------
counter_pause = 0
pause_gamecoords_x = 0
pause_gamecoords_y = 0
enemies_coords = []
game= False
just_resume = False
save_menu = ''
def change_pause(event):
    global char_choice, var, list_pause,save_menu, game, enemies_coords,back_menu ,just_resume, change_pause, enemies, game_character, counter_pause, pause_gamecoords_x, pause_gamecoords_y, counter, max_enemies, canvas, pause_pic
    if counter_pause % 2 == 0:
        game= True
        print("I am active boss")
        pause_gamecoords_x, pause_gamecoords_y = canvas.coords(game_character)
        enemies_coords = []
        counter_pause += 1
        print(counter_pause)
        for i in range(len(enemies)):
            try:
                (x, y) = canvas.coords(enemies[i])
                print("coordinates")
            except:
                print("Yahnan glti h ")
                continue
            enemies_coords.append((x, y))
        canvas.delete(game_character)
        pause_bg = canvas.create_image(window_width/2, (window_height*460)/900, image=pause_pic)
        back_menu = Button(canvas, text="Back to main menu", relief='groove', width=20, bd=2, font='Chiller 30',
                           fg='white',bg='#260707',activebackground='Red', command=creating_mainmenu)
        back_menu.place(x=0, y=0)
        
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
        save_menu = Button(canvas, text="Save", relief='groove', width=20, bd=2, font='Chiller 30',
                           fg='white',bg = '#260707' ,activebackground = 'Red', command = lambda:SaveGame(pause_gamecoords_x, pause_gamecoords_y, enemies_coords))
        save_menu.place(x=0, y = 70)
        canvas.bind_all('<Shift-Key-C>', cheats_bar)
        print("Character choice while pausing", char_choice)
        top.update()
        
        


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
        canvas.bind_all("<Key-p>", change_pause)
        canvas.bind_all('<Motion>', motion)

        game= False
        print("I am resuming")
        settingbackground()
        addingcharacter(char_choice, pause_gamecoords_x, pause_gamecoords_y)
        number = len(enemies)
        enemies = []
        adding_hostiles(number, enemies_coords, list_pause)
        counter_pause += 1
        time.sleep(0.01)
        txt = canvas.create_text(window_width/2, window_height/2, text = '3', font = "Chiller 120 bold", fill = 'dark red')
        top.update()
        time.sleep(1)
        canvas.delete(txt)
        top.update()
        txt = canvas.create_text(window_width/2, window_height/2, text = '2', font = "Chiller 120 bold", fill = 'dark red')
        top.update()
        time.sleep(1)
        canvas.delete(txt)
        top.update()
        txt = canvas.create_text(window_width/2, window_height/2, text = '1', font = "Chiller 120 bold", fill = 'dark red')
        top.update()
        time.sleep(1)
        canvas.delete(txt)
        top.update()
        just_resume = True
        hostile_movement()
        #print("Length of enemies while pausing : ", len(enemies))

####-----------------------------------------------------------------------------------------------------------------------------------
        
def SaveGame(char_x, char_y , enemies_coords):
    global player, score, counter, char_choice, enemies,list_pause, lives_counter
    print("The number of words:", len(player))
    if player != 'Guest':
        f=open(f'{player}.txt','a') #appending name and score in a file
        #print("Player and score = ",  player , "and", score)
        print("Character choice is ", char_choice)
        complete_information = {"player":player ,"list_pause":list_pause, "lives_counter":lives_counter, "length_enemies":len(enemies), "score":score, "char_x":char_x, "char_y":char_y , "enemies_coords":enemies_coords, "char_choice":char_choice}
        with open(f'{player}.txt', 'w') as filehandle:
            json.dump(complete_information, filehandle)
        f.close()


def LoadGame():
    global player,score,e, game, counter_pause, list_pause, live_counter
    print(player)
    if player != 'Guest':
        print("I am her")
        print(player, f'{player}.txt')
        f=open(f'{player}.txt','r') #appending name and score in a file
        #print("Player and score = ",  player , "and", score)
        with open(f'{player}.txt', 'r') as filehandle:
            data = json.load(filehandle)
            f.close()
        
        print(type(data))
        score = data["score"]
        char_x = data["char_x"]
        char_y = data["char_y"]
        enemies_coords = data["enemies_coords"]
        char_choice = data["char_choice"]
        length_enemies = data["length_enemies"]
        list_pause = data["list_pause"]
        live_counter = data["lives_counter"]
        

        game= False
        print("I am resuming")
        settingbackground()
        addingcharacter(char_choice, char_x, char_y)
        enemies = []
        adding_hostiles(length_enemies, enemies_coords, list_pause)
        counter_pause = 0
        time.sleep(0.01)
        just_resume = True
        hostile_movement()
          
####-----------------------------------------------------------------------------------------------------------------------------------------

'''def LoadGame():
    global player
    file = open("Save.txt")
    for line in reversed(file.readlines()):
        line = line.rstrip()
        print(line)
        
   ''' 
    


##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Bullets():
    pass


###------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def shoot(event):
    # print("Hey I'm working perfectly")
    winsound.PlaySound("Bullet Sound.wav", winsound.SND_ASYNC)
    ox, oy = canvas.coords(game_character)
    ex = event.x
    ey = event.y
    bullets.append(Bullet(canvas, ox, oy, ex, ey))


def shoot1(event):
    # print("I am shoot 1")
    ox, oy = canvas.coords(game_character)
    # img = canvas.create_oval(ox, oy, ox + 18, oy + 6, fill='black')
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
    canvas.coords(game_aim, x, y)


###------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def move_degrees(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    rads = atan2(dy, dx)
    rads %= 2 * pi
    # return degrees(rads)
    return rads


##--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Bullet(canvas, startx, starty, clickx, clicky):
    global counter, score, id, enemies, just_resume, list_pause, game_finish, cheat_counter
    canvas = canvas
    x1 = startx
    y1 = starty
    x2 = clickx
    y2 = clicky
    degs = move_degrees(x1, y1, x2, y2)
    img = canvas.create_oval(x1, y1, x1 + 18, y1 + 6, fill='#FF8B00')
    just_resume = False
    shooted = False
    # time.sleep(2)
    # img = canvas.create_image(x1, y1, image = bullet_pic)
    for i in range(100):
        canvas.delete(img)
        x1 += 5 * cos(degs)
        y1 += 5 * sin(degs)
        img = canvas.create_oval(x1, y1, x1 + 18, y1 + 6, fill='#FF8B00')
        # img = canvas.create_image(x1, y1, image = bullet_pic)
        top.update()
        for i in range(len(enemies)):
            if collision(x1, y1, enemies[i]):
                canvas.delete(img)
                canvas.delete(enemies[i])
                enemies.remove(enemies[i])
                list_pause.remove(list_pause[i])
                cheat_counter += 1
                counter += 1
                score += 10
                canvas.delete(id)
                id = canvas.create_text((window_width)/2 , (window_height*30)/675, text=f'Score = {score}', font='Chiller 30', fill='white')
                top.update()
                print("Shot down = ", counter)
                top.update()
                shooted = True
                break
        if shooted:
            print("Number of enemies now on screen :", len(enemies))
            ScoreCheck()
            shooted = False
            break
    img = canvas.delete(img)
    top.update()
    # time.sleep(0.0001)


'''#canvas.move(img, 1*cos(degs), 1*sin(degs))
dmg = 2
hit = False
speed = 15
'''
####-------------------------------------------
def ScoreCheck():
    global counter, game_finish, gameover_pic, just_resume, lives_counter,enemy2
    if not game_finish:
        if counter < 10:
            adding_hostiles(1)
            hostile_movement()
        elif counter >= 10 and counter <= 50:
            val = 4 - len(enemies)
            if val <= 0:
                return None
            else:
                adding_hostiles(val)
                hostile_movement()
        elif counter >= 51 and counter <= 100:
            val = 4 - len(enemies)
            if val <= 0:
                return None
            else:
                adding_hostiles(val)
                if counter == 51:
                    just_resume = True
                hostile_movement()
        else:
            val = 4 - len(enemies)
            if val <= 0:
                return None
            else:
                adding_hostiles(val)
                if counter == 101:
                    just_resume = True
                hostile_movement()
        if game_finish and lives_counter < 1:
            canvas.create_image(0, 0, anchor = NW, image = gameover_pic)
            

    
####------------------------------------------------------------------------------------------------------------------------

def collision(bulletx, bullety, enemies):
    position = canvas.bbox(enemies)
    try:
        if (((bulletx + 18) >= position[0]) and ((bulletx + 18) <= position[2])) or (
                (bulletx >= position[0]) and (bulletx <= position[2])):
            if (((bullety + 6) >= position[1]) and ((bullety + 6) <= position[3])) or (
                    (bullety >= position[1]) and (bullety <= position[3])):
                # print("Collided")
                return True
            else:
                return False
        else:
            return False
    except:
        return False


mainmenu_pic, filename, boss_pic, pause_pic, leaderboard_pic, gameover_pic, instructions_pic = 0,0,0,0,0,0,0
def pictures_settings(window_width, window_height):
    global instructions_pic, leaderboard_pic, mainmenu_pic, filename, boss_pic, pause_pic,gameover_pic
    #print()
    filename = PhotoImage(file=f"Game{window_width}x{window_height}.png")
    mainmenu_pic = PhotoImage(file=f"Mainmenu{window_width}x{window_height}.png")
    pause_pic = PhotoImage(file=f'pause{window_width}x{window_height}.png')
    print(f"Bosskey{window_width}x{window_height}.png")
    boss_pic = PhotoImage(file = f"Bosskey{window_width}x{window_height}.png")
    leaderboard_pic = PhotoImage(file = f'leaderboard{window_width}x{window_height}.png')
    gameover_pic = PhotoImage(file = f'Gameover{window_width}x{window_height}.png')
    instructions_pic = PhotoImage(file = f'Instructions{window_width}x{window_height}.png')


    ##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


####defining functions end here

##main code##
##setting background
counter = 0
animation_counter = 0
top = Tk()
top.geometry(f"{window_width}x{window_height}")
##loading background images
pictures_settings(window_width, window_height)
character = PhotoImage(file="AlienDone1.png")
aim_pic = PhotoImage(file="Aimfina.png")
bullet_pic = PhotoImage(file="Bullet.png")

char1_pic = PhotoImage(file="Trial 1.png")
char2_pic = PhotoImage(file="char2_1.png")
char3_pic = PhotoImage(file = "char3_1.png")


enemy2 = PhotoImage(file = 'enemy2.png')
enemy1 = PhotoImage(file="enemy2.png")
enemy3 = PhotoImage(file = 'enemy3.png')
enemy4 = PhotoImage(file = 'enemy4.png')
enemy5 = PhotoImage(file = 'enemy5.png')
enemy6 = PhotoImage(file = 'enemy6.png')

score_pic = PhotoImage(file = 'Score.png')

pics_enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]

##configuring windows
top.title("Welcome to This amazing Place")
# radiovar = IntVar()
# radiovar.set(1)
bullets = []
creating_loginmenu()
#creating_mainmenu()

# if var == 1:
# print(True)

# settingbackground()
direction = "right"

# addingcharacter()
# canvas.focus_set()
# movingcharacter()
top.resizable(0,0)
top.mainloop()
