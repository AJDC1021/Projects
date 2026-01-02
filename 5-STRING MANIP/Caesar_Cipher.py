alphabet = "abcdefghijklmnopqrstuvwxyz"
flag = True
text_list = []
encrypted = []


while True:
    print("[1] Enter list of text")
    print("[2] Encrypt")
    print("[3] View Encrypt")
    print("[4] Exit")
    choice = input("Input your choice: ")
    if choice == "1":
        text_list.clear()
        encrypted.clear()
        amount = input("How many text do you want to add? ")
        for i in range(int(amount)):
            text = input("[" + str(i+1) + "] ")
            for bit in text:
                if bit not in alphabet:
                    print("Error, only letters are allowed for an input")
                    flag = False
                    break
            if not flag:
                flag = True
                break
            text_list.append(text.lower())
        print(text_list)
    elif choice == "2":
        if text_list:
            try:
                shift = int(input("Input your first shift: "))
            except ValueError:
                print("Error, please input valid integer.")
                continue
            try:
                shift2 = int(input("Input your second shift: "))
            except ValueError:
                print("Error, please input valid integer.")
                continue
                    
            for index in range(len(text_list)):
                final_input = text_list[index]
                shift_list = []
                shift_list.append(final_input)
                value_hold = 0
                shift_to = 0
                value1 = ""
                value2 = ""

                for char in final_input:
                    for i in range(len(alphabet)):
                        if char == alphabet[i]:
                            shift_to = i + shift
                            while shift_to > 25:
                                shift_to = shift_to - 26
                            while shift_to < 0:
                                shift_to = shift_to + 26
                            value1 += alphabet[shift_to]
                
                for char in value1:
                    for i in range(len(alphabet)):
                        if char == alphabet[i]:
                            shift_to = i + shift2
                            while shift_to > 25:
                                shift_to = shift_to - 26
                            while shift_to < 0:
                                shift_to = shift_to + 26
                            value2 += alphabet[shift_to]
                
                shift_list.append(value1)
                shift_list.append(value2)
                encrypted.append(shift_list)
        else:
            print("Enter Text Firsts")
    elif choice == "3":
        if encrypted:
            for i in range(len(encrypted)):
                print("[" + str(i+1) + "] " + encrypted[i][0] + " -> " + encrypted[i][1] + " -> " + encrypted[i][2])
        else:
            print("No Cipher's Text yet")
    elif choice == "4":
        print("byeeee")
        break
    else:
        print("Invalid choice!")
            

                        
                


