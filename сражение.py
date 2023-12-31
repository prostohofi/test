from random import randint

player_name = "Вася Питонов"
player_hp = 10
player_level = 1
player_xp = 0  # опыт
player_money = 100

while True: # главный цикл игры
    # фиксми: убитый персонаж не должен делать выбор
    print("1 - сразаться с разбойником")
    print("2 - поехать в таверну")
    print("3 - поехать в магазин")
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
    elif option == "2": # таверна
        enemy_name = "Дальнобойщик"
        while True:
            print(player_name, "приехал в таверну")
            print("1 - Сыграть с дальнобойщиком в кости")
            print("0 - Уйти")
            option = int(input ("Введите номер варианта и нажмите ENTER: "))
            if option == 1:#игра в кости
                if player_money <= 0:
                    print("У", player_name, "нет денег")
                    continue
                print("У", player_name, player_money, "монет")
                bet = int(input("Сколько поставить на кон?" ))
                if bet <= 0:
                    print("Ставка должна быть больше 0")
                    continue
                if bet > player_money:
                    print("У", player_name, "нет столько монет")
                player_score = randint(2, 12)
                enemy_score = randint(2, 12)
                print(player_name, "выбросил", player_score)
                print(enemy_name, "выбросил", enemy_score)
                if player_score > enemy_score:
                    player_money += bet
                    print(player_name, "победил и забирает", bet, "монет")
                elif player_score < enemy_score:
                    player_money -= bet
                    print(player_name, "проиграл", bet, "монет")
                else:
                        print("Ничья")
            elif option == 0: #выход
                print(player_name, "уехал из таверны")
                break
            else: #ошибка ввода
                    print("Ошибка! Нет такого варианта!")

    elif option == "3":#магазин
        cashier_name = "Тётя Валя"
        shelf = 0
        while True:
            print(player_name, "приехал в магазин")
            print("1 - зелья")
            print("2 - оружия")
            print("0 - уйти")
            option = int(input ("Введите номер варианта и нажмите ENTER: "))
            if  shelf == 1 #зелья
                print("есть в асартименте: зелья здоровья,зелелья защиты,зелья невидимости.")
                if player_money <= 0:
                    print("У", player_name, "нет денег")
                    continue
                print("У", player_name, player_money, "монет")
      
    elif option == "0": #выход
        print(player_name, "уехал в закат")
        break
    
print("игра окончена")
