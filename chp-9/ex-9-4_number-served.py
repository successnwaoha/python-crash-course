class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Shows two attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        self.number_served = 0
    def describe_restaurant(self):
        """Shows description of restaurant"""
        print(f"Welcome to {self.restaurant_name},what would you like to order")
        print(f"we have {self.cuisine_type} as a special on the menu today")
    def open_restaurant(self):
        """Prints a message saying the restaurant is open for business"""
        print(f"{self.restaurant_name} is open for business")
    def set_number_served(self, number):
        """Set the number of customers served"""
        self.number_served = number
        print(f"This restaurant has served {self.number_served} people today")
    def increment_number_served(self, increase):
        """Increment the number of customers served"""
        self.number_served += increase
restaurant = Restaurant('Tastia', 'Shawarma')
print(f"This restaurant has served {restaurant.number_served} people today")
restaurant.number_served = 9
print(f"This restaurant has served {restaurant.number_served} people today")
restaurant.set_number_served(20)
restaurant.set_number_served(34)
restaurant.increment_number_served(20)
print(f"This restaurant has served {restaurant.number_served} people today")

