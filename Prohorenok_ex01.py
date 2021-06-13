import time
import locale
#first sposob
d = ["понедельник","вторник","среда",
     "четверг","пятница","суббота",
     "воскресенье"]

m = ["","январz","февралz","март",
     "апреля","май","июнь","июль",
     "август","сентябрь","октябрь",
     "ноябрь","декабрь"]


t = time.localtime()

print("Сегодня: \n%s %s %s %s %02d:%02d:%02d\n%02d.%02d.%02d\n"%(
    d[t[6]], t[2], m[t[1]], t[0], t[3],
      t[4], t[5], t[2], t[1], t[0]))

time.sleep(1)

#second sposob
locale.setlocale(locale.LC_ALL, "Russian_Russia.1251")
s = "Сегодня:\n%A %d %b %Y %H:%M:%S\n%d.%m.%Y"
print(time.strftime(s))

