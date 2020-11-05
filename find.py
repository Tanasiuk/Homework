import sqlite3

def find_record():
    conn = sqlite3.connect("Phonebook.db")
    cursor = conn.cursor()
    print("\n\nДоступные варианты поиска:\n"
          "1 - Фамилия\n"
          "2 - Имя\n"
          "3 - Телефон")
    run_find = 1
    searching = ""
    while run_find > 0:
        print("\nВведите '5' для выхода в 'Главное меню'")
        searching_row = input("\nВведите номер поля для поиска:\n")
        if int(searching_row) == 5:
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
                print(searching_row)
            with conn:
                cursor.execute("SELECT * FROM Phonebook WHERE {} LIKE '%{}%'".format(searching, desired_value))
                results = cursor.fetchall()
                notfind = []
                if results == notfind:
                    print("Нет данных по даному запросу!")
                else:
                    print("ID" + "\t|\t" + "Фамилия" + "\t\t|\t" + "Имя" + "\t\t|\t\t" + "Телефон"
                          + "\t\t|\t" + "Комментарии")
                    for row in results:
                        print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3], "\t|\t", row[4])