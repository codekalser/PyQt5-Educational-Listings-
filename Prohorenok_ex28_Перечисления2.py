#Перечисление, включающее атрибуты и методы

from enum import Enum
class VersionExtended(Enum):
    V2_7 = "2.7"
    V3_6 = "3.6"
    V3_9 = "3.9.1"

    #Методы экземпляра класса.
    #вызываются у элемента перечисления
    def describe(self):
        return self.name, self.value
    def __str__(self):
        return str(__class__.__name__) + "." + \
               self.name + ": " + self.value

    #Метод объекта класса.
    #Вызывается у самого перечисления
    @classmethod #этим декоратором создаются методы класса
    def getmostfresh(cls):
        return cls.V3_9
    
    
    
