import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}


try:
    data=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    og_data=pandas.read_csv("french_words.csv")
    to_learn=og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(title_text, text="Gujarati",fill="black")
    canvas.itemconfig(word_text, text=current_card["Gujarati"],fill="black")
    canvas.itemconfig(old_screen,image=old_img)
    flip_timer = window.after(1500, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English",fill="white")
    canvas.itemconfig(word_text, text=current_card["English"],fill="white")
    canvas.itemconfig(old_screen, image=new_img)


def is_known():
    to_learn.remove(current_card)
    new_data=pandas.DataFrame(to_learn)
    new_data.to_csv("words_to_learn",index=False)
    next_card()

window=Tk()
window.title("My Flashcards")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
flip_timer = window.after(1500, func=flip_card)
old_img=PhotoImage(file="card_front.png")
new_img=PhotoImage(file="card_back.png")
old_screen=canvas.create_image(400,263,image=old_img)
title_text=canvas.create_text(400,170,text="",font=("Ariel",40))
word_text=canvas.create_text(400,350,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

img_right=PhotoImage(file="right.png")
right_button=Button(image=img_right,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=0)

img_wrong=PhotoImage(file="wrong.png")
wrong_button=Button(image=img_wrong,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=1)













next_card()
window.mainloop()

