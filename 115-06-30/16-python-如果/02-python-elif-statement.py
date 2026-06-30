"""
Python Elif Statement
The Elif Keyword
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
"""
# Ex1. The Elif Keyword
print("Ex1. The Elif Keyword")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif a > b:
  print("a is greater than b")
print("")

"""
Multiple Elif Statements
You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.
"""
# Ex2. Testing multiple conditions:
print("Ex2. Testing multiple conditions:")
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
print("")

"""
How Elif Works
When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.

Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.
"""
# Ex3. Categorizing age groups:
print("Ex3. Categorizing age groups:")
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
print("")

"""
When to Use Elif
Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.
"""
# Ex4. Day of the week checker:
print("Ex4. Day of the week checker:")
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
print("")