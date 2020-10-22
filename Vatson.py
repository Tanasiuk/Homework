def vatson(a):
    try:
        c = list(int(item) for item in a.split())
        print("Массив чисел:", c)
        b = sum(c)
        print("Сумма чисел массива =", b)
    except ValueError:
        print("Снова сломал?! Работаем с целыми числами через пробел!\n")

vatson(input("Введите последовательность целых чисел через пробел:\n"))