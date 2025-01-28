# class Animal:
# 	def __init__(self, color):
# 		self.__color = color
# #
# # 	def eat(self):
# # 		print("Eating")
# #
# # 	def get_color(self):
# # 		return self.__color
# #
# # class Dog(Animal):
# # 	def __init__(self, ):
# # 		__owner = "John Doe"
# #
# # 	def bark(self):
# # 		print("Woof")
# #
#
# print("""
# === Asosiy Menu ===
# 1. Admin yoki Xodim sifatida kirish
# 2. Oddiy Foydalanuvchi
# 0. Chiqish
# """)
# choice = input("Menu ni tanlang: ")
#
#
#
# print("\n=== Admin/Xodim Menusi ===")
# login = input("Loginni kiriting: ")
# parol = input("Parolni kiriting: ")
#
#
# print("\n=== Foydalanuvchi Menusi ===")
# print("Lokatsiyani kiritish (viloyat): ")
#
#
# # choice = input("Tanlovingizni kiriting: ")
# # if choice == "1":
# #     print("Avtomobil raqamlari ro'yxati...")
# # elif choice == "2":
# #     shahar = input("Shahar nomini kiriting: ")
# #     print(f"Sizning lokatsiyangiz: {shahar}")
#
#
#
# print("\n=== Asosiy Menu ===")
# print("1. Mijozlarni Boshqarish")
# print("2. Avto Raqamlarni Boshqarish")
# print("3. Sotuvlarni Boshqarish")
# print("0. Chiqish")
# choice = input("Menu ni tanlang: ")
#
#
# print("\n=== Foydalanuvchilar Menusi ===")
# print("1. Foydalanuvchi qo'shish")
# print("2. Foydalanuvchi ma'lumotlarini ko'rish")
# print("3. Foydalanuvchi ma'lumotlarini o'zgartirish")
# print("4. Foydalanuvchini o'chirish")
# print("5. Foydalanuvchilar ro'yxati")
# print("0. Orqaga")
# choice = input("Tanlovingizni kiriting: ")
#
# print("\n=== Avto Raqamlar Menusi ===")
# print("1. Avto raqam qo'shish")
# print("4. Avto raqamlar ro'yxati")
# print("3. Avto raqamni o'chirish")
# print("3. Avto raqamni ID orqali ko'rish")
# print("0. Orqaga")
# choice = input("Tanlovingizni kiriting: ")
#
# print("\n=== Sotuvlar Menusi ===")
# print("1. Sotuv qo'shish")
# print("2. Sotuvlar ro'yxati")
# print("3. Foydalanuvchi ID orqali sotuvni ko'rish")
# print("4. Sotuvni ID orqali ko'rish")
# print("5. Sotuvni o'chirish")
# print("0. Orqaga")
# choice = input("Tanlovingizni kiriting: ")


""" 3 misol  """
# class Employee:
# 	def __init__(self, name, salary_per_hour):
# 		self.name = name
# 		self.salary_per_hour = salary_per_hour
#
#
# 	def salary(self, worked_hours):
# 		return  worked_hours * self.salary_per_hour
#
#
# class Manager(Employee):
#
# 	def salary(self, worked_hours, something):
# 		return worked_hours * self.salary_per_hour + 8 + something
#
#
# class Engineer(Employee):
#
# 	def salary(self, worked_hours):
# 		return worked_hours * self.salary_per_hour + 12
#
# class Internship(Employee):
# 	def salary(self, worked_hours):
# 		return worked_hours * 0
#
#
# engineer = Engineer("John Doe", 12)
#
# manager = Manager("Ilon Mask", 20)
#
# Internship = Internship("Bobur", 100)
#
# print("Manager salary is" , manager.salary(100, 15),  "$")

# from abc import ABC, abstractmethod
























