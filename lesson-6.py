# Задание 1
N = int(input("Введите целое число: "))
cnt = 0

for i in range(N):
  number = int(input("Введите целое число: "))
  if number == 0:
    cnt += 1

print("Количество чисел равных нулю:", cnt)


# Задание 2
X = int(input("Введите целое число: "))
cnt = 0

for i in range(1, X + 1):
  if X % i == 0:
    cnt += 1

print("Количество делителей числа X:", cnt)

# Задание 3
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B (B >= A): "))

print("Четные числа на отрезке от", A, "до", B, "включительно:")

for i in range(A, B + 1):
  if i % 2 == 0:
    print(i, end=" ")