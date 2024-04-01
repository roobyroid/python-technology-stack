#Задание 1
N = int(input("Введите число N: "))
numbers = []

for i in range(N):
	number = int(input())
	numbers.append(number)

uc = set(numbers)
print(len(uc))

#Задание 2
n_list1 = int(input("Введите количество чисел для первого списка: "))
list1 = []

for i in range(n_list1):
	number = int(input())
	list1.append(number)

uc1 = set(list1)

n_list2 = int(input("Введите количество чисел для второго списка: "))
list2 = []

for i in range(n_list2):
	number = int(input())
	list2.append(number)

uc2 = set(list2)

print(len(uc1.intersection(uc2)))

#Задание 3
numbers = list(map(int, input().split()))
uc = set()
for i in numbers:
	if i not in uc:
		uc.add(i)
		print('NO')
	else:
		print('YES')