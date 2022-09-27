pizzas = ['pepperoni', 'chicken', 'vegetarian']
friend_pizzas = pizzas[:]
friend_pizzas.append('beef')

print("my favourite pizzas are:")
for i in pizzas:
    print(i)

print("my friend's favorite pizzas are:")
for i in friend_pizzas:
    print(i)