"""
Python Logical Operators
Logical operators are used to combine conditional statements. Python has three logical operators:

1. and - Returns True if both statements are true
2. or  - Returns True if one of the statements is true
4. not - Reverses the result, returns False if the result is true

The and Operator
The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.
"""
# Ex1. Test if a is greater than b, AND if c is greater than a:
print("Ex1. Test if a is greater than b, AND if c is greater than a:")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
print("")

"""
The or Operator
The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.
"""
# Ex2. Test if a is greater than b, OR if a is greater than c:
print("Ex2. Test if a is greater than b, OR if a is greater than c:")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
print("")

"""
The not Operator
The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
"""
# Ex3. Test if a is NOT greater than b:
print("Ex3. Test if a is NOT greater than b:")
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
print("")

"""
Combining Multiple Operators
You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.
"""
# Ex4. Combining and, or, and not:
print("Ex4. Combining and, or, and not:")
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
print("")

"""
Using Parentheses for Clarity
When combining multiple logical operators, use parentheses to make your intentions clear and control the order of evaluation.
"""
# Ex5. Using parentheses for complex conditions:
print("Ex5. Using parentheses for complex conditions:")
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
print("")

# Ex6. User authentication check:
print("Ex6. User authentication check:")
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
print("")

# Ex7. Range checking with logical operators:
print("Ex7. Range checking with logical operators:")
score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")