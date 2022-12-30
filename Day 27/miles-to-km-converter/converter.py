#!/usr/bin/env python3

from tkinter import *

# TODO 8: Create a function that converts miles-to-kilometers:

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilo_result_label.config(
        font=(
            "SF Pro Display",
            16,
            "bold",
        ),
        text=f"{km}"
    )

# TODO 1: Create & size the GUI window:

window = Tk()
window.configure(
    borderwidth=4,
    padx=10,
    pady=10,
    relief="groove",
)
window.minsize(300, 100)
window.title("Miles-to-Kilometers Converter")

# TODO 2: Create user entry box:

miles_input = Entry(
    bg="gray",
    cursor="pencil",
    font=(
        "SF Pro Display",
        14,
        "normal",
    ),
    width=7,
)
miles_input.grid(
    column=1,
    row=0,
)

# TODO 3: Create a label for our entry box:

miles_label = Label(
    font=(
        "SF Pro Display",
        16,
        "normal",
    ),
    text="Miles"
)
miles_label.grid(
    column=2,
    row=0,
)

# TODO 4: Create label to being our conversion sentence in our window:

is_equal_to = Label(
    font=(
        "SF Pro Display",
        16,
        "normal",
    ),
    text="... is equal to: "
)
is_equal_to.grid(
    column=0,
    row=1,
)

# TODO 5: Create second part of our conversion sentence, which will
#  be a label that shows the conversion from miles to kilometers:

kilo_result_label = Label(
    font=(
        "SF Pro Display",
        16,
        "bold",
    ),
    text="0"
)
kilo_result_label.grid(
    column=1,
    row=1,
)

# TODO 6: Finish our conversion sentence by adding the label
#  "Kilometers" at the end:

kilo_label = Label(
    font=(
        "SF Pro Display",
        16,
        "normal",
    ),
    text="Kilometers"
)
kilo_label.grid(
    column=2,
    row=1,
)

# TODO 7: Finally, add a button, labeled "Calculate" at the bottom of
#  our converter:

calc_button = Button(
    command=miles_to_km,
    font=(
        "SF Pro Display",
        18,
        "bold",
    ),
    text="CALC"
)
calc_button.grid(
    column=1,
    row=2,
)

window.mainloop()