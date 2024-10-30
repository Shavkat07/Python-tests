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


# print("Son juft" if int(input()) % 2 == 0 else "Son toq")

# if int(input()) % 2 == 0:
# 	print(" Son Juft  ")
#
# else:
# 	print("Son toq")

""" vazifa 2 """

# a = 6
# b = 3
# c = 7
#
# if a > b:
# 	if a > c:
# 		print(a)
# 	else:
# 		print(c)
# else:
# 	if b > c:
# 		print(b)
# 	else:
# 		print(c)

""" vazifa 3 """

# a = 6.5
# b = 3.4
# c = 7.6
#
# if type(a) == type(b) == type(c) == int:
# 	print(3)
# elif type(a) == type(b) == int or type(b) == type(c) == int or type(a) == type(c) == int:
# 	print(2)

# """ Do'st sonlar """
#
# a = 220
# b = 284
#
#
# def dust_son(x):
# 	boluvchilar = []
# 	for i in range(1, x):
# 		if x % i == 0:
# 			boluvchilar.append(i)
# 	return sum(boluvchilar)
#
#
# if dust_son(a) == b and dust_son(b) == a:
# 	print("Ha bular dust sonlar")

"""  Alghorithm Evklida  """

# def gcd(a, b):  # Ikki sonning eng katta umumiy bo'lubchisini topish
# 	if a == b:
# 		return a
# 	elif a > b:
# 		return gcd(a-b, b)
# 	else:
# 		return gcd(a, b-a)
#
# print(gcd(87646, 754))
# import cv2
#
#
# camera = cv2.VideoCapture(0)
#
# a = input()
#
# if a == 'Qizil':
# 	print('Mashinani tuxtat')
# elif a == "Sariq":
# 	print("Tayyorlan")
# elif a == "Yashil":
# 	print("Gazni bos")
# else:
# 	if not camera.isOpened():
# 		print("Не удалось получить доступ к камере")
# 	else:
# 		ret, frame = camera.read()
#
# 		if ret:
#
# 			cv2.imwrite("snapshot.png", frame)
# 			print("Снимок сохранен как 'snapshot.png'")
# 		else:
# 			print("Не удалось сделать снимок")
# 	print("KAMERAGA TUSHDING!!!")
#
# camera.release()

""" 15 masala """
# a = 17
# b = 16
# c = 15
#
# if (a + b) > (a + c) > (b + c):
# 	print(a, b)
# elif (a + b) < (a + c) < (b + c):
# 	print(b, c)
# elif (a + b) < (a + c) > (b + c):
# 	print(a, c)

""" 16 masala  """

# a = 11
# b = 16
# c = 17
#
# if a < b < c:
# 	a *= 2
# 	b *= 2
# 	c *= 2
# 	print(a, b, c)
# else:
# 	print(-a, -b, -c)

# """  """
# a, b = map(int, input().split())
# print(a * b if a * b > 2 * (a + b) else 2 * (a + b) )
# a = "13797"
#
# for i in range(len(a)):
# 	if int(a[i]) % 2 == 0 or len(a) % 2 == 0:
# 		print("NO")
# 		break
# else:
# 	print("YES")


