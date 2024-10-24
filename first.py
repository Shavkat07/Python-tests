# """Function Separate"""
# print("Hello", "world", sep=" , ")
#
# """ end """
# print('first row', end=" ")
# print('second row')
#
# """ input """
#
# name = input('enter somthing: ')
# print(name)
#
#
# name = "Elsa"
# a = name
#
# print(a)
#
# x = 3
# y = 2
#
# x, y = y, x
#
# print(x, y)

# v = "1.0"
#
# print(type(v))

# x = 11
# y = 5
# z = x + y
#
# print(x % y)

# big_number = 10 ** 1000
# print(big_number)

# my_float = 1.5
# my_int = round(my_float)
# print(my_int)

# a = map(int, input().split())
# print(sum(a))
"""
kv_number = 25

dom_number = (kv_number-1) // 20 + 1

etaj_num = (kv_number-1) % 20  // 4 + 1

print(dom_number,  "inchi dom")
print(etaj_num, "inchi etaj")

"""
# from django.template.defaultfilters import length

# is_student = True
# is_gradueted = False
# a = 3
# b = 3
# print(a != b)
# print(False or False or False)

# var = "20_2.33_4"
# var1 = float(var)
# print(var1)

# print(bool(" "))

# x = True
# y = False
# z = False
#
# if not x and not y or z:
#     print(True)
#
# else:
#     print(False)

# scores = [80, 85, 90]
# a = zip(scores)
# print(
#     list(a)
# )

# num = 0.25
# numerator, denominator = num.as_integer_ratio()
#
# print(num.as_integer_ratio())
# print(numerator, end=" ")
# print(denominator)
""" to find leap year (kabisa yili) 
year = 2004
if not year % 4 and not year % 100:
    print("year  is leap")
elif not year % 400:
    print("Year is leap ")
else:
    print("Year is not leap")
"""

# name = "Alice "
# print(length(" "))

# my_int = 100
# my_string = str(my_int)
# print(int(my_string) + int("4544"))

# big_integer = 2 ** 1000
# print(length(f"{big_integer}"))
# print(len(str(big_integer)))

# string = "     Hello "
# print(string.strip())


# a = 121
# if  a % 11 == 0 : print("true")
# else : print("false")
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         a = str(x)[-1:-x:-1]
#         if a == str(x):
#             return True
#         else:
#             return False
#
# print(Solution().isPalindrome(-121))

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
#         return


# a = map(int, input().split())
# b = sorted(a)
# print(sum(b[0:4]), sum(b[1:5]))

# a = 'Men PDP talabasiman'
# b = 'Hello world'
# print(len(a + b))

# a = ['apple', 'banana', 'cherry']
# print(len(a))
#
# a, b = map(int, input('sonlarni kiriting: ').split())
# c = input('Operatorni belgilang: ')
# if c == "+":
#     print(f'Yigindi: {a + b}')
# elif c == '-':
#     print(f'Ayirma: {a - b}')
# elif c == '/':
#     print(f'Bolish: {a / b}')
# elif c == '*':
#     print(f'Kopaytirish: {a * b}')
# else:
#     print('Operator xato belgilandi?')
#


""" 5 - masala """

# a = input()
#
# print(len(a) * 10 * " " + a)
#
# for i in range(1, 10):
#     print(((10 - i) * len(a)) * ' ' + (2 * i * a + a))

""" 6 - masala """

# a = input()
#
# print(f"""
# {a}{8 * ' '}{a}
#  {a}{6 * ' '}{a}
#   {a}{4 * ' '}{a}
#    {a}  {a}
#     {a * 2}
#    {a}  {a}
#   {a}{4 * ' '}{a}
#  {a}{6 * ' '}{a}
# {a}{8 * ' '}{a}
# """)

"""7 - masala """

# a = input()

"""First version """

# a = input()
# print(f"""
# {a * 7}
# {6 * len(a) * ' ' + a}
# {5 * len(a) * ' ' + a}
# {4 * len(a) * ' ' + a}
# {3 * len(a) * ' ' + a}
# {2 * len(a) * ' ' + a}
# {len(a) * ' ' + a}
# {a}
# {a * 7}
#  """)

"""Second version"""
# a = input()
# print(a * 8)
# for i in range(7, 0, -1):
# 	print(i * len(a) * ' ' + a)
# print(a * 8)

""" 8 - masala """

# print('Hello\tWorld')

# a = 'Ssdf Ssdf SSDFsdf'
# print(a.casefold())

""" Vazifalar """

""" 1 - masala """
# a = input()
# b = input()
# print(a + ' ' + b)

""" 2 - masala """
# a = input("Ismingiz: ")
# b = input("Yoshingiz: ")
#
# print(f" Sizning ismingiz {a}, yoshingiz {b}. ")

""" 3 - masala """

# matn = "hello My name is Shavkat"
#
# print("Katta harflarda: " + matn.upper())
# print("Kichik harflarda: " + matn.lower())
# print("Sarlavha usulida: " + matn.title())
# print("Birinchi harfini katta qilib: " + matn.capitalize())
#
#

""" 4 - masala """

# matn = "    Man ismim Shavkat. Hello world    "
# matn = input()
#
# print(matn.strip())
# print(matn.rstrip())
# print(matn.lstrip())

""" 5 - masala """

# name = input("Ismingiz: ")
# age = input("Yoshingiz: ")
# color = input("Sevimli rangiz: ")
#
# print(f"Salom, sizning ismingiz {name}, yoshingiz {age}, Sevimli rangiz {color}")


""" 6 - masala """

# name = input("Ismingi kichik harflarda: ")
#
# print(name.upper())
# print(name.capitalize())

""" 7 - masala """

# a = int(input())
# b =  int(input())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)

""" 8 - masala """

# a = float(input())
# b = float(input())

# print(a ** 2)
# print(b ** 2)
# print(a / b)

""" 9 - masala """

# def determine_type(user_input):
#     # Попробуем преобразовать строку с помощью eval
#
#     result = eval(f"""type({user_input})""")
#     return f"Тип данных: {result.__name__}"
#
# # Получаем ввод от пользователя
# user_input = input("Введите данные: ")
#
# # Определяем тип данных
# print(determine_type(user_input))


#
# """ length funksiyasi django dan import qilingan ekan """


# a, b = map(int, input().split())
#
# print(len(range(a,b+1)))

# a = int(input())
# if a % 2 == 0: print(a)
# else: print(a * 2)
#
#
#
# b = int(a) % 100
# # # if len(str(a)) == 3 and a % 100 != 0 and a % 10 != 0:
# # # 	print(words.get(a // 100) + ' yuz ' + words.get(a % 100 // 10 * 10) + ' ' + words.get(a % 10))


# a = int(input())
# words = {
# 	0: '',
# 	1: 'bir', 2: 'ikki', 3: 'uch', 4: "to’rt", 5: 'besh', 6: 'olti', 7: 'yetti', 8: 'sakkiz', 9: "to’qqiz", 10: "o’n",
# 	20: 'yigirma', 30: "o’ttiz", 40: "qirq", 50: "ellik", 60: "oltmish", 70: "yetmish", 80: "sakson", 90: "to’qson",
# 	100: "bir yuz",
# 	1000: "bir ming"}
#
#
# if len(str(a)) == 3:
# 	answer = words.get(a // 100) + ' yuz ' + words.get(a % 100 // 10 * 10) + ' ' + words.get(a % 10)
# 	print(answer.strip())
# elif len(str(a)) == 2:
# 	print((words.get(a % 100 // 10 * 10) + ' ' + words.get(a % 10)).strip())
# elif len(str(a)) == 1:
# 	print(words.get(a))
# else:
# 	print(words.get(1000))

''' Python sanoq sistemalari bilan ishlash '''

"""
a = 0b111111100101
b = 0o11111110013242346701

print(type(a))
print(int("z", 36))
print(bin(123),
      '\n', hex(999999999),
      '\n', oct(127))

"""

"""Sonni istalgan sanoq sistemasiga o'girish"""

#
# x = int(input("O'nlik sanoqdagi son: "))
# base = int(input("Nechchilik sanoqga: "))
#
# while x > 0:
# 	digit = x % base
# 	print(digit, end='')
# 	x //= base
#


# print(int('z', base=36))

""" 15 masala """

# print(
#       f' Yuzasi: {2 * 3.14 * float(input()) ** 2}', '\n',
#       f' Uzunligi: {2 * 3.14 * float(input())}'
#       )

"""" 10 masala  """

# a = float(input())
# b = float(input())
#
# print(min(a, b))
""" 11 masala """

# a = map(int, input().split())
# print(sum(a) / 3)

""" 12 masala """
#
# print(lambda a=int(input()): print(a ** 0.5))

# print(int(input()) ** 0.5)


"""  1 masala """

# print(int(input()) // 100)

"""2 masala """

# print(int(input()) // 1000)

""" 3 masala """

# print(int(input()) // 1024)

""" 4 masala """

# a, b = map(int, input().split())

# print(a // b)

""" 5 masala """

# a, b = map(int, input().split())
#
# print(a // b)
# print(a % b)

""" 6 masala """
# a = int(input())
# print(a // 10, '\n', a % 10)

# for i in input(): print(i)

""" 7 masala """

# a = int(input())
# print(a // 10 + a % 10)

"""  8 masala  """

# print(input()[-1: -3: -1])

""" 9 masala  """

# print(int(input()) // 100 )

""" 10 masala  """

# print(input()[-1:-3:-1])


""" 11 masala """

# a = int(input())
# print(a // 100 + a // 10 % 10 + a % 10)

""" 12 masala """

# print(input()[-1:-4:-1])

""" 13 masala  """

# a = int(input())
# b = a % 100 * 10 + a // 100
# print(b)
# print(f'{a[1]}{a[2]}{a[0]}')


""" 1 masala  """
# a = int(input())
# b = int(input())
# x = a - b
# print(x)

""" 2 masala """

# a = int(input())
# b = int(input())
# x = a > b
# print(x)

""" 3 masala """

# a = int(input())
# b = int(input())
# x = a >= b
# print(x)

""" 4 masala """

# a = int(input())
# b = int(input())
# x = a / b
# print(x)

""" 5 masala """

# a = int(input())
# b = int(input())
# x = a // b
# print(x)

""" 6 masala """

# a = int(input())
# b = int(input())
# x = a % b
# print(x)

"""  10 masala """

# s = int(input())
# r = float(input())
# l = 2 * 3.14 * r
# print(f' {s // l} marta aylanadi. ')


"""  11 masala """

# mahsulat_soni = int(input())
# ishchilar = int(input())
#
# print(mahsulat_soni // 3 // ishchilar  // 8)


"""  1 masala """

# print(int(input("Sonni kiriting: ")) > 0)

""" 6 masala """
# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a <= b <= c)

""" 7 masala  """
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# print( a > b > c or c > b > a )

""" 8 masala  """

# a = int(input())
# b = int(input())
#
# print( a % 2 == 1 and b % 2 == 1)
""" 9 masala """

# a = int(input())
# b = int(input())
#
# print( a % 2 == 1 or b % 2 == 1)

""" 10 masala """

# a = int(input())
# b = int(input())
#
# print( a % 2 == 1 and b % 2 == 0 or (a % 2 == 0 and b % 2 == 1))

""" 11 masala """

# a = int(input())
# b = int(input())
#
#
# print((a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1))

""" 12 masala  """

# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a > 0 and b > 0 and c > 0)

""" 13 masala  """

# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a > 0 or b > 0 or c > 0)

""" 14 masala  """
# a = int(input())
# b = int(input())
# c = int(input())
#
# print((a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0))
""" 15 masala """

# a = int(input())
# b = int(input())
# c = int(input())
# a = 5
# b = 9
# c = 1
#
# print((a > 0 and b > 0 and c < 0) or (a > 0 and b < 0 and c > 0) or (a < 0 and b > 0 and c > 0))

""" 16 masala  """

# a = int(input())
#
# print(a % 2 == 0 and 100 > a >= 10)

""" 17 masala  """
# a = int(input())

# print( a % 2 == 1 and 100 <= a < 1000)

""" 18 masala  """
# a = 0
# b = 9
# c = 9
#
# print(a == b != c or a != b == c or a == c != b)


""" 19 masala  """

# a = -9
# b = -9
# c = 9
#
# print(a + b == 0 or b + c == 0 or a + c == 0)


"""  20 masala  """
# a = int(input())
#
# print((a // 100) != (a % 100 // 10) != (a % 10) and (a // 100) != (a % 10))

""" 21 masala """

# a = int(input())
# print((a // 100) < (a % 100 // 10) < (a % 10))
# a = 123
# print((a // 100) == (a % 100 // 10 - 1) and (a % 100 // 10) == (a % 10 - 1))

""" 24 masala """

# a, b, c = map(int, input().split())
#
# print((b ** 2 - 4 * a * c) >= 0)

""" 25 masala """
#
# x = int(input())
# y = int(input())
# print(x < 0, y > 0)

""" 26 masala """

# x = int(input())
# y = int(input())
# print(x > 0, y < 0)


""" 27 masala """
# x = int(input())
# y = int(input())
# print(x > 0 and y < 0 or x < 0 and y < 0)

""" 28 masala """

# x = int(input())
# y = int(input())
# print(x > 0 and y > 0 or x < 0 and y < 0)

""" 29 masala """
# x, y = 2, 2
# x1, y1 = 3, 1
# x2, y2 = 1, 3
#
# # x1 > x2 or y1 > y2
# print((x1 > x > x2) and ( y1 < y < y2))


""" 30 masala  """

# a = int(input())
# b = int(input())
# c = int(input())
# print(a == b == c)

""" 31 masala  """

# a = int(input())
# b = int(input())
# c = int(input())
# print(a == b != c or a != b == c or a == c != b)

""" 32 masala  """

# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a ** 2 + b ** 2 == c ** 2)
""" 33 masala  """
# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a + b > c or a + c > b or b + c > a)

""" 34 masala  """
# x = int(input())
# y = int(input())
#
# print((x + y) % 2 == 1)


""" 35 masala  """

# x1, y1 = 4 , 3
# x2, y2 = 2, 3
#
# print((x1 + y1) % 2 == 1 and (x2 + y2) % 2 == 1 or (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0)


""" 36 masala  """
# x1, y1 = 4 , 3
# x2, y2 = 2, 3
#
# print(x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2)

""" 37 masala  """
# x1, y1 = 1, 1
# x2, y2 = 1, 2
#
#
# def generate_pairs(x, y):
# 	pairs = []
# 	for i in [x-1, x, x+1]:
# 		for j in [y-1, y, y+1]:
# 			pairs.append((i, j))
# 	pairs.remove((x1,y1))
# 	return pairs
#
# # print(generate_pairs(x1, y1))
#
# print((x2, y2) in generate_pairs(x1, y1))

""" 38 masala """

# x1, y1 = 8, 6
# x2, y2 = 6, 8
#
# print(abs(x1  - x2) == abs(y1 - y2))

""" 39 masala """
#
# x1, y1 = 4, 3
# x2, y2 = 5, 5
#
# a = x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2
# b = x1 - x2 == y1 - y2
# print(a or b)

""" 40 masala  """

# x1, y1 = 4, 3
# x2, y2 = 5, 1
#
# pairs = []
# a = [(y1 - 1), (y1 + 1)]
#
# for i in [x1 - 2, x1 + 2, x1 + 1, x1 - 1, ]:
# 	if i == x1 + 1:
# 		a.clear()
# 		a.extend([(y1 - 2), (y1 + 2)])
# 	for j in a:
# 		pairs.append((i, j))
#
# print(pairs)
# print( (x2, y2) in pairs)


""" 25 misol """
# kun = 1
# hafta = ["Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]
#
# jav = kun % 7
# print(hafta[jav - 4])

""" 27 masala """
# kun = 2
# hafta = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba", ]
# #
# jav = kun % 7
# print(hafta[jav-2])


""" Topshiriq 1 """

# list1 = [4, 6, 7, 8, 89, 9, 5, 4, 3]
#
# list1.append(64)
#
# list1.sort()
# print(list1[-1])

""" Topshiriq 2  """
# list1 = [4, 6, 7, 8, 89, 9, 5, 4, 3]
#
# list1.append(64)
#
# list1.sort()
# print(list1[0])

""" Topshiriq 3 """

# a = input()
#
# list1 = [4, 6, 7, 8, 89, 9, 5, 4, 3]
#
# l = len(list1) // 2
# list1.insert(l, a)
# print(list1)

""" vazifa 1 """

# fruits = ('apple', 'banana', 'cherry', 'orrange', 'kiwi')
#
# print(fruits[0], ' va ', fruits[4])
# print(fruits[2])

""" vazifa 2 """

# numbers = (1,2,3,4,5,56,3,4,6,3,5,3,5,3,5,3,23,)
#
# print(numbers.count(2))

""" vazifa 3 """

# my_tupple = ('red', 'blue', 'green')
#
# my_list = list(my_tupple)
# my_list.append("Yellow")
#
# my_tupple = tuple(my_list)
# print(my_tupple)

""" vazifa 4 """

# letters = ('a', 'b', 'c', 'd', 'e')
#
# print(letters[-1: -6: -1])

""" vazifa 5 """

# nested_tuple = (1,3,3,4,(5,56,7,87),6,4,)

# print(nested_tuple[4][1])

# for i in nested_tuple:
# 	if type(i) == tuple:
# 		for j in i:
# 			print(j)
# 	else: print(i)


# for i in nested_tuple:
# 	for j in i:
# 		print(j)

""" vazifa 6 """

# my_tuple = 10, 20, 30, 40, 50
#
# list2 = list(my_tuple)
# list2.append(60)
# tuple2 = tuple()
#
# print(tuple(tuple2))

""" vazifa 7 """

# tuple1 = 1,2,3
#
# tuple2 = 4,5,6
#
# tuple3 = tuple1 + tuple2
#
# print(tuple3)

""" topshiriq  1   """
# numbers = [10, 20, 30, 40, 50, 30, 30 ,30, 30,]
#
# print(numbers)





""" topshiriq 2 """

""" topshiriq 3 """
# my_list = ['Ali', 'Olim', 'Zarina', 'Jasur', 'Sabina']
#
# print(my_list.index('Zarina'))
