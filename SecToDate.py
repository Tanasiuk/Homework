def SecToDate(sec):
    oneyear = 31536000
    if sec >= oneyear:
        print ("Перевалили за год! Работаем с количеством секунду не больше года! (<=31535999)")
    if sec < oneyear:
        day = 86400
        hour = 3600
        minute = 60
        resultday = 0
        resulthour = 0
        resultminute = 0
        balancesec = sec
        while day<=balancesec:
            resultday+=1
            balancesec-= day
        while hour<=balancesec:
            resulthour+=1
            balancesec-= hour
        while minute<=balancesec:
            resultminute+=1
            balancesec-= minute
        print("Дни:часы:минуты:секунды")
        print("%d    %d    %d    %d" % (resultday, resulthour, resultminute, balancesec))
try:
    SecToDate(int(input("Укажите количество секунд:\n")))
except ValueError:
    print("Снова сломал?! Вводим количество секунд в цифрах! ")