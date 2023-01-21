#!/usr/bin/env python3

# --- AUTHENTICATION IN FLASK ---

# Authentication is normally used to associate user data with individual
# user accounts. It is a way of tying unique data to users. It can also be
# used to restrict access to certain parts of a website based on the status
# of a user account.

# The difficulty of authentication is deciding on the level of security that
# the authentication offers to the users of the website.

# The structure of the website for this course section is as follows:

# HOME PAGE
# The homepage will feature links (buttons) that will allow a user to select
# from one of two pages:

# REGISTER
# LOGIN

# The REGISTER page will be used to create new user accounts on the website
# while the LOGIN page will be used to verify current users of the website
# who have already completed the information gathered on the REGISTER page.

# Both the REGISTER and LOGIN pages will push data to another page:

# SECRETS
# The SECRETS page will act as the database/repository for all of the unique
# user information that is gathered on the REGISTER page while also checking
# credentials that users enter on the LOGIN page.

# --- LEVEL 1 AUTHENTICATION ---
# For this level of authentication, we will be using a simple registration
# process that asks for the following data for new users on the REGISTER page:

#   Name
#   Email
#   Password

# The 3 pieces of information (as text inputs on teh REGISTER page) will
# then be stored on the SECRETS page. When users who have completed the
# signup on the REGISTER page go to the LOGIN page, they will be asked to
# enter their Email/Password. This will then be checked against the
# information stored in our database (accessed thru the SECRETS page) to
# determine if they are a valid user & grant website access if they are.

# --- LEVEL 2 AUTHENTICATION ---
# This level of authentication will use encryption on the user credentials.

# --- LEVEL 3 AUTHENTICATION ---
# This level of authentication will use hashing on the user credentials.

# --- LEVEL 4 AUTHENTICATION ---
# This level of authentication will use salting on the user credentials.

