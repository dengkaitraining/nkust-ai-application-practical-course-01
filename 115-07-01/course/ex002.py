def monkey(a, b, c):
    d = a + b + c
    print("inside " + str(d))
    return d

cat=monkey(1, 2, 3)
print(cat)

dog1=100
dog2=200
dog3=300

dog=monkey(dog1, dog2, dog3)
print(dog)
