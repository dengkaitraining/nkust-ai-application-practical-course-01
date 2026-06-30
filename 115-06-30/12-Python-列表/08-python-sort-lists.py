"""
Python - Sort Lists
Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
"""
# Ex1. Sort the list alphabetically:
print("Ex1. Sort the list alphabetically")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("thislist (Before - Sort) " , thislist)
thislist.sort()
print("thislist (After - Sort) " , thislist)
print("")

# Ex2. Sort the list numerically:
print("Ex2. Sort the list numerically:")
thislist = [100, 50, 65, 82, 23]
print("thislist (Before - Sort) " , thislist)
thislist.sort()
print("thislist (After - Sort) " , thislist)
print("")

"""
Sort Descending
To sort descending, use the keyword argument reverse = True:
"""
# Ex3. Sort the list descending:
print("Ex3. Sort the list descending:")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("thislist (Before - Sort) " , thislist)
thislist.sort(reverse = True)
print("thislist (After - Sort) " , thislist)
print("")

# Ex4.Sort the list descending:
print("Ex4. Sort the list descending:")
thislist = [100, 50, 65, 82, 23]
print("thislist (Before - Sort) " , thislist)
thislist.sort(reverse = True)
print("thislist (After - Sort) " , thislist)
print("")

"""
Customize Sort Function
 - You can also customize your own function by using the keyword argument key = function.
 - The function will return a number that will be used to sort the list (the lowest number first):
"""
# Ex5. Sort the list based on how close the number is to 50:
print("Ex5. Sort the list based on how close the number is to 50:")
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
print("thislist (Before - myfunc Sort) " , thislist)
thislist.sort(key = myfunc)
print("thislist (After - myfunc Sort) " , thislist)
print("")

"""
Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
"""
# Ex6. Case sensitive sorting can give an unexpected result:
print("Ex6. Case sensitive sorting can give an unexpected result:")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print("thislist (Before - Case sensitive sorting) " , thislist)
thislist.sort()
print("thislist (After - Case sensitive sorting) " , thislist)
print("")

# Ex7. Perform a case-insensitive sort of the list:
print("Ex7. Perform a case-insensitive sort of the list:")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print("thislist (Before - Case sensitive sorting) " , thislist)
thislist.sort(key = str.lower)
print("thislist (After - Case sensitive sorting) " , thislist)
print("")

"""
Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.
"""
# Ex8. Reverse the order of the list items:
print("Ex8. Reverse the order of the list items:")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print("thislist (Before - Sort) " , thislist)
thislist.reverse()
print("thislist (After - Sort) " , thislist)
print("")
