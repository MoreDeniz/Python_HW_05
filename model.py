import controller
import view

phonebook = {}
contact = ''
path = 'database.txt'

def set_db(db_path: str):
    global path
    path = 'database.txt'

def set_contact(our_contact: str):
    global contact
    contact = our_contact

def open_file():
    global phonebook
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
        for line in file:
            contact = line.strip().split(':')
            tel = line.strip().split(':')[1].replace(';', (': '))
            for cont in contact:
                phonebook[line.strip().split(':')[0]] = tel
        return phonebook

def save_file():
    ph_list = list(phonebook.items())
    print(ph_list)
    ph_str = "*".join(map(str, ph_list)).replace("'", '').replace(': ', ';')\
        .replace(', ', ':').replace(')', '').replace('(', '').replace('*', '\n')
    print(ph_str)
    with open('database.txt', 'w', encoding='UTF-8') as data:
        data.write(ph_str)

def get_phonebook():
    global phonebook
    return phonebook

def show_all(db: list):
    if db_success(db):
        get_phonebook()

def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()
    global phonebook
    surname = view.input_surname()
    name = view.input_name()
    telephone = view.input_tel()
    comment = view.input_comment()
    my_key = str(surname + ' ' + name)
    val = str(telephone + ': ' + comment)
    phonebook[my_key] = val
    new_contact[my_key] = val
    print_contact(new_contact)

def print_phonebook():
    for key in phonebook:
        print(f'{key:17}- {phonebook[key]}')

def print_contact(my_db):
    for cont_key in my_db:
        print(f'{cont_key:17}- {my_db[cont_key]}')

def choose_contact():
    ch_contact = {}
    ch_key = ''
    global phonebook
    surname = view.input_surname()
    name = view.input_name()
    cont_key = str(surname + ' ' + name)
    for i in phonebook.keys():
        if i == cont_key:
            ch_key = i
        ch_contact = phonebook.get(ch_key)
    print(f'{ch_key:17}- {ch_contact}')

def delete_contact():
    del_contact = {}
    del_key = ''
    global phonebook
    surname = view.input_surname()
    name = view.input_name()
    cont_key = str(surname + ' ' + name)
    for i in phonebook.keys():
        if i == cont_key:
            del_key = i
    del_contact = phonebook.pop(del_key, '')
    print(del_contact)
    print(phonebook)

def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False

def exit_program():
    print('Завершение программы.')
    exit()

    