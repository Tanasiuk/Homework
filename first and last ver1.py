def firstnlast(a):
    newlist = " ".join(str(x) for x in a)
    print("Первый элемент списка:", newlist[0])
    print("Последний элемент списка:", newlist[-1])

try:
    y = int(input("Укажите длину массива:\n"))
    a = [int(input("Введите число массива:\n")) for i in range(y)]
    print("\nМасссив чисел:\n", a)
    firstnlast(a)
except ValueError:
    print("Опять сломал?!")