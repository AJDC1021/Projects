import csv

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
        filename = input("Input the filename: ")
        sales_data = {}
        months = ["january", "february", "march", "april", "may", "june", 
                "july", "august", "september", "october", "november", "december"]
        try:
            with open(filename, mode='r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                try:
                    next(csv_reader)
                    for row in csv_reader:
                        if row:
                            for i in row:
                                if row[0].lower() in months:
                                    try: 
                                        sales_data[row[0]] = int(row[1])
                                    except ValueError:
                                        print("Error: Invalid input! Please put integer in second column.")
                                        exit()
                except StopIteration:
                    print("File is empty")
                    continue
        except FileNotFoundError:
            print("File does not exist. Input valid filename.")
            continue
        max_list = []
        min_list = []
        max_value = max(list(sales_data.values()))
        min_value = min(list(sales_data.values()))

        if max_value == min_value:
            print("The values of all months are the same. No maximum or minimum month.")
        else:
            for month, earnings in sales_data.items():
                if earnings == max_value:
                    max_list.append(month)
                elif earnings == min_value:
                    min_list.append(month)

            if len(max_list) == 1:
                print("The highest earning month is " + str(max_list[0]) + " with the earning of " + str(sales_data[max_list[0]]))
            else: 
                print("The highest earning months are ", end='')
                for i in range(0,len(max_list)):
                    print(str(max_list[i]), end='')
                    if (i+1) != len(max_list):
                        print(", ", end='')
                print(" with the earning of " + str(max_value))

            if len(min_list) == 1:
                print("The lowest earning month is " + str(min_list[0]) + " with the earning of " + str(sales_data[min_list[0]]))
            else: 
                print("The lowest earning months are ", end='')
                for i in range(0,len(min_list)):
                    print(str(min_list[i]), end='')
                    if (i+1) != len(min_list):
                        print(",  ", end='')
                print(" with the earning of " + str(min_value))

        total_earning = sum(sales_data.values())
        print("The average earning per month this year is " + str(total_earning/len(months)) + " and the total earning is " + str(total_earning))
    elif select == 2:
        print("Bye!")
        break
    else:
        print("Invalid option!")
