"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)
5. A variable name cannot be any of the Python keywords.
"""
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print("myvar = ", end=""); print(type(myvar), end=" , "); print("myvar = ", end=""); print(myvar);
print("my_var = ", end=""); print(type(my_var), end=" , "); print("my_var = ", end=""); print(my_var);
print("_my_var = ", end=""); print(type(_my_var), end=" , "); print("_my_var = ", end=""); print(_my_var);
print("myVar = ", end=""); print(type(myVar), end=" , "); print("myVar = ", end=""); print(myVar);
print("MYVAR = ", end=""); print(type(MYVAR), end=" , "); print("MYVAR = ", end=""); print(MYVAR);
print("myvar2 = ", end=""); print(type(myvar2), end=" , "); print("myvar2 = ", end=""); print(myvar2);

# Illegal variable names:
#2myvar = "John"
#my-var = "John"
#my var = "John"