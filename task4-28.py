import math

while bool:
    x = int(input('Введите координату на оси OX: '))
    y = int(input('Введите координату на оси OY: '))


    def area_circle(r: float):
        return math.pi * math.pow(r, 2)


    def vector_length(x0: int, y0: int):
        return math.sqrt(math.pow(x0, 2) + math.pow(y0, 2))


    min_circle = area_circle(2)
    max_circle = area_circle(4)

    vector = vector_length(x, y)
    circle = area_circle(vector)

    if x > 0 and min_circle <= circle <= max_circle:
        print("Точка (" + x.__str__() + ", " + y.__str__() + ") принадлежит заданной плоскости.")
    else:
        print("Точка (" + x.__str__() + ", " + y.__str__() + ") не принадлежит заданной плоскости.")
