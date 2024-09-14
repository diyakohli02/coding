import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
import json

def calculations():
    daily=daily_entry.get()
    assessment=assessment_entry.get()
    final=final_entry.get()

    new_data={
            "daily practice score":daily,
            "assessment score":assessment,
            "final test score":final
        }
    with open("data.json","w") as data_file:
        json.dump(new_data,data_file,indent=4)


window=Tk()
window.title("ScoreCard")
window.config(pady=50,padx=50)
canvas=Canvas(height=200,width=200)

score_label=Label(text="ScoreCard")
score_label.grid(row=0,column=0)
daily_label=Label(text="Daily test score: ")
daily_label.grid(row=1,column=0)

assessment_label=Label(text="Assessment score: ")
assessment_label.grid(row=2,column=0)

final_label=Label(text="Final Score: ")
final_label.grid(row=3,column=0)

daily_entry=Entry(width=40)
daily_entry.focus()
daily_entry.grid(row=1,column=1,columnspan=2)
assessment_entry=Entry(width=40)
assessment_entry.grid(row=2,column=1,columnspan=2)
final_entry=Entry(width=40)
final_entry.grid(row=3,column=1,columnspan=2)


record_button=Button(text="Record",width=35,command=calculations)
record_button.grid(row=5,column=1,columnspan=2)

graph_button=Button(text="Create Graph",width=35,command=calculations)
graph_button.grid(row=6,column=1,columnspan=2)

window.mainloop()



