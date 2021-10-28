from read_data import read_from_file


def dividers(value: int) -> list:
    dividers_list = []
    if value:
        for i in range(1, value // 2 + 1):
            if value % i == 0:
                dividers_list.append(i)

    return dividers_list


def friendly(pair: list) -> bool:
    a, b = pair
    return sum(dividers(a)) == b and sum(dividers(b)) == a


data = read_from_file("data_friendly.txt")

for pair in data:
    if friendly(pair):
        print(f"Pair: {pair} - friendly numbers.")


# efekt:
# Pair: [635624, 712216] - friendly numbers.
# Pair: [356408, 399592] - friendly numbers.
# Pair: [122368, 123152] - friendly numbers.
# Pair: [141664, 153176] - friendly numbers.
# Pair: [142310, 168730] - friendly numbers.
# Pair: [176272, 180848] - friendly numbers.
