#Переопределение методов

class Class1:
    def __init__(self):
        print("Конструктор базового класса")
    def func1(self):
        print("Метод func1() базового класса Class1")


class Class2(Class1): #Class2 наследует Class1
    def __init__(self):
        print("Конструктор производного класса")
        #Class1.__init__(self) #Вызываем конструктор
        super().__init__()     #базового класса
    def func1(self):
        print("Это метод func1() класса Class2")
        Class1.func1(self) #вызываем метод базового класса

c = Class2() #создаем экземпляр класса Class2
c.func1() #вызываем метод func1
