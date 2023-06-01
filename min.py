class Animal:
    animal_type = "mammal"
    counter = 0
    def __init__(self, name):
        self.name = name
        Animal.counter += 1

animal_one = Animal('rat')
animal_two = Animal('cat')

print(animal_one.animal_type)
print(animal_two.animal_type)

print(Animal.counter)

#instance method, class method, static methods 