# Import statements:
import random
import time
import tkinter as tk


def start_test():
    start_time = time.time()
    phrases = [
        'Good Morning.',
        'Nice to meet you.',
        'Happy Birthday.',
        'I comb my hair.',
        'I brush my teeth.',
        'I like my school.',
        'I love my parents.',
        'My dad is my superhero.',
        'I will see you tomorrow.',
        'May I come in?',
        'How are you?',
        'How old are you?',
        'What is your name?',
        'The dog is happy.',
        'That is a pencil.',
        'It is very cold.',
        'These are my books.',
        'It is ten in the morning.',
        'An apple is good to eat.',
        'Your dress looks very nice.',
        'I opened the door.',
        'It is getting dark.',
        'I want to eat.',
        'What is your favorite color?',
        'I like to eat ice cream.',
        'My favorite color is blue.',
        'Where are you from?',
        'What is your favorite subject?',
        'My father is in his office.',
    ]

    # Pick a random sentence from the list:
    phrase = random.choice(phrases)

    # Set the label text to the random sentence:
    label.config(
        text=phrase,
    )

    def check_phrase():
        # Calculate the elapsed time of the test:
        elapsed_time = time.time() - start_time

        # Get the text from the input box:
        input_text = input_field.get()

        # Check if the input text matches the random sentence:
        if input_text == phrase:
            label.config(
                text='Correct! Time: {:.2f} seconds'.format(elapsed_time),
            )
        else:
            label.config(
                text='Incorrect. Try again.',
            )

    # Bind the "Enter" key to the check_phrase function:
    root.bind(
        '<Return>',
        lambda event: check_phrase(),
    )


# Create the Tkinter window:
root = tk.Tk()
root.geometry(
    '800x600',
)
root.title(
    'Typing Speed Test',
)


# Create a function to bind to the 'Clear' button:
def delete():
    input_field.delete(
        0,
        'end',
    )


# Add a label to display the random sentence:
label = tk.Label(
    root,
    font=(
        'SF Pro Display',
        18,
        'bold',
    ),
)
label.pack(
    pady=30,
)

# Add an input box for typing:
input_field = tk.Entry(
    root,
    font=(
        'SF Pro Display',
        18,
    ),
)
input_field.pack(
    pady=30,
)
input_field.focus()

# Add a 'Start' button:
start_button = tk.Button(
    root,
    command=start_test,
    font=(
        'SF Pro Display',
        18,
        'bold',
    ),
    text='START',
)
start_button.pack(
    padx=30,
    pady=30,
)

# Add a 'Clear' button:
clear_button = tk.Button(
    root,
    command=delete,
    font=(
        'SF Pro Display',
        18,
        'bold',
    ),
    text='CLEAR',
)
clear_button.pack(
    pady=30,
    padx=60,
)

# Run the Tkinter event loop:
root.mainloop()
