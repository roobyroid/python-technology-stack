#Задание 1
class Transport:
	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

class Autobus(Transport):
	def __init__(self, name, max_speed, mileage):
		super().__init__(name, max_speed, mileage)

autobus = Autobus("Renaul Logan", 180, 12)

print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")

#Задание 2
class Transport:
	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

	def seating_capacity(self, capacity):
		return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

class Autobus(Transport):
	def __init__(self, name, max_speed, mileage):
		super().__init__(name, max_speed, mileage)

	def seating_capacity(self, capacity=50):
		return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

# Создаем объект Autobus
autobus = Autobus("Renaul Logan", 180, 12)

# Выводим информацию об объекте Autobus с использованием переопределенного метода
print(autobus.seating_capacity())