"""
Python - Copy Lists
Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
"""

"""
Use the copy() method
You can use the built-in List method copy() to copy a list.
"""
# Ex1. Make a copy of a list with the copy() method:
print("Ex1. Make a copy of a list with the copy() method:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
mylist = thislist.copy()
mylist2 = thislist;
thislist.pop()
print("thislist (After) = " , thislist)
print("mylist (After) = " , mylist)
print("mylist2 (After) = " , mylist2)
print("")

"""
Use the list() method
Another way to make a copy is to use the built-in method list().
"""
# Ex2. Make a copy of a list with the list() method:
print("Ex2. Make a copy of a list with the list() method:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
mylist = list(thislist)
mylist2 = thislist
thislist.pop()
print("thislist (After) = " , thislist)
print("mylist (After) = " , mylist)
print("mylist2 (After) = " , mylist2)
print("")

"""
Use the slice Operator
You can also make a copy of a list by using the : (slice) operator.
"""
# Ex3. Make a copy of a list with the : operator:
print("Ex3. Make a copy of a list with the : operator:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
mylist = thislist[:]
mylist2 = thislist
thislist.pop()
print("thislist (After) = " , thislist)
print("mylist (After) = " , mylist)
print("mylist2 (After) = " , mylist2)
print("")

