sandwich_orders = ['burger', 'tuna sandwich', 'vegetarian']
finished_sandwiches = []
while sandwich_orders:
    ready = sandwich_orders.pop()
    print(f"i made you {ready}")
    finished_sandwiches.append(ready)
print(finished_sandwiches)