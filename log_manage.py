from datetime import datetime

def wrong_option():
    while True:
        option = (input("Exit or Continue?: ")).lower()
        if option == "exit":
            return True
        elif option== "continue":
            return False
        else:
            print("Invalid option")


def visit_library(log_manage: dict):
    while True:
        log_id = (input("Please enter your Log ID FORMAT(L1, L2, L100): ")).upper()
        if log_id[0] != 'L':
            print("Error: Invalid ID Format")
            if wrong_option(): 
                break
            else:
                continue

        try:
            log_id[1]
        except IndexError:
            print("Error: Invalid ID Format")
            if wrong_option(): 
                break
            else:
                continue

        try:
            for i in range(1, len(log_id)):
                int(log_id[i])
        except ValueError:
            print("Error: Invalid ID Format")
            if wrong_option(): 
                break
            else:
                continue

        if log_id in log_manage:
            print("Error: Log ID already taken")
            if wrong_option(): 
                break
            else:
                continue

        name = input("Enter your name: ")
        date_of_log = input("Enter date of log (Format: 9 Jan 2025): ")

        try:
            date_checker = datetime.strptime(date_of_log, "%d %b %Y")
            today = datetime.now()
            if date_checker > today:
                print("Error: date has not happened yet")
                if wrong_option(): 
                    break
                else:
                    continue
        except ValueError:
            print("Error: Invalid date format")
            if wrong_option(): 
                break
            else:
                continue
        time_of_log = input("Enter time of log (Format: 9PM, 10 PM, 11:02AM, 10:30 AM): ")
        valid = False
        for char in time_of_log:
            if char == 'A':
                time_log = list(time_of_log.partition('A'))
                valid = True
                break
            elif char == ' ':
                time_log = list(time_of_log.partition(' '))
                valid = True
                break
            elif char == 'P':
                time_log = list(time_of_log.partition('P'))
                valid = True
                break
            elif char == ':':
                time_log = list(time_of_log.partition(':'))
                valid = True
                break


        if not valid:
            print('Error: Invalid Format')
            if wrong_option(): 
                break
            else:
                continue

        time_of_log = ""
        
        if len(time_log[0]) == 1:
            padded_first = '0' + time_log[0]
            time_log[0] = padded_first

        for char in time_log:
            time_of_log = time_of_log + char
        

        date_formats = ["%I%p", "%I %p", "%I:%M%p", "%I:%M %p"]
        time_checker = False
        for formats in date_formats:
            try:
                time_checker = (datetime.strptime(time_of_log, formats)).time()
            except ValueError:
                pass

        if not time_checker:
            print("Error: Invalid format")
            if wrong_option(): 
                break
            else:
                continue
        time_of_log = time_checker.strftime("%I:%M %p")
        final_date_inputted = datetime.combine(date_checker, time_checker)
        if final_date_inputted > today:
            print("Error: Date and Time has not happened yet")
            if wrong_option(): 
                break
            else:
                continue
        
        purpose_list = ['borrow', 'return', 'visit']
        purpose_found = False
        purpose = (input("Enter your purpose (borrow, return, or visit only): ")).lower()
        if purpose not in purpose_list:
            print("Error: Invalid Purpose")
            if wrong_option(): 
                break
            else:
                continue
        
        log_manage[log_id] = {
            'name': name, 
            'date_of_log': date_of_log,
            'time_of_log': time_of_log,
            'purpose': purpose
            }
        
        print()
        print("===LOG INPUTTED IN LOG DICTIONARY===")
        print("LOG ID: " + log_id)
        print("NAME: " + name)
        print("DATE OF LOG: " + date_of_log)
        if time_of_log[0] != '0':
            print("TIME OF LOG: " + time_of_log)
        else:
            print("TIME OF LOG: " + time_of_log[1:len(time_of_log)])

        print("PURPOSE: " + purpose.upper())
        print()
        break

def view_all_logs(log_manage: dict):
    while True:
        if not log_manage:
            print("Error: No logs found")
            break

        for key, value in log_manage.items():
            print()
            print("LOG ID: " + key)
            print("NAME: " + value['name'])
            print("DATE OF LOG: " + value['date_of_log'])
            time_of_log = value['time_of_log']
            if time_of_log[0] != '0':
                print("TIME OF LOG: " + time_of_log)
            else:
                print("TIME OF LOG: " + time_of_log[1:len(time_of_log)])
            print("PURPOSE: " + value['purpose'].upper())
            print()

        break

def view_entry_per_day(log_manage: dict):
    while True:
        if not log_manage:
            print("Error: No logs found")
            break
        
        date_input = input("Enter date of log (Format: 9 Jan 2021): ")
        try:
            date_checker = datetime.strptime(date_input, "%d %b %Y")
        except ValueError:
            print("Error: Invalid date format")
            if wrong_option(): 
                break
            else:
                continue

        found = False
        for key, value in log_manage.items():
            if value['date_of_log'] == date_input:
                print()
                print("LOG ID: " + key)
                print("NAME: " + value['name'])
                print("DATE OF LOG: " + value['date_of_log'])
                time_of_log = value['time_of_log']
                if time_of_log[0] != '0':
                    print("TIME OF LOG: " + time_of_log)
                else:
                    print("TIME OF LOG: " + time_of_log[1:len(time_of_log)])
                print("PURPOSE: " + value['purpose'].upper())
                print()
                found = True

        if not found:
            print("No logs in the specified date")
        
        break





def log_manage(log_manage: dict):
    while True:
        print()
        print("====LOG MANAGEMENT MENU====")
        print("[1] VISIT LIBRARY")
        print("[2] VIEW ALL TRANSACTIONS")
        print("[3] VIEW TRANSACTIONS PER DAY")
        print("[0] RETURN TO MAIN MENU")
        select = input("Enter your input: ")       

        if select == '1':
            visit_library(log_manage)
        elif select == '2':
            view_all_logs(log_manage)
        elif select == '3':
            view_entry_per_day(log_manage)
        elif select == '0':
            break
