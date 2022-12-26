# Reeborg's World Game Notes
(https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)[Click here]

>Write a program using an 'if/elif/else' statement so Reeborg can find the exit.
>```python
>if ...
>elif ...
>else ...
>```


## Instructions As Algorithm:
The last part of the game instructions offer a logical outline (or approach)
to having our Python code run such that we can "win" the game without giving
us explicit instructions. This type of guidance, in programming languages, is
considered an "***algorithm***"; this is a set of best-practices, in order, to arrive
at the solution to a problem. Pay close attention to the statements AND the order
of the instructions below:

>The secret is to have Reeborg ***follow along the right edge*** of the maze, ***turning right*** if it can, ***going straight*** ahead if it can’t turn right, or ***turning left*** as a last resort.