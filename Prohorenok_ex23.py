#Создание собственого исключения

try:
    raise ValueError("А-та-та так нельзя!")
except ValueError as msg:
    print(msg)

#В качестве исключения можно указать
# экземпляр пользовательского класса

class MyError(Exception):
    def __init__(self,value):
        self.msg = value
    def __str__(self):
        return self.msg

#тут обработка пользовательского исключения
try:
    raise MyError("ТАК НЕЛЬЗЯ!")
except MyError as err:
    print(err) #вызывается метод __str__()
    print(err.msg) #обращение к атрибуту класса

##повторно возбуждаем исключение

raise MyError("ТАК ВООБЩЕ НЕЛЬЗЯ!!1")
