class MyClass:
    pass

MyClass.x = 50 #создаем атрибут объекта класса
c1, c2 = MyClass(), MyClass() #экземпляры
c1.y = 10 #атрибут экземпляра класса
c2.y = 20

print(c1.x, c1.y)
print(c2.x, c2.y)
