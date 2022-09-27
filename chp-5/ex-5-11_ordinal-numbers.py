c_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in c_nums:
    if i == 1:
        print(f"{i}st")
    if i == 2:
        print(f"{i}nd")
    if i == 3:
        print(f"{i}rd")
    if i == 4:
        print(f"{i}th")
    if i == 5:
        print(f"{i}th")
    if i == 6:
        print(f"{i}th")
    if i == 7:
        print(f"{i}th")
    if i == 8:
        print(f"{i}th")
    if i == 9:
        print(f"{i}th")

#OR

c_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in c_nums:
    if i == 1:
        print(f"{i}st")
    if i == 2:
        print(f"{i}nd")
    if i == 3:
        print(f"{i}rd")
    if i >= 4 or i == 9:
        print(f"{i}th")