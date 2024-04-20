#Задание 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_list(n):
    fact_n = factorial(n)

    factorial_list = []
    for i in range(n, 0, -1):
        factorial_list.append(fact_n)
        fact_n //= i

    return factorial_list


user_input = int(input("Введите натуральное число: "))

result_list = factorial_list(user_input)

print(f"Список факториалов: {result_list}")
