# example 1 - Create a class without __init__():
class Person_1:
    def __init__(self):
        pass

# example 2 - With __init__(), you can set initial values when creating the object:
class Person_2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    # example 1 - Create a class without __init__():
    p1 = Person_1()
    p1.name = "Tobias"
    p1.age = 25
    print("-" * 50)
    print("Create a class without __init__():")
    print("-" * 50)
    print(p1.name)
    print(p1.age)
    print("-" * 50)
    print("\n")
    
    # example 2 - With __init__(), you can set initial values when creating the object:
    p2 = Person_2("Linus", 28)
    print("-" * 50)
    print("example 2 - With __init__(), you can set initial values when creating the object:")
    print("-" * 50)
    print(p2.name)
    print(p2.age)
    print("-" * 50)
    print("\n")