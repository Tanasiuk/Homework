import MyModule

try:
    MyModule.poisk(str(input("Введите текст: \n")), str(input("Введите искомый символ: \n")))
except ValueError:
    print("Сломали?!")