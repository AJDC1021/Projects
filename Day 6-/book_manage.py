import datetime

book_dict = {}

def book_management(books: dict):
    format_string = "%d %b %Y"
    new_entry = []
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
        print("[0] Exit")
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
                if Id[0].upper() != "B":
                    print("Error! Invalid Book Format.")
                    continue

                for i in range(1, len(Id)):
                    try:
                        int(Id[i])
                    except ValueError:
                        flag = False
                        print("Error, your id is an invalid format")
                        break
                print("")
                found_details = books[to_view]
                print("Detail of book: " + found_books[0])
                print("Title: " + found_details[0])
                print("Author: " + found_details[1])
                print("Date published: " + found_details[2])
                print("Status: " + found_details[3])
                if found_details[4]:
                    print("List of borrowers: ")
                    for borrowers in found_details[4]:
                        print("    " + borrowers)
            else:
                print("")
                found_details = books[found_books[0]]
                print("Detail of book: " + found_books[0])
                print("Title: " + found_details[0])
                print("Author: " + found_details[1])
                print("Date published: " + found_details[2])
                print("Status: " + found_details[3])
                if found_details[4]:
                    print("List of borrowers: ")
                    for borrowers in found_details[4]:
                        print("    " + borrowers)

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
                        for borrowers in found_details[4]:
                            print("    " + borrowers)
                to_edit = input("Type the book ID of the one you want to edit: ")
                if Id[0].upper() != "B":
                    print("Error! Invalid Book Format.")
                    continue

                for i in range(1, len(Id)):
                    try:
                        int(Id[i])
                    except ValueError:
                        flag = False
                        print("Error, your id is an invalid format")
                        break
            else:
                found_details = books[found_books[0]]
                print("")
                print("Detail of book: " + found_books[0])
                print("Title: " + found_details[0])
                print("Author: " + found_details[1])
                print("Date published: " + found_details[2])
                print("Status: " + found_details[3])
                if found_details[4]:
                    print("List of borrowers: ")
                    for borrowers in found_details[4]:
                        print("    " + borrowers)
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
            print("List of unavailable books: ")
            for key,value in books.item():
                if value[3] == "Unavailable":
                    print("Title: " + value[0])
                    print("Author: " + value[1])
                    print("Date Published: " + value[2])
                    if value[4]:
                        print("List of borrowers: ")
                        for borrowers in value[4]:
                            print("    " + borrowers)
        else:
            print("Invalid choice")
            continue




book_management(book_dict)