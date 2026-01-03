# https://python.org

# => This is a single-line comment in Python.

"""
This is how multi-line
comments are created in Python.
"""

'''
We can also use single quotes
for multi-line comments.
'''

# Variables in Python.
"""In Python, it is a convention to name variables using `snake_case`,
meaning all lowercase letters and words separated by underscores.
"""

# String variable type = string.
"""When we assign a value inside quotes (single or double), the variable
automatically takes the `str` (string) type, even if it looks like a number.
"""

my_variable = "Hello, this is my variable!"

my_string = "This is a string!"
my_other_string = 'This is also a string!'

my_variable_greetings = "Hello Python!"
# Variables can change their value. Up to this point, `my_variable` is:
# "Hello, this is my variable!". Now we assign a new value:
my_variable = "Now my variable has taken this new text value."

# Integer variable type = int
"""If we create a variable and assign a number without quotes,
the assigned type will automatically be an integer (`int`)."""

my_int = 1

# Floating-point variable type = float
"""If we create a variable and assign a decimal number (separated by a dot,
not a comma), the assigned type will automatically be a float (`float`).
"""

my_float = 1.735

# Boolean variable type = bool
"""Boolean variables (`bool`) can only have two possible values:
`True` or `False` (capitalized, since they are Python keywords).
"""

my_bool = True
my_second_bool = False

# Constants in Python.
"""In Python, constants do not exist as such. However, by convention,
they are written in uppercase letters to indicate they should not be modified.
Although technically, their value can still be changed.
"""

MY_CONSTANT = "My Constant"  # By convention.

# Here we change the value of the "constant", even though it should not be done.
MY_CONSTANT = "My Constant has changed its value!"

# Ways to print a value, a variable, or a CONSTANT by convention.
print("Hello World!")  # If we want to print a number or another type, we don’t use quotes.
print(my_variable_greetings)
print(MY_CONSTANT)

# How to print the type of a variable.
# The `type` function shows us the type of a variable.
print(type(my_string))  # Output: <class 'str'>
print(type(my_int))     # Output: <class 'int'>
print(type(my_float))   # Output: <class 'float'>
print(type(my_bool))    # Output: <class 'bool'>