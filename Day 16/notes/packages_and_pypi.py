#!/usr/bin/env python3

# One of the places that we are able to access Python packages for use
# in our own code (via import & installation) is pypi.org. This website
# is a repository of Python packages developed & maintained (and usually
# offered as open-source).

# For the purposed of this course section, we'll use PyPI to search for,
# locate & install the 'prettytable' package. Now, if we were running
# this program in PyCharm, we could go to "Preferences" --> "Name of
# our Project" --> "Python Interpreter" and use that interface to
# "install" the PyPI package. Since we are using VS Code for this
# exercise, we have to use our computer's terminal (via our installed
# version of Python) to do this installation via the 'pip'(or 'pip3')
# command. Most packages on the PyPI website also display the 'pip'
# command for that package for easy copy-and-paste into our terminals.

# Once packages that we wish to use are "installed" (either via PyCharm
# or via the CLI), they are treated as libraries/modules in Python &
# are accessed using the typical 'import' statement:

#     import prettytable


# If we want to access more information about installed packages that we
# are using without having to go to the PyPI website, then PyCharm will
# actually facilitate that thru a right-click action upon the imported
# package from within the editor. The menu structure to navigate within
# PyCharm to do this is "Go To..." --> "Implementation(s)"