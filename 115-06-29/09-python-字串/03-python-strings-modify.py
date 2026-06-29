"""
Python - Modify Strings
Python has a set of built-in methods that you can use on strings.
"""
# Upper Case    
# Ex1. The upper() method returns the string in upper case:
print("Ex1. The upper() method returns the string in upper case:")
a = "Hello, World!"
print("Use the a.upper() method: " + a.upper())
print("Use the str.upper(a) function: " + str.upper(a))
print("")

# Lower Case
# Ex2. The lower() method returns the string in lower case:
print("Ex2. The lower() method returns the string in lower case:")
a = "Hello, World!"
print("Use the a.lower() method: " + a.lower())
print("Use the str.lower(a) function: " + str.lower(a))
print("")

"""
Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
"""
# Ex3. The strip() method removes any whitespace from the beginning or the end:
print("Ex3. The strip() method removes any whitespace from the beginning or the end:")
a = " Hello, World! "
print("Use the a.strip() method: " + a.strip())
print("Use the str.strip(a) function: " + str.strip(a))
print("")

# Replace String
# Ex4. The replace() method replaces a string with another string:
print("Ex4. The replace() method replaces a string with another string:")
a = "Hello, World!"
print("Use the a.replace('H', 'J') method: " + a.replace("H", "J"))
print("Use the str.replace(a, 'H', 'J') function: " + str.replace(a, "H", "J"))
print("")

"""
Split String
The split() method returns a list where the text between the specified separator becomes the list items.
"""
# Ex5. The split() method splits the string into substrings if it finds instances of the separator:
print("Ex5. The split() method splits the string into substrings if it finds instances of the separator:")
a = "Hello, World!"
print("Use the a.split(',') method: " + str(a.split(",")) + " array = { " + str(a.split(",")[0]) + ", " + str(a.split(",")[1]) + " }")
print("Use the str.split(a, ',') function: " + str(str.split(a, ",")) + " array = { " + str(str.split(a, ",")[0]) + ", " + str(str.split(a, ",")[1]) + " }")
print("Use the a.split('o') method: " + str(a.split("o")) + " array = { " + str(a.split("o")[0]) + ", " + str(a.split("o")[1]) + ", " + str(a.split("o")[2]) + " }")
print("Use the str.split(a, 'o') function: " + str(str.split(a, "o")) + " array = { " + str(str.split(a, "o")[0]) + ", " + str(str.split(a, "o")[1]) + ", " + str(str.split(a, "o")[2]) + " }")
print("")

