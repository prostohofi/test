"""
уровенрь и опыт
награды в бою

возможность пить зелья перед боем
деньги игрока
инвентарь: оружия, зелья, броне

покупки в лавке

"""


class Weapon:
    "оружие"
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> str:
        return f"{self.name} ({self.power})"


class Player:  # определяем класс
    """игрок"""
    def __init__(self, name: str, hp: int, weapon=None) -> None:
        """
        конструктор класса
        вызывается автомотически сразу после создания экземпляра
        self - ссылка на экземпляр
        все атрибуты определяются здесь!
        """
        self.name = name  # атрибут
        self.hp = hp
        self.weapon_default = Weapon("кулаки", 1)
        if weapon:
            self.weapon = weapon
        else:
            self.weapon = self.weapon_default
        self.power = 1

    def __str__(self) -> str:
        """автоматически вызывается при print"""
        return f"игрок {self.name}, жизни: {self.hp}, оружие: {self.weapon}"
    
    def attack(self, enemy) -> None:
        """игрок атакует противника"""
        if self.hp <= 0:
            return
        damage = self.weapon.power * self.power
        enemy.hp -= damage
        print(self.name, "атаковал", enemy.name)
        

class Game:
    """игра"""
    def __init__(self) -> None:
        self.player = Player("Вася", 100, Weapon("меч-леденец", 5))
        self.enemy = Player("Дальнобойщик", 100)
        self.is_fighting = False
        self.fight()

    def fight(self) -> None:
        """бой - обмен ударами"""
        self.is_fighting = True
        while self.is_fighting:
            self.player.attack(self.enemy)
            print(self.player)
            self.enemy.attack(self.player)
            print(self.enemy)
            self.check_winner()          
        print("бой окончен")

    def check_winner(self) -> None:
        if self.player.hp <= 0:
            print(self.enemy.name, "победитель")
            self.is_fighting = False
        elif self.enemy.hp <=0:
            print(self.player.name, "победитель")   
            self.is_fighting = False     


Game()
