from math import sqrt
from read_data import read_from_file


def eratostenes(n: int) -> list:
    erastostenes_list = []
    temp_list = [0] + (n * [1])
    max_value = int(sqrt(n))
    for index in range(2, max_value + 1):
        if temp_list[index]:
            for index_2 in range(index * index, n + 1, index):
                temp_list[index_2] = 0

    for element in range(2, n + 1):
        if temp_list[element]:
            erastostenes_list.append(element)

    return erastostenes_list


prime_numbers = eratostenes(2000)

data = read_from_file("data_twins.txt")

for pair in data:
    value_1, value_2 = pair
    if value_1 not in prime_numbers or value_2 not in prime_numbers:
        continue
    if (
        value_1 in prime_numbers
        and value_2 in prime_numbers
        and abs(value_1 - value_2) == 2
    ):
        print(f"Found pair: {pair}")

# efekt działania
# Found pair: [3, 5]
# Found pair: [101, 103]
# Found pair: [149, 151]
# Found pair: [281, 283]
# Found pair: [461, 463]
# Found pair: [599, 601]
# Found pair: [659, 661]
# Found pair: [1019, 1021]
# Found pair: [1301, 1303]
# Found pair: [1151, 1153]
# Found pair: [1787, 1789]
# Found pair: [1931, 1933]
# Found pair: [1949, 1951]
