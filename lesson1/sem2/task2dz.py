# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions



def get_nok(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            return greater
        else:
            greater += 1


a, b = list(map(int, input('Введите первую дробь числа через /: ').split('/')))
c, d = list(map(int, input('Введите вторую дробь числа через /: ').split('/')))

numerator = a * c
denominator = b * d
multiple = f'{numerator}/{denominator}'
f_multiple = fractions.Fraction(a, b) * fractions.Fraction(c, d)
print(f'multiple = {multiple} , fraction_multiple = {f_multiple}'
      f' {multiple == f_multiple.__str__()}')

nok = get_nok(b, d)
numerator = int(nok / b) * a + int(nok / d) * c
denominator = nok
_summ = f'{numerator}/{denominator}'
f_summ = fractions.Fraction(a, b) + fractions.Fraction(c, d)
print(f'_summ = {_summ} , fraction_summ = {f_summ}'
      f' {_summ == f_summ.__str__()}')

