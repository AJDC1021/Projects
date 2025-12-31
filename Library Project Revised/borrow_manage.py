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

def borrow_book(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        found = False
        for values in book_manage.values():
            if values['status'] == "Available":
                found = True
                break 
        if not found:
            print("No available books to borrow")
            if wrong_option(): 
                break
            else:
                continue

        print("===LIST OF AVAILABLE BOOKS TO BORROW===")
        for key, value in book_manage.items():
            if value['status'] == "Available":
                print("BOOK ID: " + key)
                print("TITLE: " + value['title'])
                print("AUTHOR: " + value['author'])
                print("DATE PUBLISHED: " + value['date_published'])
                if value['list_of_borrowers']:
                    print("LIST OF PREVIOUS BORROWERS: ")
                    for borrow_id in value['list_of_borrowers']:
                        print("    " + borrow_id + ": ", end="")
                        for key, value in borrow_manage.items():
                            if key == borrow_id:
                                log_id = value['log_id']
                        
                        for key, value in log_manage.items():
                            if key == log_id:
                                print(value['name'])
                        log_id = ''
                print()

        title = (input("Enter title of book you wish to borrow: ")).lower()
        author = (input("Enter author of book you wish to borrow: ")).lower()
        list_of_books = []

        for key, value in book_manage.items():
            if value['title'].lower() == title and value['author'].lower() == author and value['status'] == "Available":
                list_of_books.append(key)
        
        if not list_of_books:
            print("No such book in the library")
            if wrong_option(): 
                break
            else:
                continue


        if len(list_of_books) == 1:
            book_id = list_of_books[0]
        else:
            print("MULTIPLE AVAILABLE BOOKS WITH SAME TITLE AND AUTHOR NAME")
            for books in list_of_books:
                for key, value in book_manage.items():
                    if key == books:
                        print("BOOK ID: " + key)
                        print("DATE PUBLISHED: " + value['date_published'])
                        if value['list_of_borrowers']:
                            for borrow_id in value['list_of_borrowers']:
                                print("    " + borrow_id + ": ", end='')
                                for key, value in borrow_manage.items():
                                    if key == borrow_id:
                                        log_id = value['log_id']
                                for key, value in log_manage.items():
                                    if key == log_id:
                                        print(value['name'])
                                log_id = ''
                        print()

            book_id = input("Which book do you select?: ")
            if book_id not in list_of_books:
                (print("Error: book not found in the options"))
                if wrong_option(): 
                    break
                else:
                    continue

        borrow_id = (input("Please input Borrow ID (Format: BL1, BL2, BL100): ")).upper()
        if borrow_id[0] != 'B' and borrow_id[1] != 'L':
            print("Error: Invalid format")
            if wrong_option(): 
                break
            else:
                continue

        try:
            borrow_id[2]
        except IndexError:
            print("Error: Invalid format")
            if wrong_option(): 
                break
            else:
                continue


        try:
            for i in range(2, len(borrow_id)):
                int(borrow_id[i])
        except ValueError:
            print("Error: Invalid format")
            if wrong_option(): 
                break
            else:
                continue

        if borrow_id in borrow_manage:
            print("Error: Duplicate Borrow ID")
            if wrong_option(): 
                break
            else:
                continue  

        date_return = input("Enter expected date of return (FORMAT: 10 Jan 2020): ")

        try:
            return_checker = datetime.strptime(date_return, "%d %b %Y")
            today = datetime.now()
            if return_checker < today:
                print("Error: date has already passed")
                if wrong_option(): 
                    break
                else:
                    continue 
                
        except ValueError:
            print("Error: Invalid Date Format")
            if wrong_option(): 
                break
            else:
                continue 


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
    
        purpose = "borrow"


        borrow_manage[borrow_id] = {
            'book_id': book_id, 
            'log_id': log_id,
            'date_return': date_return
            }

        print()
        print("===BORROW INFO INPUTTED IN BORROW DICTIONARY===")
        print("BORROW ID: " + borrow_id)
        print("BOOK ID: " + book_id)
        print("LOG ID: " + log_id)
        print("EXPECTED DATE OF RETURN: " + date_return)

        (book_manage[book_id]['status']) = "Unavailable"
        (book_manage[book_id]['list_of_borrowers']).append(borrow_id)

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


def return_book(book_manage: dict, log_manage: dict, borrow_manage:dict):
    while True:
        found = False
        unavail_books = []
        for values in book_manage.values():
            if values['status'] == "Unavailable":
                found = True
                break

        if not found:
            print("No available books to borrow")
            break
        
        print("===UNAVAILABLE BOOKS TO RETURN===")
        for key, value in book_manage.items():
            if value['status'] == "Unavailable":
                unavail_books.append(key)
                print("BOOK ID: " + key)
                print("TITLE: " + value['title'])
                print("AUTHOR: " + value['author'])
                print("DATE PUBLISHED: " + value['date_published'])
                last_borrower = value['list_of_borrowers'][len(value['list_of_borrowers'])-1]
                print("LAST BORROWER: " + last_borrower + " - ", end='')
                for key, value in borrow_manage.items():
                    if key == last_borrower:
                        log_id = value['log_id']
                        break
                for key, value in log_manage.items():
                    if key == log_id:
                        print(value['name'])
                        break
                log_id = ''
                print()

        book_id = input("Enter Book ID of the book you wish to return: ")
        if book_id not in unavail_books:
            print("Error: book not found or not unavailable")
            if wrong_option(): 
                break
            else:
                continue
        
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
    
        purpose = "return"

        book_manage[book_id]['status'] = "Available"
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

def view_all_entries(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        if not borrow_manage:
            print("Error: no borrow info entry yet")
            break

        print("ALL BORROW INFO ENTRIES")
        for key, value in borrow_manage.items():
            print("BORROW ID: " + key)
            book_id = value['book_id']
            log_id = value['log_id']
            print("BOOK TITLE: " + book_manage[book_id]['title'])
            print("BOOK AUTHOR: " + book_manage[book_id]['author'])
            print("DATE PUBLISHED: " + book_manage[book_id]['date_published'])
            if book_manage[book_id]['status'] == "Unavailable":
                print("EXPECTED DATE OF RETURN: " + value['date_return'])
            else:
                print("DATE OF RETURN: " + value['date_return'])
            print("BORROWER NAME: " + log_manage[log_id]['name'])
            print()
        break

def view_expected_returns(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        if not borrow_manage:
            print("No borrow info found yet")
        
        date_return_input = input("Enter date to check return (1 Jan 2029): ")
        try:
            return_checker = datetime.strptime(date_return_input, "%d %b %Y")
        except ValueError:
            print("Error: Invalid Date Format")
            if wrong_option():
                break
            else:
                continue
        found = False
        print("EXPECTED RETURN ON THE DAY OF " + date_return_input)
        for key, value in borrow_manage.items():
            if value['date_return'] == date_return_input:
                found = True
                print("BORROW ID: " + key)
                book_id = value['book_id']
                print("TITLE: " + book_manage[book_id]['title'])
                print("AUTHOR: " + book_manage[book_id]['author'])
                print("DATE PUBLISHED: " + book_manage[book_id]['date_published'])
                print("STATUS: " + book_manage[book_id]['status'])
                log_id = value['log_id']
                print("BORROWER: " + log_manage[log_id]['name'])
                print()
        break

def borrow_manage(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        if not book_manage:
            print("No books found to borrow or return.")
            break
        print()
        print("===BORROW MANAGEMENT MENU===")
        print("[1] BORROW BOOK")
        print("[2] RETURN BOOK")
        print("[3] VIEW ALL ENTRIES")
        print("[4] VIEW EXPECTED RETURNS")
        print("[0] RETURN TO MAIN MENU")
        select = input("Enter your input: ")

        if select == '1':
            borrow_book(book_manage, log_manage, borrow_manage)
        elif select == '2':
            return_book(book_manage, log_manage, borrow_manage)
        elif select == '3':
            view_all_entries(book_manage, log_manage, borrow_manage)
        elif select == '4':
            view_expected_returns(book_manage, log_manage, borrow_manage)
        elif select == '0':
            break
        else:
            print("Error: Invalid input")