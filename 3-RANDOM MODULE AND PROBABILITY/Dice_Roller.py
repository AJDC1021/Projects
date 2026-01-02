import random

first_try = True

while True:

    print("MENU")
    print("[1] START")
    print("[2] STOP")
    continue_ = input("Input: ")
    if continue_ == str(1):
        try:
            no_of_sides = int(input("How many sides does this dice have? "))
        except(ValueError, TypeError):
            print("Sorry! Input must be a integer")
            break

        try:
            no_of_dices = int(input("How many dices rolls will you have? "))
        except(ValueError, TypeError):
            print("Sorry! Input must be a integer")
            break

        list_value = []

        for i in range(0,no_of_sides):
            list_value.append(0)

        for i in range(0, no_of_dices):
            value = random.randint(1, no_of_sides)
            list_value[value-1] += 1

        for i in range (0, no_of_sides):
            print("The probability of " + str(i+1) + " in a " + str(no_of_sides) + "-sided dice is " + str((list_value[i]/no_of_dices)*100) + "%" + " in " + str(no_of_dices) + " rolls of the dice.")
        
        for i in range(0, no_of_sides):
            if list_value[i] == max(list_value):
                print("The most common number to appear is " + str(i+1) + " with a percentage of " + str((list_value[i]/no_of_dices)*100))
            
        
    elif continue_ == str(2):
        break
    else: 
        print("Invalid option, not in the menu")
