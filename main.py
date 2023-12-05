import os # для очистки экрана
from random import randint

def pause():
    input("нажмите ENTER для продолжения")

"""
сражается
играет в кости
покупает в лавке
"""


def start_game():
    """ создаёт игрока и отправляет к камню """
    player_name = input("введите имя игрока: ")
    player_hp = 100
    player_money = 100
    player_xp = 0
    player_level = 1
    player_potions = 0
    visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)


def show_hero(name, hp, money, xp, level, potions):
    """выводит на экран инфо о персонже"""
    print("имя", name)
    print("здоровье", hp)
    print("деньги", money)
    print("опыт", xp)
    print("уровень", level) 
    print("зелья:", potions)
    print("-" * 20)


def visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    """камень: выбор дороги"""
    os.system("cls") # очищает экран
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    print(player_name, "приехал к камню")
    print("1 - поехать на арену")
    print("2 - поехать в таверну")
    print("3 - заглянуть в лавку")
    print("0 - выйти из игры")
    option = input("введите номер варианта: ")
    if option == "1": 
        visit_arena(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "2": 
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "3": 
        visit_store(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "0": 
        print("вышел из игры")
    else:
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)


def visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    """ играть в кости или выйти к камню """
    os.system("cls")
    print(player_name, "приехал в таверну")
    print("1 - сыграть в кости")
    print("2 - вернуться к камню")
    print("0 - выйти из игры")
    option = input("введите номер варианта: ")
    if option == "1": 
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "2": 
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "0": 
        print("вышел из игры")
    else:
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)


def play_dice(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    os.system("cls")
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    bet = int(input("введите ставку"))
    if not player_money:     
        print("у", player_name, "нет денег чтобы играть")
        input("нажмите ENTER чтобы продолжить")
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif bet < 1:
        print("ставка должна быть больше 0!")
        input("нажмите ENTER чтобы продолжить")
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif bet > player_money:
        print("недостаточно денег!")
        input("нажмите ENTER чтобы продолжить")
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    player_score = randint(2, 12)
    tavern_score = randint(2, 12)
    print("игрок выбросил", player_score)
    print("дальнобойщик выбросил", tavern_score)
    if player_score > tavern_score:
        player_money += bet
        print(player_name, "выиграл", bet, "монет")
        input("нажмите ENTER чтобы продолжить")
    elif player_score < tavern_score:
        player_money -= bet
        print(player_name, "проиграл", bet, "монет")
        input("нажмите ENTER чтобы продолжить")
    else:
        print("ничья!")
        input("нажмите ENTER чтобы продолжить")

    visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_potions)


def visit_store(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    """ покупает что то в лавке или уходит"""
    potion_price = 20
    os.system("cls")
    print(player_name, "приехал в лавку")
    print(f"1 - купить зелье лечения за  {potion_price} менет")
    print("2 - вернуться к камню")
    print("0 - выйти из игры")
    option = input("введите номер варианта: ")
    if option == "1":
        if player_money < potion_price:
            print(f"у, {player_name} недастаточно денег")
        else:
            player_money -= potion_price
            player_potions += 1
            print(f"{player_name} купил зелье за {potion_price} монет")
        pause()
        visit_store(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "2":
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "0":
        print("вышел из игры")

def start_combat(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    enemy_name ="Ящер Подиков" # таду: какие статы у врага
    enemy_hp = 100
    enemy_money = 10
    enemy_xp = 0
    enemy_level = 1
    enemy_potions = 1

    while player_hp > 0 and enemy_hp > 0:
        os.system("cls")
        show_hero(player_name, player_hp, player_money, player_xp, player_level, player_potions)
        print("--- против ---")
        show_hero(enemy_name, enemy_hp, enemy_money, enemy_xp, enemy_level, enemy_potions)
        print("- " * 20)
        if player_hp > 0:
            enemy_hp = combat_turn(player_name, enemy_name, enemy_hp)
        if enemy_hp > 0:
            player_hp = combat_turn(enemy_name, player_name, player_hp)
        pause()


    if player_hp > 0:
        print(f"{player_name} победил!")
        player_xp += 10 # таду: зависит от противника
        new_level = xp // 100 + 1
        max_xp_level = 100
        if new_level > player_level : #дать новый уровень, если достаточно опыта
            player_level = new_level
            print(f"{player_name} получил {player_level} уровень!")
                                    #от уровня зависит жизнь и урон
        if max_xp_level > 100:
            player_hp + 50
            player_level + 1

        #visit_arena(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    else:
        print(f"{player_name} проиграл")
         #геймовер и завершить игру


def combat_turn(attacker_name, defender_name, defender_hp):
    damage = randint(0, 10) # таду: урон должен зависеть от игрока
    defender_hp -= damage
    print(f"{attacker_name} ударил {defender_name} на {damage}")
    
    return defender_hp


def visit_arena(player_name, player_hp, player_money, player_xp, player_level, player_potions):
    "сражается на арене "
    os.system("cls")
    print(player_name, "приехал на арену")
    print("1 - пойти сражаться")
    print("2 - вернуться к камню")
    print("0 - выйти из игры")
    option = input("введите номер варианта: ")
    if option == "1":
        start_combat(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "2":
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)
    elif option == "0":
        print("вышел из игры")


start_game()
