def create_record():
    pass

def find_record():
    pass

def edit_record():
    pass

def delete_record():
    pass


run = 1
while run == 1:
    print("Главное меню\n")
    print("1 - Создать запись\n"
          "2 - Найти запись\n"
          "3 - Редактировать запись\n"
          "4 - Удалить запись\n"
          "5 - Выход")
    user_input = input("Укажите необходимый пункт: \n")
    try:
        if int(user_input) == 1:
            create_record()
        elif int(user_input) == 2:
            find_record()
        elif int(user_input) == 3:
            edit_record()
        elif int(user_input) == 4:
            delete_record()
        elif int(user_input) == 5:
            run = 0
        else:
            print("Некорректный ввод! Введите число соответствующее пункту меню!\n")
            run = 0
    except ValueError:
        print("Снова сломал?!")
