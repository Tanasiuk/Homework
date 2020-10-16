from datetime import datetime, timedelta

def SecToDate():
    sec = timedelta(seconds=int(input("Укажите количество секунд:\n")))
    t = datetime(1,1,1) + sec
    print("Дни:часы:минуты:секунды")
    print("%d    %d    %d    %d" % (t.day-1, t.hour, t.minute, t.second))
try:
    SecToDate()
except ValueError:
    print("Снова сломал?!")