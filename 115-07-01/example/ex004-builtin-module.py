import math # 載入「數學」模組

# 2026-07-01 bulit-in 函式
x = pow(1.5, 1.5)
print("pow(1.5, 1.5) x =", x)

x = round(1.5)
print("round(1.5) x =", x)

# 多數數學計算不在 built-in function , 必須載入 math module 才能使用
# 2026-07-01 import math module
y = math.sqrt(100)
print("math.sqrt(100) y =", y)

y = math.ceil(1.4)
print("math.ceil(1.4) y =", y)

y = math.floor(1.4)
print("math.floor(1.4) y =", y)