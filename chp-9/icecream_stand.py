"""This is ex-9-6_ice-cream-stand, name changed due to importing issues"""

"""A class to represent a restaurant"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Shows two attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """Shows description of restaurant"""
        print(f"Welcome to {self.restaurant_name},what would you like to order")
        print(f"we have {self.cuisine_type} as a special on the menu today")
    def open_restaurant(self):
        """Prints a message saying the restaurant is open for business"""
        print(f"{self.restaurant_name} is open for business")
restaurant = Restaurant('Tastia', 'Shawarma')
print(f"Our restaurant is called {restaurant.restaurant_name}")
print(f"\nToday we have {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,):
        super().__init__(restaurant_name, cuisine_type)
        flavors=['vanilla', 'strawberry', 'banana', 'chocolate']
        self.flavors = flavors
    def display_flavors(self):
        """Displays ice cream flavors"""
        print(f"Welcome, we have: {self.flavors} available today")
iceCreamStand = IceCreamStand('Tastia', 'Shawarma')
iceCreamStand.display_flavors()