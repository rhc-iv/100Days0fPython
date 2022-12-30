#!/usr/bin/env python3

# --- IMPORTS ---

from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

# --- CONSTANTS ---

BACKGROUND = "#32302F"
RED = "#BE5046"
GRAY = "#545862"
GREEN = "#98C379"


# --- PASSWORD GENERATOR ---

#     This is previous Python code imported from the Day 05 Course
#     Section of the class wherein we built a password generator. It
#     is being repurposed for implementation into our app here. We
#     are going to assign it as a function as well:

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in
                        range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in
                        range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in
                        range(randint(2, 4))]

    password_list = password_letters + password_symbols + \
                    password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# --- SAVE PASSWORD ---

#     Create a function that adds the user's information, supplied in
#     the app entries, to a file that is created/amended each time
#     the "Add" button is pressed. Each entry should be created
#     with its own line in the file. Also, after the "Add" button is
#     clicked & the user information is added to our text file,
#     clear both the "Website" and "Password" entry fields:

def save():
    website = website_entry.get()
    email = email_user_entry.get()
    pwd = password_entry.get()

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(
            title="Oops!",
            message="Please make sure to complete all fields!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \n Email: "
                    f"{email} \n "
                    f"Password: {pwd} \n Is it okay to save?",
        )
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(
                    f"{website} | {email} | {pwd}\n"
                )
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --- UI SETUP ---

#     Create application window:

window = Tk()
window.config(
    bg=BACKGROUND,
    padx=50,
    pady=50,
)
window.title("MyPass Manager")

#     Create background image via PhotoImage() class  and Canvas()
#     class:

canvas = Canvas(
    bg=BACKGROUND,
    highlightthickness=0,
    width=200,
    height=200,
)

lock_img = PhotoImage(
    file="logo.png"
)

canvas.create_image(
    125,
    100,
    image=lock_img,
)

canvas.grid(
    column=1,
    row=0,
)

#     Create labels for the following: Website, Email/Username,
#     & Password. These labels should all be within column 0,
#     then (in order of appearance) they should reside in row 1,
#     row 2, & row 3:

website_label = Label(
    fg=RED,
    font=(
        "SF Pro Display",
        16,
        "bold",
    ),
    text="Website :",
)
website_label.grid(
    column=0,
    row=1,
)

email_user_label = Label(
    fg=RED,
    font=(
        "SF Pro Display",
        16,
        "bold",
    ),
    text="Email/Username :",
)
email_user_label.grid(
    column=0,
    row=2,
)

password_label = Label(
    fg=RED,
    font=(
        "SF Pro Display",
        16,
        "bold",
    ),
    text="Password :",
)
password_label.grid(
    column=0,
    row=3,
)

#     Create 3 corresponding entries for the labels above. In order,
#     they should appear as such:
#         "Website" Entry should have a width of 35 and should appear
#         on column 1, row 1, with a columnspan of 2. The app,
#         when run, should also focus this entry field.
#         "Email/Username" Entry should have a width of 21 and should
#         appear on column 1, row 2. It should also have a rote email
#         address from the user appear in the entry field.
#         "Password" Entry should have a width of 21 and should
#         appear on column 1, row 3.

website_entry = Entry(
    bg=RED,
    borderwidth=2,
    cursor="pencil",
    fg=BACKGROUND,
    font=(
        "SF Pro Display",
        15,
        "normal",
    ),
    justify="center",
    width=42,
)
website_entry.grid(
    column=1,
    row=1,
    columnspan=2,
)
website_entry.focus()

email_user_entry = Entry(
    bg=RED,
    borderwidth=2,
    cursor="pencil",
    fg=BACKGROUND,
    font=(
        "SF Pro Display",
        15,
        "normal",
    ),
    justify="center",
    width=42,
)
email_user_entry.grid(
    column=1,
    row=2,
    columnspan=2,
)
email_user_entry.insert(
    END,
    "rhc.iv@icloud.com",
)

password_entry = Entry(
    bg=RED,
    borderwidth=2,
    cursor="pencil",
    fg=BACKGROUND,
    font=(
        "SF Pro Display",
        15,
        "normal",
    ),
    justify="center",
    width=24,
)
password_entry.grid(
    column=1,
    row=3,
)

#     Create 2 buttons, one labeled "Generate Password" and another
#     one labeled "Add". Their specifications are as follows:
#         The "Generate Password" button should be located in column
#         2, row 3.
#         The "Add" button should be located in column 1, row 4,
#         and have a width of 36.

gen_pass = Button(
    bg=GRAY,
    command=generate_password,
    fg=GREEN,
    font=(
        "SF Pro Display",
        16,
        "bold",
    ),
    highlightthickness=0,
    justify="center",
    text="Generate Password",
)
gen_pass.grid(
    column=2,
    row=3,
)

add_button = Button(
    bg=GRAY,
    command=save,
    fg=GREEN,
    font=(
        "SF Pro Display",
        16,
        "bold",
    ),
    highlightthickness=0,
    justify="center",
    text="Add",
    width=36,
)
add_button.grid(
    column=1,
    row=4,
    columnspan=2,
)

window.mainloop()
