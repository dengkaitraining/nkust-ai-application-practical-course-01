"""
The Walrus Operator
Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
"""
# Ex1. The count variable is assigned in the if statement, and given the value 5:
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")