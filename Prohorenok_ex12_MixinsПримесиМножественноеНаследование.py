#Расширение функциональности классов
#посредством примесей

class Mixin: # Определяем класс-примесь
    attr = 0 # это атрибут примеси
    def mixin_method(self): #метод примеси
        print("метод примеси")

class Class1(Mixin):
    def method1(self):
        print("метод Class1")

class Class2(Class1, Mixin):
    attr = 10
    def method2(self):
        print("метод Class2")

c1 = Class1()
c1.method1()
c1.mixin_method()

c2 = Class2()
c2.method1()
c2.mixin_method()
