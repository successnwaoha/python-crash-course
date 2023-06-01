pizzas = ['pepperoni', 'chicken', 'vegetarian']
for pizza in pizzas:
    print("I love {} pizza".format(pizza))
print("I really love pizza")

friends_pizzas=pizzas[:]
pizzas.append("special")
friends_pizzas.append("beef")

print("My favorite pizzas are:")
for i in pizzas:
   print(i)

print("\nMy friend's favorite pizzas are:")
for i in friends_pizzas:
   print(i)