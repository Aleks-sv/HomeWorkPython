def get_type():
    type = int(input('1 - добавить школьника\n 2 - добавить предмет\n 3 - добавить оценку ученику\n 4 - показать весь список\n 5 - показать конкретный список\n 6 - выход'))
    return type

def input_student():
    name = input('Введите имя и фамилию ученика: ')
    return name

def input_subject():
    subject = input("Введите предмет: ")
    return subject

def input_mark():
    name = input("Введите имя ученика: ")
    subject = input("Введите предмет: ")
    mark = input("Введите оценку: ")
    return name, subject, mark

def name_to_show():
    name = input("Введите имя для просмотра оценок: ")
    return name
