def nwd_odejmowanie(x, y):
	while x != y:
		if x > y:
			x -= y
		else:
			y -= x

	return x

# przykład wywołania:
# nwd_odejmowanie(23849876, 34)
