#Пример перегрузки оператора сравнения

class MyClass:
    def __init__(self, name):
        self.name = name
        print(self.name)
        self.x = 50
        self.arr = [1,2,3,4,5]
        
    def __eq__(self,y):      #== operator
        return self.x == y
    def __contains__(self,y):#in operator
        return y in self.arr

c = MyClass("Imechko")

print("равно " if c == 50
      else "Не равно")

print("равно " if c == 51
      else "Не равно")

print("Есть такое " if 5 in c
      else "Нету")

