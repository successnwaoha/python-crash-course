def get_formatted_name(firt_name, last_name):
    full_name = f"{firt_name} {last_name}"
    return full_name
while True:
    print("Please tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formated_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formated_name}!")