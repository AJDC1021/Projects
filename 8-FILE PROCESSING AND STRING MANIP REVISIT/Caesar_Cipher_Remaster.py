text_list = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
first_sc = ""
second_sc = ""
flag = True
encrypt_flag = False
while True:
    print()
    print()
    print("===MENU===")
    print("[1] Enter Text")
    print("[2] Encrypt")
    print("[3] View Text List")
    print("[0] Exit")
    try:
        select = int(input("Select input: "))
    except ValueError:
        print("Error: Invalid input! Please input integer.")
        continue
    if select == 1:
        text_list.clear()
        try:
            amount = int(input("How many inputs do you want to have? "))
        except ValueError:
            print("Error: Invalid input! Please input integer.")
            continue
        if amount > 0:
            for i in range(0, amount):
                input_list = []
                input_text = input("Enter input: ")
                for char in input_text:
                    if char not in alphabet:
                        print("Invalid! Please enter text only.")
                        flag = False
                        break
                if not flag:
                    flag = True
                    input_list.clear()
                    text_list.clear()
                    break
                input_list.append(input_text.lower())
                text_list.append(input_list)
        encrypt_flag = False
    elif select == 2:
        if not text_list:
            print("Error: no text inputted yet")
            continue
        if encrypt_flag:
            print("Error: Inputs already encrypted.")
            continue
        try:
            first_shift = int(input("Enter first shift: "))
            second_shift = int(input("Enter second shift: "))
        except ValueError:
            print("Error: Invalid input! Please input integer.")
            continue
        if text_list:
            for texts in text_list:
                for text in texts:
                    first_sc = ''
                    second_sc = ''
                    for char in text:
                        for i in range(len(alphabet)):
                            if alphabet[i] == char.lower():
                                index = i + first_shift
                                if index > 25 or index < 0:
                                    index = index % 26
                                first_sc = first_sc + alphabet[index]
                                index = index + second_shift
                                if index > 25 or index < 0:
                                    index = index % 26
                                second_sc = second_sc + alphabet[index]
                            elif char not in alphabet:
                                print("Error: Invalid characters found (only letters)")
                texts.append(first_sc)
                texts.append(second_sc)
                encrypt_flag = True
        else:
            print("Error: no text inputted yet")
            continue
    elif select == 3:
        if not text_list:
            print("Error: no text inputted yet")
            continue
        for i in range(len(text_list)):
            for j in range(len(text_list[i])):
                if j == 0:
                    print()
                    print("[" + str(i) + "] "+ '"' + text_list[i][j] + '"', end='')
                else:
                    print(" ----> " + '"' + text_list[i][j] + '"', end='')
    elif select == 0:
        print("Bye!")
        break
    else:
        print("Invalid input.")