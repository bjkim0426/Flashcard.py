import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):

        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text='Score: 0', bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg='white', highlightbackground=THEME_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text='questions',
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic')
                                                     )
        self.canvas.grid(column=0, row=2, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file='./images/true.png')
        self.true_button = tk.Button(image=true_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.pressed_true)
        self.true_button.grid(column=0, row=3)

        false_image = tk.PhotoImage(file='./images/false.png')
        self.false_button = tk.Button(image=false_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.pressed_false)
        self.false_button.grid(column=1, row=3)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score :{self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve reached the end of the quiz!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer('True'))


    def pressed_false(self):

        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)



