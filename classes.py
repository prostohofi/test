"""
ООП - стиль программирования
класс - идея объекта, фабрика экземпляров
экземпляр - конкретная реализация объекта
переменные и функции внутри класса - атрибуты и методы
"""


class Player:  # определяем класс
    """игрок"""
    def __init__(self, name: str, hp: int) -> None:
        """
        конструктор класса
        вызывается автомотически сразу после создания экземпляра
        self - ссылка на экземпляр
        все атрибуты определяются здесь!
        """
        self.name = name  # атрибут
        self.hp = hp
        self.power = 1

    def __str__(self) -> str:
        return f"игрок {self.name}, жизни: {self.hp}"
    
    def attack(self, enemy) -> None:
         enemy.hp -= self.power
            print(self.name, "атаковал", self.name)
            print(enemy)



class Game:
    def __init__(self) -> None:
        self.player = Player("Вася", 100)
        self.enemy = Player("Дальнобойщик", 99)
        self.fight()

    def fight(self) -> None:
        while True:
            self.player.attack(self.enemy)
            print(self.player)
            self.enemy.attack(self.player)
            print(self.enemy)
            # таду: завершать бой и определять победителя           
            #фихс ми: ошибка отступа в 27 строке

        print("бой окончен!")

Game()
