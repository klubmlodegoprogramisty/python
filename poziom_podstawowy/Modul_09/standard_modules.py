# przykładowy skrypt do wykonywania w trybie REPL
# każda linia pojedynczo

import math
# używamy konwencji f-string do wyświetlania (wprowadzona w lekcji 3)
print(f"Pi value is: {math.pi}") # wartość π
print(f"Square root from 4 is: {math.sqrt(4)}") # √4
print(f"E value is: {math.e}") # wartość e

from math import pi, sqrt
print(f"Pi value is: {pi}")
print(f"Square root from 4 is: {sqrt(4)}")

# to będzie błąd
print(f"E value is: {e}")

# efekt w IDLE:
# >>> print(f"E value is: {e}")
# Traceback (most recent call last):
#  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
#    exec(code, self.locals)
#  File "<pyshell#2>", line 1, in <module>
# NameError: name 'e' is not defined
