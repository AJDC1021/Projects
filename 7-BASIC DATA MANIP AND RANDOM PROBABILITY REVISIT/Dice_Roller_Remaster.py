import random

while True:
    print("MENU")
    print("[1] START")
    print("[2] STOP")
    try:
        select = int(input("Select an option: "))
    except ValueError:
        print("Error: Invalid input! Please integer.")
        continue
    if select == 1:

        try:
            no_sides = int(input("How many sides will the die have? "))
        except ValueError:
            print("Error: Invalid input! Please integer.")
            continue

        try:
            amount_rolls = int(input("How many dice rolls will there be? "))
        except ValueError:
            print("Error: Invalid input! Please integer.")
            continue

        list_of_amounthit = []
        list_of_percentages = []
        list_max = []
        list_min = []

        for i in range(0, no_sides):
            list_of_amounthit.append(0)

        for i in range(0, amount_rolls):
            side_selected = int(random.randint(1, no_sides))
            list_of_amounthit[side_selected-1] += 1

        for i in range(0, no_sides):
            list_of_percentages.append(float(list_of_amounthit[i]/amount_rolls)*100)

        for i in range(0, no_sides):
            print("Side " + str(i+1) + " appeared " + str(list_of_amounthit[i]) + " times, which has the total probability of " + str(list_of_percentages[i]) + "%")
            
        for i in range(0, no_sides):
            if list_of_amounthit[i] == max(list_of_amounthit):
                print("The number that appeared the most is " + str(i+1) + " which appeared " +  str(list_of_amounthit[i]) + " times, which has the total probability of " + str(list_of_percentages[i]) + "%")
            if list_of_amounthit[i] == min(list_of_amounthit):
                print("The number that appeared the least is " + str(i+1) + " which appeared " +  str(list_of_amounthit[i]) + " times, which has the total probability of " + str(list_of_percentages[i]) + "%")
    elif select == 2:
        print("Bye!")
        break
    else:
        print("Invalid option!")