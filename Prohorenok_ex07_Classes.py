class MyClass:
    def __init__(self): #Конструктор класса
        self.x = 10 #Атрибут экземпляра класса

    def print_x(self): #self - это ссылка на
        print(self.x)  #экземпляр класса
    def get_x(self):
        return self.x
    
c = MyClass()
c.print_x()
print(c.x,
      getattr(c,"x"),
      getattr(c, "get_x")(),
      getattr(c, "y", "Netu!"), "\n sozdaem:\n",
      setattr(c, "y", 20),
      getattr(c, "y",0),
      delattr(c, "y"),
      hasattr(c, "x"),
      hasattr(c, "y")
      )


        
