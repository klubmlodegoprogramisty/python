from math import radians, sin, cos
from random import randint, random
import matplotlib.pyplot as plt


steps_count = 45
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

way_X = [brown_X[0]] + brown_X[-1:]
way_Y = [brown_Y[0]] + brown_Y[-1:]

plt.plot(brown_X, brown_Y, color="red")
plt.plot(way_X, way_Y, "o:", color="green", linewidth=2)
plt.title(
    f"Ruchy Browna dla {steps_count} kroków, współrzędne początkowe: {way_X[0]},{way_Y[0]}; współrzędne końcowe: {way_X[1]},{way_Y[1]}"
)
plt.grid()
plt.show()
