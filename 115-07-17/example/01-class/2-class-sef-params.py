# [The self Parameter]
# example 1 - Use self to access class properties:
class Person_1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("example 1 - Use self to access class properties:")
        print("Hello, my name is " + self.name +"\n")

# [self Does Not Have to Be Named "self"]
# example 2 - Use the words myobject and abc instead of self:
class Person_2:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def greet(abc):
        print("example 2 - Use the words myobject and abc instead of self:")
        print("Hello, my name is " + abc.name + "\n")

# [Accessing Properties with self]
# example 3 - Access multiple properties using self:
class Person_3:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("example 3 - Access multiple properties using self:")
        print(f"{self.year} {self.brand} {self.model}\n")

# [Calling Methods with self]
# example 4 - Call one method from another method using self:
class Person_4:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print("example 4 - Call one method from another method using self:")
        print(message + "! Welcome to our website.\n")

if __name__ == "__main__":
    # example 1 - Use self to access class properties:
    p1 = Person_1("Emil", 25)
    p1.greet()

    # example 2 - Use the words myobject and abc instead of self:
    p2 = Person_2("Emil", 36)
    p2.greet()

    # example 3 - Access multiple properties using self:
    p3 = Person_3("Toyota", "Corolla", 2020)
    p3.display_info()

    # example 4 - Call one method from another method using self:
    p4 = Person_4("Tobias")
    p4.welcome()
 