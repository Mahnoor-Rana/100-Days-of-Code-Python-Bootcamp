# Task 1:
print("Hello, world! Welcome to Python programming. Let's start our journey with some fun coding!")

# Task 2:
# 1. New Line Escape Sequence
# Learn to use `\n` to add a new line within a single string.

print("Hello\nWorld")

# 2. String Concatenation
# Use the plus symbol `+` to concatenate different strings together.

print("My name is" + " " + "Mahnoor")

# Task 3:
# Prompt the user for their name and print a personalized greeting.
print("Hello " + input("What is your name?") + "!")

# Task 4:
# Store user input in a variable and print the length of that input.
username = input("What is your name?")
length = len(username)
print("The length of your name is:", length)

# Task 5:
# Demonstrate good variable naming and length calculation.
name = "Mahnoor"
length = len(name)
print("The length of the name 'Mahnoor' is:", length)

# Task 6:
# Band Name Generator
print("Welcome to the Band Name Generator.")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of a pet?\n")
print("Your band name could be " + city + " " + pet)