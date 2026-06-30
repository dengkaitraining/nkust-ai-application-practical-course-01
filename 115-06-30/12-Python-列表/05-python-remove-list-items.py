"""
Python - Remove List Items
Remove Specified Item
The remove() method removes the specified item.
"""
# Ex1. Remove "banana":
print("Ex1. Remove \"banana\":")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
thislist.remove("banana")
print("thislist (After) = " , thislist)
print("")

"""
If there are more than one item with the specified value, the remove() method removes the first occurrence:
"""
# Ex2. Remove the first occurrence of "banana":
print("Ex2. Remove the first occurrence of \"banana\":")
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print("thislist (Before) = " , thislist)
thislist.remove("banana")
print("thislist (After) = " , thislist)
print("")

"""
Remove Specified Index
The pop() method removes the specified index.
"""
# Ex3. Remove the second item:
print("Ex3. Remove the second item:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
thislist.pop(1)
print("thislist (After) = " , thislist)
print("")

"""
If you do not specify the index, the pop() method removes the last item.
"""
# Ex4. Remove the last item:
print("Ex4. Remove the last item:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
thislist.pop()
print("thislist (After) = " , thislist)
print("")

"""
The del keyword also removes the specified index:
"""
# Ex5. Remove the first item:
print("Ex5. Remove the first item:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
del thislist[0]
print("thislist (After) = " , thislist)
print("")

"""
The del keyword can also delete the list completely.
"""
# Ex6. Delete the entire list:
print("Ex6. Delete the entire list:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
del thislist
print("thislist (After) = null")
print("")

"""
Clear the List
The clear() method empties the list.
The list still remains, but it has no content.
"""
# Ex7. Clear the list content:
print("Ex7. Clear the list content:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
thislist.clear()
print("thislist (After) = " , thislist)
print("")