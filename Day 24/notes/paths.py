#!/usr/bin/env python3

# -> Paths <-
# -----------

# When working with files, we know that all files have a name of some
# sort. But because these files "live" on our computers and because
# computer operating systems use hierarchical methods, files also have
# what it known as a "path" or a place within the operating system's
# hierarchy where they reside.

# Let's look at an example file structure (hierarchy):

# Macintosh HD (Root)
# |
# |__ Users (Directory)
#     |
#     |__ rhc.iv (Directory)
#         |
#         |__ Development (Directory)
#             |
#             |__ 100 Days Of Python (Directory)
#                 |
#                 |__ Course Sections (Directory)
#                     |__ README.md (file)
#                     Day 01 (Directory)
#                     |__ main.py (file)
#                     |__ project.py (file)
#                     Day 02 (Directory)
#                     |__ main.py (file)
#                     |__ project.py (file)
#                     Day 03 (Directory)
#                     |__ main.py (file)
#                     |__ project.py (file)

# The "root" of a path is the origin for the file structure
# hierarchy. Within this "root", we can have both directories and
# files and they are "nested" (placed within) the "root" and those
# directories and files are nested within other directories.

# -> Absolute File Path <-
# ------------------------

# An absolute path is the ordered direction to a directory or a path
# within a computer's hierarchical system starting from the ROOT. It
# starts from the "origin", or the highest-level part of the
# computer's storage system. (In the example above, the ROOT would be
# the "Macintosh HD", which is the computer's hard drive.)

# -> Relative File Path <-
# ------------------------

# If we are working from within a directory (called the "working
# directory"), then we can use relative file paths. Relative file
# paths are the way we access directories and files when we are
# already within a directory that contains those directories and
# files. Let's repeat the directory structure from above, but let's
# make the assumption that we are already in the Day 3 project folder
# using our IDE (PyCharm, in this case):

# Macintosh HD (Root)
# |
# |__ Users (Directory)
#     |
#     |__ rhc.iv (Directory)
#         |
#         |__ Development (Directory)
#             |
#             |__ 100 Days Of Python (Directory)
#                 |
#                 |__ Course Sections (Directory)
#                     |__ README.md (file)
#                     Day 01 (Directory)
#                     |__ main.py (file)
#                     |__ project.py (file)
#                     Day 02 (Directory)
#                     |__ main.py (file)
#                     |__ project.py (file)
#                     Day 03 -> (Working Directory) <-
#                     |__ main.py (file)
#                     |__ project.py (file)

# If we were trying to access the "main.py" file in the "Day 03"
# directory, the absolute file path would be:

# /Users/rhc.iv/Development/100_Days_Of_Python/Course_Sections/Day_03
# /main.py

# But if we were already using "Day 03" as our working directory,
# then the relative file path to "main.py" would simply be:

# ./main.py

# The "./" characters together indicate to Python to "look" in the
# current folder (working directory) for the directory or file that
# is indicated after them. This methodology does not change as we
# move to a higher-level directory above our working directory. For
# instance, the relative file path of the same file from 1 level
# above our working directory would look like this:

# ./Day_03/main.py

# If we want to get a relative file path for a directory or file that
# is at a higher-level than the current working directory, we use a
# different notation. Assuming that we are back in "Day 03" (our
# working directory), but we want to access the "README.md" file that
# is in the parent "Course Sections" folder, we would do this:

# ../README.md

# The "../" characters tell Python to search for the directory or
# file that we want in the directory ABOVE (hierarchically speaking)
# the current directory we are in. We can even iterate thru the file
# structure beyond the immediate parent directory:

# ../../file.file

# In the above example, we have moved 2 levels above our working
# directory in order to access a given file.

# As long as directories and files are in the same hierarchical level
# as our working directory, then Python does not require us to use
# the "./" characters for the relative file path. If we were again in
# "Day 03" as our working directory & we wanted to access the
# "main.py" file, in Python we simply would have to type the file name:

# main.py
