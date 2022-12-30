#!/usr/bin/env python3

from tkinter import *
import math

# --- CONSTANTS ---

BACKGROUND = "#32302F"
LAVENDER = "#C678DD"
RED = "#E06C75"
GREEN = "#98C379"
YELLOW = "#E5C07B"
FONT_NAME = "SF Pro Display"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

# --- TIMER RESET ---

# We need to create a function that gives the Reset button some
# usability:

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(
        timer_text,
        text="00:00",
    )
    title_label.config(
        text="Timer",
    )
    check_marks.config(
        text="",
    )
    global reps
    reps = 0

# --- TIMER MECHANISM ---

# We are going to need to create a function that starts our timer &
# ensures that the timer is started by the user pressing the "Start"
# button in our GUI:

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # We are going to call our "count_down" function that uses the
    # .after() method to create a count total:

    count_down(work_sec)

    # If it's the 8th repetition:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(
            text="Break",
            fg=RED,
        )
    elif reps % 2 == 0:
        # If it's 2nd/4th/6th repetition:
        count_down(short_break_sec)
        title_label.config(
            text="Break",
            fg=LAVENDER,
        )
    else:
        # If it's the 1st/3rd/5th/7th repetition:
        count_down(work_sec)
        title_label.config(
            text="Work",
            fg=GREEN,
        )

# --- COUNTDOWN MECHANISM ---

# We are going to create a "count_down" function here that Tkinter
# will use via the .after() method:

def count_down(count):
    count_min = math.floor(count /60)
    count_sec = count % 60

    # We are going to use Dynamic Typing to change the integer "0" to
    # a string "0" for any second count that is less than 10 so that
    # there is always a leading zero, which is the proper display
    # formatting for time:

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(
        timer_text,
        text=f"{count_min}:{count_sec}",
    )
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(
            text=marks,
        )

# --- UI SETUP ---

# Call the Tk() class & create our window:

window = Tk()

# We're going to use the .config() function in the Tk() class to
# "center" our supplied image even more:

window.config(
    bg=BACKGROUND,
    padx=100,
    pady=50,
)
window.title("Pomodoro Timer")

# We care going to create a title Label from the Label() class and
# use the .grid() function to position it in our window:

title_label = Label(
    bg=BACKGROUND,
    fg=GREEN,
    font=(
        FONT_NAME,
        32,
        "bold",
    ),
    text="TIMER"
)
title_label.grid(
    column=1,
    row=0,
)

# Call the PhotoImage() class to reference our supplied image for use
# by other classes:

butt_img = PhotoImage(
    file="background.png",
)

# Call the Canvas() class to use our supplied image as the background
# for our window:

canvas = Canvas(
    bg=BACKGROUND,
    highlightthickness=0,
    width=200,
    height=200,
)

# Within the Canvas() class, use the .create_image() function to
# create a tuple that takes as input: integers for the "center" of
# the supplied image expressed as x & y coordinates, then an "image="
# argument that references the variable previously created within the
# PhotoImage() class that allows access to the supplied image in our
# project folder:

canvas.create_image(
    100,
    100,
    image=butt_img,
)

# Within the Canvas() class, we are going to also use the
# .create_text() function to add text to our screen. The tuple type
# is the same as the .create_image() function, except the last
# argument is going to be a string of the text we want to display. We
# are also going to stipulate the color of the text with the "fill="
# argument and specify the font per Tkinter specifications:

timer_text = canvas.create_text(
    100,
    100,
    text="00:00",
    fill=BACKGROUND,
    font=(
        FONT_NAME,
        24,
        "bold",
    ),
)

# Finally, we need to use the .grid() function to load our Canvas
# object into our window:

canvas.grid(
    column=1,
    row=1,
)

# At this point, we need to create 2 different buttons from the
# Button() class in Tkinter; one to "start" the timer & one to
# "reset" the timer:

start_btn = Button(
    command=start_timer,
    fg=GREEN,
    font=(
        FONT_NAME,
        16,
        "bold",
    ),
    text="Start",
)
start_btn.config(
    padx=10,
    pady=10,
)
start_btn.grid(
    column=0,
    row=3,
)
reset_btn = Button(
    command=reset_timer,
    fg=YELLOW,
    font=(
        FONT_NAME,
        16,
        "bold",
    ),
    text="Reset",
)
reset_btn.config(
    padx=10,
    pady=10,
)
reset_btn.grid(
    column=3,
    row=3,
)

# We are going to create another Label() class object that uses an
# emoji in the form of a "check mark":

check_marks = Label(
    bg=BACKGROUND,
)
check_marks.grid(
    column=1,
    row=4,
)

window.mainloop()
