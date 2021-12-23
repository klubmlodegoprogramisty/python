# kody do wykonania w trybie REPL

import matplotlib.pyplot as plt

# tworzymy listy za pomocą „generatora listowego”
x = [ x for x in range(-50, 50) ]
y = [ z**3 + 1.03 for z in x ]
print(x)
print(y)

plt.ioff() # wyłączamy tryb interaktywny w Pycharm Python Console
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.ioff.html

plt.plot(x, y)
plt.grid(True)
plt.show()
