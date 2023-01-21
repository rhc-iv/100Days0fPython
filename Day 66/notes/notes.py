#!/usr/bin/env python3

# Today we are going to be attempting to create our own RESTful API in
# Python. REST stands for:

# RE(presentational) (S)tate (T)ransfer

# REST is actually an API architecture that has become commonplace in
# programming. There are other popular API architectures: SOAP, Falcor,
# and GraphQL to name a few. But Web APIs are almost universally
# constructed using REST.

# REST provides a collection of rules for creating an API & having that API
# be thought of as RESTful. There are 2 essential parts to crafting RESTful
# APIs:

# 1.    Use HTTP Request Verbs.
# 2.    Use a specific pattern of Routes/Endpoint URLs.

# --- HTTP REQUEST VERBS ---

# The 5 HTTP Request Verbs that make an API RESTful:

#   Get
#   Post
#   Put
#   Patch
#   Delete

# --- ROUTE/ENDPOINT URL PATTERNS ---

# --- ---  RESTful Routing --- ---

# HTTP VERBS          /articles          /articles/things

# GET                 Fetches ALL        Fetches THE article
#                     the articles.      on /things.
# POST                Creates ONE             ---
#                     new article.
# PUT                    ---             Updates THE article
#                                        on /things.
# PATCH                  ---             Updates THE article
#                                        on /things.
# DELETE              Deletes ALL        Deletes THE article
#                     the articles.      on /things.
