"""
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:
"""
# Ex1.
print("Ex1. ")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
print("newlist (Before) = " , newlist)

for x in fruits:
  if "a" in x:
    newlist.append(x)

print("newlist (After newlist.append(x)) = " , newlist)
print("")

# Ex2. With list comprehension you can do all that with only one line of code:
print("Ex2. With list comprehension you can do all that with only one line of code:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print("newlist (After - [x for x in fruits if \"a\" in x]) = " , newlist)
print("")

"""
The Syntax
 - newlist = [expression for item in iterable if condition == True]
 - The return value is a new list, leaving the old list unchanged.

Condition
The condition is like a filter that only accepts the items that evaluate to True.

* The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
* The condition is optional and can be omitted:
"""
# Ex3. Only accept items that are not "apple":
print("Ex3. Only accept items that are not \"apple\":")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print("newlist (After - [x for x in fruits if x != \"apple\"]) = " , newlist)
print("")

# Ex4. With no if statement:
print("Ex4. With no if statement:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print("newlist (After - [x for x in fruits]) = " , newlist)
print("")

"""
Iterable
The iterable can be any iterable object, like a list, tuple, set etc.
"""
# Ex5. You can use the range() function to create an iterable:
print("Ex5. You can use the range() function to create an iterable:")
newlist = [x for x in range(10)]
print("newlist (After - [x for x in range(10)]) = " , newlist)
print("")

# Ex6. Accept only numbers lower than 5:
print("Ex6. Accept only numbers lower than 5:")
newlist = [x for x in range(10) if x < 5]
print("newlist (After - [x for x in range(10) if x < 5]) = " , newlist)
print("")

"""
Expression
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
"""
# Ex7. Set the values in the new list to upper case:
print("Ex7. Set the values in the new list to upper case:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print("newlist (After - [x.upper() for x in fruits]) = " , newlist)
print("")

# Ex8. Set all values in the new list to 'hello':
print("Ex8. Set all values in the new list to 'hello':")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print("newlist (After - ['hello' for x in fruits]) = " , newlist)
print("")

# Ex9. Return "orange" instead of "banana":
print("Ex9. Return \"orange\" instead of \"banana\":")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print("newlist (After - [x if x != \"banana\" else \"orange\" for x in fruits]) = " , newlist)
print("")

