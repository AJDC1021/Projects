import datetime


def book_management(books: dict, logs: dict, borrow: dict):
    format_string    = "%d %b %Y"
    new_entry = []
    deleted_book_id = []
    flag = True

    while True:
        print(" ")
        print("BOOK MANAGEMENT MENU")
        print("[1] Add Book")
        print("[2] Delete Book")
        print("[3] Delete All Book")
        print("[4] View Book")
        print("[5] Edit Book")
        print("[6] View Pending")
        print("[0] Return to Main Menu")
        choice = input("Input your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            new_entry.clear()
            print("")
            Id = input("Input book id (format B<number?):")
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
            
            if flag == False:
                flag = True
                continue
            
            if Id in books:
                print("Book ID already taken")
                continue
            
            if Id in deleted_book_id:
                print("Book ID is associated with formerly deleted book, choose another one for record safety")
                continue

            Title = input("Enter title of book: ")
            if not Title:
                print("Input required")
                continue
            Author = input("Enter author of book: ")
            if not Author:
                print("Input required")
                continue
            Date_init = input("Enter date of publish (format 1 Jan 2000): ")
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
            
            Status = "Available"
            List_of_borrowers = []
            books[Id.upper()] = [Title, Author, Date_init, Status, List_of_borrowers]
            print("Added successfully")
            print(books)
        elif choice == "2":
            if not books:
                print("Book dictionary is empty.")
                continue

            to_delete = []
            print("")
            title_finder = input("Enter Title of book to delete: ")
            if not title_finder:
                print("Input required")
                continue
            author_finder = input("Enter Author of book to delete: ")
            if not author_finder:
                print("Input required")
                continue

            for key,value in books.items():
                if value[0] == title_finder and value[1] == author_finder:
                    to_delete.append(key)
            

            if len(to_delete) > 1:
                print("More than on instance of book with the inputted title and author")
                for keys in to_delete:
                    for key,value in books.items():
                        if keys == key:
                            print(keys)
                key_to_delete = input("Select which key to delete: ")
                if key_to_delete not in to_delete:
                    print("Book with id not found")
                    continue
            elif len(to_delete) < 1:
                print("Book with Title and Author specified not found")
                continue
            else:
                key_to_delete = to_delete[0]
            deleted_book_id.append(key_to_delete)
            del books[key_to_delete]
            print("Deleted Successfully")


        elif choice == "3":
            if not books:
                print("Book dictionary is empty.")
                continue
                
            while True:
                print("")
                delete_all_choice = input("Are you sure you want to delete all books? (y/n)")
                if delete_all_choice == "y" or delete_all_choice == "Y":
                    for key in books.keys():
                        deleted_book_id.append(key)
                    books.clear()
                    break
                elif delete_all_choice == "n" or delete_all_choice == "N":
                    break
                else: 
                    print("Invalid input")
        elif choice == "4":
            if not books:
                print("Book dictionary is empty.")
                continue
            found = False
            found_books = []
            title_to_view = input("What is the title of the book you want to view? ")
            if not title_to_view:
                print("Input required")
                continue


            for key,value in books.items():
                if value[0] == title_to_view:
                    found_books.append(key)
                    found = True
            
            if not found:
                print("No books with that title found.")
                continue
            
            if len(found_books) > 1:
                print("More than one book with the same title found")
                print("IDs with the same title")
                for book_ids in found_books:
                    print(book_ids)
                to_view = input("Type the book ID of the one you want to view: ")
                if to_view[0].upper() != "B":
                    print("Error! Invalid Book Format.")
                    continue

                for i in range(1, len(to_view)):
                    try:
                        int(to_view[i])
                    except ValueError:
                        flag = False
                        print("Error, your id is an invalid format")
                        break
                print("")
                found_items= []
                found_details = books[to_view]
                print("Detail of book: " + found_books[0])
                print("Title: " + found_details[0])
                print("Author: " + found_details[1])
                print("Date published: " + found_details[2])
                print("Status: " + found_details[3])
                if found_details[4]:
                    print("List of borrowers: ")
                    for borrow_id in found_details[4]:
                        for key, value in borrow.items():
                            if key == borrow_id:
                                associated_log = value[1]
                                for k,v in logs.items():
                                    if k == associated_log:
                                        name_of_borrower = v[0]
                                        tuple_borrow = (borrow_id, name_of_borrower)
                                        found_items.append(tuple_borrow)
                    for borrowers in found_items:
                        print(borrowers[0] + " - " + borrowers[1])

            else:
                print("")
                found_items = []
                found_details = books[found_books[0]]
                print("Detail of book: " + found_books[0])
                print("Title: " + found_details[0])
                print("Author: " + found_details[1])
                print("Date published: " + found_details[2])
                print("Status: " + found_details[3])
                if found_details[4]:
                    print("List of borrowers: ")
                    for borrow_id in found_details[4]:
                        for key, value in borrow.items():
                            if key == borrow_id:
                                associated_log = value[1]
                                for k,v in logs.items():
                                    if k == associated_log:
                                        name_of_borrower = v[0]
                                        tuple_borrow = (borrow_id, name_of_borrower)
                                        found_items.append(tuple_borrow)
                    for borrowers in found_items:
                        print(borrowers[0] + " - " + borrowers[1])


            print(" ")

        elif choice == "5":
            if not books:
                print("Book dictionary is empty.")
                continue
            found = False
            found_books = []
            title_to_edit = input("What is the title of the book you want to edit? ")
            if not title_to_edit:
                print("Input required")
                continue


            for key,value in books.items():
                if value[0] == title_to_edit:
                    found_books.append(key)
                    found = True
            
            if not found:
                print("No books with that title found.")
                continue
            
            if len(found_books) > 1:
                found_items = []
                print("More than one book with the same title found")
                print("IDs with the same title")
                for book_ids in found_books:
                    print("")
                    found_details = books[book_ids]
                    print("Detail of book: " + book_ids)
                    print("Title: " + found_details[0])
                    print("Author: " + found_details[1])
                    print("Date published: " + found_details[2])
                    print("Status: " + found_details[3])
                    if found_details[4]:
                        print("List of borrowers: ")
                        for borrow_id in found_details[4]:
                            for key, value in borrow.items():
                                if key == borrow_id:
                                    associated_log = value[1]
                                    for k,v in logs.items():
                                        if k == associated_log:
                                            name_of_borrower = v[0]
                                            tuple_borrow = (borrow_id, name_of_borrower)
                                            found_items.append(tuple_borrow)
                        for borrowers in found_items:
                            print(borrowers[0] + " - " + borrowers[1])


                to_edit = input("Type the book ID of the one you want to edit: ")
                if to_edit[0].upper() != "B":
                    print("Error! Invalid Book Format.")
                    continue

                for i in range(1, len(to_edit)):
                    try:
                        int(to_edit[i])
                    except ValueError:
                        flag = False
                        print("Error, your id is an invalid format")
                        break
            else:
                found_details = books[found_books[0]]
                found_items = []
                print("")
                print("Detail of book: " + found_books[0])
                print("Title: " + found_details[0])
                print("Author: " + found_details[1])
                print("Date published: " + found_details[2])
                print("Status: " + found_details[3])
                if found_details[4]:
                    print("List of borrowers: ")
                    for borrow_id in found_details[4]:
                        for key, value in borrow.items():
                            if key == borrow_id:
                                associated_log = value[1]
                                for k,v in logs.items():
                                    if k == associated_log:
                                        name_of_borrower = v[0]
                                        tuple_borrow = (borrow_id, name_of_borrower)
                                        found_items.append(tuple_borrow)
                    for borrowers in found_items:
                        print(borrowers[0] + " - " + borrowers[1])
                to_edit = found_books[0]  
            print(" ")
            Title = input("Enter new title of book: ")
            Author = input("Enter new author of book: ")
            Date_init = input("Enter new date of publish (format 1 Jan 2000): ")
            try:
                date_object = datetime.datetime.strptime(Date_init, format_string).date()
            except ValueError:
                print("Date in wrong format.")
                continue
            
            if datetime.date.today() < date_object:
                print("Error, date has not happened yet")
                continue
            books[to_edit][0] = Title
            books[to_edit][1] = Author
            books[to_edit][2] = Date_init
            print(books)
        elif choice == "6":
            if not books:
                print("Book dictionary is empty.")
                continue
            flagger = False
            for value in books.values():
                if value[3] == "Unavailable":
                    flagger = True
                    break
            if flagger:
                print("List of unavailable books: ")
                for key,value in books.items():
                    if value[3] == "Unavailable":
                        print("Title: " + value[0])
                        print("Author: " + value[1])
                        print("Date Published: " + value[2])
                        print("Last borrower: " + value[4][len(value[4])-1])
                        print("Date of return " + borrow[value[4][len(value[4])-1]][2])                  
            else:
                print("No unavailable books")
        else:
            print("Invalid choice")
            continue
