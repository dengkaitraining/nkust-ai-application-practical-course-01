"""
Python - Add List Items
Append Items
To add an item to the end of the list, use the append() method:
"""
# Ex1. Using the append() method to append an item:
print("Ex1. Using the append() method to append an item:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
thislist.append("orange")
print("thislist (After - thislist.append(\"orange\")) = " , thislist)
print("")

"""
Insert Items
To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:
* Note: As a result of the examples above, the lists will now contain 4 items.
"""
# Ex2. Insert an item as the second position:
print("Ex2. Insert an item as the second position:")
thislist = ["apple", "banana", "cherry"]
print("thislist (Before) = " , thislist)
thislist.insert(1, "orange")
print("thislist (After - thislist.insert(1, \"orange\")) = " , thislist)
print("")

"""
Extend List
To append elements from another list to the current list, use the extend() method.
* The elements will be added to the end of the list.
"""
# Ex3. Add the elements of tropical to thislist:
print("Ex3. Add the elements of tropical to thislist:")
thislist = ["apple", "banana", "cherry"]
print(type(thislist) , " : thislist (Before) = " , thislist)
tropical = ["mango", "pineapple", "papaya"]
print(type(tropical) , "tropical (Before) = " , tropical)
thislist.extend(tropical)
print(type(thislist) , " : tthislist (After - thislist.extend(tropical)) = ", thislist)
print("")

"""
Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
"""
# Ex4. Add elements of a tuple to a list:
print("Ex4. Add elements of a tuple to a list:")
thislist = ["apple", "banana", "cherry"]
print(type(thislist) , " : thislist (Before) = " , thislist)
thistuple = ("kiwi", "orange")
print(type(thistuple) , " : thistuple (Before) = " , thistuple)
thislist.extend(thistuple)
print(type(thislist) , " : thislist (After - thislist.extend(thistuple)) = ", thislist)
print("")