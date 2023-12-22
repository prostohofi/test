from random import choice


def get_hero(name=None, hp=100, level=1, xp=0, money=30, inventory=None) -> list:
    """ возвращает список характеристик героя"""
    if not name:
        names = ("Алексей", "Олег", "Лютый", "Меченый")
        name = choice(names)
    if not inventory:
        inventory = []
    return [name, hp, level, xp, money, inventory]


def show_hero(hero: list) -> None:
    """ выводит на экран характеристики персонажа """
    print("имя:", hero[0])
    print("здоровье:", hero[1])
    print("уровень:", hero[2])
    print("опыт:", hero[3])
    print("деньги:", hero[4])
    print("инвентарь:", hero[5])


def show_enumerated_items(items: list) -> None:
    """выводит на экран пронумированные предметы"""
    for num, item in enumerate(items, 1):
            print(f"{num} - {item}")   


def get_option(items: list) -> str:
    """ """
    print("0 - отмена")
    option = input("введите номер опции: ")
    if option == "0":
        print("отмена покупки")
        return ""
    elif int(option) < 0 or int(option) > len(shop_items):
        print("ошибка! неверная опция ")
        return ""
    else:
         return option


def visit_shop(hero: list, shop_items: list):
    """
    выводит на экран информацию о герое
    выводит на экран текст магазина
    выводит на экран опции
    предаставляет игроку выбор опции
    действует по выбранной опции
    """
    show_hero(hero)
    print(f"{hero[0]} приехал в лавку торговца")
    print("враменная акция: все товары по 10 монет!")
    price_tmp = 10
    print("1 - купить товары")
    print("2 - продать предметы")
    print("0 - выйти из лавки")
    option = input("введите номер опции")
    if option == "1":
        show_enumerated_items(shop_items)
        option = get_option(shop_items)
        if /-/--//*-/-*/*-*-//*-
        if hero[4] < price_tmp:
            print("недостаточно денег!")
        else:
            hero[4] -= price_tmp
            item_index = int(option) - 1
            item_name = shop_items[item_index]
            hero[5].append(item_name)
            shop_items.pop(item_index)
               

player = get_hero()
shop_items = ["зелье лечения", "зелье копчение", "зелье подводного дыхания"]
visit_shop(player, shop_items)
print("---конец---")
show_hero(player)
print(shop_items)
