"""This file is for all import exercises in this chapter"""
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings: 
        print(f"- {topping}")
make_pizza('12', 'pepperoni')