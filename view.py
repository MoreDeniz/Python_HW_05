
def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Открыть файл',
                 'Показать все контакты',
                 'Создать контакт',
                 'Найти контакт',
                 'Удалить контакт',
                 'Сохранить файл',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи команду: '))
    # TODO: сделать валидацию
    return user_input

def input_surname():
    return input('Введите фамилию: ').capitalize()

def input_name():
    return input('Введите имя: ').capitalize()

def input_tel():
    return input('Введите номер телефона: ')

def input_comment():
    return input('Введите Комментарий: ').lower()



