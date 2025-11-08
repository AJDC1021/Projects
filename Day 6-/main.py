import book_manage
import borrow_manage 
import log_manage

books = {}
logs = {}
borrows = {}

while True:
    print()
    print("MAIN MENU")
    print("[1] Book Management")
    print("[2] Borrow Management")
    print("[3] Log Management")
    print("[0] Exit")
    choice = input("Enter your choice: ")
    if choice == "0":
        break
    elif choice == "1":
        book_manage.book_management(books, logs, borrows)
    elif choice == "2":
        borrow_manage.borrow_management(borrows, logs, books)
    elif choice == "3":
        log_manage.log_management(logs)
    else:
        print("Invalid choice")
        continue

