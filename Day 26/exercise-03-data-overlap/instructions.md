💪 This exercise is **HARD**

# Instructions

Take a look inside `file1.txt` and `file2.txt`. They each contain a 
bunch of numbers; each number on a new line. You are going to create 
a list called `result` which contains the numbers that are common in 
both files.

e.g. if `file1.txt` contained:
```
1
2
3
```
and file2.txt contained:
```
2
3
4
```
```
result = [2, 3]
```

### IMPORTANT: 
The result should be a list that contains **Integers**, not **Strings**. 
Try to use **List Comprehension** instead of a **Loop**.

#### Example Output
```
[3, 6, 5, 33, 12, 7, 42, 13]
```
**_Hint_**:

Use the keyword method for starting the List comprehension and fill in 
the relevant parts. First, you will need to read from the files and 
create a list using the lines in the files.

This method will be really useful: 

[Readlines](https://www.w3schools.com/python/ref_file_readlines.asp)

Remember you can check if a value exists in a list using the in keyword.

[Keyword "in"](https://www.w3schools.com/python/ref_file_readlines.asp)

Remember you can convert a **string** to an **int** using the `int()` method. 

[int() method](https://www.w3schools.com/python/ref_file_readlines.asp)