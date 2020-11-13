import sqlite3

def edit_record():
    conn = sqlite3.connect("Phonebook.db")
    cursor = conn.cursor()
    print("\n\nДоступные варианты поиска:\n"
          "1 - Фамилия\n"
          "2 - Имя\n"
          "3 - Телефон")
    run_find = 1
    run_edit = 0
    searching = ""
    while run_find == 1:
        print("\nВведите '5' для выхода в 'Главное меню'")
        searching_row = input("\nВведите номер поля для поиска:\n")
        if not searching_row.isnumeric():
            print("Укажите цифру соотвествующую пункту меню!\n")
            run_find = 0
        elif int(searching_row) == 5:
            run_find = 0
        elif (int(searching_row) >= 6 or int(searching_row) == 4):
            print("Некорректный ввод! Введите число соответствующее пункту меню!\n")
        else:
            desired_value = input("Введите нужные данные: ")
            if int(searching_row) == 1:
                searching = 'surname'
            elif int(searching_row) == 2:
                searching = 'name'
            elif int(searching_row) == 3:
                searching = 'phone_number'
            with conn:
                cursor.execute("SELECT * FROM Phonebook WHERE {} LIKE '%{}%'".format(searching, desired_value))
                results = cursor.fetchall()
                notfind = []
                if results == notfind:
                    print("Нет данных по даному запросу!")
                    run_edit = -1
                else:
                    print("ID" + "\t|\t" + "Фамилия" + "\t\t|\t" + "Имя" + "\t\t|\t\t" + "Телефон"
                          + "\t\t|\t" + "Комментарии")
                    for row in results:
                        print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3], "\t|\t", row[4])
                run_edit += 1

        while run_edit == 1:
            print("\n\nДоступные варианты редактирования:\n"
                  "1 - Фамилия\n"
                  "2 - Имя\n"
                  "3 - Телефон")
            editing = ""
            print("\nВведите '5' для выхода в предыдущее меню")
            editing_row = input("\nВведите номер поля для редактирования:\n")
            if int(editing_row) == 5:
                run_edit = 0
            elif (int(editing_row) >= 6 or int(editing_row) == 4):
                print("Некорректный ввод! Введите число соответствующее пункту меню!\n")
            else:
                new_value = input("Введите новое значение: ")
                if int(editing_row) == 1:
                    editing = 'surname'
                elif int(editing_row) == 2:
                    editing = 'name'
                elif int(editing_row) == 3:
                    editing = 'phone_number'
                with conn:
                    cursor.execute("UPDATE Phonebook SET {} = '{}' WHERE {} LIKE '%{}%'"
                                   .format(editing, new_value, searching, desired_value))
                    print("Запись изменена!")
                    run_edit = 0
                    run_find = 0