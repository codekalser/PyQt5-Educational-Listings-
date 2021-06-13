#Пример перегрузки мат операторов

class MyClass:
    def __init__(self,y):
        self.x = y
    def __add__(self, y): # + operator
        print("Экземпляр слева\n")
        return self.x + y
    def __radd__(self, y): # + operator
        print("Экземпляр справа\n")
        return self.x + y
    
    def __iadd__(self, y): # += operator
        print("Сложение с присваиванием \n")
        self.x += y
        return self

c = MyClass(50)
print(c + 10) #выведет экземпляр слева 60
print(20 + c) # выведет экземпляр справа 70
c += 30 #выведет сложение с присваиванием
print(c.x) #80

