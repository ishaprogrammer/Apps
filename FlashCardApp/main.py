from tkinter import *
import pandas
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
BACKGROUND_COLOR = "#B1DDC6"

current_card={}
to_learn={}

try:
    data=pandas.read_csv(r"C:\Users\isha\Desktop\python100Days\Flash_card_project.py\data\french_words.csv")
except FileNotFoundError:
    original_file=pandas.read_csv(r"C:\Users\isha\Desktop\python100Days\Flash_card_project.py\data\french_words.csv")
    to_learn=original_file.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
    
def flip():
    canvas.itemconfig(title_text,text="English",fill="white")
    canvas.itemconfig(content_text,text=current_card["English"],fill="white")
    canvas.itemconfig(background,image=back_img)
    
def change_card():
    global flip_timer,current_card
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(content_text,text=current_card["French"],fill="black")
    canvas.itemconfig(background, image=front_img)
    flip_timer=window.after(3000,func=flip)
    
def known_words():
    to_learn.remove(current_card)
    file=pandas.DataFrame(to_learn)
    file.to_csv("words_to_learn.csv",index=False)
    change_card()
    
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip)

canvas=Canvas(width=800,height=526)
front_img=PhotoImage(file=r"C:\Users\isha\Desktop\python100Days\Flash_card_project.py\images\card_front.png")
back_img=PhotoImage(file=r"C:\Users\isha\Desktop\python100Days\Flash_card_project.py\images\card_back.png")
background=canvas.create_image(400,263,image=front_img)
title_text=canvas.create_text(400,150,text="",font=("Ariel", 40, "italic"))
content_text=canvas.create_text(400,263,text="", font=("Ariel", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

check_path=PhotoImage(file=r"C:\Users\isha\Desktop\python100Days\Flash_card_project.py\images\right.png")
check_button=Button(image=check_path,highlightthickness=0,command=known_words)
check_button.grid(row=1,column=1)

cross_path=PhotoImage(file=r"C:\Users\isha\Desktop\python100Days\Flash_card_project.py\images\wrong.png")
cross_button=Button(image=cross_path,highlightthickness=0,command=change_card)
cross_button.grid(row=1,column=0)

change_card()

window.mainloop()
