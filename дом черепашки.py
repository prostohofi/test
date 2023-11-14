#Фихс ми:рисуется крыша левее того чего надо
import turtle

turtle.speed(0)


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
    turtle.goto(x, y + walls_h + base_h)
    turtle.fd(walls_w)

    print(roof_w)
    
    turtle.goto(roof_w // 2, roof_h + walls_h + base_h + x - walls_h // 2 + y)
 


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


draw_house(x=100, y=100, base_w=100, base_h=20, roof_color="green", walls_w= 100, roof_w= 200)

turtle.done()
