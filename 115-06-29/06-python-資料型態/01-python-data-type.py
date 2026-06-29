"""
Built-in Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text Type:      str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:  	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
"""

"""
Getting the Data Type
You can get the data type of any object by using the type() function:
"""
# Print the data type of the variable x:
x = 5;
#print(type(x))
print("ex. Print the data type of the variable x: " + str(type(x)) + " value: " + str(x));

"""
Setting the Data Type
In Python, the data type is set when you assign a value to a variable:

Example	                                        Data Type	Try it
x = "Hello World"	                            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                    bool	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview	
x = None	                                    NoneType	
"""

"""
Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:

Example	                                        Data Type	Try it
x = str("Hello World")	                        str	
x = int(20)	                                    int	
x = float(20.5)	                                float	
x = complex(1j)	                                complex	
x = list(("apple", "banana", "cherry"))	        list	
x = tuple(("apple", "banana", "cherry"))	    tuple	
x = range(6)	                                range	
x = dict(name="John", age=36)	                dict	
x = set(("apple", "banana", "cherry"))	        set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	                                    bool	
x = bytes(5)	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview	
"""

# ex. string data type
x = str("Hello World");
# display x value and data type
print("ex. string data type: " + str(type(x)) + " value: " + x);

# ex. integer data type
x = int(20);
# display x value and data type
print("ex. integer data type: " + str(type(x)) + " value: " + str(x));

# ex. float data type
x = float(20.5);
# display x value and data type
print("ex. float data type: " + str(type(x)) + " value: " + str(x));

# ex. complex data type
#x = complex(1j);
x = complex(20);
# display x value and data type
print("ex. complex data type: " + str(type(x)) + " value: " + str(x));

# ex. list data type
x = ["apple", "banana", "cherry"]
# display x value and data type
print("ex. list data type: " + str(type(x)) + " value: " + str(x));

# ex. tuple data type
x = ("apple", "banana", "cherry")
# display x value and data type
print("ex. tuple data type: " + str(type(x)) + " value: "+ str(x));

# ex. range data type
x = range(6)
# display x value and data type
print("ex. range data type: " + str(type(x)) + " value: "+ str(x));

# ex. dictionary data type
x = {"name" : "John", "age" : 36}
# display x value and data type
print("ex. dictionary data type: " + str(type(x)) + " value: "+ str(x));

# ex. set data type
x = {"apple", "banana", "cherry"}
# display x value and data type
print("ex. set data type: " + str(type(x)) + " value: "+ str(x));

# ex. frozenset data type
x = frozenset({"apple", "banana", "cherry"})
# display x value and data type
print("ex. frozenset data type: " + str(type(x)) + " value: "+ str(x));

# ex. boolean data type
#x = True; x = bool(5); x = bool(0)
x = bool(0.000000001);
# display x value and data type
print("ex. boolean data type: " + str(type(x)) + " value: "+ str(x));

# ex. bytes data type
x = b"Hello"
# display x value and data type
print("ex. bytes data type: " + str(type(x)) + " value: "+ str(x));

# ex. bytearray data type
x = bytearray(5)
# display x value and data type
print("ex. bytearray data type: " + str(type(x)) + " value: "+ str(x));

# ex. memoryview data type
x = memoryview(bytes(5))
# display x value and data type
print("ex. memoryview data type: " + str(type(x)) + " value: "+ str(x));

# ex. None data type
x = None
# display x value and data type
print("ex. None data type: " + str(type(x)) + " value: "+ str(x));
