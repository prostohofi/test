names = [
    "Вася",
    "Ася",
    "Вася",
    "Вася",
    "Ся",
    "Ася"
]

counter = {}
for name in names:
    if name not in counter:  # если name встретилось впервые
        counter[name] = 1  # создать ключ name и связать с 1
    else:  # если name уже было в словаре
        counter[name] += 1  # добавляем 1 к значению name

print(counter)
