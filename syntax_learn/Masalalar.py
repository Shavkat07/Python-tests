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

""" 16 topshiriq """

# alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

# a = alphabet[0:3]
# print(a)
# print(alphabet[-3::1])

""" 17 topshiriq """

# for i in ['Ali', 'Olim', 'Zarina', 'Jasur']:
# 	print(f'{i} talaba')


""" 18 topshiriq """

# for i in (22, 25, 28, 30, 27, 23): print(i)


""" 19 topshiriq """
# b = 0
# for i in [1, 5, 'banana', 10, 'apple', 20]:
# 	if type(i) == int:
# 		b += i
# print(b)

# def find_abc(n):
#     limit = int(n ** (1/3)) + 1  # Ограничиваем a и b до кубического корня из n
#
#     for a in range(1, limit):
#         if n % a != 0:
#             continue  # Если n не делится на a, переходим к следующему a
#         for b in range(a + 1, limit):  # b > a, чтобы избежать одинаковых значений
#             if (n // a) % b != 0:
#                 continue  # Если n/a не делится на b, пропускаем
#             c = n // (a * b)  # Вычисляем c
#             if c > b and a * b * c == n:  # c > b и проверка произведения
#                 return a, b, c  # Найдено подходящее решение
#     return -1  # Решение не найдено
#
# # Пример вызова функции
# n = int(input("Введите число n: "))
# result = find_abc(n)
# print(result)


# def find_divisors(n):
#     divisors = []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n // i)
#     divisors.sort()
#     return divisors
#
# def find_abc(n):
#     divisors = find_divisors(n)
#     for i in range(len(divisors)):
#         a = divisors[i]
#         for j in range(i + 1, len(divisors)):
#             b = divisors[j]
#             c = n // (a * b)
#             if c > b and a * b * c == n:
#                 return a, b, c
#     return -1
#

# n = int(input())
# result = find_abc(n)
# print(result)

"""  1 vazifa  """
# b = 0
# while True:
# 	a = int(input())
# 	if a == 0:
# 		print(b)
# 		break
# 	else:
# 		b += a

""" 2 vazifa """

# a = int(input())
# b = int(input())
# c = 0
# while b - a != 0:
# 	c += a
# 	a += 1
#
# print(c+a)
""" 3 vazifa  """

# a = []
# while True:
# 	a.append(int(input()))
# 	if 0 in a:
# 		break
# print(a)

""" 4 vazifa """

# x = [1, 2, 34, 4, 4, 5, ]
# a = len(x)
# b = 0
# while a != 0:
# 	if x[-1] < x[b]:
# 		g = x.pop(b)
# 		x.append(g)
# 	else:
# 		b += 1
# 	a -= 1
# print(x[-1])

""" 5 vazifa """

# x = [1, 2, 34, 444, 4, 545, 3, 5, 6, 7, 7, 8, 98, 6, 5, 5, 63455]
# a = 0
# i = 0
# l = len(x)
# j = 0
# while l > 0:
# 	if a < x[i]:
# 		a = x[i]
# 		j = i
# 	i += 1
# 	l -= 1
# print(j)

""" 6 vazifa """

# a = input()
# l = len(a)
# g = 0
# while l > 0:
# 	g += 1
# 	l -= 1
# print(g)

"""  """

# a = [1, 2, 3, 4, 5, 6, 7, 8, 7, 5, 4, 3, 2]
#
# b = max(a)
# c = True
# g = False
#
# def compare(x, y):
# 	if x <= y:
# 		return True
# 	else:
# 		return False
#
# for i in range(0, len(a) - 1):
# 	if a[i] == b or g:
# 		g = True
# 		if compare(a[i + 1], a[i]):
# 			pass
# 		else:
# 			c = False
# 	else:
# 		if compare(a[i], a[i + 1]):
# 			pass
# 		else:
# 			c = False
#
# print(c)
""" 7 masala """

# x = [1, 2, 0, -14, 5, -6]
# l = len(x)
# i = 0
# j = 0
# k = 0
# while l > 0:
# 	if j <= x[i]:
# 		j = x[i]
# 	elif k > x[i]:
# 		k = x[i]
# 	i += 1
# 	l-=1
# print(j)
# print(k)

""" 8 masala """
# x = [-2, 31, 104, 51, 19, 7]
#
#
# l = len(x)
# i = 0
# j = 0
# k = 0
# while l > 0:
# 	if x[j] <= x[i]:
# 		j = i
# 	elif x[k] >= x[i]:
# 		k = i
# 	i += 1
# 	l-=1
#
# x[k], x[j] = x[j], x[k]
#
# print(x)

""" 9 masala """
# x = [-2, 31, 104, 51, 19, 7]
# son = int(input())
# l = len(x)
# i = 0
# j = False
# while l > 0:
# 	if x[i] == son:
# 		j = True
# 	else:
# 		j = False
# 	l -= 1
# 	i += 1
#
# print(j)

""" while 4  """

# n = int(input())
# k = 0
#
# while n != 0:
# 	if n == 1:
# 		print("3 ning 0 inchi darajasi")
# 		break
# 	n -= 3
# 	k += 1
# 	if n < 0:
# 		print("3 ga bulinmaydi")
# 		break
# else:
# 	k -= 3
# 	while k > 0 or k == -1:
# 		k -= 3
# 		if k < 0:
# 			print("3 ning darajasi emas")
# 			break
# 	else:
# 		print("3 ning darajasi")

""" 10 masala """
# a = int(input())
# b = int(input())
#
# ekub = 0
# m = 1
# while m >= 0:
# 	if a % m == 0 or b % m == 0:
# 		ekub = m
#
# 	m += 1
# print(ekub)

# while a > 1:
# 	if a % x == 0:
# 		devisors.append(x)
# 		a //= x
# 	else:
# 		x += 1
#
# while b > 1:
# 	if b % y == 0:
# 		devisors2.append(y)
# 		b //= y
# 	else:
# 		y += 1
# l = len(devisors)
# l2 = len(devisors2)
#
# um_devisors = []
#
# i = 0
# while l > 0:
# 	if devisors[i] in devisors2:
# 		um_devisors.append(devisors[i])
# 	i += 1
# print(devisors)


# write_to_file.py

# Читаем данные из source.py
# with open("source.py", "r") as source_file:
# data =

# Открываем target.py для записи данных
# for i in range(10,20):
# 	with open("dars1.py", "a") as target_file:
# 		target_file.write(f'""" for {i} """\n')
#
# print("Данные успешно записаны в target.py!")


# rows = 5
# for i in range(1, rows + 1):
# 	for j in range(1, rows + 1):
# 		if j <= i:
# 			print("0", end=' ')
# 		else:
# 			print('*', end=' ')
# 	print()


# rows = 6
# for i in range(1, rows):
# 	for j in range(1, rows):
# 		if 1 < i < 5 and (j == rows - i or j == i)and i != :
# 			print(1, end=' ')
# 		else:
# 			print(0, end=' ')
# 	print()


# print("""
# ****************        **            **             *
# **            **        **            **            * *
# **                      **            **           *   *
# **                      **            **          *     *
# **                      **            **         *       *
# ****************        ****************        ***********
#               **        **            **       *           *
#               **        **            **      *             *
#               **        **            **     *               *
# **            **        **            **    *                 *
# ****************        **            **   *                   *
# """)


# # Определяем количество строк и столбцов
# rows = 11
#
#
# for i in range(rows):
#     for j in range(cols):
#
#     print()

# print('' .split(' ')
#
#
# print("\033[31mЭтот текст будет красным\033[0m")

""" 1 vazifa """
#
# for i in range(1, 26, 5):
# 	for j in range(i, i + 5):
# 		if j % 5 == 1 or j % 5 == 0 or 11 < j < 15:
# 			print(f"\033[31m{j}\033[0m", end=' ')
# 		else:
# 			print(j, end=' ')
# 	print()
#
# """ 2 vazifa """
#
# for i in range(1, 26, 5):
# 	for j in range(i, i + 5):
# 		if (j % 5) % 2 == 0 and (j % 5) != 0 and j != 12 and j != 14:
# 			print(j, end=' ')
# 		else:
# 			print(f"\033[31m{j}\033[0m", end=' ')
# 	print()

""" 3 masala """

# for i in range(1, 6):
# 	for j in range(1, 6):
# 		if ((j == 1 or j == 5) or j == i or 2 * i == j) and 1 < i < 4:
# 			print('*', end=' ')
# 		elif j == 1 or j == 5:
# 			print('*', end=' ')
# 		else:
# 			print(' ', end=' ')
# 	print()

""" Ismimni  chiqarish  """

# height = 7
# width = 13
# for i in range(1, 8):
#
# 	for j in range(1, 8):
# 		if i == 1 or i == 4 or i == 7 or (j == 1 and 1 < i < 4) or (j == 7 and 4 < i < 8):
# 			print("*", end=' ')
# 		else:
# 			print(" ", end=' ')
# 	print("   ", end=' ')
#
# 	for j in range(1, 8):
# 		if j == 1 or j == 7 or i == 4:
# 			print("*", end=' ')
# 		else:
# 			print(" ", end=' ')
#
# 	print("   ", end=' ')
#
# 	for j in range(width):
# 		if (j == width // 2 - (i - 1)
# 				or j == width // 2 + (i - 1)
# 				or ((i - 1) == height // 2
# 				    and width // 2 - (i - 1) <= j <= width // 2 + (i - 1))):
# 			print("*", end='')
# 		else:
# 			print(" ", end='')
#
# 	print("", end=' ')
#
# 	for j in range(1, 14):
# 		if i == j or i + j == 14:
# 			print("*", end='')
# 		else:
# 			print(" ", end='')
#
# 	print("   ", end=' ')
#
# 	for j in range(1, 10):
# 		if i + 4 + j == 10 or j == 1 or i - j == 2:
# 			print("*", end=' ')
# 		else:
# 			print(" ", end=' ')
#
# 	print("", end='')
#
# 	for j in range(width):
# 		if (j == width // 2 - (i - 1)
# 				or j == width // 2 + (i - 1)
# 				or ((i - 1) == height // 2
# 				    and width // 2 - (i - 1) <= j <= width // 2 + (i - 1))):
# 			print("*", end='')
# 		else:
# 			print(" ", end='')
#
# 	print("   ", end=' ')
#
# 	for j in range(1, 8):
# 		if j == 4 or i == 1:
# 			print("*", end=' ')
# 		else:
# 			print(" ", end=' ')
#
# 	print("   ", end=' ')
# 	print()

"""############################################################"""

# for i in range(1, 6):
# 	for j in range(1, 6):
# 		if j == 1:
# 			print("#", end=" ")
# 		else:
# 			print("*", end=" ")
# 	print()

"""############################################################"""
#
# for i in range(1, 8):
# 	for j in range(1, 8):
# 		if i == 1 or i == 7 or j == 1 or j == 7:
# 			print("*", end=" ")
# 		else:
# 			print(" ", end=" ")
#
# 	print()

"""############################################################"""

# import time
# import sys
#
#
# def console_animation():
# 	text = "OPEN"
# 	while True:
# 		for i in range(len(text)):
# 			sys.stdout.write(f"\033[31m\r {text[i:]} {text[:i]}\033[0m")  # Перемещаем часть текста
# 			sys.stdout.flush()
# 			time.sleep(0.1)  # Задержка для создания эффекта анимации
#
#
# try:
# 	console_animation()
# except KeyboardInterrupt:
# 	print("\nАнимация остановлена.")


"""############################################################"""
# c = 1
# for i in range(1, 6):
# 	for j in range(1, 6):
# 		if j <= i:
# 			print(f"\033[31m{c}\033[0m", end=" ")
# 		else:
# 			print(c, end=" ")
# 		if 0 < c < 11:
# 			print("", end=" ")
# 		c += 1
# 	print()
#
# print()
"""############################################################"""

# c = 1
# for i in range(1, 6):
# 	for j in range(1, 6):
# 		if c == 17 or c == 21 or c == 13 or i < j:
# 			print(c, end=" ")
# 		else:
# 			print(f"\033[31m{c}\033[0m", end=" ")
# 		if 0 < c < 11:
# 			print("", end=" ")
# 		c += 1
# 	print()
#
"""###############################################################"""

"""  Array 1 """
# a = []
# n = 7
#
# for i in range(1 + n*2):
# 	if i % 2 == 1:
# 		a.append(i)
#
#
# print(a)
# print(len(a))
""" Array 2  """

# n = 5
# a = []
# for i in range(1, n+1):
# 	a.append(2 ** i)
# print(a)

""" Array 3 """

# d = 2
# a = 6
# n = 6
# j = []
# def recursion_progressiya(a, d, n):
# 	if n == 0:
# 		return
# 	n -= 1
# 	j.append(a)
# 	return recursion_progressiya(a+d, d, n)
# recursion_progressiya(a, d, n)
# print(j)

""" Array 4 """
# n = 6
# a = 5
# d = 3
# j = []
# def recursion_progressiya(a, d, n):
# 	if n == 0:
# 		return
# 	n -= 1
# 	j.append(a)
# 	return recursion_progressiya(a*d, d, n)
# recursion_progressiya(a, d, n)

# print(j)


""" Array 5 """

# n = 6
# j = []
# def fibonacci(a, b, n):
# 	j.append(a)
# 	a, b = a + b, a
# 	if n <= 0:
# 		return j
# 	n -= 1
#
# 	return fibonacci(a, b, n)
#
# print(fibonacci(0, 1, n))

""" Array 7 """

# n = 5
# l = [1,2,3,4,5,6,4,2,3,5,6,5,3,32,4,6,67,7]
#
# for i in l[-1::-1]:
# 	l.append(i)
#
# print(l)

""" Array 8 """

# l = [4,5,7,8,6,9]
# b = []
# for i in l:
# 	if i% 2 == 1:
# 		b.append(i)
#
# print(b, len(b))

""" Array 9 """

# l = [4, 5, 7, 8, 6, 9]
# b = []
# for i in l:
# 	if i % 2 == 0:
# 		b.append(i)
#
# print(b[-1::-1], len(b))
""" Array 10 """

# l = [4, 5, 7, 8, 6, 9]
# toq = []
# juft = []
#
# for i in l:
# 	if i % 2 == 0:
# 		juft.append(i)
# 	else:
# 		toq.append(i)
# print(juft, toq[-1::-1])

""" Array 11 """

# a = [1,2,4,5,6,6,4,3,2,34,65]
# k = 3
#
# for i in a[k::k]:
# 	print(i)


""" Array 12 """
# z = 55555555555
#
# counter = 0
# if z < 0:
# 	for a in range(z, -z):
# 		for b in range(z, -z+1):
# 			if a * b == z and a <= b:
# 				counter += 1
# 				print(a, b)
# 	print(counter)
#
# elif z == 0:
# 	print(-1)
# else:
# 	for a in range(-z, z):
# 		for b in range(-z, z+1):
# 			if a * b == z and a <= b:
# 				counter += 1
# 				print(a, b)
# 	print(counter)

""" Array 13 """

# a = [1,3,4,5234,234,234,234,23,42,4,1,657,5677]
# b = [7,5,4,23,3,34,23,23,2,34,54,76,89,98,78]
# c = [4,5,4,2,2,4,5,6,6,5,4,4,3,4,55]
# g = a + b + c
# print(g)

""" Array 3 """

# d = {1,2,23,4,4,5,2,3,6,6}
#
# d.remove(23)
#
# print(d)

""" Array 4 """

# d = {1, 2, 3, 4, 5, 6, 23}
# f = {66, 5, 7, 8, 77, 478}
#
# a = d.union(f)
#
# # print(a)
# # print(d)
# print(f)
""" Array 5 """

# d = {1, 2, 3, 7, 4, 5, 6, 23}
# f = {66, 5, 7, 8, 77, 478}

# max(d)
# print(min(d))

""" Array 6 """

# d = {1, 2, 3, 7, 4, 5, 6, 23}

# d.add(4556)

# d.remove(4556)
# print(d)

""" Array 7 """

# d = {1, 2, 3, 7, 4, 5, 6, 23}
# f = {66, 5, 7, 8, 77, 478}
# j = 1
# for i in d:
# 	j *= i

# print(d.symmetric_difference(f))

""" Array 8 """
# d = {1, 2, 3, 7, 4, 5, 6, 23}
# f = {66, 5, 7, 8, 77, 478}
# j = 1
# for i in d:
# 	j *= i

# print(j)

""" Array 9 """
# d = {1,3,5,5,97,986,8,8}
# f = {66, 5, 7, 8, 77, 478}
#
#
#
# print(len(d) == 0)


""" Array 10 """

# d = {1,3,5,5,97,986,8,8}
# f = {66, 5, 7, 8, 77, 478}

# print(len(d))

""" Functions  """

# n = 10
# l = [0]
#
#
# def fibonacci(x):
# 	a = 0
# 	b = 1
# 	for i in range(x - 1):
# 		a, b = b, a + b
# 		l.append(a)
# 	return a
#
#
#
# print(fibonacci(n+1))
# print(l)


# if x == 1:
# 	return 0
# if x == 2:
# 	return 1
#
# return fibonacci(x - 1) + fibonacci(x - 2)


# print(fibonacci(10))
# print(l)

#################################################

""" 5 misol """

#
# def RectPS(x1, y1, x2, y2):
# 	a1, a2 = x1, y1
# 	b1, b2 = x2, y1
# 	c1, c2 = x1, y2
# 	d1, d2 = x2, y2
#
# 	A = a2
# 	B =
#
# 	print(a1, a2, '\n',  b1, b2,'\n', c1, c2,'\n', d1, d2)
#
#
# RectPS(2, 1, 5,6)

""" 2 misol  """

# l = [3,2,2,3,4,5,5,4,3,45,46,898]
# g = filter(lambda x: x % 2 ==0, l)
# print(list(g))

""" 3 misol """

# k = [ {'key': 5}, {'key': 6}, {'key': 7}, {'key': 8}, {'key': 9} ]

# data = []
# h = filter(lambda x: x['key'] == 5, k)

# print(list(h))

""" 5 misol """

# l = ["Abror", "Asad", "Shavkat", "Aziz", "Axror"]

# h = filter(lambda x: x.startswith("A"), l)

# print(list(h))

""" 6 misol """

# l = [12000, 34000, 54000, 76000]
#
# j = map(lambda x: x + x / 10, l)
#
# print(list(j))

""" 7 misol """

# l = ['sdf', 'asdfg', 'sdfg', 'ertyer']

# j = map(lambda x:  x.capitalize() , l)

# print(list(j))

""" 9 misol """

# l = [234, 34, 4, 897, 7, 7, 45, 3, 34, 23]
#
# h = sorted(l)
#
# print(h)

""" 10 misol """

# l = [234, 34, 4, 897, 7, 7, 45, 3, 34, 23]



""" 11 misol """
import math
import random
# d = random.randint(1, 124)
# print(math.ceil(1.49))
# print(math.floor(1.9))
# print(d)

""" 6 misol """
# a = random.randint(1, 50)
#
# for i in range(5):
# 	son = int(input())
# 	if son > a:
# 		print("Son Kichikroq")
# 	elif son < a:
# 		print("Son Kattaroq")
# 	else:
# 		print("Topdiz")


"""  misol """

# print(" ".join(map(str, [x for x in range(2, int(input("Введите число n: ")) + 1) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))])))
#

""" 1 misol """
# a = input("Name: ")
#
# talabalar = {
# 	"John": 23,
# 	"Mary": 22,
# 	"Bob": 21,
# 	"Anna": 20,
# 	"Peter": 19
#
# }
#
# print(talabalar.get(a))
#
""" 2 misol """

# l = [1,3,4,556,87,43,5,3,3,5,6,6,7,4,3]
#
# print(max(l))
# print(min(l))

"""3 misol """

# a = "Hello World"
#
# print(a[::-1])

""" 4 misol """
#
# matn = "Hello World my name is Shavkat"
#
# print(len(matn.split()))

""" 5 misol """



""" 6 misol """

# import turtle
# import math
#
# t = turtle.Turtle()
# t.speed(0)
# t.color("red")
# turtle.bgcolor("black")
#
# def corazon(n):
#     x = 16 * math.sin(n) ** 3
#     y = 13 * math.cos(n) - 5 * \
#         math.cos(2*n) - 2*math.cos(3*n) - \
#         math.cos(4*n)
#     return x, y
#
# t.penup()
# for i in range(15):
#     t.goto(0, 0)
#     t.pendown()
#     for n in range(0, 100, 2):
#         x, y = corazon(n/10)
#         t.goto(x*i, y*i)
#     t.penup()
#
# t.hideturtle()
# turtle.done()


# import matplotlib.pyplot as plt
#
# # Example: Draw a circle
# circle = plt.Circle((0.5, 0.5), 0.4, fill=True, color="blue")
# fig, ax = plt.subplots()
#
# ax.add_artist(circle)
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_aspect('equal')
# plt.show()