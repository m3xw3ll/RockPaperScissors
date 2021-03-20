# Icons are under creative commons license by Cristiano Zoucas from the Noun Project
# His work is available under https://thenounproject.com/cristiano.zoucas/

from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from functools import partial
import random

BACKGROUND = '#e0e0e0'

def update_user_score():
    '''
    Update the player score
    :return: None
    '''
    score = int(user_score_label['text'])
    score += 1
    user_score_label['text'] = str(score)

def update_computer_score():
    '''
    Update the computer score
    :return: None
    '''
    score = int(comp_score_label['text'])
    score += 1
    comp_score_label['text'] = str(score)
    
def update_message(result):
    '''
    Update the message text after each round
    :param result: The text message
    :return: None
    '''
    textmessage['text'] = result

def update_labels(user_choice, comp_choice):
    '''
    A function which updates the images for user and computer
    :param user_choice: The choice the user made with the button click
    :param comp_choice: The random computer choice
    :return: None
    '''
    if user_choice == 'rock':
        user_pick.configure(image=player_rockimg)
    elif user_choice == 'paper':
        user_pick.configure(image=player_paperimg)
    else:
        user_pick.configure(image=player_scissorimg)

    if comp_choice == 'rock':
        comp_pick.configure(image=computer_rockimg)
    elif comp_choice == 'paper':
        comp_pick.configure(image=computer_paperimg)
    else:
        comp_pick.configure(image=computer_scissorimg)


def play(choice):
    '''
    The acutial rock paper scissor function with the game logic
    :param choice: The user choice
    :return: None
    '''

    user_choice = choice
    comp_choice = random.sample({'rock', 'paper', 'scissor'}, 1)
    comp_choice = str(comp_choice[0])

    update_labels(user_choice, comp_choice)

    if user_choice == comp_choice:
        update_message('Tie')
    elif user_choice == 'rock':
        if comp_choice == 'paper':
            update_message('You loose')
            update_computer_score()
        else:
            update_user_score()
            update_message('You win')
    elif user_choice == 'paper':
        if comp_choice == 'scissor':
            update_message('You loose')
            update_computer_score()
        else:
            update_message('You win')
            update_user_score()
    elif user_choice == 'scissor':
        if comp_choice == 'rock':
            update_message('You loose')
            update_computer_score()
        else:
            update_message('You win')
            update_user_score()


root = Tk()
root.title("Rock Paper Scissor")
root.configure(background=BACKGROUND)
root.resizable(0, 0)

# Load images
player_rockimg = ImageTk.PhotoImage(Image.open('./src/player_rock.png'))
player_paperimg = ImageTk.PhotoImage(Image.open('./src/player_hand.png'))
player_scissorimg = ImageTk.PhotoImage(Image.open('./src/player_scissor.png'))
computer_rockimg = ImageTk.PhotoImage(Image.open('./src/computer_rock.png'))
computer_paperimg = ImageTk.PhotoImage(Image.open('./src/computer_hand.png'))
computer_scissorimg = ImageTk.PhotoImage(Image.open('./src/computer_scissor.png'))


# Labels
infofont = font.Font(family='Arial', size=10, weight='normal')
messagefont = font.Font(family='Arial', size=20, weight='bold')
user_pick = Label(root, image=player_rockimg, bg=BACKGROUND)
comp_pick = Label(root, image=computer_rockimg, bg=BACKGROUND)
user_pick.grid(row=1, column=0, padx=20, pady=(60,0))
comp_pick.grid(row=1, column=4, padx=20, pady=(60,0))
textmessage = Label(root, text='', font=messagefont, bg=BACKGROUND)
textmessage.grid(row=0, column=2, pady=(20,0))
usertext = Label(root, text='Player', font=infofont, bg=BACKGROUND).grid(row=0, column=0)
computertext = Label(root, text='Computer', font=infofont, bg=BACKGROUND).grid(row=0, column=4)

# Scores
scorefont = font.Font(family='Arial', size=50, weight='bold')
user_score_label = Label(root, font=scorefont, text=0, bg=BACKGROUND)
user_score_label.grid(row=1, column=1, pady=(60,0))
sep = Label(root, font=scorefont, text=':', bg=BACKGROUND).grid(row=1, column=2, pady=(60,0))
comp_score_label = Label(root, font=scorefont, text=0, bg=BACKGROUND)
comp_score_label.grid(row=1, column=3, pady=(60,0))

# Buttoms
btnfont = font.Font(family='Arial', size=10, weight='bold')
rockbtn = Button(root, width=20, height=2, text="Rock", bg='#F77494', font=btnfont, highlightcolor='white', command=partial(play, 'rock')).grid(row=4, column=1, padx=5)
paperbtn = Button(root, width=20, height=2, text="Paper", bg='#FFE076', font=btnfont, command=partial(play, 'paper')).grid(row=4, column=2, padx=5)
scissorbtn = Button(root, width=20, height=2, text="Scissor", bg='#A1E3F3', font=btnfont, command=partial(play, 'scissor')).grid(row=4, column=3, pady=20, padx=5)

root.mainloop()


