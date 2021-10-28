from read_data import read_from_file


def check_longest(sequence: list) -> list:
    """sequence: list of int"""
    length = len(sequence)
    longest = []
    increment = []

    for index in range(length - 1):
        increment.append(sequence[index])
        if sequence[index + 1] < sequence[index]:
            if len(increment) > len(longest):
                longest = increment[:]  # dlaczego tak?
            increment = []
    return longest[:]


data = read_from_file("data_consistent.txt")

tmp_sequence = None
longest_counter = 0
longest_sequence = None
longest_line = 0


for index, values_sequence in enumerate(data):
    tmp_sequence = check_longest(values_sequence)
    tmp_length = len(tmp_sequence)
    if tmp_length > longest_counter:
        longest_sequence = tmp_sequence[:]
        longest_counter = tmp_length
        longest_line = index


print(f"The longest non-decreasing sequence has {longest_counter} entries - {longest_sequence}.")
print(f"It is in line nr {longest_line}: {data[longest_line]}")

# efekt działania
# The longest non-decreasing sequence has 7 entries - [1, 3, 10, 10, 15, 22, 28].
# It is in line nr 267: [15, 15, 22, 13, 1, 3, 10, 10, 15, 22, 28, 18, 8, 24, 6]
