# [Create a Parent Class]
# example 1 - Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    message = ""
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.message)
        print(self.firstname, self.lastname, "\n")

# [Create a Child Class]
# example 2 - Create a class named Student_1, which will inherit the properties and methods from the Person class:
class Student_1(Person):
    pass

# [Add the __init__() Function]
# example 3 - Add the __init__() function to the Student class:
#             When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#             Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
class Student_2(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

# example 4 - To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
#             Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
class Student_3(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

if __name__ == "__main__":
    # example 1 - Create a class named Person, with firstname and lastname properties, and a printname method:
    p1 = Person("John", "Doe")
    p1.message = "example 1 - Create a class named Person, with firstname and lastname properties, and a printname method:"
    p1.printname()

    # example 2 - Create a class named Student_1, which will inherit the properties and methods from the Person class:
    s1 = Student_1("Mike-2", "Olsen-2")
    s1.message = "example 2 - Create a class named Student_1, which will inherit the properties and methods from the Person class:"
    s1.printname()

    # example 3 - Add the __init__() function to the Student class:
    s2 = Student_2("Mike-3", "Olsen-3")
    s2.message = "example 3 - Add the __init__() function to the Student class:"
    s2.printname()

    # example 4 - To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    s3 = Student_3("Mike-4", "Olsen-4")
    s3.message = "example 4 - To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:"
    s3.printname()
