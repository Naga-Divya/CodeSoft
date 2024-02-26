from tkinter import *
import tkinter.font as font
import random

player_score_val = 0
computer_score_val = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def player_choice(player_input):
    global player_score_val, computer_score_val

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if(player_input == computer_input):
        winner_label.config(text = "it's Tie" , fg="blue")
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score_val += 1
        winner_label.config(text="You Won!!!", fg="green")
        player_score.config(text = 'Your Score : ' + str(player_score_val))
    else:
        computer_score_val += 1
        winner_label.config(text="Computer Won!!!" , fg="red")
        computer_score.config(text='Your Score : ' + str(computer_score_val))

#Function to Randomly Select Computer Choice
def get_computer_choice():
    return random.choice(options)
        
    
window = Tk()
window.geometry("700x350")
window.title("Rock Paper Scissors Game")
window.configure(bg="aqua")
frame1 = Frame(window, highlightbackground="black", highlightthickness=4,highlightcolor='blue')
frame1.pack(padx=200, pady=150)

game_title = Label(frame1, text="ROCK PAPER SCISSORS GAME !", font=font.Font(size=30), fg="red", pady=5)
game_title.pack()

winner_label = Label(frame1, text="Let's start the game..", fg="blue", font=font.Font(size=20), padx=10, pady=20)
winner_label.pack()

frame_input = Frame(frame1)
frame_input.pack()

# Player options
player_option = Label(frame_input, text=" Your options", font=font.Font(size=20), fg="blue")
player_option.grid(row=0, column=0,pady=8)

rock_bt = Button(frame_input , text="ROCK" , width=20 , height=2 , bd=2 , bg='pink' , fg='black' , relief="raised" , command =lambda: player_choice(options[0]))
rock_bt.grid(row=1, column=1,padx=8,pady=5)

paper_bt = Button(frame_input , text="PAPER" , width=20 , height=2 , bd=1 , bg='pink' , fg='black' , relief="raised" , command =lambda: player_choice(options[1]))
paper_bt.grid(row=1, column=2,padx=8,pady=5)

scissor_bt = Button(frame_input , text="SCISSOR" , width=25 , height=2 , bd=1 , bg='pink' , fg='black' , relief="raised" , command =lambda: player_choice(options[2]))
scissor_bt.grid(row=1, column=3 ,padx=8,pady=5)

# Scores
score_label = Label(frame_input, text="Scores:", font=font.Font(size=20), fg="blue")
score_label.grid(row=2, column=0)

player_choice_label = Label(frame_input, text="Your selected option       : ---", font=font.Font(size=20) , fg="blue")
player_choice_label.grid(row=3, column=1, pady=5)

player_score = Label(frame_input, text="     Your score        : ---", font=font.Font(size=20) , fg="blue")
player_score.grid(row=3, column=2, pady=5)

computer_choice_label = Label(frame_input, text="Computer selected option: ---", font=font.Font(size=20) , fg="blue")
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score = Label(frame_input, text="     Computer score: ---", font=font.Font(size=20) , fg="blue")
computer_score.grid(row=4, column=2, pady=5)

window.mainloop()
