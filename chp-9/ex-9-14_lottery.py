from random import choice
possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winning_ticket = []
while len(winning_ticket)<4:
    pulled_item= choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f"we pulled a {pulled_item}")
        winning_ticket.append(pulled_item)

print(f"The final winning ticket is: {winning_ticket}")