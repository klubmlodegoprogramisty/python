from sys import exit
from turtle import *

MAX_VALUE = 400
MAX_SUM = (2 * MAX_VALUE) + 10
Y_LEVEL = -300
x_position = -300


def rectangle(start_x, value_1, value_2, colors):
    # value_1
    penup()
    goto(start_x, Y_LEVEL)
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
    goto(start_x, Y_LEVEL + value_1 + 5)
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


value_1 = int(input(f"Please give me first number (max {MAX_VALUE}): "))
value_2 = int(input(f"Please give me second number (max {MAX_VALUE}): "))

if value_1 > MAX_VALUE or value_2 > MAX_VALUE:
    print(f"Too high values - {MAX_VALUE} maximum!")
    exit(2)

if value_1 + value_2 > MAX_SUM:
    print(f"Sum of values too high - {MAX_SUM} maximum!")
    exit(2)

# tryb standardowy okna żółwia
mode("standard")
# prędkość rysowania: slowest, slow, normal, fast, fastest
speed("slow")
# tytuł okna
title("Euklides animation")
# ukrywamy znacznik żółwia
hideturtle()


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
