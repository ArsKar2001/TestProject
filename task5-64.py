import math

print("64. Вычислить бесконечную сумму с заданной точностью.")

e = float(input("Введите точность E (E>0 и Е<1): "))

i = 0
res = 1

while abs(res) > e:
    f = math.factorial(i)
    res = ((-1) ** i) / f
    i += 1
    print("a", i, " = ", res, sep='')
