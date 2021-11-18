class Dog:
    def __init__(self, breed: str):
        self.breed = breed
        self.age = 0
        self.mass = 1
        print(f"Object ID={id(self)} has been created")

    def __del__(self):
        print(f"Object ID={id(self)} has been deleted")

    def about(self):
        print(f"Hello, I am {self.age} years old and I weigh {self.mass}.")
        print(f"My breed is: {self.breed}")

    def update_age(self, new_age: int):
        data_type = type(new_age)
        if data_type is int:
            self.age = new_age
        else:
            print(f"Sorry, bad type of data: {data_type} for 'age' property.")


kunegunda = Dog("Ratonero")
bethoven = Dog("Hovawart")
print("--------------------------")

print("Properties of kunegunda")
print(dir(kunegunda))
print("--------------------------")
print("Properties of bethoven")
print(dir(bethoven))
print("--------------------------")

kunegunda.age = "Bad_age"
kunegunda.mass = 5
kunegunda.about()
print("--------------------------")

bethoven.update_age("Bad_age")
bethoven.update_age(3)
bethoven.about()
print("--------------------------")

# przykład wykonania
# Object ID=139905408284464 has been created
# Object ID=139905408285760 has been created
# --------------------------
# Properties of kunegunda
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'about', 'age', 'breed', 'mass', 'update_age']
# --------------------------
# Properties of bethoven
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'about', 'age', 'breed', 'mass', 'update_age']
# --------------------------
# Hello, I am Bad_age years old and I weigh 5.
# My breed is: Ratonero
# --------------------------
# Sorry, bad type of data: <class 'str'> for 'age' property.
# Hello, I am 3 years old and I weigh 1.
# My breed is: Hovawart
# --------------------------
# Object ID=139905408284464 has been deleted
# Object ID=139905408285760 has been deleted
