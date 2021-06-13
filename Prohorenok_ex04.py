from timeit import Timer


#Примеры функций

def print_ok():
    """ Пример функции без параметров """
    print("I'm okay ")

def echo(m):
    """ Пример функции с параметром """
    print(m)

def summa(x, y):
    """ Пример функции с параметрами,
    возвращающей сумму двух переменных """
    return x + y


def func(f, a, b):
    """ Через переменную f будет доступна
    ссылка на функцию summa() """
    return f(a,b)
print('func(summa, 10, 20) = ',
      func(summa, 10, 20))

f = summa
v = f(10,20)
print(v)

print_ok()
echo(123)
x = summa(4333,555)
a, b = 10, 50
y = summa(a,b)

code1 = """\
def summa(x, y):
    return x + y
x = summa(4333,555)
"""
t1 = Timer(stmt=code1)
print(round(min(t1.repeat(repeat = 100,
                    number = 1000)),5))

code2 = """\
x = sum([4333,555])
"""
t2 = Timer(stmt=code2)
print(round(min(t2.repeat(repeat = 100,
                    number = 1000)),5))

#пример передачи значений из кортежа и списка
def summa(a, b, c):
    return a + b + c
t1, arr = (1,2,3), [1,2,3]
print(summa(*t1)) #распаковываем кортеж
print(summa(*arr)) #распаковываем список
t2 = (2,4)
print(summa(1,*t2))
d1 = {"a":1, "b": 2, "c": 3}
print('распаковывaем словарь ** ', summa(**d1))#распаковывем словарь

#Передача изменяемого объекта в функцию
def func(a,b):
    a = a[:]
    b = b.copy()
    a[0], b["a"] = "str", 800
x = [1,2,3]
y = {"a":1, "b":2}
func(x,y)
print(x[:],y.copy())

#Сумма произвольного количества параметров
def summa(*t):
    res = 0
    for i in t:
        res += i
    return res
print(summa(10,20))
print("Вот сейчас их реально дофига ",
      summa(10,20,30,40,50,60,70,80))

#Две звездочки сохраняют данные в словарь
def func(**d):
    for i in d:
        print("{0} => {1}".format(i,d[i], end = " "))
func(a=1,b=2,c=3)    


