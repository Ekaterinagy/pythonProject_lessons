a = 45
b = 'jjkjss'
c = 3.25
d = True
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#Создайте в переменной data список значений разных типов перечислив их
# через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты.

data = [a, b, c, d, e]

for n,i in enumerate(data, start=1):
    print(n, i, id(i), i.__sizeof__(), hash(i))
    if isinstance(data, int) or isinstance(i, str) :
        print(n, i, id(i), i.__sizeof__(), hash(i), True)
    else:
        print(n, i, id(i), i.__sizeof__(), hash(i))
       

