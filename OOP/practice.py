class Animal:
	def __init__(self, color):
		self.__color = color

	def eat(self):
		print("Eating")

	def get_color(self):
		return self.__color
class Dog(Animal):
	def __init__(self, ):
		__owner = "John Doe"

	def bark(self):
		print("Woof")

