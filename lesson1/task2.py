#Пользователь вводит число от 1 до 999. Используя операции с числами сообщите
# что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

number = int(input())
MIN_NUMBER = 0
MAX_NUMBER = 1000
res = 0
if MIN_NUMBER < number < 10:
    res = number**2

elif 10 <= number < 100:
    number1 = number % 10
    number2 = number // 10
    res = number1 * number2
elif 100 <= number < MAX_NUMBER:
    number1 = number % 10
    number2 = (number // 10) % 10
    number3 = number//100
    res = number1 * 100 + number2 * 10 + number3
else:
    res = 'Введите число из диапозона'

print(res)