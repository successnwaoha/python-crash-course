people = ['dumaga','gabriel','parem']
print(f"{people[0]}, you are invited to my party")
print(f"{people[1]}, you are invited to my party")
print(f"{people[2]}, you are invited to my party")

print(f"{people[1]}, cant make it to the party")
people[1] = 'solomon'
print (people)

print("Sorry everyone i just found a bigger dinner table")
people.insert(0, 'joshua')
people.insert(2, 'daniel')
people.append('samuel')
print(people)

popped_person = people.pop(5)
print("{}, im so sorry i couldnt invite you please bear with me".format(popped_person))
print(people)

popped_person = people.pop(0)
print("{}, im so sorry i couldnt invite you please bear with me".format(popped_person))
print(people)

popped_person = people.pop(1)
print("{}, im so sorry i couldnt invite you please bear with me".format(popped_person))
print(people)

popped_person = people.pop(1)
print("{}, im so sorry i couldnt invite you please bear with me".format(popped_person))
print(people)

print("{}, This is just to let you know that your still invited".format(people[0]))
print("{}, This is just to let you know that your still invited".format(people[1]))

del people[0]
del people[0]
print(people)