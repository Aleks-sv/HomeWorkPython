import view

main_dict = {}
student_name_list = []
subject_list = []
def start():
    while True:
        input_number = view.get_type()
        if input_number == 1:
            student = view.input_student()
            if student not in student_name_list:
                main_dict[student] = {}
                student_name_list.append(student)
                if subject_list:
                    for i in subject_list:
                        main_dict[student][i] = []
        elif input_number == 2:
            subject = view.input_subject()
            subject_list.append(subject)
            for name in student_name_list:
                main_dict[name][subject] = []
        elif input_number == 3:
            name, subject, mark = view.input_mark()
            main_dict[name][subject].append(mark)
        elif input_number == 4:
            print(main_dict)
        elif input_number == 5:
            name = view.name_to_show()
            print(f'Оценки ученика {[name]} - {main_dict[name]}')
        elif input_number == 6:
            break