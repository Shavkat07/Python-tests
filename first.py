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

""" 22 masala """
