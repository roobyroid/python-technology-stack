#Задание 1
N = int(input("Введите число N: "))

numbers = []
if 1 <= N <= 10000:
	for _ in range(N):
		number = int(input())
		numbers.append(number)

	reversed_numbers = numbers[::-1]

	print(f"{N} чисел - {reversed_numbers}")

#Задание 2
N = int(input("Введите число N: "))

if 1 <= N <= 100000:
	numbers = list(map(int, input().split()))
	numbers.insert(0, numbers.pop())
	print(f"{N} чисел - {numbers}")


#Задание 3
max_weight = int(input("Введите максимальный вес который может выдержать одна лодка: "))
count_fishermen = int(input("Введите количество рыбаков: "))

weights = []

for _ in range(count_fishermen):
	number = int(input("Введите вес рыбака: "))
	weights.append(number)

weights.sort()

boats = 0
left = 0
right = len(weights) - 1

while left <= right:
	if(weights[left] + weights[right] <= max_weight):
		left += 1
	right -= 1
	boats += 1

print(boats)

