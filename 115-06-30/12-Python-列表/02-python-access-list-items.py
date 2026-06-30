"""
Python - Access List Items
Access Items
List items are indexed and you can access them by referring to the index number:
"""
# Ex1. Print the second item of the list:
print("Ex1. Print the second item of the list:")
thislist = ["apple", "banana", "cherry"]
print("thislist[1] = " , thislist[1])
print("")

"""
Negative Indexing
1. Negative indexing means start from the end
2. -1 refers to the last item, -2 refers to the second last item etc.
"""
# Ex2. Print the last item of the list:
print("Ex2. Print the last item of the list:")
thislist = ["apple", "banana", "cherry"]
print("thislist[-1] = " , thislist[-1])
print("")

"""
Range of Indexes
1. You can specify a range of indexes by specifying where to start and where to end the range.
2. When specifying a range, the return value will be a new list with the specified items.

* Note: The search will start at index 2 (included) and end at index 5 (not included).
* Remember that the first item has index 0.
"""
# Ex3. Return the third, fourth, and fifth item:
print("Ex3. Return the third, fourth, and fifth item:")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("thislist[2:5] = " , thislist[2:5])
print("")

# By leaving out the start value, the range will start at the first item:
# Ex4. This example returns the items from the beginning to, but NOT including, "kiwi":
print("Ex4. This example returns the items from the beginning to, but NOT including, \"kiwi\":")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("thislist[:4] = " , thislist[:4])
print("")

# By leaving out the end value, the range will go on to the end of the list:
# Ex5. This example returns the items from "cherry" to the end:
print("Ex5. This example returns the items from \"cherry\" to the end:")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("thislist[2:] = " , thislist[2:])
print("")

"""
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:
"""
# Ex6. This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
print("Ex6. This example returns the items from \"orange\" (-4) to, but NOT including \"mango\" (-1):")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("thislist[-4:-1] = " , thislist[-4:-1])
print("")

"""
Check if Item Exists
To determine if a specified item is present in a list use the in keyword:
"""
# Ex7. Check if "apple" is present in the list:
print("Ex7. Check if \"apple\" is present in the list:")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print("")