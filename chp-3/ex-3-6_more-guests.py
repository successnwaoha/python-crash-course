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