#Задание 1
input_string = input("Введите строку без пробелов: ")

if input_string == input_string[::-1]:
	print("yes")
else:
	print("no")

# Задание 2
input_string = input("Введите строку: ")

output_string = ' '.join(input_string.split())

print("Измененная строка:")
print(output_string)
