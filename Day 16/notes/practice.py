#!/usr/bin/env python3

# First, let's import the PrettyTable class from our installation of the
# prettytable package:

from prettytable import PrettyTable, DOUBLE_BORDER
# from prettytable.colortable import ColorTable, Themes


# Next, let's create a 'table' object from the PrettyTable class, being
# careful to be mindful of proper Python syntax. Our class must be
# written using PascalCase & we must use parentheses in order to ensure
# that the class gets activated:

# table = PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
# table.add_rows([
#     ["Pikachu", "Electric"],
#     ["Squirtle", "Water"],
#     ["Charmander", "Fire"],
#     ])
# print(table)

# A quicker way to achieve this would be:
table = PrettyTable()
# table = ColorTable(theme=Themes.DEFAULT)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.set_style(DOUBLE_BORDER)
table.align = "c"

print(table)

# We've used a single method (.add_column) to populate our initial table
# from the prettytable import. Remember: in order to understand the
# structure, syntax & usage of attributes/methods called from Python
# packages, we can always refer to the documentation.

# In addition to methods, remember that objects also have attributes
# that can be changed (or defined) similar to variables. In the above
# example, we're going to change the .align attribute (that is part
# of the prettytable module) such that our table data gets aligned to
# the left as opposed to the center, which is the default alignment
# built into prettytable. According to the prettytable documentation,
# we use our object name (table) followed by the insertion of a "."
# character then follow that with an "=" character (just as we would
# when defining a variable) & then use a string of "l" to indicate a
# left-aligned table. We could also use "c" for center-aligned and
# "r" for right-aligned tables.
