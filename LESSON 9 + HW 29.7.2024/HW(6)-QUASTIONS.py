# HOMEWORK 6 QUESTIONS

# 1. What is the meaning of global inside a function?

# The global keyword in Python is used inside a function to indicate that
# a particular variable refers to a global variable.
# This means that instead of creating a new local variable within the function,
# the function will access and modify the variable that exists in the global scope.

# Disadvantages of using global in a function:

# Using global within a function can lead to several issues:

# 1. Unintended Side Effects: When you modify a global variable inside a function,
# it affects the variable globally throughout your program.
# This can lead to bugs that are hard to track, as changes in one part of the code might unintentionally affect other parts.

# 2. Decreased Code Readability: Code that heavily relies on global variables can be harder to understand and maintain.
# It is often unclear where and how global variables are modified, making the code more difficult to debug and extend.

# 3. Tight Coupling: Using global increases the dependency between different parts of the code.
# Functions that depend on global variables are less modular and more difficult to reuse in different contexts.

# 4. Future Maintenance: As the codebase grows, managing global variables becomes more challenging.
# Changes to global variables require careful consideration of all parts of the code that might be affected,
# leading to more complex and error-prone maintenance.

# START

# Why does the following code produce an error?
x: int = 1

def foo():
    print(x)
    x = 4

foo()

# END

# Explanation:

# The code produces an error because of how Python handles variable scope within functions.
# Specifically, this code will result in an UnboundLocalError with the message
# “local variable ‘x’ referenced before assignment.”

# Here’s what’s happening:

# 	1.	Local vs. Global Scope: When you assign a value to a variable inside a function,
# 	Python treats that variable as a local variable unless explicitly declared as global.

# 	2.	Local Variable Detection:
# 	In the function foo(), the line x = 4 causes Python to treat x as a local variable. However,
# 	before this assignment, the function tries to print x with print(x).
# 	At this point, Python hasn’t yet assigned a value to the local variable x,
# 	so it tries to reference a local variable that hasn’t been defined, resulting in an error.

# START

# Correcting the Code:

# To avoid the error, you can either:

# 1.Remove the Assignment:
x: int = 1

def foo():
    print(x)

foo()

# 2. Use the global Keyword if you intend to modify the global variable:
x: int = 1

def foo():
    global x
    print(x)
    x = 4

foo()
print(x)
# Now x is 4

# END