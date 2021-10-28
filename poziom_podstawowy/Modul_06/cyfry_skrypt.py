print("Hi, i will check all singns in value.")
some_value = input("Please enter value (as integer):")
signs_list = []

for one_sign in some_value:
    signs_list.append(one_sign)

print(f"Total list is: {signs_list}")

# dla chętnych
for one_sign in some_value:
    print(f"{one_sign} => {int(one_sign) * '@'}")

# efekt przykładowego działania
# Hi, i will check all singns in value.
# Please enter value (as integer):6248531
# Total list is: ['6', '2', '4', '8', '5', '3', '1']
# 6 => @@@@@@
# 2 => @@
# 4 => @@@@
# 8 => @@@@@@@@
# 5 => @@@@@
# 3 => @@@
# 1 => @
