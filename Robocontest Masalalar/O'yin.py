# n = 7
#
# numbers = list(range(2, n+1))
#
# print(numbers)
#
# for i in numbers[1::]:
# 	for j in numbers[1::]:
# 		if j % i == 0:
# 			numbers.remove(j)
#
#
# 	print(numbers)
# 	print(i)
#
#
# print(numbers)


# n = int(input())
#
#
# tub_sonlar = []
# for i in range(2, n + 1):
#     tub = True
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             tub = False
#             break
#     if tub:
#         tub_sonlar.append(i)
# b = len(tub_sonlar)
# if b % 2 == 1:
#     print("Ali")
# else:
#     print("Bobur")

# a = [1,2,43,4,5,65,6,534,3]
#
# def increment(x: list):
# 	x.append("as")
#
#
# increment(a)
# print(a)
# increment(a)
# increment(a)
# increment(a)
# increment(a)
# # y = 10
# print(a)  # Результат: 11
# # print(y)  # Результат