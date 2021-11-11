def nwd_modulo(x, y):
    while y > 0:
        modulo = x % y
        x = y
        y = modulo

    return x

# przykład wywołania:
nwd_modulo(23849876, 34)
