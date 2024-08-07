from tkinter import *

window=Tk()
window.minsize(width=300,height=300)
window.title("Miles to kilometer converted")
window.config(padx=50,pady=50)

lable=Label(text="equal to",font=("Arial",10,"bold"))
lable.grid(row=1,column=0)

lable0=Label(text="Miles",font=("Arial",10,"bold"))
lable0.grid(row=0,column=2)

lable1=Label(text="Km",font=("Arial",10,"bold"))
lable1.grid(row=1,column=2)

lable2=Label(text="0",font=("Arial",10,"bold"))
lable2.grid(row=1,column=1)

def miles_to_km(miles):
    return miles*1.60934

def click():
    miles=float(enter.get())
    km=miles_to_km(miles)
    lable2.config(text=f"{km:.2f}")
button=Button(text="Calculate",font=("Arial",15,"bold"),command=click)
button.grid(row=2,column=1)

enter=Entry()
enter.insert(END,string="0")
enter.focus()
enter.grid(row=0,column=1)

window.mainloop()