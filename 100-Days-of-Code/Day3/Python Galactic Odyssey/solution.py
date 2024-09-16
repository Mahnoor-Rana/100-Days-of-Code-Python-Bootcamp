print('''
*******************************************************************************
               .        .    .        .         .      .
        .          .  .   .      .        .        .   .
    .    .  .     .  .      .  .   .    .       .       .
         .   .      .    .   .  .   .   .     .     .     .  .
 .   .   .  .     .      .  .   .      .   .       .       .
     .    .      .   .  .    .   .    .  .      .   .     .   .
     .   .  .   .    .  .      .      .     .  .    .       .   .
        .  .    .    .     .      .    .    .    .    .   .    .
   .  .   .     .     .   .   .   .    .   .   .      .  .  .
          .  .    .   .    .   .      .    .   .  .      .   .
      .   .    .      .   .   .   .    .   .     .   .    .   .
     .    .   .  .  .     .  .     .  .   .  .     .   .  .  .
        .    .    .   .  .    .   .      .   .     .  .     .
  .     .  .   .     .   .    .  .  .   .  .    .   .    .    .
        .   .      .  .   .   .    .  .      .   .   .   .  .
        .  .  .    .    .   .  .   .  .   .    .   .    .   .
   .  .     .    .   .     .  .    .   .  .    .   .   .     .
       .    .    .   .    .    .   .   .    .   .  .  .  .   .
  .   .   .     .     .    .   .     .  .  .    .    .     .  .
        .    .  .   .     .   .   .  .    .  .  .  .    .  .  
     .  .  .      .   .     .    .   .   .   .     .     .   .
     .    .    .     .    .    .   .  .     .    .   .   .  .
  .   .     .   .   .    .   .   .  .    .  .    .  .   .    .
       .  .   .    .   .   .   .   .    .    .   .    .   .
      .    .  .   .     .  .   .    .   .   .   .   .   .  
*******************************************************************************
''')
print("Welcome to the Galactic Odyssey.")
print("Your mission is to explore the galaxy and discover new worlds.")
choice1 = input('You\'re at a space station orbiting a mysterious planet. '
                'Do you want to "land" on the planet or "stay" in orbit?\n').lower()

if choice1 == "land":
    choice2 = input('You\'ve landed on the planet. It\'s a lush, alien landscape. '
                    'Do you want to "explore" the surroundings or "set up" a base?\n').lower()
    if choice2 == "explore":
        choice3 = input('While exploring, you discover a hidden alien artifact. '
                        'Do you want to "analyze" it or "leave" it untouched?\n').lower()
        if choice3 == "analyze":
            print("You uncover advanced technology. Congratulations, you’ve made a groundbreaking discovery!")
        elif choice3 == "leave":
            print("You return to your spaceship, unsure of what you missed. Game Over.")
        else:
            print("You chose an invalid action. Game Over.")
    elif choice2 == "set up":
        print("Your base is established, but you encounter a hostile alien species. Game Over.")
    else:
        print("You chose an invalid action. Game Over.")

elif choice1 == "stay":
    print("You continue orbiting, but the station's supplies run out. Game Over.")

else:
    print("You made an invalid choice. Game Over.")
