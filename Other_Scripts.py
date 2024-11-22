# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def tail_swap(strings):
#     num = (strings[0].split(':')[1])
#     num2 = (strings[1].split(':')[1])
#     a = strings[0].split(':')[0]
#     b = strings[1].split(':')[0]
#
#     return str(':'.join(str(a+' '+num2).split()) + ' ' + ':'.join(str(a+' '+ num).split())).split()
# print(tail_swap(['abc:123', 'cde:456']))
# ----------------------------------------------------------------------------------------
""" while orqali listdan son a ni topish"""
# a = 78
#
# myList = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]
# c = 0
#
# while myList[c] != a:
# 	c = c + 1
# 	if c == len(myList):
# 		print(None)
# 		break
# else:
# 	print(c)


# ----------------------------------------------------------------------------------------

# def ali(func):
#     """Alias for"""
#     def inner():
#         print(" ali decorator")
#         func()
#         print("bolongi func ")
#     return inner()
#
#
# @ali
# def test():
#     """docs test"""
#     print("bexruz")
#
#
# print(help(test))

"""  Qrcode yasash  """
# import qrcode
#
# # Текст или данные, которые вы хотите закодировать в QR-коде
# data = "https://github.com/Shavkat07"
#
# # Создайте объект QRCode
# qr = qrcode.QRCode(
#     version=1,  # Размер QR-кода (от 1 до 40)
#     error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок (L, M, Q, H)
#     box_size=10,  # Размер одного "блока" QR-кода
#     border=4,  # Количество блоков вокруг QR-кода
# )
#
# # Добавьте данные в QR-код
# qr.add_data(data)
# qr.make(fit=True)
#
# # Создайте изображение QR-кода (может потребоваться установить библиотеку Pillow)
# img = qr.make_image(fill_color="black", back_color="white")
#
# # Сохраните изображение QR-кода в файл
# img.save("qrcode.png")

"""  Web Kamera orqali rasm olish  """

# import cv2
#
# # Инициализация камеры (0 - первая камера, подключенная к ноутбуку)
# camera = cv2.VideoCapture(0)
#
# # Проверка, что камера была успешно инициализирована
# if not camera.isOpened():
#     print("Не удалось получить доступ к камере")
# else:
#     # Захват одного кадра
#     ret, frame = camera.read()
#
#     # Если кадр успешно захвачен
#     if ret:
#         # Сохранение снимка в файл
#         cv2.imwrite("snapshot.png", frame)
#         print("Снимок сохранен как 'snapshot.png'")
#     else:
#         print("Не удалось сделать снимок")
#
# # Освобождение ресурса камеры
# camera.release()


"""  SH ni faqat for loop orqali chiqarish   """

# for i in range(1, 8):
#     for j in range(1, 8):
#         if i == 1 or i == 4 or i == 7 or (j == 1 and 1 < i < 4) or (j == 7 and 4 < i < 8):
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print("   ", end=' ')
#
#     for k in range(1, 8):
#         if k == 1 or k == 7 or i == 4:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# def likes(names):
# 	if len(names) == 0:
# 		return "no one likes this"
# 	elif len(names) == 1:
# 		return names[0] + " likes this"
# 	elif len(names) == 2:
# 		return names[0] + " and " + names[1] + " likes this"
# 	elif len(names) == 3:
# 		return names[0] + ', ' + names[1] + " and " + names[2] + " likes this"
# 	else:
# 		return names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + " others likes this"
#
#
# print(likes([]))


"""  Suzni Har xil ranglarda chiqarish  """


# import os
# import sys
# import time
# from colorama import Fore, Style, init
#
# open = """
# *****************************************************************************************************************************
# *                                                                                                                           *
# *            * * * * * * * * * * *     * * * * * * * * * * *     * * * * * * * * * * *     *                   *            *
# *            *                   *     *                   *     *                         * *                 *            *
# *            *                   *     *                   *     *                         *   *               *            *
# *            *                   *     *                   *     *                         *     *             *            *
# *            *                   *     *                   *     *                         *       *           *            *
# *            *                   *     * * * * * * * * * * *     * * * * * * * * * * *     *         *         *            *
# *            *                   *     *                         *                         *           *       *            *
# *            *                   *     *                         *                         *             *     *            *
# *            *                   *     *                         *                         *               *   *            *
# *            *                   *     *                         *                         *                 * *            *
# *            * * * * * * * * * * *     *                         * * * * * * * * * * *     *                   *            *
# *                                                                                                                           *
# *****************************************************************************************************************************
#
# """
#
#
# def console_frame():
# 	os.system('clear' if os.name == 'posix' else 'CLS')
# 	# sys.stdout.write(output + "\n")
# 	sys.stdout.flush()
#
#
# # Инициализация colorama
# init(autoreset=True)
#
#
# def smooth_color_change(word, colors, delay=0.2, repetitions=10):
# 	"""
# 	Плавно меняет цвет слова на консоли.
#
# 	:param word: Слово, которое будет отображаться
# 	:param colors: Список цветов из библиотеки colorama
# 	:param delay: Задержка между изменениями цвета
# 	:param repetitions: Количество повторений смены цвета
# 	"""
# 	for _ in range(repetitions):
# 		for color in colors:
# 			# Удаляем предыдущее слово
# 			# sys.stdout.write("\r" + " " * len(word))
# 			console_frame()
# 			# sys.stdout.flush()
# 			# Печатаем слово в новом цвете
# 			sys.stdout.write(f"\r{color}{word}")
# 			sys.stdout.flush()
# 			time.sleep(delay)
#
#
# # Список цветов для смены
# colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW]
#
# # Слово для демонстрации
# word = open
#
# # Запуск функции
# smooth_color_change(word, colors)


"""   OPEN  Animation ni for bilan chiqarish"""



# import os
# import time
#
#
# def loop_write(word: str):
# 	print(word * 125, f"\n{word}")
# 	for i in range(1, 12):
# 		print(word, " " * 10, end=" ")
# 		for j in range(1, 12):
# 			if i == 1 and (j != i) or i == 11 and (j != i) or j == 1 or j == 11:
# 				print(word, end=" ")
# 			else:
# 				print(" ", end=" ")
#
# 		print("   ", end=" ")
#
# 		for j in range(1, 12):
# 			if i == 1 or j == 1 or j == 11 and 0 < i < 7 or i == 6:
# 				print(word, end=" ")
# 			else:
# 				print(" ", end=" ")
#
# 		print("   ", end=" ")
#
# 		for j in range(1, 12):
# 			if i == 1 or j == 1 or i == 6 or i == 11:
# 				print(word, end=" ")
# 			else:
# 				print(" ", end=" ")
#
# 		print("   ", end=" ")
#
# 		for j in range(1, 12):
# 			if i == j or j == 1 or j == 11:
# 				print(word, end=" ")
# 			else:
# 				print(" ", end=" ")
# 		print(" " * 10, word)
#
# 	print('\n', word * 125)
#
#
# def clear_terminal():
# 	os.environ['TERM'] = 'xterm'
# 	command = 'cls' if os.name == 'nt' else 'clear'
# 	os.system(command)
#
#
# c = f"\033[31m*\033[0m"
#
# i = 0
# while i < 100:
# 	i += 1
# 	if i % 2 == 0:
# 		loop_write(c)
# 		#print(c)
# 		time.sleep(0.3)
# 		clear_terminal()
# 	else:
# 		loop_write("*")
#
# 		time.sleep(0.3)
# 		clear_terminal()




"""  Sticker Man         """




