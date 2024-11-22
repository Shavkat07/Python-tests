from PIL import Image
import os
import time

# Расширенный набор символов (11 символов для большей детализации)
ASCII_CHARS = "@#%*+=-:. "
contents = os.listdir("../frames/")

def clear_terminal():
	os.environ['TERM'] = 'xterm'
	command = 'cls' if os.name == 'nt' else 'clear'
	os.system(command)

def resize_image(image, new_width=200):
	"""Изменение размера изображения для консоли"""
	width, height = image.size
	aspect_ratio = height / width
	new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 компенсирует пропорции текста в консоли
	return image.resize((new_width, new_height))


def grayscale_image(image):
	"""Преобразование изображения в градации серого"""
	return image.convert("L")


def image_to_ascii(image, new_width=200):
	"""Преобразование изображения в ASCII-арт"""
	image = resize_image(image, new_width)
	image = grayscale_image(image)

	pixels = image.getdata()
	# Правильное деление на длину символов
	ascii_str = "".join([ASCII_CHARS[min(pixel * len(ASCII_CHARS) // 256, len(ASCII_CHARS) - 1)] for pixel in pixels])
	ascii_lines = [ascii_str[index:index + new_width] for index in range(0, len(ascii_str), new_width)]
	return "\n".join(ascii_lines)


def main(path):
	path = f'frames/{path}/'
	try:
		image = Image.open(path)
	except Exception as e:
		print(f"Ошибка: {e}")
		return

	ascii_art = image_to_ascii(image)

	# print(ascii_art)


if __name__ == "__main__":
	frame_duration = 1 / 9
	while True:
		for i in contents[-1::-1]:
			clear_terminal()
			main(i)
			time.sleep(frame_duration)

