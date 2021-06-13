class Class1: #это базовый класс
    def func1(self):
        print("Метод func1() класса Class1")

class Class2(Class1):
   def func2(self):
        print("Метод func2() класса Class2")

class Class3(Class1):
    def func1(self):
        print("Метод func1() класса Class3")
    def func2(self):
        print("Метод func2() класса Class3")
    def func3(self):
        print("Метод func3() класса Class3")
    def func4(self):
        print("Метод func4() класса Class3")

#Множественное наследование
class Class4(Class2,Class3):
    #изменяем порядок наследования
    func2 = Class3.func2
    
    def func4(self):
        print("Метод func4() класса Class4")

c = Class4()
