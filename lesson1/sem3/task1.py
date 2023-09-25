# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

initially = [1, 2, 3, 1, 2]
duplicates = []
for el in initially:
    if initially.count(el) > 1 and el not in duplicates:
        duplicates.append(el)
print(f'{initially} список с дублирующимися элементами -> {duplicates}')
