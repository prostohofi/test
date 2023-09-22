x = int (input ("Введите икс"))
y = int (input ("Введите игрек"))

if x > 0:
    print("правая")
elif x < 0:
    print("левая")
if y > 0:
    print("верхняя")
elif y < 0:
    print("нижняя")
if x == 0 and y == 0:
    print("центр")

