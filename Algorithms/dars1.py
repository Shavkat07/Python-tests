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

""" Svetafor faqat qushimcha prikoliyam bor """
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

"""  Misollar 1    """
#
# a = 134
# b = 25
# c = 3
# if a > b :
# 	if a > c:
# 		print(a)
# 	else:
# 		print(c)
# else:
# 	if b > c:
# 		print(b)
# 	else:
# 		print(c)

"""  Misollar 2 """

# yil = 2024
#
# print(yil % 4 == 0 and yil % 100 != 0 or yil % 400 == 0)

""" Misollar 3 """

# a = 89
#
# if 90 <= a <= 100:
# 	print("A")
# elif 80 <= a < 90:
# 	print("B")
# elif 70 <= a < 80:
# 	print("C")
# elif 60 <= a < 70:
# 	print("D")
# else:
# 	print("F")
#

""" Misollar 4 """

# temp = 20
# if 20 > temp:
# 	print('qish')
# elif 20 < temp:
# 	print('yoz')
# else:
# 	print('Bahor')

""" Misollar 5 """

# kun = int(input())
#
# week = {
# 	1: 'Dushanba',
# 	2: 'Seshanba',
# 	3: 'Chorshanba',
# 	4: 'Payshanba',
# 	5: 'Juma',
# 	6: 'Shanba',
# 	7: 'Yakshanba'
# }
# print(week[kun])

""" Misollar 6 """

# a = input()
#
# if a[0] == '9':
# 	print("Beeline")
# elif a[0] == '8':
# 	print('Ucell')
# elif a[0] == '7':
# 	print("Uzmobile")
# else:
# 	print("NOMA'LUM OPEROTOR")
#


""" Misollar 7 """

# a = int(input())
#
# dic = {
# 	(12, 1, 2): "Qish",
# 	(3, 4, 5): "Bahor",
# 	(6, 7, 8): "Yoz",
# 	(9, 10, 11): "Kuz",
# }
#
# # for i in dic if (a in i) print(dic[i])
# print( dic[i] if (a in i) else dic for i in dic)
# print(15 | 22)

""" Vazifa 1 """

# a = int(input())
# baho = int(input())
#
# if a >= 5:
# 	if baho >= 90:
# 		print('Mukofot')
# 	elif baho >= 70:
# 		print("Ma'qullangan")
# 	else:
# 		print("Qoniqarsiz")
# else:
# 	if a >= 85:
# 		print("Mukofot")
# 	elif a >= 60:
# 		print("Ma'qullangan")
# 	else:
# 		print("Qoniqarsiz")

""" Vazifa 2 """

# yili = int(input())
# yoshi = int(input())
#
# if yili >= 2020:
# 	if yoshi >= 25:
# 		print("500$")
# 	else:
# 		print('700$')
# elif yili >= 2015:
# 	if yoshi >= 25:
# 		print("600$")
# 	else:
# 		print('800$')
# else:
# 	if yoshi >= 25:
# 		print("700$")
# 	else:
# 		print('900$')

""" vazifa 3 """

# tajriba = int(input())
# daraja = int(input())
#
# if tajriba >= 10:
# 	if daraja == "yuqori":
# 		print(f'bonus 20%')
#
# 	elif daraja == "urta":
# 		print(f'bonus 15%')
# 	else:
# 		print(f'bonus 10%')
# elif tajriba > 5:
# 	if daraja == "yuqori":
# 		print(f'bonus 15%')
# 	else:
# 		print(f'bonus 10%')
# else:
# 	print(f'bonus 5%')

""" vazifa 4 """

# balance = int(input("Balance: "))
# cart = int(input("Cart: "))
# if balance >= 10000:
# 	if  cart == "premium":
# 		print(f"Limit 5 000$")
# 	elif cart == "standard":
# 		print(f"Limit 3 000$")
# 	else:
# 		print(f"Limit 2 000$")
# elif balance > 5000:
# 	if cart == "premium":
# 		print(f"Limit 2 500$")
# 	else:
# 		print(f"Limit 1 500$")
# else:
# 	print("limit 500$")

""" vazifa 5 """

# meva = int(input("Meva Turi: "))
# miqdor = int(input("Miqdor: "))
#
# if meva == "olma":
# 	if miqdor > 10:
# 		print(f"skidka 15%")
# 	else:
# 		print(f"skidka 10%")
# elif meva > "banan":
# 	if miqdor > 5:
# 		print("skidka 12%")
# 	else:
# 		print(f"skidka 8%")
# else:
# 	if miqdor > 8:
# 		print("skidka 10%")
#
# 	else:
# 		print("skidka 5%")

""" vazifa 6 """
#
# balance = int(input("Balance: "))
# cart = int(input("Cart: "))
#
# if balance >= 10000:
# 	if  cart == "premium":
# 		print(f"Limit 5 000$")
# 	elif cart == "standard":
# 		print(f"Limit 3 000$")
# 	else:
# 		print(f"Limit 2 000$")
# elif balance > 5000:
# 	if cart == "premium":
# 		print(f"Limit 2 500$")
# 	else:
# 		print(f"Limit 1 500$")
# else:
# 	print("limit 500$")
#
""" vazifa 7 """

# balance = int(input("Balance: "))
# cart = int(input("Cart: "))
# if balance >= 10000:
# 	if  cart == "premium":
# 		print(f"Limit 5 000$")
#
# 	elif cart == "standard":
# 		print(f"Limit 3 000$")
# 	else:
# 		print(f"Limit 2 000$")
# elif balance > 5000:
# 	if cart == "premium":
# 		print(f"Limit 2 500$")
# 	else:
# 		print(f"Limit 1 500$")
# else:
# 	print("limit 500$")

""" Tenglama robocontest """

# a = int(input())
# b = []
# c = int(a ** 0.5)
# i = 2
# while c != 1:
# 	if a % i == 0:
# 		b.append(i)
# 		c -= 1
# 		a //= i
# 	else:
# 		i += 1
# 		c -= 1
#
# if len(b) < 3:
# 	print(-1)

# a = int(input())
# b = []
# i = 2
#
# while i * i <= a:
# 	while a % i == 0:
# 		b.append(i)
# 		a //= i
# 	i += 1
#
# if a > 1:
# 	b.append(a)
#
# if len(b) < 3:
# 	print(-1)
# else:
# 	h = b[1:-1]
# 	del b[1:-1]
# 	j = 1
# 	for i in h:
# 		j *= i
# 	b.append(j)
# 	if b[0] == b[1] or b[1] == b[2] or b[0] == b[2]:
# 		print(-1)
# 	else:
# 		print(f"{b[0]} {b[1]} {b[2]}")

# for i in range(2, c):
# 	if a % i == 0:
# 		b.append(i)
# 		a //= i
# if a != 1:

# 	b.append(a)
# 	print(a)
# 	for i in b:
# 		h = b.count(i)
# 		if h != 1:
# 			for j in range(h):  b.remove(i)
# 			b.append(i**h)


# print(b)

# while a != 1:
# 	for i in range(2, a):
# 		if a % i == 0:
# 			a //= i
# 			b.append(i)
#
# if len(b) == 2 or len(b) == 1:
# 	print(-1)
# else:
# 	for j in b:
# 		if b.count(j) == 1:
# 			jav.append(j)
# 		else:
# 			jav.append(j ** b.count(j))

# print(f"{jav[0]} {jav[1]} {jav[2]}")

# n = 0
# jav = 0
# while n <= 10:
# 	jav += n
# 	n+=1
# print(jav)

# else:
# 	for j in b:
# 		if

# for i in range(1, a+1):
# 	if a % i == 0:
# 		b.append(i)
""" The End """

""" Slides Window Algorithm """
# a = "abcbada"
# b = "axbxcxd"
# c = "aaaaaaa"
# f = "abcdefg"
# j = []
"""  """

#
# for i in range(2, 101, 2):	print(f'juft son {i}')
#
# for i in range(1, 100, 2): print(f'toq sonlar {i}')
"""  """
# a = 0
# for i in range(100):
# 	a += i
# print(a)


"""  """
# a = 0
# b = 0
# for i in range(50):
# 	if i % 2 == 0:
# 		a += i
# 	else:
# 		b += i
# print(a, b)
""" 3 """
# j = 0
# for i in range(-80, 80):
# 	if i % 7 == 0:
# 		j += 1
# print(j)

""" 4 """
# j = 0
# for i in ['olma', 'banan', 'apelsin', 'olma']:
# 	if i == 'olma':
# 		j += 1
# print(j)
#
""" 5 """

# a = 2
# b = 45
# j = 0
# t = 0
#
# for i in range(a, b):
# 	if i % 2 ==0:
# 		j = j + 1
# 	else:
# 		t = t + 1
# print(j, t)
#
""" 6  """

# j = 0
# for i in [1,2,3,4,5,6,6,7,8,8,9,9,6,6,54,4,54,5,75,75,7]:
# 	if i % 2 == 0:
# 		j += 1
# print(j)

""" 7 """
# a = input()
# j = 0
# for i in a:
# 	if i.isupper():
# 		j += 1
# print(j)

"""  """
# a = int(input())
# b = a
# n = int(input())
#
# for i in range(n-1):
# 	a *= b
# print(a)

"""   2  """
# a = int(input())
# b = a
# n = int(input())
#
# for i in range(n):
# 	print(a)
# 	a *= b

"""  for 1  """
# n = int(input())
# k = int(input())
#
# for i in range(n):
# 	print(k)
""" for 2 """

# a = 2
# b = 9
# h = 0
# for i in range(a, b+1):
# 	print(i)
# 	h += 1
#
# print(h)

"""  for 3  """

# a = 2
# b = 9
# h = 0
# for i in range(b-1, a, -1):
# 	print(i)
# 	h += 1
#
# print(h)

""" for 4 """

# price = int(input())
#
#
# for i in range(1,10):
# 	print(i*price)
#


""" for 5 """

# price = int(input())
#
# for i in range(1,11):
# 	print(i * 0.1 * price)

""" for 6  """

# price = 500
#
# for i in range(12, 20, 2):
# 	print(round(i * 0.1 * price))

""" for 7 """

# a = 1
# b = 10
# h = 0
# for i in range(a, b+1):
# 	h += i
#
# print(h)

""" for 8 """
#
# a = 1
# b = 10
# h = 1
# for i in range(a, b+1):
# 	h *= i
#
# print(h)

""" for 9 """

# a = 2
# b = 7
# h = 0
# for i in range(a, b+1):
# 	h += i ** 2
# print(h)

""" for 10 """

# n = 5
# S = 0
# for i in range(1, n+1):
# 	S += 1/i
# print(S)


""" for 11 """

# n = 5
# S = 0
# for i in range(1, (n+1)*2):
# 	S += (n+i)**2
# print(S)

""" for 12 """
# n = 25
# j = 1
#
# for i in range(10,n+10):
# 	j *= i * 0.1
#
# print(j)

""" for 13 """

# n = 10
# s = 0
#
# for i in range(n):
# 	s += -0.1
# print(s)
""" for 14 """

# n = 6
# j = 0
# for i in range(1, 2 * n, 2):
# 	j += i
# print(j)

""" for 15 """

# n = 2
# a = 2
# s = a
#
#
# for i in range(n-1):
# 	a *= s
#
# print( 1 if n == 0 else a)


""" Masalalar No_1 """

# for i in range(1, 10):
# 	if i % 2 == 1:
# 		print(i)
# 		break


""" No 2  """

# for i in range(11):
# 	if i % 2 == 0:
# 		continue
# 	else:
# 		print(i)
#


""" No 3 """
# while True:
# 	a = input()
# 	if a == 'stop':
# 		break
# 	else:
# 		print(1)


""" No 4  """

# a = input()

# for i in a:
# 	if i == 'a':
# 		break
# 	else:
# 		print(i)

""" No 5 """
# a = map(int, input().split())
# j = 0
# for i in a:
# 	if i < 0:
# 		continue
# 	else:
# 		j += i
# print(j)

"""  """
# n = int(input())
# for i in range(11):
# 	print(i * n)

""" faktorial """

# a = int(input())
#
# j = 1
# for i in range(1, a+1):
# 	j *= i
#
# print(j)

""" 1 masala  """

# l = [23, 3, 4, 4, 3, 32, 2, 2, 3, 4, 4, 5]
# print(int(input()) in l)

""" 2 masala """

# for i in range(100, 1000):
# 	if 5 < i // 100 + i // 10 % 10 + i % 10 < 8:
# 		print(i)

""" 3 masala  """
#
# a = input()
# print(len(a))

""" 4 masala """

# a = 23, 4, 5, 35, 54, 3, 3
# g = 0
#
# for i in a:
# 	g += i
#
# print(g)
""" 5 masala """

# a = [3,4,5,56,4,3,3,5,6,6,4,33,3]
# max_son = 0
# for i in a:
# 	if max_son < i:
# 		max_son = i
#
# print(max_son)

""" 6 masala """

# a = [3, 4, 5, -56, 4, -3, -3, 5, 6, 6, 4, 33, 3]
# min_son = 0
# for i in a:
# 	if i < min_son:
# 		min_son = i
#
# print(min_son)

""" 7 masala """


#
# x = 5
# while 2 + 2 == 4:
# 	while True:
# 		break
# 	x = x - 1
# 	if x == 2:
# 		break
# 	print('S;asdafasdfas')
# else:
# 	print('vghjgghjhgjh')
#
# print('werw cxg g fgh ')


"""####################################################################33"""

# c = 1
# for i in range(1, 5):
# 	for j in range(1, 5):
# 		print(c, end=" ")
# 		c += 2
# 	print()
#
# a = {1,2,3,4,5,6}
# b = {1,2,3,4,5,6,7,8,9,10,11}
# c = a.difference(b)
# # b = c
# # for i in c:
# # 	print(i)
# print(a)
#
#
# a = {2,34,5,6,3,32,3,2,4,5,}
# b = {4.3433,4,4,4,3,3,5,5,3,33}


# a | b
# print(a.union(b))
# print(a | b)
# print(a.intersection(b))

""" ############################################################# """
"""  Task about convert string(avvvvsssssddffff) to (a1v4s5d2f4)  """

def char_counter(word: str):
	counter = 0
	previous_letter = word[0]
	answer = ''
	for i in word:
		if i == previous_letter:
			counter += 1
		else:
			answer += previous_letter + str(counter)
			counter = 1
		previous_letter = i
	answer += previous_letter + str(counter)

	return answer

print(char_counter("avvvvsssssddffff"))

