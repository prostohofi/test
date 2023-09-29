name = "Андрей Благородный"

way_1 = False
way_2 = False
way_3 = False

while way_1 == False or way_2 == False or way_3 ==False:

    print (name, "приехал к табличке а на ней написано")
    print ("направо пойдёшь богатым будешь")
    print ("налево пойдёшь женатым будешь")
    print ("напрямо пойдёшь убитым будешь")

    way = input (" в какую сторону ехать? ")

    if way == "налево":
        if way_1 == False:
            print(name, "попал на дорогу с разбойниками")
            print("убить разбойников или стать разбойником")
            choice = input (" что же мне сделать? ")
            if choice == "убить разбойников":
                print("разбойники убиты")
                way_1 = True
            elif choice == "стать разбойником":
                print("Андрей Благородный стал разбойником")
                break
        else:
            print(name,"ты уже был на этой дороге")

    elif way == "прямо":
        if way_2 == False:
            print(name, "попал на дорогу с жёнами")
            print("заподозрить или нет?")
            way_2 = True
        else:
            print (name,"ты уже был на этой дороге")

    elif way == "направо":
        if way_3 == False:
            print(name, "богат")
            way_3 = True
        else:
            print (name,"ты уже был на этой дороге")
    else:
        print("нет такой дороги")

print("сказка конец")
