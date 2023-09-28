# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции
# — функции. Дополнительно сохраняйте все операции поступления и снятия средств
# в список.
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# Любое действие выводит сумму денег
def addition(props):
    withdraw = int(input('Введите сумму: '))
    if withdraw % FREENDERING == 0:
        props['count'] = props['count'] + 1
        props['s'] = props['s'] + withdraw
        props['operation'].append(withdraw)
        print(props['s'])


def check_tax(props):
    if props['s'] >= RICHLIMIT:
        tax = props['s'] - props['s'] * RICHTAX
        props['s'] = props['s'] - tax
        props['operation'].append(tax)

def check_bonus(props):
    if props['count'] % THREFOPERATIONS == 0 and props['count'] != 0:
        bonus = props['s'] * BONUSTREE - props['s']
        props['s'] = props['s'] + bonus
        props['count'] = 0

def removal(props):
    withdraw = int(input('Введите сумму: '))

    if withdraw % FREENDERING == 0:

        percentage = withdraw * COMMISSIONOUTDROW
        if percentage < MINLIMIT:
            percentage = MINLIMIT
        elif percentage > MAXLIMIT:
            percentage = MAXLIMIT
        if (percentage + withdraw) < props['s']:

            res = withdraw + percentage
            props['s'] = props['s'] - res
            props['count'] = props['count'] + 1
            props['operation'].append(-res)
def get_operation_type():
    return input('Введите операцию 1(пополнение),2(снятие),3(выход): ')


props = {'s': 0, 'count': 0, 'operation': []}
s = 0
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
    action = get_operation_type()
    check_tax(props)
    check_bonus(props)
    if action == '1':
        addition(props)
    elif action == '2':
        removal(props)
    else:
        break
    print(props['s'], props['operation'])

