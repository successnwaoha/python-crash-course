while True:
    p = int(input())
    if p <= 3:
        print("Your ticket is free, Enjoy")
        break
    elif p > 3 and p <= 12:
        print("Your ticket is $10")
        break
    else:
        print("Your ticket is $15")
        break