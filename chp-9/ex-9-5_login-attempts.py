class User:
    def __init__(self, first_name, last_name, age, gender):
        """Shows attributes of the user"""
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.gender = gender

        self.login_attempts = 0
    def describe_user(self):
        """Summary of user's information"""
        print(f"\nHi i'm {self.firstname} {self.lastname}")
        print(f"I'm {self.gender}, and {self.age} years of age")
    def greet_user(self):
        """Personalized greeting"""
        print(f"Welcome {self.firstname} {self.lastname}")
    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1"""
        self.login_attempts +=1
    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0"""
        self.login_attempts = 0
user = User('James', 'Daniel', '28', 'male')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
