#!/usr/bin/env python3

#  Up until now in this chapter, we haven't yet attempted to
#  check different conditions all within the same line of code.
#  Like this:
#      if condition1 & condition2 & condition3:
#          do this
#      else:
#          do this instead

# ---- Logical Operators ----
# There are 3 logical operators that allow us to check multiple
# conditions at once within a single line of code. They are:
#    and (i.e. - 'A and B')
#    or (i.e. - 'C or D')
#    not (i.e. - 'not E')

# ---- The 'and' Operator ----
# The logic of the 'and' operator is that if both conditions
# produce a boolean value of TRUE, then 'and' is parsed as
# TRUE. Otherwise, if either condition in the operator is
# parsed as FALSE, then the 'and' operator produces a boolean
# value of FALSE.

# The below 'and' operator would be TRUE given the value of 'a'
# stored in the variable.
a = 12
a > 10 and a < 13

# In this instance, the 'and' statement would be FALSE because at
# least one of the conditions (given the 'a' variable's value) 
# is FALSE.
a = 12
a > 15 and a <13

# ---- The 'or' Operator ----
# With the 'or' operator's logic, only one of the conditions 
# need to be TRUE in order for the entire statement to be parsed
# as TRUE. Like the 'and' operator mentioned before, both conditions
# being TRUE will also produce a result of TRUE.  Only if both
# conditions of the 'or' operator are FALSE will the whole statement
# be FALSE. In fact, we can re-use the previous code, changing only
# the operand from 'and' to 'or' to get a different result.

# This statement parses as TRUE because we've used the 'or' operator
# in place of the 'and' operator.
a = 12
a > 15 or a < 13

# The below code produces a boolean condition of FALSE because, even
# though we've used the 'or' operator, BOTH of the conditions in the
# statement are FALSE.
a = 12
a > 15 or a < 8

# ---- The 'not' Operator ----
# Finally, the 'not' operator reverses the boolean value of a
# condition. If the condition is TRUE, 'not' changes the value
# to FALSE and vice-versa.

# This code will switch the boolean value from FALSE to TRUE.
a = 12
not a > 15

