from sys import exit
from turtle import *

max_value = 400
max_sum = (2 * max_value) + 10
y_level = -300
x_position = -300

value_1 = int(input(f"Please give me fist number (max {max_value}): "))
value_2 = int(input(f"Please give me second number (max {max_value}): "))

if value_1 > max_value or value_2 > max_value:
    print(f"Too high values - {max_value} maximum!")
    exit(2)

if value_1 + value_2 > max_sum:
    print(f"Sum of values too high - {max_sum} maximum!")
    exit(2)

# tryb standardowy okna żółwia
mode("standard")
# prędkość rysowania: slowest, slow, normal, fast, fastest
speed("slow")
# tytuł okna
title("Euklides animation")
# ukrywamy znacznik żółwia
hideturtle()


def rectangle(start_x, value_1, value_2, colors):
    # value_1
    penup()
    goto(start_x, y_level)
    pendown()
    color(colors[0])
    begin_fill()
    for _ in range(2):
        forward(5)
        left(90)
        forward(value_1)
        left(90)
    end_fill()

    # value_2
    penup()
    goto(start_x, y_level + value_1 + 5)
    pendown()
    color(colors[1])
    begin_fill()
    for _ in range(2):
        forward(5)
        left(90)
        forward(value_2)
        left(90)
    end_fill()

    return start_x + 10


while value_1 != value_2:
    if value_1 > value_2:
        x_position = rectangle(x_position, value_1, value_2, ["red", "blue"])
        value_1 -= value_2
    else:
        x_position = rectangle(x_position, value_2, value_1, ["blue", "red"])
        value_2 -= value_1

print("Click on graphics to exit.")
print(f"Euklides result is: {min([value_1, value_2])}")
# zatrzymujemy obraz na ekranie do kliknięcia myszą
exitonclick()
