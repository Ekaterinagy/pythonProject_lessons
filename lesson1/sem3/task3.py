# Создайте словарь со списком вещей для похода в качестве ключа и их массой
# в качестве значения. Определите какие вещи влезут в рюкзак передав его
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
def find_combinations(things):
    sorted_things = sorted(things, key=lambda el: el[1], reverse=True)
    return sorted_things


def find_combinations_rec(current_mass, current_combination,
                          remaining_tools):
    if current_mass <= max_mass:
        backpacks.append(current_combination)
    for i in range(len(remaining_tools)):
        new_combination = current_combination + [remaining_tools[i]]
        new_mass = current_mass + remaining_tools[i][1]
        new_remaining = remaining_tools[i + 1:]
        find_combinations_rec(new_mass, new_combination, new_remaining)


max_mass = 3000
tools = [
    ('спички', 10), ("спальник", 600), ("дрова", 1000), ("топор", 500),
    ("вода", 1500), ("еда", 2000), ("косметичка", 500), ("аптечка", 300)]
backpacks = []
sorted_tools = find_combinations(tools)
find_combinations_rec(0, [], sorted_tools)

for i in backpacks[1:]:
    k = ''
    for j in i:
        k = k + f'{j[0]} {j[1]}, '
    print(k[:-2])
