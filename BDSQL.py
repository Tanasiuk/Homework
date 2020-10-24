import sqlite3

print("1 - Добавить запись в БД\n"
      "2 - Отобразить БД")
choice = int(input("> "))
conn = sqlite3.connect("Worker.db")
with conn:
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Worker (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        surname VARCHAR,
        name VARCHAR,
        position VARCHAR)""")
    if choice == 1:
        surname = input("Фамилия\n> ")
        name = input("Имя\n> ")
        position = input("Должность\n ")
        cursor.execute(f"INSERT INTO `Worker` VALUES (NULL, '{surname}', '{name}', '{position}')")
    elif choice == 2:
        cursor.execute("SELECT * FROM `Worker`")
        rows = cursor.fetchall()
        print("ID" + "\t|\t" + "Фамилия" + "\t\t|\t" + "Имя" + "\t\t|\t" + "Должность")
        for row in rows:
            print(row[0], "\t|\t", row[1], "\t|\t", row[2], "\t|\t", row[3])
    else:
        print("Снова сломал?!")
    conn.commit()
    cursor.close()