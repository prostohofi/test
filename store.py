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
    print("1 - купить товары")
    print("2 - продать предметы")
    print("0 - выйти из лавки")
    option = input("введите номер опции")
    if option == "1":
        for num, item in enumerate(shop_items, 1):
            print(f"{num} - {item}")
        print("0 - выйти из покупки")
        option = input("введите номер опции: ")
        # проверить, усть ли такой товар у лавчника
        # проверить, хватает ли на него денег герою
        #добавить товар в инвентарь героя
        #убрать товар из списка товаров лавки


player = get_hero()
shop_items = ["зелье лечения", "зелье копчение", "зелье подводного дыхания"]
visit_shop(player, shop_items)