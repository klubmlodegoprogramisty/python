from math import radians, sin, cos
from random import randint, random


steps_count = 15
r_vector = random()
brown_X = [0]
brown_Y = [0]

for step in range(1, steps_count):
    fi = radians(randint(0, 360))
    old_x = brown_X[step - 1]
    nowe_x = old_x + (r_vector * cos(fi))
    old_y = brown_Y[step - 1]
    nowe_y = old_y + (r_vector * sin(fi))
    brown_X.append(nowe_x)
    brown_Y.append(nowe_y)

print(f"Brown_X => {brown_X}")
print(f"Brown_Y => {brown_Y}")
