# Задание 1
number = int(input("Введите целое число: "))

if number == 0:
    print("Нулевое число")
elif number % 2 == 0:  # число четное
  if number > 0:
    print("Положительное четное число")
  else:
    print("Отрицательное четное число")
else:  # число нечетное
  if number > 0:
    print("Положительное нечетное число")
  else:
    print("Число не является четным")

# Задание 2
word = input("Введите слово из маленьких латинских букв: ")

vowel_a = "a" in word
vowel_e = "e" in word
vowel_i = "i" in word
vowel_o = "o" in word
vowel_u = "u" in word

if vowel_a and vowel_e and vowel_i and vowel_o and vowel_u:
  print("Количество гласных букв в слове:", word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u"))
else:
  print(False)

# Задание 3

X = float(input("Введите минимальную сумму инвестиций X: "))
A = float(input("Введите сумму инвестиций Майкла A: "))
B = float(input("Введите сумму инвестиций Ивана B: "))

if A >= X and B >= X:
  print(2)
elif A >=X:
  print('Mike')
elif B >= X:
  print('Ivan')
elif (A + B) >= X:
	print(1)
else:
	print(0)