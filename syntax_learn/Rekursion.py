# Рекурсия

# def rec(x):
#     if x < 5:
#         print(x)
#         rec(x + 1)
#         print(x)
#
#
# rec(1)
#
#
# # Формула нахождения факториала
# # 5! = 5 * 4 * 3 * 2 * 1
# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x - 1) * x
#
#
# print(fact(998))
#
#
# Формула нахождения числа Фибоначчи
# def fib(x):
#     if x == 1:
#         return 0
#     if x == 2:
#         return 1
#     return fib(x - 1) + fib(x - 2)
#
#
# print(fib(10))
#

# # Формула нахождения числа Фибоначчи через цикл
#
# def fib(x):
#     a = 0
#     b = 1
#     for i in range(x - 1):
#         a, b = b, a + b
#     return a
#
#
# print(fib(8))

# Полиндром
# шалаш
# asdffdsa
# " " and "a"

# def palindrome(x):
#     if len(x) <= 1:
#         return True
#     if x[0] != x[-1]:
#         return False
#     return palindrome(x[1:-1])
#
#
# print(palindrome('asdffdsa'))


# def rec(x):
#     if len(x) == 1 or len(x) == 2:
#         return x
#     return x[0] + '(' + rec(x[1:-1]) + ')' + x[-1]
#
# print(rec('asdfghjdjhgfdsa'))

# Степень числа через рекурсию
# def power(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1/power(x, -n)
#
#     if n % 2 == 9:
#         return power(x, n // 2)*power(x, n//2)
#     else:
#         return power(x, n-1)*x
#
# print(power(4, -256))
#
#
# def rec(lists, level=1):
#     print(*lists, 'level=', level)
#     for i in lists:
#         if type(i) == list:
#             rec(i, level + 1)
#
#
# aa = [1, [1, 3, [5, 7, 8, 45, 23], 4, [5, 6, [8, 4, 3, 2], 7, 8, ], 65, 7]]
# rec(aa)
