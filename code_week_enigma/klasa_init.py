class Klasa:
    def __init__(self, parameter):
        self.property = parameter

    def method(self):
        print("Property value is:", self.property)


print(" ")
some_object = Klasa("test")
print(type(some_object))
some_object.method()
print(type(some_object.property))

print("---------------------------")
other_object = Klasa(234)
print(type(other_object))
other_object.method()
print(type(other_object.property))
