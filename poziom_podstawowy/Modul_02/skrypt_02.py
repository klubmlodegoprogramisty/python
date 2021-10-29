print("To jest pierwsza linia.")

# komentarz - nic nie wnosi, poza informacjami
# definiujemy zmienne różnego typu

language = "Python"     # str 	- ciąg znaków
year_of_birth = 1991    # int  	- liczby całkowite
version = 3.8           # float	- liczby ułamkowe
is_cool = True          # bool 	- wartości logiczne

print("Computer language named:", language, end=" ")
print("was born in", year_of_birth, end=". ")
print("Now we use version", version, sep=":", end=" - ")
print("it is cool, isn't it", is_cool, sep="?")

# dane dla obliczeń
a = 10.4
b = 44
r = 27
h = 8
pi = 3.1415927

rectangle_area = a * b
triangle_area = (a * h) / 2
circle_area = pi * r * r

print("Rectangle", end=" ")
print("Area:", rectangle_area)
print("Circle", end=" ")
print("Are:", circle_area)
print("Triangle", end=" ")
print("Area:", triangle_area)
