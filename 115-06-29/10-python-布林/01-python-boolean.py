"""
Python Booleans
Booleans represent one of two values: True or False.

Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""
# Ex1. Python returns the Boolean answer:
print("Ex1. Python returns the Boolean answer:")
print(10 > 9)
print(10 == 9)
print(10 < 9)
print("")

"""
When you run a condition in an if statement, Python returns True or False:
"""
# Ex2. Print a message based on whether the condition is True or False:
print("Ex2. Print a message based on whether the condition is True or False:")
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print("")

"""
Evaluate Values and Variables
The bool() function allows you to evaluate any value, and give you True or False in return,
"""
# Ex3. Evaluate a string and a number:
print("Ex3. Evaluate a string and a number:")
print(bool("Hello"))
print(bool(""))
print(bool(15))
print(bool(0))
print("")

# Ex4. Evaluate two variables:
print("Ex4. Evaluate two variables:")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
print("")

"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
# Ex5. The following will return True:
print("Ex5. The following will return True:")
print("bool(\"abc\") = " + str(bool("abc")))
print("bool(123) = " + str(bool(123)))
print("bool([\"apple\", \"cherry\", \"banana\"]) = " + str(bool(["apple", "cherry", "banana"])))
print("")

"""
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
"""
# Ex6. The following will return False:
print("Ex6. The following will return False:")
print("bool(False) = " + str(bool(False)))
print("bool(None) = " + str(bool(None)))
print("bool(0) = " + str(bool(0)))
print("bool(\"\") = " + str(bool("")))
print("bool(()) = " + str(bool(())))
print("bool([]) = " + str(bool([])))
print("bool({}) = " + str(bool({})))
print("")

"""
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""
# Ex7. Create a class with a __len__ function that returns 0:
print("Ex7. Create a class with a __len__ function that returns 0:")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print("bool(myobj) = " + str(bool(myobj)))
print("")

"""
Functions can Return a Boolean
You can create functions that returns a Boolean Value:
"""
# Ex8. Print the answer of a function:
print("Ex8. Print the answer of a function:")
def myFunction() :
  return True
print("myFunction() = " + str(myFunction()))
print("")

# Ex0. Print "YES!" if the function returns True, otherwise print "NO!":
print("Ex0. Print \"YES!\" if the function returns True, otherwise print \"NO!\":")
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
print("")

"""
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
"""
# Ex9. Check if an object is an integer or not:
print("Ex9. Check if an object is an integer or not:")
x = 200
print("isinstance(x, int) = " + str(isinstance(x, int)))