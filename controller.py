import model
import view

def input_handler(inp: int):
    global phonebook
    match inp:
        case 1:
            model.open_file()
        case 2:
            model.show_all(model.phonebook)
            model.print_phonebook()
        case 3:
            model.create_contact()
        case 4:
            model.choose_contact()
        case 5:
            model.delete_contact()
        case 6:
            model.save_file()
        case 7:
            model.exit_program()
        case _:
            print(f'Error input!')


def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)


