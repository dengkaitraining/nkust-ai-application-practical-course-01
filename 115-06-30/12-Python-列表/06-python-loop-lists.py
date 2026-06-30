"""
Python - Loop Lists
Loop Through a List
You can loop through the list items by using a for loop:
"""
# Ex1. Print all items in the list, one by one:
print("Ex1. Print all items in the list, one by one:")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print("")

"""
Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
"""
# Ex2. Print all items by referring to their index number:
print("Ex2. Print all items by referring to their index number:")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(f"thislist[{i}] = " , thislist[i])
print("")

"""
Using a While Loop
You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
Remember to increase the index by 1 after each iteration.
"""
# Ex3. Print all items, using a while loop to go through all the index numbers
print("Ex3. Print all items, using a while loop to go through all the index numbers")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(f"thislist[{i}] = " , thislist[i])
  i = i + 1
print("")

"""
Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:
"""
# Ex4. A short hand for loop that will print all items in a list:
print("Ex4. A short hand for loop that will print all items in a list:")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
print("")