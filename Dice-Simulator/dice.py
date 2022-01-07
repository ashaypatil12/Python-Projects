import random


def roll_dice():                                                            # ------------ function definition
    choice = input("Do you want to continue (y/n) :")
    if choice.lower() == 'y':
        number = random.randint(1, 6)
        if number == 1:
            print("""                                                               # instead of multiple prints, use one print docstrings
                     -----------
                     |         |
                     |    0    |
                     |         |
                     -----------
                     """)

        elif number == 2:
             print("""
                      -----------
                      |         |
                      | 0     0 |
                      |         |
                      -----------
                      """)

        elif number == 3:
            print("""
                     -----------
                     |    0    |
                     |    0    |
                     |    0    |
                     -----------
                     """)

        elif number == 4:
            print("""
                     -----------
                     | 0     0 |
                     |         |
                     | 0     0 |
                     -----------
                     """)

        elif number == 5:
            print("""
                     -----------
                     | 0     0 |
                     |    0    |
                     | 0     0 |
                     -----------
                     """)

        elif number == 6:
            print("""
                     -----------
                     | 0     0 |
                     | 0     0 |
                     | 0     0 |
                     -----------
                     """)
        roll_dice()                                                         # Call the same function to ask if they want to continue
    elif choice.lower() == 'n':
        print("Thanks for playing")                                         # terminate the program
    else:
        print("You entered an Incorrect input. ")
        roll_dice()                                                         # Incase the input is invalid, Call the same function to ask if they want to continue


print("<-------------------->Dice Simulator<------------------------->")

roll_dice()
