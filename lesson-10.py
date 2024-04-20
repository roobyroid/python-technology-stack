#Задание 1
pets = {}

# Запрашиваем у пользователя данные о питомце
pet_name = input("Введите имя питомца: ")
pet_species = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# Заполняем словарь с информацией о питомце
pets[pet_name] = {
    'Вид питомца': pet_species,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

# Форматируем возраст питомца
if pet_age % 10 == 1 and pet_age != 11:
    age_str = "год"
elif pet_age % 10 in [2, 3, 4] and pet_age not in [12, 13, 14]:
    age_str = "года"
else:
    age_str = "лет"

# Выводим информацию о питомце
info_str = f"Это {pet_species.lower()} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {age_str}. Имя владельца: {owner_name}"
print(info_str)

#Задание 2
my_dict = {}

for i in range(10, -6, -1):
    my_dict[i] = i ** i

print(my_dict)
