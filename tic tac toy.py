"""
+ поле из 9 клеток
+ игрок_1 - X
+ игрок_2 - O
игроки ходет по очереди
начинает X
победа:
    3 одинаковых по горизонтали, вертикали или диагонали
ничья - нет победителя и нет клеток
"""


field = ["."] * 9


def draw_filed(field: list) -> None:
    """выводит на экран 3 ряда игрового поля """
    for i in range(0, 7, 3):
        print(field[i], field[i + 1], field[i + 2])


def make_move(field: list, player: str):
    """ 
    спрашивает номер клетки поля: 1-9 вкл
    проверяет, есть ли на поле клетка с таким номером
    проверяет, что клетка с эти номером свободна
    если пройдёт все проверки, ставит игрока в эту клетку
    """
    while True:
        cell_num = int(input("введите номер клетки (1-9): "))
        if cell_num < 1 or cell_num > 9:
            print("ошибка! номер должен быть от 1 до 9 вкл")
            continue
        if field[cell_num - 1] in players:
            print("ошибка! эта клетка занята")
            continue
        field[cell_num - 1] = player
        break



player_1 = "X"
player_2 = "O"
players = (player_1, player_2)
field = list(range(1, 10, 1))
moves = 1

while True:
    draw_filed(field)
    if moves % 2:
        make_move(field, player_1)
    else:
        make_move(field, player_2)
    moves += 1


print("игра окончена")