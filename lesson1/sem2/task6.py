#Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег


s = 100000
count = 0
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREFOPERATIONS = 3
BONUSTREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600

while True:
    action = input('Введите операцию 1,2,3: ')
    if s >= RICHLIMIT:
        s *= RICHTAX
    if count % THREFOPERATIONS == 0 and count != 0:
        s *= BONUSTREE
        count = 0
    if action == '1':
        withdrow = int(input('Введите сумму: '))
        if withdrow % FREENDERING == 0:
            count += 1
            s += withdrow
            print(s)
    elif action =='2':
        withdrow = int(input('Введите сумму: '))
        if withdrow % FREENDERING == 0:
            percentage = withdrow*COMMISSIONOUTDROW
            if percentage < MINLIMIT:
                percentage = MINLIMIT
            elif percentage > MAXLIMIT:
                percentage = MAXLIMIT
            if (percentage + withdrow) < s:
                s -= (withdrow + percentage)
                count += 1
    else:
        break
    print(s)