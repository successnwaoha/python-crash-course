class User:
    def __init__(self, first_name, last_name, age, gender):
        """Shows attributes of the user"""
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.gender = gender
    def describe_user(self):
        """Summary of user's information"""
        print(f"\nHi i'm {self.firstname} {self.lastname}")
        print(f"I'm {self.gender}, and {self.age} years of age")
    def greet_user(self):
        """Personalized greeting"""
        print(f"Welcome {self.firstname} {self.lastname}")
first_user = User('James', 'Daniel', '28', 'male')
first_user.describe_user()
first_user.greet_user()

second_user = User('Alex', 'Williams', '28', 'female')
second_user.describe_user()
second_user.greet_user()

last_user = User('John', 'David', '34', 'male')
last_user.describe_user()
last_user.greet_user()