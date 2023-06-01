people = ['dumaga','gabriel','faith']
print(f"{people[0]}, you are invited to my party")
print(f"{people[1]}, you are invited to my party")
print(f"{people[2]}, you are invited to my party")

print("Hi everyone, so i just found a bigger dinner table and i thought to invite more people")
people.insert(0, 'blessing')
people.insert(2, 'daniel')
people.append('emmanuella')
print(people)
print(f"{people[0]}, you are invited to my party")
print(f"{people[1]}, you are invited to my party")
print(f"{people[2]}, you are invited to my party")
print(f"{people[3]}, you are invited to my party")
print(f"{people[4]}, you are invited to my party")
print(f"{people[5]}, you are invited to my party")

print("Sorry due to some issues with the new dinner table, i can only invite two people to the dinner party")

popped_person = people.pop(5)
print("{}, i'm so sorry i could'nt invite you please it's not my fault".format(popped_person))
print(people)

popped_person = people.pop(0)
print("{}, i'm so sorry i could'nt invite you please it's not my fault".format(popped_person))
print(people)

popped_person = people.pop(1)
print("{}, i'm so sorry i could'nt invite you please it's not my fault".format(popped_person))
print(people)

popped_person = people.pop(1)
print("{}, i'm so sorry i could'nt invite you please it's not my fault".format(popped_person))
print(people)

print("{}, This is just to let you know that you're still invited".format(people[0]))
print("{}, This is just to let you know that you're still invited".format(people[0]))

del people[0]
del people[0]
print(people)