"""
scope
"""
x = 300

def myfunc():
    y = 1000
    print("inside x =", x)
    print("inside y =", y)

myfunc()

print("x = ", x)
#print("y = ", y) # 因為 y 定義於 myfunc 內，所以照不到該數值。