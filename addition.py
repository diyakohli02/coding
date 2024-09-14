from tkinter import *
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}


def flip_card():
   canvas.itemconfig(title_text, text="Meaning",fill="white")
   canvas.itemconfig(word_text, text="hello",fill="white")
   canvas.itemconfig(old_screen, image=new_img)


# #buttons
def next_time():
    global flip_timer
    canvas.itemconfig(title_text, text="Image", fill="black")
    canvas.itemconfig(old_screen,image=new_img )
    flip_timer = window.after(1500, func=flip_card)


window=Tk()
window.title("My Flashcards")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
flip_timer = window.after(1500, func=flip_card)
old_img=PhotoImage(file="C:/Users/asus 1/OneDrive/Pictures/Screenshots/Screenshot 2024-09-02 142425.png")
new_img=PhotoImage(file="images/card_back.png")
old_screen=canvas.create_image(400,263,image=old_img)
title_text=canvas.create_text(400,170,text="",font=("Ariel",40))
word_text=canvas.create_text(400,350,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

img_right=PhotoImage(file="data/right.png")
right_button=Button(image=img_right,highlightthickness=0)
right_button.grid(row=1,column=0)

img_wrong=PhotoImage(file="data/wrong.png")
wrong_button=Button(image=img_wrong,highlightthickness=0)
wrong_button.grid(row=1,column=1)

window.mainloop()