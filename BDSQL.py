import sqlite3

print("1 - Добавить запись в таблицу Работник\n"
      "2 - Отобразить таблицу Работник\n"
      "3 - Отобразить таблицу Зарплата\n"
      "4 - Отобразить таблицу Должность\n")

choice = int(input("> "))
conn = sqlite3.connect("MyDB.db")
with conn:
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Worker (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        surname VARCHAR,
        name VARCHAR,
        position VARCHAR,
        salary VARCHAR)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Salary (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname VARCHAR,
        name VARCHAR,
        salary VARCHAR,
        FOREIGN KEY (user_id) REFERENCES Worker (ID))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Position (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname VARCHAR,
        name VARCHAR,
        position VARCHAR,
        FOREIGN KEY (user_id) REFERENCES Worker (ID))""")

    if choice == 1:
        surname = input("Фамилия\n> ")
        name = input("Имя\n> ")
        position = input("Должность\n")
        salary = input("Зарплата\n")
        cursor.execute(f"INSERT INTO Worker VALUES (NULL, '{surname}', '{name}', '{position}', '{salary}')")
        cursor.execute(f"INSERT INTO Salary VALUES (NULL, '{surname}', '{name}', NULL)")
        cursor.execute("""UPDATE Salary SET salary =
                      (SELECT salary FROM Worker WHERE Salary.user_id = Worker.id)""")
        cursor.execute(f"INSERT INTO Position VALUES (NULL, '{surname}', '{name}', NULL)")
        cursor.execute("""UPDATE Position SET position =
                      (SELECT position FROM Worker WHERE Position.user_id = Worker.id)""")
    elif choice == 2:
        cursor.execute("SELECT * FROM `Worker`")
        rows = cursor.fetchall()
        print("ID" + "\t|\t" + "Фамилия" + "\t\t|\t" + "Имя" + "\t\t|\t" + "Должность" + "\t\t|\t" + "Зарплата")
        for row in rows:
            print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3], "\t\t|\t", row[4])
    elif choice == 3:
        cursor.execute("SELECT * FROM Salary")
        rows = cursor.fetchall()
        print("ID" + "\t|\t" + "Фамилия" + "\t\t|\t" + "Имя" + "\t\t|\t" + "Зарплата")
        for row in rows:
            print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3])
    elif choice == 4:
        cursor.execute("SELECT * FROM Position")
        rows = cursor.fetchall()
        print("ID" + "\t|\t" + "Фамилия" + "\t\t|\t" + "Имя" + "\t\t|\t" + "Должность")
        for row in rows:
            print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3])
    else:
        print("Снова сломал?!")
    conn.commit()
    cursor.close()