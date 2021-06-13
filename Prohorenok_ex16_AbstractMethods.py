#Абстрактные методы содержат только методы
#без реализаии. Реализует их производный класс

class Class1:
    def func(self, x): #это абстрактный метод
        #Генерим исключение с помощью raise
        raise NotImplementedError("Необходимо" +
                                  " переопределить"+
                                  " метод")

class Class2(Class1): #наследуем абстр метод из класса1
    def func(self,x): #переопределяем метод
        print(x)

class Class3(Class1):
    pass # Класс не переопределяет метод

c2 = Class2()
c2.func(50)

c3 = Class3()
try:
    c3.func(50)
except NotImplementedError as msg:
    print(msg)
