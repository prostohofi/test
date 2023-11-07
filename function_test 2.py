import turtle

turtle.shape("turtle")
turtle.speed(10)

def draw_square(side_length, line_color):
    turtle.pencolor(line_color)
    counter = 0
    while counter <= 3:
        turtle.right(90)
        turtle.fd(side_length)
        counter += 1


side_lenght = 100
line_color = 
while side_lenght < 300:
    draw_square(side_lenght, line_color)
    side_lenght += 10

draw_square(100, "red")
draw_square(120, "blue")

turtle.fd(1)
turtle.done()