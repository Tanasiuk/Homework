def poisk(a, b):
    for i in b:
        count = a.count(i)
        if count >= 1:
            print("Символ:", i)
            print("Встречается:", count, "раз(-а)")
try:
    poisk(str(input("Введите текст: \n")), str(input("Введите искомый символ: \n")))
except ValueError:
    print("Сломали?!")