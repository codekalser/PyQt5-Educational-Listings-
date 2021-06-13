class MyClass:
    def __enter__(self):
        print("Вызван метод __enter__()")
        return self

    def __exit__(self,Type,Value,Trace):
        print("Вызван метод __exit__()")
        if Type is None: #Если исключение не возникло
            print("исключение не возникло")

        else:
            print("Value = ", Value)
            return False #False - исключение не обработано
                        #True - исключение обработано

print("Последовательность при отсутствии исключения:\n")
with MyClass():
    print("Вызван блок внутри With")

print("\nПоследовательность при наличии исключения:\n")
with MyClass() as obj:
    print("Вызван блок внутри With")
    raise TypeError("Исключение TypeError ")
