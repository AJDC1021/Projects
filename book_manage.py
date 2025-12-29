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


def add_book(book_manage: dict):
    while True:
        book_id = (input("What is the id of the book? (FORMAT: B1, B2, B100): ")).upper()
        if book_id[0] != 'B':
            print("Error: Invalid ID format")
            if wrong_option(): 
                break
            else:
                continue
        try:
            book_id[1]
        except IndexError:
            print("Error: Invalid ID Format")
            if wrong_option(): 
                break
            else:
                continue            

        try:
            for i in range(1,len(book_id)):
                int(book_id[i])
        except ValueError:
            print("Error: Invalid ID format")
            if wrong_option(): 
                break
            else:
                continue
            

        if book_id in book_manage:
            print("Error: Book ID already exists.")
            if wrong_option(): 
                break
            else:
                continue
            

        title = input("What is the title of the book?: ")
        author = input("Who is the author of the book?: ")
        date_published = input("When was this book published? (FORMAT: 22 Feb 2024): ")
        try:
            date_validate = datetime.strptime(date_published, "%d %b %Y")
            today = datetime.now()
            if date_validate > today:
                print("Error: date inputted has not happened yet.")
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
            
        
        status = "Available"
        list_of_borrowers = []

        book_info_dict = {
            'title': title, 
            'author': author, 
            'date_published': date_published, 
            'status': status,
            'list_of_borrowers': list_of_borrowers
            }
        book_manage[book_id] = book_info_dict
        print("===BOOK ADDED TO DICTIONARY WITH FOLLOWING DETAILS===")
        print("BOOK ID: " + book_id)
        print("TITLE:" + title)
        print("AUTHOR: " + author)
        print("STATUS: " + status)
        print("LIST OF BORROWERS is empty")
        print()
        break

def delete_book(book_manage: dict):
    while True:
        if not book_manage:
            print("Error: there is no book in the library yet.")
            break

        find_title = (input("Please enter the title of the book you are going to delete: ")).lower()
        find_author = (input("Please enter the author of the book you are going to delete: ")).lower()
        found = False
        to_be_deleted = []

        for key, value in book_manage.items():
            if value['title'].lower() == find_title and value['author'].lower() == find_author:
                to_be_deleted.append(key)
                
        if not to_be_deleted:
            print("Book with corresponding title and author not found")
            if wrong_option(): 
                break
            else:
                continue
            
        for keys in to_be_deleted:
            book_manage.pop(keys)
            print("Deleted book with book id " + str(keys))
        print()
        
        break

def delete_all_books(book_manage: dict):
    while True:
        if not book_manage:
            print("Error: there is no book in the library yet.")
            break

        choice = (input("Are you sure you want to delete the entire library? (y/n): ")).lower()
        if choice == 'y':
            key_list = list(book_manage.keys())
            for key in key_list:
                book_manage.pop(key)
                print("Deleted book with book id " + str(key))
            print("Successfully deleted entire library")
            print()
            break

        elif choice == 'n':
            print("Deletion aborted")
            break
        
        else:
            print("Invalid choice")
            if wrong_option(): 
                break
            else:
                continue

def view_book(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        if not book_manage:
            print("Error: there is no book in the library yet.")
            break

        title_view = (input("Please input the title to be viewed: ")).lower()
        found = False

        for details in book_manage.values():
            if details['title'].lower() == title_view:
                found = True

        if not found:
            print("No book with the title found.")
            if wrong_option(): 
                break
            else:
                continue

        print()
        print("====BOOK/S FOUND WITH CORRESPONDING TITLE====")
        for key,value in book_manage.items():
            if value['title'].lower() == title_view:
                print("BOOK ID: " + str(key))
                print("TITLE: " + value['title'])
                print("AUTHOR: " + value['author'])
                print("DATE PUBLISHED: " + str(value['date_published']))
                print("STATUS: " + value['status'])
                if value['list_of_borrowers']:
                    print("LIST OF BORROWERS:")
                    for borrow_id in value['list_of_borrowers']:
                        print("    " + str(borrow_id) + ": ", end='')
                        for key, value in borrow_manage.items():
                            if key == borrow_id:
                                log_id = value['log_id']
                        for key, value in log_manage.items():
                            if key == log_id:
                                print(value['name'])

                print()
        break

def view_all_books(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        if not book_manage:
            print("Error: there is no book in the library yet.")
            break

        print()
        print("====ALL BOOK/S IN THE LIBRARY====")
        for key,value in book_manage.items():
            print("BOOK ID: " + str(key))
            print("TITLE: " + value['title'])
            print("AUTHOR: " + value['author'])
            print("DATE PUBLISHED: " + str(value['date_published']))
            print("STATUS: " + value['status'])
            if value['list_of_borrowers']:
                print("LIST OF BORROWERS:")
                for borrow_id in value['list_of_borrowers']:
                    print("    " + str(borrow_id) + ": ", end='')
                    
                    for key, value in borrow_manage.items():
                        if key == borrow_id:
                            log_id = value['log_id']
                    
                    for key, value in log_manage.items():
                        if key == log_id:
                            print(value['name'])

                            
            print()
        break



def edit_book(book_manage:dict, log_manage: dict, borrow_manage: dict):
    while True:
        if not book_manage:
            print("Error: there is no book in the library yet.")
            break
        list_to_edit = []

        title_edit = (input("Please input the title to be edited: ")).lower()
        found = False

        for details in book_manage.values():
            if details['title'].lower() == title_edit:
                found = True

        if not found:
            print("No book with the title found.")
            if wrong_option(): 
                break
            else:
                continue
        
        for key, value in book_manage.items():
            if value['title'].lower() == title_edit:
                list_to_edit.append(key)
        
        if len(list_to_edit) > 1:
            print()
            print("Please select one to edit")
            for key,value in book_manage.items():
                if value['title'].lower() == title_edit:
                    print("BOOK ID: " + str(key))
                    print("TITLE: " + value['title'])
                    print("AUTHOR: " + value['author'])
                    print("DATE PUBLISHED: " + str(value['date_published']))
                    print("STATUS: " + value['status'])
                    if value['list_of_borrowers']:
                        print("LIST OF BORROWERS:")
                        for borrow_id in value['list_of_borrowers']:
                            print("    " + str(borrow_id) + ": ", end='')
                            for key, value in borrow_manage.items():
                                if key == borrow_id:
                                    log_id = value['log_id']
                            for key, value in log_manage.items():
                                if key == log_id:
                                    print(value['name'])

                    print()
            select_edit = input("Enter the Book ID of the book you wish to edit: ")
            if select_edit[0] != 'B':
                print("Error: Invalid ID format")
                if wrong_option(): 
                    break
                else:
                    continue


            try:
                for i in range(1,len(select_edit)):
                    int(select_edit[i])
            except ValueError:
                print("Error: Invalid ID format")
                if wrong_option(): 
                    break
                else:
                    continue
            
            if select_edit not in list_to_edit:
                print("Book ID specified not in options")
                if wrong_option(): 
                    break
                else:
                    continue
            
            value_to_edit = select_edit
        else:
            value_to_edit = list_to_edit[0]
        
        new_title = input("What is the new title of the book?: ")
        new_author = input("Who is the new author of the book?: ")
        date_published = input("Edit the publishing date (FORMAT: 22 Feb 2024): ")
        try:
            date_validate = datetime.strptime(date_published, "%d %b %Y")
            today = datetime.now()
            if date_validate > today:
                print("Error: date inputted has not happened yet.")
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
        status = book_manage[value_to_edit]['status']
        list_of_borrowers = book_manage[value_to_edit]['list_of_borrowers']

        book_manage[value_to_edit]['title'] = new_title
        book_manage[value_to_edit]['author'] = new_author
        book_manage[value_to_edit]['date_published'] = date_published


        print("===BOOK EDITED WITH FOLLOWING DETAILS===")
        print("BOOK ID: " + value_to_edit)
        print("TITLE:" + new_title)
        print("AUTHOR: " + new_author)
        print("STATUS: " + status)
        if list_of_borrowers:
            for borrow_id in list_of_borrowers:
                print("   " + str(borrow_id) + ": ", end='')
                for key, value in borrow_manage.items():
                    if key == borrow_id:
                        log_id = value['log_id']
                for key, value in log_manage.items():
                    if key == log_id:
                        print(value['name'])
        print()
        break

def view_pending(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        if not book_manage:
            print("Error: there is no book in the library yet.")
            break
        found = False
        for key, value in book_manage.items():
            if value['status'] == "Unavailable":
                found = True
                break
        if found:
            print("===THESE ARE ALL THE UNAVAILABLE BOOKS===")
            for key, value in book_manage.items():
                if value['status'] == "Unavailable":
                    print("BOOK ID: " + str(key))
                    print("TITLE: " + value['title'])
                    print("AUTHOR: " + value['author'])
                    print("DATE PUBLISHED: " + str(value['date_published']))
                    last_idx = len(value['list_of_borrowers']) - 1
                    borrow_id = value['list_of_borrowers'][last_idx]
                    print("LAST BORROWER: " + str(borrow_id) + ' - ', end='')
                    for key, value in borrow_manage.items():
                        if key == borrow_id:
                            log_id = value['log_id']

                    for key, value in log_manage.items():
                        if key == log_id:
                            print(value['name'])
                    
                    for key, value in borrow_manage.items():
                        if key == borrow_id:
                            print("EXPECTED RETURN: " + value['date_return'])
            break
        else:
            print("No unavailable books")
            break

def book_manage(book_manage: dict, log_manage: dict, borrow_manage: dict):
    while True:
        print()
        print("==== BOOK MANAGEMENT MENU ====")
        print("[1] ADD BOOK")
        print("[2] DELETE BOOK")
        print("[3] DELETE ALL BOOKS")
        print("[4] VIEW BOOK")
        print("[5] VIEW ALL BOOKS")
        print("[6] EDIT BOOK")
        print("[7] VIEW PENDING BOOKS")
        print("[0] RETURN TO MAIN MENU")

        try:
            select = int(input("Enter your input: "))
        except ValueError:
            print("Invalid input")
            continue
        if select == 1:
            add_book(book_manage)
        elif select == 2:
            delete_book(book_manage)
        elif select == 3:
            delete_all_books(book_manage)
        elif select == 4:
            view_book(book_manage, log_manage, borrow_manage)
        elif select == 5:
            view_all_books(book_manage, log_manage, borrow_manage)
        elif select == 6:
            edit_book(book_manage, log_manage, borrow_manage)
        elif select == 7:
            view_pending(book_manage, log_manage, borrow_manage)
        elif select == 0:
            break
        else:
            print("Invalid option")



