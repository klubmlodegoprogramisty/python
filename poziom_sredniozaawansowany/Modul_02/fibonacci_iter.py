fibonacci = [0, 1]
print(f"Initial list: {fibonacci}.")
value = 0
while value < 200:
    value = sum(fibonacci[-2:])
    fibonacci.append(value)
    print(f" Actual list: {fibonacci}.")

# efekt wykonania:
# Initial list: [0, 1].
#  Actual list: [0, 1, 1].
#  Actual list: [0, 1, 1, 2].
#  Actual list: [0, 1, 1, 2, 3].
#  Actual list: [0, 1, 1, 2, 3, 5].
#  Actual list: [0, 1, 1, 2, 3, 5, 8].
#  Actual list: [0, 1, 1, 2, 3, 5, 8, 13].
#  Actual list: [0, 1, 1, 2, 3, 5, 8, 13, 21].
#  Actual list: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].
#  Actual list: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55].
#  Actual list: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#  Actual list: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144].
#  Actual list: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233].
