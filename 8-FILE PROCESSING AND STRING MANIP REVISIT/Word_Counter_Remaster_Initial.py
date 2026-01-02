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
        #filename = input("What is the name of the file? ")
        filename = "input.txt"
        text = []
        word_counter = {}
        try:
            with open(filename, mode='r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=" ")
                for row in csv_reader:
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

        first = []
        for word, value in word_counter.items():
            if value == max(amount_list):
                first.append(word)
        if len(first) > 1:
            print("The word that appeared the most are ", end='')
            for i in range(0, len(first)):
                print('"' + str(first[i]) + '"', end='')
                if (i+1) != len(first):
                        print(", ", end='')
            print(" appearing a total of " + str(max(amount_list)) + " time/s.")
        else:
            print("The word that appeared the most is " + '"' + str(first[0]) + '"' + " appearing a total of " + str(max(amount_list)) + " time/s.")
        amount_list.remove(max(amount_list))

        if amount_list:
            second=[]
            for word, value in word_counter.items():
                if value == max(amount_list):
                    second.append(word)
            if len(second) > 1:
                print("The word that appeared the 2nd most are ", end='')
                for i in range(0, len(second)):
                    print('"' + str(second[i]) + '"', end='')
                    if (i+1) != len(second):
                            print(", ", end='')
                print(" appearing a total of " + str(max(amount_list)) + " time/s.")
            else:
                print("The word that appeared the 2nd most is " + '"' + str(second[0]) + '"' + " appearing a total of " + str(max(amount_list)) + " time/s.")
            amount_list.remove(max(amount_list))
        if amount_list:
            third=[]
            for word, value in word_counter.items():
                if value == max(amount_list):
                    third.append(word)
            if len(third) > 1:
                print("The word that appeared the 3rd most are ", end='')
                for i in range(0, len(third)):
                    print('"' + str(third[i]) + '"', end='')
                    if (i+1) != len(third):
                            print(", ", end='')
                print(" appearing a total of " + str(max(amount_list)) + " time/s.")
            else:
                print("The word that appeared the 3rd most is " + '"' + str(third[0]) + '"' + " appearing a total of " + str(max(amount_list)) + " time/s.")
            amount_list.remove(max(amount_list))
        if amount_list:
            fourth=[]
            for word, value in word_counter.items():
                if value == max(amount_list):
                    fourth.append(word)
            if len(fourth) > 1:
                print("The word that appeared the 4th most are ", end='')
                for i in range(0, len(fourth)):
                    print('"' + str(fourth[i]) + '"', end='')
                    if (i+1) != len(fourth):
                            print(", ", end='')
                print(" appearing a total of " + str(max(amount_list)) + " time/s.")
            else:
                print("The word that appeared the 4th most is " + '"' + str(fourth[0]) + '"' + " appearing a total of " + str(max(amount_list)) + " time/s.")
            amount_list.remove(max(amount_list))
        if amount_list:
            fifth=[]
            for word, value in word_counter.items():
                if value == max(amount_list):
                    fifth.append(word)
            if len(fifth) > 1:
                print("The word that appeared the 5th most are ", end='')
                for i in range(0, len(fifth)):
                    print('"' + str(fifth[i]) + '"', end='')
                    if (i+1) != len(fifth):
                            print(", ", end='')
                print(" appearing a total of " + str(max(amount_list)) + " time/s.")
            else:
                print("The word that appeared the 5th most is " + '"' + str(fifth[0]) + '"' + " appearing a total of " + str(max(amount_list)) + " time/s.")
            amount_list.remove(max(amount_list))
    elif select == 2:
        print("Bye!")
        break
    else:
        print("Invalid input.")