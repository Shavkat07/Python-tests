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
import qrcode

# Текст или данные, которые вы хотите закодировать в QR-коде
data = "https://github.com/Shavkat07"

# Создайте объект QRCode
qr = qrcode.QRCode(
    version=1,  # Размер QR-кода (от 1 до 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок (L, M, Q, H)
    box_size=10,  # Размер одного "блока" QR-кода
    border=4,  # Количество блоков вокруг QR-кода
)

# Добавьте данные в QR-код
qr.add_data(data)
qr.make(fit=True)

# Создайте изображение QR-кода (может потребоваться установить библиотеку Pillow)
img = qr.make_image(fill_color="black", back_color="white")

# Сохраните изображение QR-кода в файл
img.save("qrcode.png")
