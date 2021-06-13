class MyClass:
    def __init__(self, name):
        self.i = 20
        self.name = name
    def __call__(self):
        print(self.name)
    def __getattr__(self, attr):
        print("\nвызван метод __getattr__()\n")
        return 0
    def __getattribute__(self,attr):
        print("\nвызван метод __getattribut__()\n")
        return object.__getattribute__(
            self,attr) #Только такой вызов!
    def __setarrt__(self, attr, value):
        print("Was called __setattr__() \n")
        self.__dict__[attr] = value #Только такой вызов!

#__getattr__ method probe here
c = MyClass("__getattr__ method probe here")
print(c.i, " - атрибут i существует",
      "\n И поэтому метод __getattr__ не вызывается\n")
print(c.s, " - атрибут s НЕ существует",
      "\n И поэтому вызывается метод __getattr__\n")
print("c.i = ", c.i)
#__call__ method probe here
c1 = MyClass("Value One")
c2 = MyClass("Value Two")
c1() #позволяет вызвать экземпляр класса
c2() #как функцию

c = MyClass(" ")
c.i = 10
print("c.i =" , c.i)

