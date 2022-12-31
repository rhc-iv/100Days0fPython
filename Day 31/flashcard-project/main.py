#!/usr/bin/env python3

# --- IMPORTS ---

from tkinter import *
import pandas as pd
import random

# --- CONSTANTS/GLOBALS ---

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# --- EXCEPTIONS ---

try:
    data = pd.read_csv("data/words-to-learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(
        orient="records",
    )
else:
    to_learn = data.to_dict(
        orient="records",
    )

# --- FUNCTIONS ---


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(
        card_title,
        text="French",
        fill="black",
    )
    canvas.itemconfig(
        card_word,
        text=current_card["French"],
        fill="black",
    )
    canvas.itemconfig(
        card_background,
        image=card_front,
    )
    flip_timer = window.after(
        7000,
        func=flip_card,
    )


def flip_card():
    canvas.itemconfig(
        card_title,
        text="English",
        fill="white",
    )
    canvas.itemconfig(
        card_word,
        text=current_card["English"],
        fill="white",
    )
    canvas.itemconfig(
        card_background,
        image=card_back,
    )


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(
        "data/words-to-learn.csv",
        index=False
    )
    next_card()


# --- UI CREATION ---

#     - Window Setup -


window = Tk()
window.config(
    bg=BACKGROUND_COLOR,
    padx=50,
    pady=50,
)
window.title("Flashy")
flip_timer = window.after(
    7000,
    func=flip_card,
)

#     - Canvas Setup -

canvas = Canvas(
    height=526,
    width=800,
)
card_front = PhotoImage(
    file="images/card_front.png"
)
card_back = PhotoImage(
    file="images/card_back.png"
)
card_background = canvas.create_image(
    400,
    263,
    image=card_front,
)
card_title = canvas.create_text(
    400,
    150,
    fill="black",
    font=(
        "Lemon Milk",
        40,
        "italic",
    ),
    text="",
)
card_word = canvas.create_text(
    400,
    263,
    fill="black",
    font=(
        "Lemon Milk",
        60,
        "bold",
    ),
    text="",
)
canvas.config(
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
)
canvas.grid(
    column=0,
    row=0,
    columnspan=2,
)

#    - Button Setup -

wrong_image = PhotoImage(
    file="images/wrong.png"
)
wrong_button = Button(
    borderwidth=0,
    command=next_card,
    highlightthickness=0,
    image=wrong_image,
)
wrong_button.grid(
    column=0,
    row=1,
)

right_image = PhotoImage(
    file="images/right.png"
)
right_button = Button(
    borderwidth=0,
    command=is_known,
    highlightthickness=0,
    image=right_image,
)
right_button.grid(
    column=1,
    row=1,
)

# --- FUNCTION CALLS ---

next_card()

window.mainloop()
