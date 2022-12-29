#!/usr/bin/env python3

# -> The open() method <-
# -----------------------

# The open() method is a built-in function in Python that allows for
# interaction with files. It typically takes 2 positional arguments
# and another keyword argument. The first argument is a string that
# gives the filename: the filename only if the file is in the same
# directory as the Python file accessing it with the open() method
# or the file path if not.
# The second argument is a string containing characters describing
# how the file will be used: "r" = read only, "w" = write only (this
# overwrites the file), and "a" = open the file and append to it;
# that is, the file will be opened and any data passed to the file
# will be added to the end. Additionally, "r+" opens the file for
# reading AND writing. This argument is optional: if no mode is
# passed, the file will be opened for reading only. By default,
# if no mode argument is passed, any subsequent data added to the
# file will be appended.
# The third argument is a keyword argument that sets the encoding of
# the file. In almost all cases, the encoding will be set to "utf-
# 8". Since there are rare use-cases (binary files) where the
# encoding is different, "utf-8" is implicitly understood by Python &
# does not need to be typed.


# open("test.txt", "r+", encoding="utf-8")

# After arguments have been passed to the open() method, it can then
# be saved as a variable:

# file = open("test.txt")

# -> read() method <-
# -------------------

# The read() method returns the contents of the file. It does take an
# integer as an argument to indicate the byte size of the returned
# file. The default argument is -1 and is implicit; it does not have
# to be typed & represents the entire contents of the file.

# file.read()

# Similar to the write() method, the read() method can also be saved
# to a variable. As with any variable, the data can be printed to the
# console using the print() function. Therefor, a print statement made
# on the variable that contains the read() method will print the
# contents of the file being read:

# contents = file.read()

# print(contents)

# -> The close() method <-
# ------------------------

# The close() method closes an open file in Python.

# file.close()

# -> The "with" keyword <-
# ------------------------

# The "with" keyword can be used as a way to implement the open()
# method while also ensuring that the file will be closed without
# adding the additional close() method and also allows, using the
# "as" keyword in conjunction, the file to be saved to a variable:

# with open("test.txt") as file:
#     contents = file.read()
#     print(contents)

# -> The write() method <-
# ------------------------

# The write() method takes, as input, a string that will be written
# to our current file in Python. The open() method must specify the
# "w" mode argument for the write() method to work, otherwise Python
# parses the file that is the target of the open() method as "r" or
# read-only.

# with open("test.txt", mode="w") as file:
#     file.write("hijklmnop")

# The above write() method operation OVERWRITES the contents of the
# file.  That is, each time the write() method is called, it will
# take the string input and replace the previous contents of the
# file. If we want to keep the contents of the open file and use the
# write() method to ADD its input to the open file (instead of
# replacing it), we need to use the "a" mode argument. The string
# inside of the write() method should be prepended with a newline
# character.

# with open("test.txt", mode="a") as file:
#     file.write("\nhijklmnop")

# The write() method, use along with the open() method & the "with"
# keyword, can be used to create a NEW FILE and pass data to it. For
# this, we simply need to indicate within the open() method an unused
# file name. Once done, a new file (of the file type we input) will
# be created in the current directory & will also pass the string
# from the write() method into that file.

with open("new_test.txt", mode="a") as file:
    file.write("This is a new file created in Python.")

# The mode argument in our open() method above can be set to either
# "w" or "a"; either works for the INITIAL creating & writing to the
# new file.