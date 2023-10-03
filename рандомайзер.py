import random

money = 100

while True:
        input("Нажмите ENTER чтобы сыграть")
        player = random.randint(2, 12)
        computer = random.randint(2, 12)

        print ("Вы выбросили", player)
        print("Компьютер выбросил", computer)
        print("У вас", money)

        if player > computer:
            print("Вы победили")
            money += 1
        elif player < computer:
            print("Компьютер победил")
            money -= 1
        else:
            print("Ничья")
    
