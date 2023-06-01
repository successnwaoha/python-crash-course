class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Shows two attributes of the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """Shows description of restaurant"""
        print(f"\nWelcome to {self.restaurant_name},what would you like to order")
        print(f"we have {self.cuisine_type} as a special on the menu today")
    def open_restaurant(self):
        """Prints a message saying the restaurant is open for business"""
        print(f"{self.restaurant_name} is open for business")
restaurant = Restaurant('Tastia', 'Shawarma')
restaurant.describe_restaurant()

second_restaurant = Restaurant("Domino's pizza", 'Vegetarian pizza')
second_restaurant.describe_restaurant()

third_restaurant = Restaurant('Kfc', 'Kfc drumsticks')
third_restaurant.describe_restaurant()