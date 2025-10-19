# strip() will extra spaces from the input function (from 1st and from last it will remove space)

age= int(input("Enter your age\n").strip())

if age >=21:
    print("Yes, Can go Club")
else:
    print("No,Can't go club")