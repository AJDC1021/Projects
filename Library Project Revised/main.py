import book_manage
import log_manage
import borrow_manage
import csv
import save_load

books = {}
logs = {}
borrows = {}


save_load.load_file("load_file.txt", books, logs, borrows)
while True:
    print(books)
    print(logs)
    print(borrows)
    print("=== MAIN MENU ===")
    print("[1] BOOK MANAGEMENT")
    print("[2] BORROW MANAGEMENT")
    print("[3] LOG MANAGEMENT")
    print("[0] EXIT")
    select = input("Enter your input: ")
    if select == '1':
        book_manage.book_manage(books, logs, borrows)
    elif select == '2':
        borrow_manage.borrow_manage(books, logs, borrows)
    elif select == '3':
        log_manage.log_manage(logs)
    elif select == '0':
        print("Bye!")
        save_load.save_file("load_file.txt", books, logs, borrows)
        break
    else:
        print("Invalid Input.")
