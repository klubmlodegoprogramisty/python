some_elements = ["A", "B", "C", 22, 10, 30]

some_elements.append("X")
some_elements.append(11)

for element in some_elements:
    print(element, end=" / ")


# efekt
# A / B / C / 22 / 10 / 30 / X / 11 /
