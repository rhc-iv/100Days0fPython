#!/usr/bin/env python3

# -> The Tkinter Module <-
# ------------------------

# The Tkinter Module allows the creation of a Graphical User
# Interface (or GUI) for our Python code.

# -> The Packer <-
# ----------------

# The packer is one of Tk’s geometry-management mechanisms. Geometry
# managers are used to specify the relative positioning of widgets
# within their container - their mutual master. In contrast to the
# more cumbersome placer (which is used less commonly, and we do not
# cover here), the packer takes qualitative relationship
# specification - above, to the left of, filling, etc - and works
# everything out to determine the exact placement coordinates for you.
#
# The size of any master widget is determined by the size of the
# “slave widgets” inside. The packer is used to control where slave
# widgets appear inside the master into which they are packed. You
# can pack widgets into frames, and frames into other frames,
# in order to achieve the kind of layout you desire. Additionally,
# the arrangement is dynamically adjusted to accommodate incremental
# changes to the configuration, once it is packed.
#
# Note that widgets do not appear until they have had their geometry
# specified with a geometry manager. It’s a common early mistake to
# leave out the geometry specification, and then be surprised when
# the widget is created but nothing appears. A widget will appear
# only after it has had, for example, the packer’s pack() method
# applied to it.
#
# The pack() method can be called with keyword-option/value pairs
# that control where the widget is to appear within its container,
# and how it is to behave when the main application window is resized.

# More documentation on the pack() method can be found at:

# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm

# -> Advanced Python Arguments <-
# -------------------------------

# Most methods & functions the take arguments or parameter delineate
# between argument types. If a parameter is optional (or the hover
# documentation shows "..." for that parameter), that typically means
# that there is a default value for that parameter. Otherwise,
# the parameter must be specified.

# -> Unlimited Positional Arguments <-
# -------------------------

# In order to have unlimited argument inputs when creating functions,
# we use the "*args" within the function brackets. This tells python
# that the function can have any number of arguments. It is important
# to note that all of the arguments are positional & will be treated
# as such:

#   def add(*args):
#       for n in args:
#           print(n)

# -> Unlimited Keyword Arguments <-
# ---------------------------------

