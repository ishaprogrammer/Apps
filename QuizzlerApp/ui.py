from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self,quiz_brain:QuizBrain) -> None:
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.label=Label(text="score:",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)
        self.canvas=Canvas(background="white",width=300,height=250)
        self.question=self.canvas.create_text(150,125,text="question_text",
                fill=THEME_COLOR,
                font=("Arial",20,"italic"),
                width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.get_next_q()
        self.path=PhotoImage(file=r"C:\Users\isha\Desktop\python100Days\quizzler-app-start\images\false.png")
        self.cross=Button(image=self.path,highlightthickness=0,command=self.true_pressed)
      
        self.cross.grid(row=2,column=0)
        
        self.path1=PhotoImage(file=r"C:\Users\isha\Desktop\python100Days\quizzler-app-start\images\true.png")
        self.check=Button(image=self.path1,highlightthickness=0,command=self.false_pressed)
        self.check.grid(row=2,column=1)
        
       
        self.window.mainloop()
    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="you have reached the end of the quiz")
            self.check.config(state="disabled")
            self.cross.config(state="disabled")
       
    def true_pressed(self):
      self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self,is_right):
        if is_right:
           self.canvas.config(bg="green")
        else:
           self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_q)  
        
        