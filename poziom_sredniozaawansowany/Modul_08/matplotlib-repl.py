# kody do wykonania w trybie REPL

import matplotlib.pyplot as plt

x = [ x for x in range(-50, 50) ]
y = [ z**3 + 1.03 for z in x ]
print(x)
print(y)
plt.plot(x, y)
plt.grid(True)
plt.show()
