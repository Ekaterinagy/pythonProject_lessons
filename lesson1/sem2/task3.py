# Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
a = a2 = int(input('Введите число: '))
b = bin(a)
c = oct(a)
print(b, c)
res1 = ''
res2 = ''

while a > 0:
    res1 = str(a % 2) + res1
    a = a // 2

print(res1)

if res1 == b[2:]:
    print(True)

while a2> 0:
    res2 = str(a2 % 8) + res2
    a2 = a2 // 8
print(res2)

if res2 == c[2:]:
    print(True)
