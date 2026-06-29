"""
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""
# ex1. Create a variable outside of a function, and use it inside the function
x = "awesome";
def myfunc():
  print("ex1. Python is " + x);
myfunc();

# ex2. Create a variable inside a function, with the same name as the global variable
x = "awesome";

def myfunc():
  x = "fantastic";
  print("ex2-1. Python is " + x);

myfunc();

print("ex2-2. Python is " + x);

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""
# ex3. If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("ex3. Python is " + x)

# ex4. To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("ex4. Python is " + x)