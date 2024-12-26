# class Car:
# 	# color: str = ''
# 	# engine: str = ''
# 	# year: int = 0
#
# 	def __init__(self, color, engine, year):
# 		self.colour = color
# 		self.engine = engine
# 		self.year = year
#
#
# 	def yuradi(self):
# 		return f"Yurdi "
#
# 	def buzildi(self):
# 		print("buzildi")
#
#
# BMW = Car("black", "Mercedes", 1999)
#
#
#
# print(BMW)
# BMW.buzildi()


# Car.buzildi()
# avtomobil = Car()
# avtomobil.color = 'blue'
# avtomobil.engine = 'Metan'
# avtomobil.year = 2020
# # avtomobil.color = 'red'

# avtomobil = Car('black', 'engine', 1999)

# print(avtomobil.colour)

# print(avtomobil)

"""  1 misol  """

# class Calculator:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
#
# 	def sum(self):
# 		return self.a + self.b
# 	def ayirish(self):
# 		return self.a - self.b
# 	def kupaytirish(self):
# 		return self.a * self.b
# 	def bolish(self):
# 		return self.a / self.b
#
# Misol = Calculator(10, 5)
#
# print(Misol.sum())
#
""" 2 misol  """

#
# class PasswordValidator:
#
# 	def __init__(self, password):
# 		self.password = password
#
# 	def check_length(self):
# 		return self.password.__len__()
#
# 	def check_uppercase(self):
# 		return self.password.isupper()
#
# 	def check_not_space(self):
# 		return len(self.password.split()) == 1
#
# 	def check_lowercase(self):
# 		return self.password.islower()
#
# 	def check_digits(self):
# 		return self.password.isdigit()
#
# 	def check_symbols(self):
# 		return not self.password.isalnum()
#
# 	def validate(self):
# 		return self.check_length() >= 6 and self.check_not_space() and self.check_symbols() and not self.check_digits() and not self.check_lowercase() and not self.check_uppercase()
#
#
# password = PasswordValidator(password='Hellowor23@#12ld')
# print(password.validate())

""" 3 misol """

# class EmployeeSalary:
# 	def __init__(self, name, worked_hours, hourly_wage):
# 		self.name = name
# 		self.worked_hours = worked_hours
# 		self.hourly_wage = hourly_wage
#
# 	def calculate_salary(self):
# 		return self.worked_hours * self.hourly_wage
#
#
#
# employee = EmployeeSalary('Murat', 10, 100)
# print(str(employee.calculate_salary()) + " $")


""" 4 misol """
# from forex_python.converter import CurrencyRates
#
# c = CurrencyRates()
#
#
# class ChangeCurrency:
# 	def __init__(self, amount, currency):
# 		self.amount = amount
# 		self.currency = currency
#
# 	def convert_from_usd(self):
# 		rate = c.get_rate('USD', self.currency)
# 		return self.amount * rate
#
# cur = ChangeCurrency(100, 'EUR')
# print(cur.convert_from_usd())

""" 5 misol """

# class Students:
# 	teachers = []
#
# 	def __init__(self,student, teacher):
# 		self.student = student
# 		self.teacher = teacher
#
# 	def add_student(self):
# 		self.teachers.append({self.teacher: [self.student]})
# 		return
# 	def remove_student(self):
# 		self.teachers.pop()

