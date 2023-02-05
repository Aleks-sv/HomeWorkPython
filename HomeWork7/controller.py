import view

def start():
    type = view.get_type()
    if type == '1':
       add_spisok = view.input_data()
       save_data(add_spisok)
    elif type == '2':
        spisok = []
        open_data(spisok)
        for i in range(len(spisok)):
            print(f'id = {spisok[i][0]}, name = {spisok[i][1]}, surname = {spisok[i][2]}, phone = {spisok[i][3]}, coment = {spisok[i][4]}')
    elif type == '3':
        filter = view.sorted_name()
        if filter == '1':
            print('Not yet')
        elif filter == '2':
            open_list = []
            open_data(open_list)

            open_list.sort()

            list = []
            
            for i in range(len(open_list)):
                list.append(f'{open_list[i][0]};{open_list[i][1]};{open_list[i][2]};{open_list[i][3]};{open_list[i][4]}')

            file = open('HomeWork7/data.csv', 'w')
            for i in list:
                file.write(i)
            file.close

        else:
            print('Нет такого варианта! Еще раз!')
    else:
        print('Вы ввели несуществующий вариант. Попробуйте еще раз!')
        return start()

def save_data(spisok):
    with open('HomeWork7/data.csv', 'a') as file:
        file.writelines(f'{spisok[3]};{spisok[0]};{spisok[1]};{spisok[2]};{spisok[4]}\n')

def open_data(list):
    file = open('HomeWork7/data.csv', 'r')
    lines = file.readlines()
    for line in lines:
        list.append(line.split(';'))
    file.close
    return list



