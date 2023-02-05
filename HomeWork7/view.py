def get_type():
    type = input('Что вы ходите сделать:\n 1 - ввести данные\n 2 - вывести данные\n 3 - сортировать данные\n Выберите номер: ')
    return type

def input_data():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    id = input('Введите идентификатор: ')
    coment = input('Введите коментарий: ')
    return name, surname, phone, id, coment

def sorted_name():
    first = input('Сортировать данные:\n 1 - по имени \n 2 - по id\n Выберите номер: ')
    return first