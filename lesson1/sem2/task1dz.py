# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

a = int(input('Введите число: '))
h = hex(a)
print(f'Вы ввели {a}, через функцию hex = {h}')

res = ''
d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

while a > 0:
    res = str(d[a % 16]) + res
    a = a // 16
print(f'в шестнадцатеричной {res}, {res == h[2:]} ')
