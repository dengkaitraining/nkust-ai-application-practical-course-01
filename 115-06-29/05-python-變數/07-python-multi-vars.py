"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x, y, z = "Orange", "Banana", "Cherry";
x, y, z = "Orange", 2.33, 2;
print("vars x : ", end=""); print(type(x), end=" , value = "); print(x);
print("vars y : ", end=""); print(type(y), end=" , value = "); print(y);
print("vars z : ", end=""); print(type(z), end=" , value = "); print(z);

"""
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
"""
x = y = z = "Orange";
print("vars x : ", end=""); print(type(x), end=" , value = "); print(x);
print("vars y : ", end=""); print(type(y), end=" , value = "); print(y);
print("vars z : ", end=""); print(type(z), end=" , value = "); print(z);

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print("vars x : ", end=""); print(type(x), end=" , value = "); print(x);
print("vars y : ", end=""); print(type(y), end=" , value = ");print(y);
print("vars z : ", end=""); print(type(z), end=" , value = "); print(z);