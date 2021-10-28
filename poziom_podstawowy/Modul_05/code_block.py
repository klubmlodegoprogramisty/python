# skrypt z instrukcjami warunkowymi i blokami kodu

actual_year = 2021

print("Hi, we'll try to compute your age ;-)")
name = input("Please tell me your name:")
birth = input(f"OK {name} - at what year have you birth?")
birth = int(birth)
age = actual_year - birth

if age >= 18:
    print(f"Oh, I see, {name} - you are an adult now.")
    print(f"You are {age} years old.")
else:
    print(f"You are young - {age} years old.")


if name.endswith("a"):
    print(f"I guess {name} - you are a woman.")
    if name.lower() == "barnaba":
        print(f"But your name: {name} is an exception - you are a man!")
else:
    print("You probably are a man...")

print("That is all - see you next time!")
