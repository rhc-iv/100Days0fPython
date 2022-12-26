#!/usr/bin/env python3

# The general idea of "nesting" in Python is that we
# take one part of our code & 'put it inside' another
# part of our code. This can take place in the form of
# code blocks (like nesting 'if/else' statements inside
# , say, a 'for' loop) or it can be the same types of
# Python elements: we can nest lists or dictionaries
# inside of other lists or dictionaries.

# Let's begin with the following dictionary:
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Next let's try to nest a list within another
# dictionary:
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Above, it's important that we don't forget the
# syntax, particularly the comma-separation between
# both the list items and the dictionaries. This can get
# confusing at times, so let's look at a template for
# nesting:

#     [{
#         Key: [List],
#         Key2: {Dictionary},
#     },
#     {
#         Key: Value,
#         Key2: Value,
#     }]

# We can also nest dictionaries inside of lists.
# Let's use the same 'travel_log' template as
# above:

travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
    },
]

# Usually in Python, code tends to be more readable
# when it is line-separated between multiple line &
# dictionary entries. Since those items are usually
# comma-separated, that is a good point to move the 
# follow-on code to a newline.