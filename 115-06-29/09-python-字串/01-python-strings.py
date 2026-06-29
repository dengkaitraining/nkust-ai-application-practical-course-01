"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""
# Ex1.
print("Ex1.")
print("Hello")
print('Hello')
print("")

"""
Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
"""
# Ex2.
print("Ex2.")
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("")

"""
Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
"""
# Ex3.
print("Ex3.")
a = "Hello"
print(a)
print("")

"""
Multiline Strings
You can assign a multiline string to a variable by using three quotes:
"""
# Ex4-1. You can use three double quotes:
print("Ex4-1. You can use three double quotes:")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("")

# Ex4-2. Or three single quotes:
print("Ex4-2. Or three single quotes:")
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("")

"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""
# Ex5. Get the character at position 1 (remember that the first character has the position 0):
print("Ex5. Get the character at position 1 (remember that the first character has the position 0):")
a = "Hello, World!"
print(a[1])
print("")

"""
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""
# Ex6. Loop through the letters in the word "banana":
print("Ex6. Loop through the letters in the word 'banana':")
for x in "banana":
  print(x)
print("")

"""
String Length
To get the length of a string, use the len() function.
"""
# Ex7. The len() function returns the length of a string:
print("Ex7. The len() function returns the length of a string:")
a = "Hello, World!"
print(len(a))
#print(a[12])
print("")

"""
Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.
"""
# Ex8. Check if "free" is present in the following text:
print("Ex8. Check if 'free' is present in the following text:")
txt = "The best things in life are free!"
print("free" in txt)
print("")

# Ex9. Print only if "free" is present:
print("Ex9. Print only if 'free' is present:")
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
if "l" in txt and "e" in txt:
  print("Yes, both 'l' and 'e' are present.")
print("")

"""
Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
"""
# Ex10. Check if "expensive" is NOT present in the following text:
print("Ex10. Check if 'expensive' is NOT present in the following text:")
txt = "The best things in life are free!"
print("expensive" not in txt)
print("")

# Ex11. print only if "expensive" is NOT present:
print("Ex11. print only if 'expensive' is NOT present:")
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
print("")