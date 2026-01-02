import csv
import string

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
        filename = input("What is the name of the file? ")
        text = []
        word_counter = {}
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file, delimiter=" ")
                for row in reader:
                    for i in range(0, len(row)):
                        translator = str.maketrans('','', string.punctuation)
                        temp_text = str(row[i])
                        temp_text = (temp_text.translate(translator)).lower()
                        text.append(temp_text)
        except FileNotFoundError:
            print("Error: File not found")
            continue

        for word in text:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1

        amount_list = list(dict.fromkeys(word_counter.values()))

        if not amount_list:
            print("Error: file is empty")
            continue

        for i in range(0,5):
            if amount_list:
                list_temp=[]
                rank = i + 1
                for word, value in word_counter.items():
                    if value == max(amount_list):
                        list_temp.append(word)
                if len(list_temp) > 1:
                    print("The word that ranked " + str(rank) + " in the most appearing count are ", end='')
                    for i in range(0, len(list_temp)):
                        print('"' + str(list_temp[i]) + '"', end='')
                        if (i+1) != len(list_temp):
                                print(", ", end='')
                    print(" appearing a total of " + str(max(amount_list)) + " time/s.")
                else:
                    print("The word that ranked " +  str(rank) + " in the most appearing count is " + '"' + str(list_temp[0]) + '"' + " appearing a total of " + str(max(amount_list)) + " time/s.")
                amount_list.remove(max(amount_list))
            else:
                break

    elif select == 2:
        print("Bye!")
        break
    else:
        print("Invalid input.")

