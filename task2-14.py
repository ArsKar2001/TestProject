import math
print("Введите катет А: ")
a = int(input())
print("Введите катет B: ")
b = int(input())
c = math.hypot(a, b)
c1 = a ** 2 + b ** 2
c1 = c1 ** 0.5
print("Гипотенуза треугольника ABC: " + c.__str__())
print("Гипотенуза треугольника ABC: " + c1.__str__())
