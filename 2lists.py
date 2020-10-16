from random import randint

def check_list(a, b):
    c = list(set(a) & set(b))
    return c


k = int(input("Укажите длину первого списка чисел:\n"))
a = [randint(1, 9) for i in range(k)]
print(a)
l = int(input("Укажите длину второго списка чисел:\n"))
b = [randint(1, 9) for j in range(l)]
print(b)

try:
    finish_list = check_list(a, b)
    print("Одинаковые элементы списков:\n", sorted(finish_list))
except ValueError:
    print("Снова сломал?!")