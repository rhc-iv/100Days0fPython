# Errors, Exceptions, and JSON Data

---

### Handling Errors & Exceptions:

#### _FileNotFoundError_

In a directory that only contains a `.py` file, if we write code 
that attempts to open another file in the same directory (and again, 
the file doesn't exist there):

```python
with open("a_file.txt") as file:
    file.read()
```
...we are then presented with a `FileNotFoundError` message in **Python**:
```text
FileNotFoundError: No such file or directory: 'a_file.txt'
```
To anticipate & avoid `FileNotFoundError` messages, ensure that:
* The path of the file is correct
* The spelling of the file is correct
---

#### _KeyError_

If we are accessing a `dictionary` & attempt to access a `key` 
pair that doesn't exist within that `dictionary`:

```python
a_dictionary = {"key1": "value1"}
value = a_dictionary["key2"]
```
...we are met with a `KeyError` message in **Python**:

```text
KeyError: 'key2'
```
To avoid `KeyError` messages, double-check the `dictionary` entries 
and ensure the `key` you want to access is in that `dictionary`.
---

#### _IndexError_

If we want to use index numbers to access items on a `list`, yet we 
supply an index number that doesn't correspond to a `list item`:

```python
fruit_list = ["Apple", "Banana", "Orange"]
fruit = fruit_list[3]
```
...we notice that an `IndexError` message appears in **Python**:

```text
IndexError: list index out of range
```
Avoiding `IndexError` messages is as easy as:
* Indexing within the range of `list items` in our list
* Remembering that a `list` index always begins with `0`
---

#### _TypeError_

If we attempt to use `functions` or `mathematical operands` on mixed 
data types or particular data types:

```python
text = "abc"
print(text + 5)
```
...we see that **Python** returns a `TypeError` message:

```text
TypeError: can only concatenate str (not "int") to str
```
`TypeError` does not implicitly return only the above message. When 
a `TypeError` is discovered in **Python**, the `TypeError` message 
will often tell the programmer what the exact problem is with the data 
types involved.
---

### Catching Exceptions:

In Python, there a 4 `keywords` that we can employ in order to deal 
with error messages more easily:

* `try`
* `except`
* `else`
* `finally`

The `try` keyword: Useful when dealing with a code block that 
_might_ cause an exception.

The `except` keyword: If an _exception does exist_, then this keyword 
is used.

The `else` keyword: This keyword gets applied to the code block if 
there _wasn't an exception_.

The `finally` keyword: This keyword is appropriate for a code block 
that we want to execute _no matter whether there was or wasn't an 
exception_.

---

### Examples:

An example of a `try`, `except` statement:
```python
try:
    file = open("a_text.txt")
except:
    print("There was an error finding the file.")
```
```text
There was an error

Process finished with error code 0
```

Here is another example, using the same keywords, that adds the 
`"w"`(write) argument so that if the file specified isn't found by 
**Python**, then it will be created instead:
```python
try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", "w")
```
```text
Process finished with exit code 0
```
In the above code, the file `a_file.txt` gets created in the same 
directory as the `.py` file with that code & the console simply 
shows an `exit code` of `0` which is a successful, error-free program.

---

`except` statement require specific scope:
```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["abcdefg"])
except:
    file = open("a_file.txt", "w")
```
```text
Process finished with exit code 0
```
In the above code, the `try` statement for that `a_dictionary` code 
should return a `KeyError`. But the `except` statement has already 
created a contingency for any errors caught in the `try` statement. 
**Python** has a way of dealing with this by having the `except` 
statement only return output for specific types of errors. The code 
below shows how this would be handled with our previous example:
```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["abcdefg"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
```
We point our `except` statement to the specific type of error we 
wish to correct; thus, all other errors in the `try` statement will 
not have an exception & will display as the correct type of error:
```text
KeyError: "abcdefg"\

Process finished with error code 1
```
We don't have to have only a single error exception; **Python** 
allows multiple `except` statements for all of the code in our `try` 
statement:
```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["abcdefg"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
except KeyError:
    print("That key does not exist.")
```
```text
That key does not exist.

Process finished with error code 0
```
Even if we've written `except` statements to handle all of the code 
in our `try` statement, we can still capture the specific errors 
that would have otherwise been generated by using the `as` keyword & 
using it to create a variable (here, `error_message`) that we can 
then use in our exception as an `f-string`:
```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["abcdefg"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
```
```text
The key "abcdefg" does not exist.

Process finished with error code 0
```

---

The `else` statement is used when we want to do something after our 
`try` statement has been executed with no exceptions:
```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
```
```text
value
Something

Process finished with exit code 0
```

---

Last, the `finally` statement is meant to include code that we want 
to run no matter what. If there is an error or not in the previous 
code, our `finally` statement code will run regardless:
```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
```
```text
value
Something
File was closed.

Process finished with error code 0
```