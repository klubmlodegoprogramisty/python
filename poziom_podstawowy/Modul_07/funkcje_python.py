# przykłady definiowania i wywoływania funkcji w Python

def just_print():
    print("Just printing some text.")

def just_return():
    return "Just returning some text"

def parameter_print(some_value):
    print(f"You pass value: {some_value}")

def parameter_return(some_value):
    return f"You pass value: {some_value}"

def more_parameters(first, second):
    print(f"First parameter: {first}")
    print(f"Second parameter: {second}")

def quadrat_area(side_length):
    return side_length * side_length

# przykłady wywołania w trybie REPL - zwracamy uwagę na funkcje zwracające wartość
# >>> just_print()
# Just printing some text.
# >>> just_return()
# 'Just returning some text'
# >>> parameter_print(1234)
# You pass value: 1234
# >>> parameter_return("Something")
# 'You pass value: Something'
# >>> more_parameters(123, "Some value")
# First parameter: 123
# Second parameter: Some value
# >>> quadrat_area(10)
# 100

# funkcja wywołana bez nawiasów nie uruchamia się
# >>> just_print
# <function just_print at 0x7fa340ab89d0>

# dla chętnych
def parameters_return(first, second):
    return first, second

# przykłady wywołania w trybie REPL - dziwnie wyglądające zwrócone dane to typ Tuple
# https://docs.python.org/3/library/stdtypes.html#tuples
# >>> parameters_return(123, "Some value")
# (123, 'Some value')
