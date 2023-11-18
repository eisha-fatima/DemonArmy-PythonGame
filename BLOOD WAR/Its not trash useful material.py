
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
canvas.bind_all("<Left>", leftKey)
canvas.bind_all("<Right>", rightKey)
canvas.bind_all("<Up>", upKey)
canvas.bind_all("<Down>", downKey)
canvas.bind_all("<Left> + <Down>", leftdownKey)



    chose_char1_button = Radiobutton(top, width=100, height = 100, bd=2, image = character,  variable=var, value = 1)
    chose_char1_button.place(x=100, y=220)

    chose_char2_button = Radiobutton(char_selection_canvas, relief='groove',width=30, bd=2, fg='white', bg='dark green', activebackground='Red',variable=var, value = 2)
    chose_char2_button.place(x=100, y=320)

    chose_char3_button = Radiobutton(char_selection_canvas, relief='groove',width=30, bd=2, fg='white', bg='dark green', activebackground='Red',variable=radiovar, value = 3)
    chose_char3_button.place(x=100, y=420)

    chose_char4_button = Radiobutton(char_selection_canvas, relief='groove',width=30, bd=2, fg='white', bg='dark green', activebackground='Red', variable=radiovar, value = 4)
    chose_char4_button.place(x=100, y=520)
