print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
junk_food_bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")

    junk_food = input("You want to buy junk food? Yes or NO ")

    if junk_food == "Yes":
        junk_food_bill += 10
    print(f"Your final bill is ${junk_food_bill}")

else:
    print("Sorry you have to grow taller before you can ride.")