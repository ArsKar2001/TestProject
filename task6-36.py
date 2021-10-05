print("36. Вычислить сумму.")

n = int(input("Введите n: "))
res = 0
for i in range(1, n + 1):
    res += (i ** 2) / (i ** -2 + 2 * i + 3)
    print("sum =", res)
