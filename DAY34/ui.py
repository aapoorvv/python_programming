from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quizbrain: QuizBrain):
        self.score = 0
        self.quiz = quizbrain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR,font=("Segoe UI",13,"bold"))
        self.score_label.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300, height= 250, bg = 'white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text = "question text", 
            fill=THEME_COLOR,
            font = ("Arial",20,"italic")
        )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        tick_img = PhotoImage(file="DAY34/images/true.png")
        cross_img = PhotoImage(file="DAY34/images/false.png")
        self.true =Button(image = tick_img,highlightthickness=0, highlightbackground=THEME_COLOR,command=self.trueans)
        self.true.grid(row=3,column=0)
        self.false = Button(image = cross_img,highlightthickness=0, highlightbackground=THEME_COLOR,command=self.falseans)
        self.false.grid(row=3,column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else: 
            self.canvas.itemconfig(self.question_text,text = "You've reached the end of quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def trueans(self):
        is_right = self.quiz.check_answer("True")
        self.givefeedback(is_right)
    
    def falseans(self):
        is_right = self.quiz.check_answer("False")
        self.givefeedback(is_right)
        
    def givefeedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score+=1
            self.score_label.config(text= f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_next_question)
    
    