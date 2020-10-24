def newslovar(dict1, dict2):
    newslovar = dict1.copy()
    newslovar.update(dict2)
    return newslovar

def slovar1_2(a, b):
    slovar1 = {}
    slovar2 = {}
    id_counter = 0
    for i in a:
        id_counter += 1
        slovar1[str(id_counter)] = i
    for j in b:
        id_counter += 1
        slovar2[str(id_counter)] = j
    print(newslovar(slovar1, slovar2), "\n")
print("Данные вводим слитно, не разделяем пробелами, запятыми и т.п.")
slovar1_2(
    input("Введите данные первого словаря:\n"),
    input("Введите данные второго словаря:\n"))