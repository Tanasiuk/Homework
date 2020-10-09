def justdoit(a,b,c):
    while a<b:
        a+=c
        if a<b:
            print(a, "- Пока что нет!")
        elif a>b:
            print(a, "- Немного переборщили, но конечное число достигнуто...")
        else:
            print("Дождались! -", a)
try:
    justdoit(
        int(input("Введите начальное число:\n")),
        int(input("Введите конечное число:\n")),
        int(input("Укажите шаг:\n")))
except ValueError:
    print("\nНеккоректные данные ввода! Работаем с целыми числами!")