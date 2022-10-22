class Dog:
    def __init__(self, name, age, breed, height):
        self.name = name
        self.age = age
        self.breed = breed
        self.height = height
dog1=Dog(
    "Ragnarok",
    3,
    "Doberman",
    120
)
print(dog1.name)
print(dog1.age)
print(dog1.breed)
print(dog1.height)
