
# 1. Программа должна выводить данные

def input_data():
    print('Введите данные файла в формате: Фамилия Имя Отечество Телефон')
    with open('save.txt', 'a') as write_info:
        write_info.writelines(input())
        write_info.write('\n')
    print('Данные внесены!')

# 3. Поиск по заданному параметру и вывод всего при отсутствии запроса

def find_with_parameters(parameter):
    with open('save.txt', 'r') as saved_info:
        for line in saved_info:
            if str(parameter).lower() in str(line).lower():
                print(line)
                print()


# 3.1 Запрос параметра

def ask_for_parameters():
    print('Введите параметр поиска или оставьте пустым для вывода всех данных')
    parameter = str(input('Параметр поиска: '))
    return parameter


# 4.1 Изменение и удаление данных

def change_del_data(parameter):
    change_move = int(input('Выберите требуемое изменение: "0" - удаление "1" - изменение: '))
    if change_move == 1:
        with open('save.txt') as data:
            change_list = []
            for line in data:
                if parameter in line.split():
                    print('Введите данные для изменения: ')
                    change_list.append(input(f'{line}').lower() + '\n')
                else:
                    change_list.append(line)
        with open('save.txt', 'w') as data:
            data.writelines(change_list)
    else:
        with open('save.txt') as data:
            list_del = []
            for line in data:
                if parameter in line:
                    print(f'Данные {line} удалены')
                else: list_del.append(line)
        with open('save.txt', 'w') as data:
            data.writelines(list_del)

    data.close()




input_data()
# find_with_parameters(ask_for_parameters())
change_del_data(ask_for_parameters())

