from icecream_stand import Restaurant

restaurant = Restaurant('Tastia', 'Shawarma')
print(f"Our restaurant is called {restaurant.restaurant_name}")
print(f"\nToday we have {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()