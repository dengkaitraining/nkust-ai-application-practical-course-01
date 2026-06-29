"""
Python Ternary Operator
The Ternary Operator
The ternary operator allows you to assign one value if a condition is true, and another if it is false:
"""
# Ex1. Assign a value to x: Assign the value "WEEKEND!" if the number is higher than 5, otherwise "Workday":
print("Ex1. Assign a value to x: Assign the value \"WEEKEND!\" if the number is higher than 5, otherwise \"Workday\":")
num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print("x = " + str(x))
print("")

"""
Instead of Elif:
The ternary operator can be used instead of elif in longer if statements:
"""
# Ex2. Assign: - "Fri" if num is 5 , - "Sat" if num is 6 , - "Sun" if num is 7 , - otherwise assign "weekday":
print("Ex2. Assign: - \"Fri\" if num is 5 , - \"Sat\" if num is 6 , - \"Sun\" if num is 7 , - otherwise assign \"weekday\":")
num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
print("x = " + str(x))
print("")