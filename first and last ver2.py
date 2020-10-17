def firstnlast(a):
    try:
        new_list = list(int(item) for item in a.split())
        print("Массив чисел:", new_list)
        print("Первый элемент списка:", new_list[0])
        print("Последний элемент списка:", new_list[-1], "\n")
    except ValueError:
        print("Снова сломал?! Работаем с числами!\n")

firstnlast (input("Введите последовательность цифр через пробел:\n"))