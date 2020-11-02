import sqlite3

def create_record():
    surname = input("Фамилия\n> ")
    name = input("Имя\n> ")
    phone_number = input("Номер телефона\n")
    comment = input("Комментарии\n")
    cursor.execute(f"INSERT INTO Phonebook VALUES (NULL, '{surname}', '{name}', '{phone_number}', '{comment}')")

def find_record():
    pass

def edit_record():
    pass

def delete_record():
    pass

conn = sqlite3.connect("Phonebook.db")
run = 1
while run == 1:
    with conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Phonebook(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        surname VARCHAR,
        name VARCHAR,
        phone_number VARCHAR,
        comment VARCHAR)""")

        print("\n\tГлавное меню")
        print("1 - Создать запись\n"
              "2 - Найти запись\n"
            "3 - Редактировать запись\n"
            "4 - Удалить запись\n"
            "5 - Выход\n"
            "0 - Отобразить таблицу\n")
        user_input = int(input("Укажите необходимый пункт: \n"))
        if user_input == 1:
            create_record()
        elif user_input == 2:
            find_record()
        elif user_input == 3:
            edit_record()
        elif user_input == 4:
            delete_record()
        elif user_input == 5:
            run = 0
        elif user_input == 0:
            cursor.execute("SELECT * FROM `Phonebook`")
            rows = cursor.fetchall()
            print("ID" + "\t|\t" + "Фамилия" + "\t\t|\t" + "Имя" + "\t\t|\t\t" + "Телефон" + "\t\t|\t" + "Комментарии")
            for row in rows:
                print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3], "\t|\t", row[4])
        else:
            print("Некорректный ввод! Введите число соответствующее пункту меню!\n")
        conn.commit()
        cursor.close()