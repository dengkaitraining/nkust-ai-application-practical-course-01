"""
Python - Format - Strings
String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
"""
# Ex1. As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
print("Ex1. As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:")
age = 36
# print("My name is John, I am " + age) # This will raise an error.
print("Use the str(age) function: " + "My name is John, I am " + str(age))
print("")

"""
F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
"""
# Ex2. Use the f-string to combine strings and numbers:
print("Ex2. Use the f-string to combine strings and numbers:")
age = 36
txt = f"My name is John, I am {age}"
print(txt)
print("")

"""
Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.
"""
# Ex3. Add a placeholder for the price variable:
print("Ex3. Add a placeholder for the price variable:")
price = 59
txt = f"The price is {price} dollars"
print(txt)
print("")

"""
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
"""
# Ex4. Display the price with 2 decimals:
print("Ex4. Display the price with 2 decimals:")
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
print("")

"""
A placeholder can contain Python code, like math operations:
"""
# Ex5. Perform a math operation in the placeholder, and return the result:
print("Ex5. Perform a math operation in the placeholder, and return the result:")
txt = f"The price is {20 * 59:.2f} dollars"
print(txt)
usa = 1000
exchange_rate = 32.5
txt = f"The price is {usa * exchange_rate:.2f} New Taiwan Dollars"
print(txt)
print("")
