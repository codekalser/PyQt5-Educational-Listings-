class ReverseString:
    def __init__(self, s):
        self.__s = s
    def __iter__(self):
        self.__i = 0
        return self
    def __next__(self):
        if self.__i > len(self.__s) - 1:
            raise StopIteration
        else:
            a = self.__s[-self.__i - 1]
            self.__i = self.__i + 1
            return a
    def __len__(self): 
        return len(self.__s)
    def __str__(self):
        return self.__s[::-1]
    
s = str(ReverseString("Argentina Manit Negra"))
      
    
print(''.join(s), end="")
