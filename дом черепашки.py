import turtle


def draw_house(
    x=0,
    y=0,
    base_w=100, 
    base_h=60,
    base_color="grey", 
    walls_w=100,
    walls_h=60, 
    walls_color="blue", 
    roof_w=100, 
    roof_h=30, 
    roof_color="black"
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
    draw_walls()
    draw_roof()


def draw_base(x, y, width, height, color):
    """ рисует фундамент"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_walls():
    """рисует стены"""
    print("рисуем стены")


def draw_roof():
    """рисует крышу"""
    print("рисуем крышу")

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


draw_house(x=100, y=100,base_w=100, base_h=20, roof_color="green")

turtle.done()
