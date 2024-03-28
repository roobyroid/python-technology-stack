# # Задание 1
side1 = float(input("Введите длину первой стороны прямоугольника: "))
side2 = float(input("Введите длину второй стороны прямоугольника: "))

area = side1 * side2
perimeter = 2 * (side1 + side2)

print("Площадь прямоугольника: ", area)
print("Периметр прямоугольника: ", perimeter)

# Задание 2
number = int(input("Введите пятизначное число: "))

units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

result = ((tens ** units) * hundreds) / (ten_thousands - thousands)

print(result)
