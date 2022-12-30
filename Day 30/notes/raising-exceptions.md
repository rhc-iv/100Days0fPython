# Raising Exceptions:

---

In order to raise our own exceptions, we need to use the `raise` 
keyword to accomplish this. The syntax involves using the keyword, 
as well as the error type. We can even attach messages to our own 
exceptions:
```python
raise.TypeError("This is an error that I made up")
```
```text
TypeError: This is an error that I made up

Process finished with error code 1
```
Let's take a look at a more fleshed-out example:
```python
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should be less than 3 meters!")

bmi = weight / height ** 2
```
```text
ValueError: Human height should be less than 3 meters!

Process finished with error code 1
```
In the above example, we've stipulated thru our `raise` statement 
that any user input that exceed 3 meters will raise an exception 
that we've created.