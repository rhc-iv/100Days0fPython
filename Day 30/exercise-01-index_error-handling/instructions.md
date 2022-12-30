### Issue

We've got some buggy code. Try running the code. The code will crash and 
give you an `IndexError`. This is because we're looking through the 
`list` of fruits for an `index` that is out of range.

### Bad Output

```text
Traceback (Most recent call last):
    File "main.py", line 9, in <module>
    File "main.py", line 5, in make_pie
IndexError: list index out of range
```

### Instructions
Use what you've learnt about exception handling to prevent the program 
from crashing. If the user enters something that is out of range just 
print a default output of "_Fruit pie_". e.g.
```text
Fruit pie
```

### Hint

* You'll need to catch the `IndexError` exception.
* You'll need the `try`, `except` and `else` keywords.