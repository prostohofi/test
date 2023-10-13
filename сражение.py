from random import randint

player_name = "Вася Питонов"
player_hp = 10
player_level = 1
player_xp = 0  # опыт
player_money = 100

while True: # главный цикл игры
    # фиксми: убитый персонаж не должен делать выбор
    print("1 - сразаться с разбойником")
    print("2 - сыграть к кости")
    print("0 - уйти")
    option = input("введите номер и нажмите ENTER:")

    if option == "1": #сражение

        enemy_name = "Ящер Подиков"
        enemy_hp = 10
        enemy_level = 1
        enemy_xp = 0
        enemy_money = 100

        print(player_name, "сражается с ", enemy_name)

        while  True:
            #ход игрока
            damage = randint(0, 10)
            enemy_hp -= damage
            print(player_name, "ударил", enemy_name, "на", damage, "жизней")
            print ("у", enemy_name, "осталось", enemy_hp, "жизней")
            if enemy_hp <= 0: # победа игрока
                print(player_name, "выиграл бой!")
                player_xp += enemy_xp
                print(player_name, "получил", enemy_xp, "опыта")
                if player_xp >= 10:
                    player_level += player_xp // 10
                    player_xp += enemy_xp % 10
                    print(player_name, "достиг", player_level, "уровня")
                break
            
            #ход противника
            damage = randint(0, 10)
            player_hp -= damage
            print(enemy_name, "ударил", player_name, "на", damage, "жизней")
            print ("у", player_name, "осталось", player_hp, "жизней")
            if enemy_hp <= 0:
                print (player_name, "проиграл бой :(")
                break

            print("---------------------")
    elif option == "2": # игра в кости
        if player_money > 0:
            print("играем")
            bet = int(input("сколько ставим:"))
            if bet > 0:
                print("вы поставили", bet)

                while True:
                    input("Нажмите ENTER чтобы сыграть")
                    player = randint(2, 12)
                    enemy = randint(2, 12)

                    print ("Вы выбросили", player)
                    print("Компьютер выбросил", enemy)
                    print("У вас", player_money)

                    if player > enemy:
                        print("Вы победили")
                        player_money += 1
                    elif player < enemy:
                        print("Компьютер победил")
                        player_money -= 1
                    else:
                        print("Ничья")

        else:
            print(" у вас нет денег")

    elif option == "0": #выход
        print(player_name, "уехал в закат")
        break
    
print("игра окончена")
