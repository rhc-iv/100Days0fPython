### Issue

We've got some buggy code, try running the code. The code will crash and 
give you a `KeyError`. This is because some of the posts in the 
`facebook_posts` don't have any "_Likes_".

### Bad Output
```text
Traceback (most recent call last):
    File "main.py", line 12, in <module>
NameError: name 'facebook_posts' is not defined

Process finished with error code 1
```

### Instructions

Use what you've learnt about exception handling to prevent the program 
from crashing.

### Hint

* You'll need to catch the `KeyError` exception.
* Posts without any likes can be counted as `0` likes.