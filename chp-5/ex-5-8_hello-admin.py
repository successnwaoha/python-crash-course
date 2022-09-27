usernames = ['dumaga','admin','parem','bonet','faith']
if usernames:
    for i in usernames:
        if i == 'admin':
            print("Hello {}, would you like to see a status report".format(i))
        else:
            print("hello {}, thank you for logging in".format(i))