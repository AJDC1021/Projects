
import datetime


def log_management(log_dict: dict):
    flag = True
    format_string = "%d %b %Y"
    format_string_time = "%-I:%M %p"
    format_string_time2 = "%-I%p"
    format_string_time3 = "%-I %p"
    purpose_list = ["borrow", "return", "visit"]
    print("Input the details properly to visit the library")
    print("")

    while True:
        print("")
        print("LOG MANAGMENT MENU")
        print("[1] Visit library (enter log details)")
        print("[2] View all entries")
        print("[3] Transactions per day")
        print("[0] Return to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            Id = input("Input Log id (format L<number>): ")
            Id = Id[0].upper() + Id[1:]
            if Id[0] != "L":
                print("Error! Invalid Log ID Format.")
                continue

            for i in range(1, len(Id)):
                try:
                    int(Id[i])
                except ValueError:
                    flag = False
                    print("Error, your id is an invalid format")
                    break
            
            if not flag:
                continue

            if Id in log_dict:
                print("ID associated with another log")
                continue

            Name = input("Enter name: ")
            if not Name:
                print("Input required")
                continue
                
            Date_init = input("Enter date (format 1 Jan 1990): ")
            if not Date_init:
                print("Input required")
                continue
            try:
                date_object = datetime.datetime.strptime(Date_init, format_string).date()
            except ValueError:
                print("Date in wrong format.")
                continue
            
            if datetime.date.today() < date_object:
                print("Error, date has not happened yet")
                continue
            
            Time_init = input("Enter time (format: 10 PM, 10:00 PM, 10PM): ")
            if not Time_init:
                print("Input required")
                continue
            check2 = True
            try:
                time_object = datetime.datetime.strptime(Time_init, format_string_time).date()
                time_final = time_object
                check = True
            except ValueError:
                check = False
            
            if not check:
                try:
                    time_object = datetime.datetime.strptime(Time_init, format_string_time2).date()
                    time_final = time_object.strftime("%I:%M %p")
                    check2 = True
                except ValueError:
                    check2 = False

            if not check2:
                try:
                    time_object = datetime.datetime.strptime(Time_init, format_string_time3).date()
                    time_final = time_object.strftime("%I:%M %p")
                except ValueError:
                    print("Invalid Time Format")
                    continue
            
            
            purpose = input("Enter purpose: ")
            if not purpose:
                print("Input required")
                continue
            purpose = purpose.lower()
            if purpose not in purpose_list:
                print("Purpose is not valid")
                continue
            
            log_dict[Id] = [Name, Date_init, time_final, purpose]
        elif choice == "2":
            if not log_dict:
                print("No log entries yet!")
                continue
            
            for key,value in log_dict.items():
                print()
                print("Log ID: " + key)
                print("Logged by: " + value[0])
                print("Date: " + value[1])
                print("Time: " + value[2])
                print("Purpose: " + value[3])
        elif choice == "3":
            logs_in_date =[]
            Date_init = input("Enter date (format 1 Jan 1990) for logs to display: ")
            if not Date_init:
                print("Input required")
                continue
            try:
                date_object = datetime.datetime.strptime(Date_init, format_string).date()
            except ValueError:
                print("Date in wrong format.")
                continue
            
            if datetime.date.today() < date_object:
                print("Error, date has not happened yet")
                continue
            
            
            for key,value in log_dict.items():
                if value[1] == Date_init:
                    logs_in_date.append(key)
            if logs_in_date:
                for logs in logs_in_date:
                    for key,value in log_dict.items():
                        if logs == key:
                            print()
                            print("Log ID: " + key)
                            print("Logged by: " + value[0])
                            print("Time: " + value[2])
                            print("Purpose: " + value[3])
            else:
                print("No logs in the date specified")
        else:
            print("Invalid Choice")
            continue
        
