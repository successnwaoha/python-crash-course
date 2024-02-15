from admin import Admin

success = Admin('success', 'Nwaoha', '17', 'Nigerian')
success.describe_user()

success_privileges = [
    'can reset password', 
    'can edit profile', 
    'can suspend accounts'
    ]
success.privileges.privileges = success_privileges
print(f"The admin {success.firstname} has 3 privileges: ")
success.privileges.show_privileges()