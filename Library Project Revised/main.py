import book_manage
import log_manage
import borrow_manage
import csv
import save_load

books = {}
"""
    'B1': {
        'title': "Bible", 
        'author': "Jesus", 
        'date_published': "1 Jan 1990", 
        'status': "available",
        'list_of_borrowers': ["BL1"] # Changed BL3 to BL2 to match borrows
    },
    'B2': {
        'title': "Bible", 
        'author': "God", 
        'date_published': "25 Dec 1990", 
        'status': "Unavailable",
        'list_of_borrowers': ["BL2"] # Changed BL3 to BL2 to match borrows
    },
    'B3': {
        'title': "Harry Potta", 
        'author': "JK lang", 
        'date_published': "25 Dec 1998", 
        'status': "Available",
        'list_of_borrowers': ["BL5"] # Changed BL3 to BL2 to match borrows
    }
"""


logs = {}
"""
    'L1': {
        'name': 'jeffrey',
        'date_of_log': '22 Feb 2022',
        'time_of_log': '2:30 PM',
        'purpose': 'borrow'
    }, # Added missing comma
    'L2': {
        'name': 'jason',
        'date_of_log': '22 Oct 2022',
        'time_of_log': '1:00 PM',
        'purpose': 'borrow'
    },
    'L3': {
        'name': 'mj',
        'date_of_log': '22 Jan 2022',
        'time_of_log': '1:00 PM',
        'purpose': 'borrow'
    }
"""


borrows = {}
"""
    'BL1': {
        'book_id': 'B1',
        'log_id': 'L1',
        'date_return': '9 Mar 2029'
    }, # Added missing comma
    'BL2': {
        'book_id': 'B2',
        'log_id': 'L2',
        'date_return': '9 Nov 2029'    
    },
    'BL5': {
        'book_id': 'B3',
        'log_id': 'L3',
        'date_return': '9 Jan 2020'    
    }
"""




                




while True:
    save_load.load_file("load_file.txt", books, logs, borrows)
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
