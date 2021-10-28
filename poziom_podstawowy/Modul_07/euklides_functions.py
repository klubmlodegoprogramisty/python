def nwd_modulo(x, y):
	while y > 0:
		modulo = x % y
		x = y
		y = modulo

	return x


print("Hello, I will compute Euklides")
value_1 = int(input("Please give me fist number: "))
value_2 = int(input("Please give me second number: "))

nwd = nwd_modulo(value_1, value_2)

print(f"Computed value is {nwd}")
