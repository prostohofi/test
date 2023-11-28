#фихс ми: когда выходишь с лавки пишет недастаточно денег и выключает игру
import os # для очистки экрана
from random import randint

"""
сражается
играет в кости
покупает в лавке
"""


def start_game():
    """ создаёт игрока и отправляет к камню """
    player_name = input("введите имя игрока: ")
    player_hp = 100
    player_money = 10
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
        print("уехал на арену")
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
    os.system("cls")
    print(player_name, "приехал в лавку")
    print("1 - посмотреть ассортимент товаров")
    print("2 - вернуться к камню")
    print("0 - выйти из игры")
    option = input("введите номер варианта: ")
    if option == "1":
        print("у нас в ассортименте : 1 - кот поводырь за 20 монет, 2 - фраза которая наносит очень много урона за 50 монет")
        number_purchases = input("введите номер товара : ")
        if number_purchases == "1":
            player_money - 20
        if number_purchases == "2":
            player_money - 50
    elif player_money < 20:
        print("недостаточно денег")
    elif option == "2":
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_potions)

    

start_game()
