#Задание 1
def recursive_print_list(my_list, index):
    if index < len(my_list):
        print(my_list[index])
        recursive_print_list(my_list, index + 1)
    else:
        print("Конец списка")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
recursive_print_list(my_list, 0)
