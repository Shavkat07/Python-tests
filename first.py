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
from django.template.defaultfilters import length

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

a = input()

print(f"""
{a}{8 * ' '}{a}
 {a}{6 * ' '}{a}
  {a}{4 * ' '}{a}
   {a}  {a}
    {a*2}
   {a}  {a}
  {a}{4 * ' '}{a}
 {a}{6 * ' '}{a}
{a}{8 * ' '}{a}
""")

"""7 - masala """

# a = input()

"""First version """

# print(f"""
# {a * 7}
# {6 * len(a) * ' ' + a}
# {5 * len(a) * ' ' + a}
# {4 * len(a) * ' ' + a}
# {3 * len(a) * ' ' + a}
# {2 * len(a) * ' ' + a}
# {' ' + a}
# {a * 7}
# """)

"""Second version"""

# print(a * 8)
# for i in range(7, 0, -1):
# 	print(i * len(a) * ' ' + a )
# print(a * 8)

""" 8 - masala """

# print('Hello\tWorld')

# a = 'Ssdf Ssdf SSDFsdf'
# print(a.casefold())

