class Version:
    def __init__(self, major, minor, sub):
        self.__major = major
        self.__minor = minor
        self.__sub = sub
    def __str__(self):
        return str(self.__major) + "." + str(self.__minor)\
               + "." + str(self.__sub)
    def __getitem__(self, k):
        if k == "major":
            return self.__major
        elif k == "minor":
            return self.__minor
        elif k == "sub":
            return self.__sub
        else:
            raise IndexError
    def __setitem__(self, k, v):
        if k == "major":
            self.__major = v
        elif k == "minor":
            self.__minor = v
        elif k == "sub":
            self.__sub = v
        else:
            raise IndexError
    def __delitem__(self, k):
        raise TypeError
    def __contaons__(self, v):
        return v == "major" or v == "minor" or v == "sub"
    
