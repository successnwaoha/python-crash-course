"""For importing to ex-9-12_multiple_modules"""

from User import User

class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges
        self.privileges = Privileges()

class Privileges:
    def __init__(self, privileges=[]):
        """stores a list of strings"""
        self.privileges = privileges
    def show_privileges(self):
        """lists the administrator's set of privileges"""
        print("\nPrivileges")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This user has no privileges")