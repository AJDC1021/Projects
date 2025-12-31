import csv
import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
shift = 1

def encrypt(to_translate: str):
    final = ''
    for char in to_translate:
        if char in lowercase:
            char_idx = lowercase.index(char) + shift
            if char_idx > 25:
                char_idx = (char_idx % 26)
            final += lowercase[char_idx]
        elif char in uppercase:
            char_idx = uppercase.index(char) + shift
            if char_idx > 25:
                char_idx = (char_idx % 26)
            final += uppercase[char_idx]
        elif char in digits:
            char_idx = digits.index(char) + shift
            if char_idx > 9:
                char_idx = (char_idx % 10)
            final += digits[char_idx]
        else:
            final += char
    return final

def decrypt(to_translate: str):
    final = ''
    for char in to_translate:
        if char in lowercase:
            char_idx = lowercase.index(char) - shift
            if char_idx < 0:
                char_idx = (char_idx % 26)
            final += lowercase[char_idx]
        elif char in uppercase:
            char_idx = uppercase.index(char) - shift
            if char_idx < 0:
                char_idx = (char_idx % 26)
            final += uppercase[char_idx]
        elif char in digits:
            char_idx = digits.index(char) - shift
            if char_idx < 0:
                char_idx = (char_idx % 10)
            final += digits[char_idx]
        else:
            final += char
    return final



def load_file(file: str, book_manage: dict, log_manage: dict, borrow_manage: dict):
    with open(file, mode='r', newline='') as file_reader:
        file_load = csv.reader(file_reader, delimiter=',')
        temp_dict = {}
        turn = 0
        for line in file_load:
            if line:
                turn_switcher = decrypt(line[0])
                if turn_switcher == "START_BOOK":
                    turn = 1
                    continue
                elif turn_switcher == "END_BOOK":
                    turn = 0
                    continue
                elif turn_switcher == "START_LOG":
                    turn = 2
                    continue
                elif turn_switcher == "END_LOG":
                    turn = 0
                    continue
                elif turn_switcher == "START_BORROW":
                    turn = 3
                    continue
                elif turn_switcher == "END_BORROW":
                    turn = 0
                    continue
                
                if turn == 0:
                    continue
                elif turn == 1:
                    book_id = str(line[0])
                    book_id = decrypt(book_id)
                    title = decrypt(line[1])
                    author = decrypt(line[2])
                    date_published = decrypt(line[3])
                    status = decrypt(line[4])
                    list_of_borrowers = []
                    try:
                        if line[5]:
                            for i in range(5,len(line)):
                                borrower = decrypt(line[i])
                                list_of_borrowers.append(borrower)
                    except IndexError:
                        pass
                    book_manage[book_id] = {
                        'title': title,
                        'author': author,
                        'date_published': date_published,
                        'status': status,
                        'list_of_borrowers': list_of_borrowers
                    }
                elif turn == 2:
                    log_id = decrypt(line[0])
                    name = decrypt(line[1])
                    date_of_log = decrypt(line[2])
                    time_of_log = decrypt(line[3])
                    purpose = decrypt(line[4])
                    log_manage[log_id] = {
                        'name': name,
                        'date_of_log': date_of_log,
                        'time_of_log': time_of_log,
                        'purpose':purpose
                    }
                elif turn == 3:
                    borrow_id = decrypt(line[0])
                    book_id = decrypt(line[1])
                    log_id = decrypt(line[2])
                    date_return = decrypt(line[3])
                    borrow_manage[borrow_id] = {
                        'book_id': book_id,
                        'log_id': log_id,
                        'date_return': date_return
                    }
            else:
                continue 

def save_file(file: str, book_manage:dict, log_manage:dict, borrow_manage: dict):
    with open(file, mode='w', newline='') as file_writer:
        if book_manage:
            start = "START_BOOK\n"
            start = encrypt(start)
            file_writer.write(start)
            for key, value in book_manage.items():

                book_id = encrypt(key)
                file_writer.write(book_id)
                file_writer.write(',')

                title = encrypt(value['title'])
                file_writer.write(title)
                file_writer.write(',')

                author = encrypt(value['author'])
                file_writer.write(author)
                file_writer.write(',')

                date_published = encrypt(value['date_published'])
                file_writer.write(date_published)
                file_writer.write(',')

                status = encrypt(value['status'])
                file_writer.write(status)

                list_of_borrowers = value['list_of_borrowers']
                if len(list_of_borrowers)>0:
                    for i in range(0, len(list_of_borrowers)):
                        file_writer.write(',')
                        borrower = encrypt(list_of_borrowers[i])
                        file_writer.write(borrower)

                file_writer.write('\n')
            end = "END_BOOK\n"
            end = encrypt(end)
            file_writer.write(end)
        file_writer.write('\n')
        if log_manage:
            start = "START_LOG\n"
            start = encrypt(start)
            file_writer.write(start)
            for key, value in log_manage.items():
                log_id = encrypt(key)
                file_writer.write(log_id)
                file_writer.write(',')

                name = encrypt(value['name'])
                file_writer.write(name)
                file_writer.write(',')

                date_of_log = encrypt(value['date_of_log'])
                file_writer.write(date_of_log)
                file_writer.write(',')

                time_of_log = encrypt(value['time_of_log'])
                file_writer.write(time_of_log)
                file_writer.write(',')

                purpose = encrypt(value['purpose'])
                file_writer.write(purpose)
                file_writer.write('\n')
            end = "END_LOG\n"
            end = encrypt(end)
            file_writer.write(end)
        file_writer.write('\n')
        if borrow_manage:
            start = "START_BORROW\n"
            start = encrypt(start)
            file_writer.write(start)
            for key, value in borrow_manage.items():
                borrow_id = encrypt(key)
                file_writer.write(borrow_id)
                file_writer.write(',')


                book_id = encrypt(value['book_id'])
                file_writer.write(book_id)
                file_writer.write(',')

                log_id = encrypt(value['log_id'])
                file_writer.write(log_id)
                file_writer.write(',')

                date_return = encrypt(value['date_return'])
                file_writer.write(date_return)
                file_writer.write('\n')
            end = "END_BORROW\n"
            end = encrypt(end)
            file_writer.write(end)