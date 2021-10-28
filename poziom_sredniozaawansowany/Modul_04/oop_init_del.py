class Dog:
    def __init__(self, breed: str):
        self.breed = breed
        self.age = 0
        self.mass = 1
        print(f"Object ID={id(self)} has been created")

    def __del__(self):
        print(f"Object ID={id(self)} has been deleted")


kunegunda = Dog("Ratonero")
bethoven = Dog("Howawart")

print("Properties of kunegunda")
print(dir(kunegunda))
print("--------------------------")
print("Properties of bethoven")
print(dir(bethoven))

# efekt działania
# Properties of kunegunda
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'breed', 'mass']
# --------------------------
# Properties of bethoven
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'breed', 'mass']
# Object ID=140361889154864 has been deleted
# Object ID=140361889210224 has been deleted
