class Person:
	def iq(self):
		iq = 75
		print(str(iq) + " PErson " )
		print(self.__dict__)

class Scientist(Person):
	def iq(self):
		iq = 150
		print(str(iq) + " S C I E N T I S T " )
		print(self.__dict__)


class Worker(Person):
	def iq(self):
		iq = 60
		print(str(iq) + " Worker ")
		print(self.__dict__)

p = Person()
w = Worker()
w.iq()