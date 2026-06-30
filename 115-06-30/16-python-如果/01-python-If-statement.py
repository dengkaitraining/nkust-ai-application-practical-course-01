"""
Python If Statement
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

1. Equals: a == b
2. Not Equals: a != b
3. Less than: a < b
4. Less than or equal to: a <= b
5. Greater than: a > b
6. Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""
# Ex1. If statement:
print("EX1. If statement:")
a = 33
b = 200
if b > a:
  print("b is greater than a")
print("")

"""
How If Statements Work
The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.
"""
# Ex2. Checking if a number is positive:
print("Ex2. Checking if a number is positive:")
number = 15
if number > 0:
  print("The number is positive")
print("")

"""
Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
"""
# Ex3. If statement, without indentation (will raise an error):
print("Ex3. If statement, without indentation (will raise an error):")
a = 33
b = 200
if b > a:
#print("b is greater than a") # you will get an error
  print("b is greater than a")
#print("a is >- than b")
print("")

"""
Multiple Statements in If Block
You can have multiple statements inside an if block. All statements must be indented at the same level.
"""
# Ex4. Multiple statements in an if block:
print("Ex4. Multiple statements in an if block:")
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
print("")

"""
Using Variables in Conditions
Boolean variables can be used directly in if statements without comparison operators.
"""
# Ex5. Using a boolean variable:
print("Ex5. Using a boolean variable:")
is_logged_in = True
if is_logged_in:
  print("Welcome back!")
print("")