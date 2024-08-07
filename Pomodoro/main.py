from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1#25
SHORT_BREAK_MIN =1 #5
LONG_BREAK_MIN =1 #20
REPS=0
TIMER=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(texts,text="00:00")
    label.config(text="TIMER",fg=GREEN)
    label1.config(text="")
    REPS=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    # if REPS==2:
    #     label1.config(text="✓")
    #     label.grid(row=0,column=1)
    # elif REPS==4:
    #     label1.config(text="✓✓")
    #     label.grid(row=0,column=1)
    # elif REPS==6:
    #     label1.config(text="✓✓✓")
    #     label.grid(row=0,column=1)
    # elif REPS==8:
    #     label1.config(text="✓✓✓✓")
    #     label.grid(row=0,column=1)
    if REPS%8==0:
        label.config(text="LONG-BREAK TIME",fg=RED)
        coun_down(long_break_sec)
    elif REPS%2==0:
        label.config(text="SHORT-BREAK TIME",fg=PINK)
        coun_down(short_break_sec)
    else:
        label.config(text="WORK-TIME",fg=GREEN)
        coun_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def coun_down(count):
    global TIMER
    min=math.floor(count/60)
    sec=count%60
    if sec==0:
        sec="00"
    elif sec<10:
        sec=f"0{sec}"
        
    canvas.itemconfig(texts,text=f"{min}:{sec}")
    if count>0:
        TIMER=window.after(1000,coun_down,count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(REPS/2)
        for _ in range(work_sessions):
            mark+="✓"
            label1.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=YELLOW)
path=PhotoImage(file=r"C:\Users\isha\Downloads\pomodoro-start\tomato.png")
canvas=Canvas(width=200,height=224,highlightthickness=0,bg=YELLOW)
canvas.create_image(100,113,image=path)
texts=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

label=Label(text="TIMER",font=(FONT_NAME,35),fg=GREEN,bg=YELLOW)
label.grid(row=0,column=1)

label1=Label(text="",font=(FONT_NAME,20),fg=GREEN,bg=YELLOW)
label1.grid(row=3,column=1)

button=Button(text="Start",font=(FONT_NAME,20),command=start_timer)
button.grid(row=2,column=0)

button1=Button(text="Reset",font=(FONT_NAME,20),command=reset)
button1.grid(row=2,column=2)

window.mainloop()

