"""
List
1. Lists are used to store multiple items in a single variable.
2. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
3. Lists are created using square brackets:
"""
# Ex1. Create a List:
print("Ex1. Create a List:")
thislist = ["apple", "banana", "cherry"]
print("thislist = " , thislist)
print("")

"""
List Items
1. List items are {ordered}, {changeable}, and {allow duplicate} values.
2. List items are indexed, the first item has index [0], the second item has index [1] etc.


{Ordered}
1. When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
2. If you add new items to a list, the new items will be placed at the end of the list.
Note: There are some list methods that will change the order, but in general: the order of the items will not change.

{Changeable}
1. The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

{Allow Duplicates}
1. Since lists are indexed, lists can have items with the same value:
"""
# Ex2. Lists allow duplicate values:
print("Ex2. Lists allow duplicate values:")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("thislist = " , thislist)
print("")

"""
List Length
To determine how many items a list has, use the len() function:
"""
# Ex3. Print the number of items in the list:
print("Ex3. Print the number of items in the list:")
thislist = ["apple", "banana", "cherry"]
print("len(thislist) = " , len(thislist))
print("")

""""
List Items - Data Types
List items can be of any data type:
"""
# Ex4. String, int and boolean data types:
print("Ex4. String, int and boolean data types:")
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print("list1 = " , list1)
print("list2 = " , list2)
print("list3 = " , list3)
print("")

"""
A list can contain different data types:
"""
# Ex5. A list with strings, integers and boolean values:
print("Ex5. A list with strings, integers and boolean values:")
list1 = ["abc", 34, True, 40, "male"]
print("list1 = " , list1)
print("")

"""
type()
From Python's perspective, lists are defined as objects with the data type 'list':
<class 'list'>
"""
# Ex6. What is the data type of a list?
print("Ex6. What is the data type of a list?")
mylist = ["apple", "banana", "cherry"]
print("type(mylist) = " , type(mylist))
print("")

"""
The list() Constructor
It is also possible to use the list() constructor when creating a new list.
"""
# Ex7. Using the list() constructor to make a List:
print("Ex7. Using the list() constructor to make a List:")
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print("thislist = " , thislist)
print("")