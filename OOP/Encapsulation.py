class NewCard:
	def __init__(self, balance, card_number):
		self.__pin_code = 4321
		self.__balance = balance
		self.card_number = card_number

	def set_pin_code(self, new_pincode:str):
		if len(new_pincode) == 4 and new_pincode.isdigit():
			self.__pin_code = new_pincode
		else:
			print("Wrong pin code!")
	def get_pin_code(self):
		return self.__pin_code


card1 = NewCard(balance=0.0, card_number="1234567856786789", )
card1.set_pin_code("1234")
print(card1.get_pin_code())


