import datetime

def log_create_for_borrow(log_dict: dict):
    flag = True
    purpose_list = ["borrow", "return", "visit"]
    while True:
        format_string = "%d %b %Y"
        format_string_time = "%-I:%M %p"
        format_string_time2 = "%-I%p"
        format_string_time3 = "%-I %p"
        Id = input("Input Log id (format L<number>): ")
        Id = Id[0].upper() + Id[1:]
        if Id[0] != "L":
            print("Error! Invalid Book Format.")
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
        
        return Id, Name, Date_init, time_final, purpose

def view_available_books (books: dict):
    print("Here are the available book details: ")
    for key, value in books.items():
        if value[3] == "Available":
            print()
            print("Title: " + value[0])
            print("Author: " + value[1])
            print("Date Published: " + value[2])
            if value[4]:
                print("List of Borrowers: ")
                for values in value[4]:
                    print(values)




def borrow_management(borrow: dict, logs: dict, books: dict):
    while True:
        format_string = "%d %b %Y"
        print("")
        print("BORROW MANAGMENT MENU")
        print("[1] Borrow Book")
        print("[2] Return Book")
        print("[3] View all Entries")
        print("[4] View all expected returns")
        print("[0] Return to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            Log_ID, Name, Date_init, time_final, purpose = log_create_for_borrow(logs)
            view_available_books(books)
            valid_books_list = []
            title_to_borrow = input("Enter the title of the book you wish to borrow: ")
            if not title_to_borrow:
                print("Input cannot be empty")        
                continue
            for value in books.values():
                if value[0] == title_to_borrow:
                    break    
            author_to_borrow = input("Enter the author of the book you wish to borrow: ")
            if not author_to_borrow:
                print("Input cannot be empty")        
                continue
            for value in books.values():
                if value[1] == author_to_borrow:
                    break

            for key,value in books.items():
                if value[0] == title_to_borrow and value[1] == author_to_borrow:
                    valid_books_list.append(key)

            book_id_to_borrow = ""
            if not valid_books_list:
                print("A book with the same title and author you inputted is not in the dictionary.")
                continue
                    
            if len(valid_books_list) > 1:
                flag_book = True
                print("Multiple instance of book with the same author and title")
                print("Select the book ID of the book you wish to borrow")
                book_id_select = input("Book ID: ")
                Id = Id[0].upper() + Id[1:]
                if Id[0] != "B":
                    print("Error! Invalid Book Format.")
                    continue


                for i in range(1, len(Id)):
                    try:
                        int(Id[i])
                    except ValueError:
                        flag = False
                        print("Error, your id is an invalid format")
                        break
                
                if flag_book == False:
                    flag_book = True
                    continue
                
                if book_id_select in valid_books_list:
                    book_id_to_borrow = book_id_select
            elif len(valid_books_list) == 1:
                book_id_to_borrow = valid_books_list[0]
            
            date_return = input("Input date of return: ")

            if not date_return:
                print("Input required")
                continue
            try:
                date_object = datetime.datetime.strptime(date_return, format_string).date()
            except ValueError:
                print("Date in wrong format.")
                continue
            
            if datetime.date.today() < date_object:
                print("Error, date has not happened yet")
                continue
            flag_borrow = True
            Id = input("Input Borrow id (format BL<number>):")
            Id = Id[0].upper() + Id[1].upper() + Id[2:]
            if Id[0] != "B" and Id[1] != "L":
                print("Error! Invalid Borrow ID Format.")
                continue

            for i in range(2, len(Id)):
                try:
                    int(Id[i])
                except ValueError:
                    flag = False
                    print("Error, your id is an invalid format")
                    break
            
            if not flag_borrow:
                flag_borrow = True
                continue
            
            if Id in borrow:
                print("Borrow ID is already existing")
                continue

            Borrow_ID = Id
            Book_ID = book_id_to_borrow
            value_to_append = books[Book_ID]
            value_to_append[4].append(Borrow_ID)
            books[Book_ID][3] = "Unavailable"
            logs[Log_ID] = [Name, Date_init, time_final, purpose]
            borrow[Borrow_ID] = [Book_ID, Log_ID, date_return]
        elif choice == "2":
            if not borrow:
                print("No books borrowed yet")
                continue
            flagger = False
            for value in books.values():
                if value[3] == "Unavailable":
                    flagger = True
                    break
            if flagger:
                print("Unavailable books to return")
                for key,value in books.items():
                    if value[3] == "Unavailable":
                        print()
                        print("Book ID: " + key)
                        print("Title: " + value[0])
                        print("Author: " + value[1])
                        print("Date Published: " + value[2])
                        if value[4]:
                            print("List of Borrowers: ")
                            for values in value[4]:
                                print(values)
                try:
                    book_to_return = input("Choose Book ID of book to return: ")
                    books[book_to_return][3] = "Available"
                    Log_ID, Name, Date_init, time_final, purpose = log_create_for_borrow(logs)
                    logs[Log_ID] = [Name, Date_init, time_final, purpose]
                except KeyError:
                    print("Invalid ID inputted")
            else:
                print("No books to return")
        elif choice == "3":
            if not borrow:
                print("No books borrowed yet")
                continue
            print("Borrow Dictionary Information: ")
            for key,value in borrow.items():
                print()
                print("Borrow ID: " + key)
                print("Title: " + books[value[0]][0])
                print("Author: " + books[value[0]][1])
                print("Date Return: " + value[2])
                print("Borrower: " + logs[value[1]][0])
        elif choice == "4":
            if not borrow:
                print("No books borrowed yet")
                continue

            format_string = "%d %b %Y"
            expected_borrow_return = input("Enter return date: ")
            if not expected_borrow_return:
                print("Input required")
                continue
            try:
                date_object = datetime.datetime.strptime(expected_borrow_return, format_string).date()
            except ValueError:
                print("Date in wrong format.")
                continue
            
            if datetime.date.today() < date_object:
                print("Error, date has not happened yet")
                continue
            flagger = False
            for key, value in borrow.items():
                if value[2] == expected_borrow_return:
                    flagger = True
                    break
            if flagger:
                for key,value in borrow.items():
                    if value[2] == expected_borrow_return:
                        print("Borrow ID: " + key)
                        print("Title: " + books[value[0]][0])
                        print("Author: " + books[value[0]][1])
                        print("Date Return: " + value[2])
                        print("Borrower: " + logs[value[1]][0])
            else:
                print("No books to return that day")
        else:
            print("Invalid Choice")
            continue