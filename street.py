#Фихс ми:рисуется крыша левее того чего надо
import turtle
from random import randint

turtle.speed(0)
turtle.colormode(255)

def draw_house(
    x=0,
    y=0,
    base_w=100, 
    base_h=60,
    base_color="grey", 
    walls_w=100,
    walls_h=60, 
    walls_color="orange", 
    roof_w=0, 
    roof_h=0, 
    roof_color="yellow"
):
    """
    + вызывает функции рисования фундамента
    вызывает функции рисования стен
    вызывает функции рисования крыши

    x - левый нижний угол фундамента
    y - левый нижний угол фундамента

    base_w - ширина фундамента 
    base_h - высота фундамента 
    base_color - цвет фундамента

    walls_w - ширина стен 
    walls_h - высота стен
    walls_color - цвет стен

    roof_w - ширина крыши
    roof_h - высота крыши
    roof_color - цвет крыши
    """
    print("начинаем строить дом")
    draw_base(x, y, base_w, base_h, base_color)
    draw_walls(x, y, walls_w, walls_h, walls_color, base_h)
    draw_roof(x, y, roof_color, base_h, walls_h, walls_w, roof_w, roof_h)


def draw_base(x, y, width, height, color):
    """ рисует фундамент"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_walls(x, y, width, height, color, base_height):
    """рисует стены"""
    turtle.penup()
    turtle.goto(x, y + base_height)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_roof(x, y, roof_color, base_h, walls_h, walls_w, roof_w, roof_h):
    """рисует крышу"""
    turtle.goto(x, y + walls_h + base_h) #левый верхний угол стены
    turtle.fd(walls_w // 2)
    turtle.fd(roof_w // 2)


    turtle.goto(x - roof_w // 2, roof_h)
    


def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()


def draw_street(x, y, houses):
    counter = 0
    while counter <= houses:
        base_w = randint(30, 70)
        base_h = base_w * 0.1
        base_color =(randint(0, 255), randint(0, 255), randint(0, 255))

        walls_color =(randint(0, 255), randint(0, 255), randint(0, 255))
        walls_w = randint(int(base_w * 0.9), base_w)
        walls_h = randint(walls_w, walls_w * 2)

        roof_w = randint(walls_w, int(walls_w * 1.2))
        roof_h = randint(roof_w, int(roof_w * 1.5))
        draw_house(x=x, y=y, base_w=base_w, walls_w=walls_w, roof_w=roof_w, base_color=base_color, base_h=base_h, walls_h=walls_h, walls_color=walls_color, roof_h=roof_h)
        counter += 1
        x += roof_w + base_w

draw_street(-200, 0, 5)

turtle.done()
