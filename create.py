import sqlite3

def create_record():
    surname = input("Фамилия\n> ")
    name = input("Имя\n> ")
    phone_number = input("Номер телефона\n")
    comment = input("Комментарии\n")

    conn = sqlite3.connect("Phonebook.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Phonebook VALUES (NULL, '{surname}', '{name}', '{phone_number}', '{comment}')")
    conn.commit()