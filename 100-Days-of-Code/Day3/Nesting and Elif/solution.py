print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 15:
        print("You have to pay $10.")
    elif age <= 7:
        print("You have to pay $7.")
    else:
        print("You have to pay $15")
else:
    print("Your height should be 120 cm or above.")