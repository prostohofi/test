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
from os import system

field = ["."] * 9


def draw_filed(field: list) -> None:
    """выводит на экран 3 ряда игрового поля """
    system("cls")
    for i in range(0, 7, 3):
        print(field[i], field[i + 1], field[i + 2])


def make_move_human(field: list, player: str) -> None:
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

def make_move_copmuter(field: list, player: str) -> None:
     """
    собрать индексы клеток, куда можно ходить:
        на поле
        пустые
    выбрать случайную из них
    сделать туда ход
     """
    empty_cells_indexes = []
    for i in range(9):
        if not field[i] in players:
            empty_cells_indexes.append(i)
# таду: c помощью чёйса выбрать случайную клетку из свободных
#!!!!! тут ошибка


def get_winner(field: list, player: str) -> str:
    # победа в горизонатли
    for i in range(0, 7, 3):
        if field[i] == field[i + 1] == field[i + 2] == player:
            return player 


    # победа вертикали
    for i in range(3):
            if field[i] == field[i + 3] == field[i + 6] == player:
                return player 




    # победа в диагонали
    if field[0] == field[4] == field[8] == player: 
            return player 
    if field[2] == field[4] == field[6] == player:
            return player 


    return ""



player_1 = "X"
player_2 = "O"
players = (player_1, player_2)
field = list(range(1, 10, 1))
moves = 1

while True:
    if moves > 9:
        draw_filed(field)
        print("ничья")
        break
    draw_filed(field)
    if moves % 2:
        player = player_1
        make_move_human(field, player)
    else:
        player = player_2
        make_move_copmuter(field, player)
    moves += 1
    winner = get_winner(field, player)
    if winner:
        draw_filed(field)
        print("победил", winner)
        break


print("игра окончена")