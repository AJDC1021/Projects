import book_manage
import log_manage

books = { 
    'B1': {
        'title': "Bible", 
        'author': "Jesus", 
        'date_published': "1 Jan 1990", 
        'status': "Unavailable",
        'list_of_borrowers': ["BL1", "BL2"] # Changed BL3 to BL2 to match borrows
    },
    'B2': {
        'title': "Bible", 
        'author': "God", 
        'date_published': "25 Dec 1990", 
        'status': "Unavailable",
        'list_of_borrowers': ["BL1", "BL2"] # Changed BL3 to BL2 to match borrows
    }
}

logs = {
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
    }
}

borrows = { 
    'BL1': {
        'book_id': 'B1',
        'log_id': 'L1',
        'date_return': '9 Mar 2022'
    }, # Added missing comma
    'BL2': {
        'book_id': 'B1',
        'log_id': 'L2',
        'date_return': '9 Nov 2022'    
    }
}


while True:
    print("=== MAIN MENU ===")
    print("[1] BOOK MANAGEMENT")
    print("[2] LOG MANAGEMENT")
    print("[3] BORROW MANAGEMENT")
    print("[0] EXIT")
    select = input("Enter your input: ")
    if select == '1':
        book_manage.book_manage(books, logs, borrows)
    elif select == '2':
        log_manage.log_manage(logs)
    elif select == '3':
        print()
    elif select == '0':
        print("Bye!")
        break
    else:
        print("Invalid Input.")