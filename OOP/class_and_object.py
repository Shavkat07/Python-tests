
class Car:
	# color: str = ''
	# engine: str = ''
	# year: int = 0

	def __init__(self, color, engine, year):
		self.colour = color
		self.engine = engine
		self.year = year


	def yuradi(self):
		return f"Yurdi "

	def buzildi(self):
		print("buzildi")


BMW = Car("black", "Mercedes", 1999)



print(BMW)
BMW.buzildi()



# Car.buzildi()
# avtomobil = Car()
# avtomobil.color = 'blue'
# avtomobil.engine = 'Metan'
# avtomobil.year = 2020
# # avtomobil.color = 'red'

# avtomobil = Car('black', 'engine', 1999)

# print(avtomobil.colour)

# print(avtomobil)
