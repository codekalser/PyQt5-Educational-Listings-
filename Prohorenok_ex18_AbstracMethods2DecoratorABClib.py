from abc import ABCMeta, abstractmethod
class Class1(metaclass=ABCMeta):
    @abstractmethod
    def func(self, x):
        pass


class Class2(Class1):
    def func(self, x):
        print(x)

c2  = Class2()
c2.func(50)
