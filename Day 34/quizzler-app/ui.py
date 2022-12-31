#!/usr/bin/env python3

# --- IMPORTS ---

from quiz_brain import QuizBrain
from tkinter import *

# --- CONSTANTS, DICTS, GLOBALS ---

THEME_COLOR = "#375362"


# --- CLASSES ---

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            bg=THEME_COLOR,
            padx=20,
            pady=20,
        )

        self.score_label = Label(
            bg=THEME_COLOR,
            fg="white",
            font=(
                "Louis George Cafe",
                16,
                "normal",
            ),
            text="Score: 0",
        )
        self.score_label.grid(
            column=1,
            row=0,
        )

        self.canvas = Canvas(
            bg="white",
            height=250,
            width=300,
        )

        self.question_text = self.canvas.create_text(
            150,
            125,
            fill=THEME_COLOR,
            font=(
                "Louis George Cafe",
                20,
                "italic",
            ),
            text="Some Question Text",
            width=280,
        )
        self.canvas.grid(
            column=0,
            row=1,
            columnspan=2,
            pady=50,
        )

        true_image = PhotoImage(
            file="images/true.png",
        )
        self.true_button = Button(
            command=self.true_pressed,
            highlightthickness=0,
            image=true_image,
        )
        self.true_button.grid(
            column=0,
            row=2,
        )
        false_image = PhotoImage(
            file="images/false.png",
        )
        self.false_button = Button(
            command=self.false_pressed,
            highlightthickness=0,
            image=false_image,
        )
        self.false_button.grid(
            column=1,
            row=2,
        )

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(
            bg="white",
        )
        if self.quiz.still_has_questions():
            self.score_label.config(
                text=f"Score: {self.quiz.score}",
            )
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(
                self.question_text,
                text=q_text,
            )
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz.",
            )
            self.true_button.config(
                state="disabled",
            )
            self.false_button.config(
                state="disabled",
            )

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(
                bg="green",
            )
        else:
            self.canvas.config(
                bg="red",
            )
        self.window.after(
            1000,
            self.get_next_question,
        )
