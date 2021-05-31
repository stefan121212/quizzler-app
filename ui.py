from tkinter import *
from quiz_brain import QuizBrain


ACTIVE = "active"
DISABLED = "disabled"

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question here",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        photo = PhotoImage(file="images/false.png")
        photo2 = PhotoImage(file="images/true.png")
        self.true_button = Button(image=photo2, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=photo, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
            self.buttons_state(ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.buttons_state(DISABLED)


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.buttons_state(DISABLED)
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.buttons_state(DISABLED)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state: str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)