#!/usr/bin/env python3

# When working with modules and libraries, basic imports conform to
# the following syntax:

#   Keyword:            Module Name:
#   import              Module

# A more efficient way of doing imports is to directly import classes
# using the 'from...import' syntax:

#   from turtle import Turtle

# The 'from...import' syntax is very helpful if we plan on using our
# imported parts of the module over & over and don't want to keep
# typing the module name into our code.

# There's actually another way, using the 'from...import' syntax',
# to import the entire contents of the module by using an "*"
# character in place of what we want to import:

#    from turtle import *

# One issue with this syntax is that it's very confusing to
# understand the origin or even the order-of-operations of the
# attributes & methods of the module. As a result, this syntax is
# rarely used in Python code, but it is still useful to know what it
# looks like and what it does.

# ---- Aliasing Modules ----

# We can alias any module we'd like to import using the 'import...as'
# syntax. Let's alias the Turtle Graphics (turtle) module below:

# import turtle as t

# Aliasing modules is useful if we want to truncate module names or
# for modules with confusing or very long names.

# ---- Installing Modules ----

# Some modules/libraries/packages can't be imported in Python;
# instead, they must be installed to our computer in order to have
# access to them. These are often modules that aren't packaged with
# Python installations as standard libraries. However, in PyCharm,
# if we create an import statement for an uninstalled module,
# a red light bulb will pop-up informing the user of the issue AND it
# will allow that package (if one exists) to be installed from the
# PyCharm program without having to resort to the CLI.
