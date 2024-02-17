import Notepad


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите тело заметки: '), number)
    return Notepad.Note(title=title, body=body)


def menu():
    print("\nВ данной программе доступны следующие функции:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выбор заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВыберите функцию: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text