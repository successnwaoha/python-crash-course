current_users = ['dumaga','gabriel','parem','bonet','faith','precious', 'princess']
new_users = ['dumaga', 'daniel', 'solomon', 'lydia', 'bonet', 'esther']
for i in new_users:
    if i in current_users:
        print("Sorry username taken")
    else:
        print("This username is available")