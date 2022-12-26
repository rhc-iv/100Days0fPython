# ---- Indentation -----

# In Python, indentation is a way to create 'blocks' of code
# that carry out all of their operations separate from our
# other code. The default indentation in Python is 4 spaces
# inside whatever our editor we are using to write code.
# Let's look at the format of a properly-indented code block:

# def my_function():
#     print("Hello")
#     print("World!")

# The above code will run, in order, independent from any
# other code in our program.

# Indentation is also important when we want to write outside
# of a code block we've created or we want to start another
# code block:

# def my_function():
#     print("Hello")
# print("World!")

# Above, the first print statement will operate within our
# defined function; the second print statement, by virtue
# of it's indentation, will operate outside of our defined
# function.

# A good way to understand indentation is to think about how
# computers work with files/folders. We have a directory, say
# "Home" and we can create sub-directories within it that
# serve their own purpose and contain their own files. But,
# these sub-directories are still within the "Home" folder:

# - HOME                         <---- Parent Folder (Main Function)
#   - Documents                  <----     Sub-Folder (Code Block 1)
#     - document1.doc            <----         File (Code Line 1)
#     - document2.doc            <----         File (Code Line 2)
#   - Movies                     <----     Sub-Folder (Code Block 2)
#     - Horror Movies            <----         Sub-Folder (Nested Code Block 1 in Code Block 2)
#       - horror_movie1.mov      <----             File (Code Line 1)
#       - horror_movie2.mov      <----             File (Code Line 2)
#     - Comedy Movies            <----         Sub-Folder (Nested Code Block 2 om Code Block 2)
#       - comedy_movie1.mov      <----             File (Code Line 1)
#       - comedy_movie2.mov      <----             File (Code Line 2)
#   - Music                      <----     Sub-Folder (Code Block 3)
#     - Rock Music               <----         Sub-Folder (Nested Code Block 1 in Code Block 3)
#       - rock_song1.song        <----             File (Code Line 1)
#       - rock_song2.song        <----             File (Code Line 2)

# ---- Spaces vs. Tabs ----

# Spaces and Tabs are functionally, for the most part, identical.
# But the official Python documentation prefers using Spaces. In
# fact, Python 3 disallows the mixing of Spaces and Tabs. Since the
# default indentation in Python is 4 Spaces, it's best to just
# remain consistent with the official Python documentation and use
# Spaces where appropriate.