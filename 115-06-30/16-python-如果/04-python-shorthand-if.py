"""
Python Shorthand If
Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

Note: You still need the colon : after the condition.
"""
# Ex1. One-line if statement:
print("Ex1. One-line if statement:")
a = 5
b = 2
if a > b: print("a is greater than b")
print("")

"""
Short Hand If ... Else
If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

This is called a conditional expression (sometimes known as a "ternary operator").
"""
# Ex2. One-line if/else that prints a value:
print("Ex2. One-line if/else that prints a value:")
a = 2
b = 330
print("A") if a > b else print("B")
print("")

"""
Assign a Value With If ... Else
You can also use a one-line if/else to choose a value and assign it to a variable:

The syntax follows this pattern:
variable = value_if_true if condition else value_if_false
"""
# Ex3. You can also use a one-line if/else to choose a value and assign it to a variable:
print("Ex3. You can also use a one-line if/else to choose a value and assign it to a variable:")
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
print("")

print("Ex3. (equivalent) You can also use a one-line if/else to choose a value and assign it to a variable:")
bigger = a
if a > b:
  bigger = a
else:
  bigger = b
print("Bigger is", bigger)
print("")

"""
Multiple Conditions on One Line
You can chain conditional expressions, but keep it short so it stays readable:
"""
# Ex4. One line, three outcomes:
print("Ex4. One line, three outcomes:")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print("")

print("Ex4. (equivalent) One line, three outcomes:")
if a > b:
  print("A")
else:
  if a == b:
    print("=")
  else:
    print("B")
print("")