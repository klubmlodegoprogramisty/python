# przykładowy skrypt do wykonywania w trybie REPL
# każda linia pojedynczo
# wykazujemy błąd przy braku konwersji

value_float = 3.1415927

input_data = input("Please, give me some number:")
input_data
type(input_data)

new_value = input_data * value_float

# !! tutaj wystąpi błąd
# Traceback (most recent call last):
#   File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
#     exec(code, self.locals)
#   File "<pyshell#4>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'float'

# poprawne wykonanie
input_data = float(input_data)
input_data
type(input_data)
new_value = input_data * value_float
new_value
type(new_value)
