def fibonacci_iter(max_value):
    fibonacci = [0, 1]
    print(f"Initial list: {fibonacci}.")
    value = 0
    while value < max_value:
        value = sum(fibonacci[-2:])
        fibonacci.append(value)
        print(f" Actual list: {fibonacci}.")

def fibonacci_iter_items(max_count):
    fibonacci = [0, 1]
    print(f"Initial list: {fibonacci}.")
    items = 2
    while items < max_count:
        value = sum(fibonacci[-2:])
        fibonacci.append(value)
        print(f" Actual list: {fibonacci}.")
        items += 1

# tu musimy wykorzystać importowanie z plików:
# from fibonacci_iter_fun import *