name = "Андрей Благородний"

way_1 = False
way_2 = False
way_3 = False

while way_1 == False or way_2 == False or way_3 ==False:

    print (name, "приехал к табличке а на ней написано")
    print ("направо пойдёшь богатым будешь")
    print ("налево пойдёшь женатым будешь")
    print ("напрямо пойдёшь убитым будешь")

    way = input ("в какую сторону ехать?")

    if way == "налево":
        if way_1 == False:
            print(name, "убит")
            way_1 = True
        else:
            print(name,"ты уже был на этой дороге")
    elif way == "прямо":
        if way_2 == False:
            print(name, "женат")
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
