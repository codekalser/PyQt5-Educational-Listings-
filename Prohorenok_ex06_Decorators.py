def deco(f):
    print("Вызвана функция func()")
    return f #возвращаем ссылку на функцию

@deco #аналог func = deco(func)
def func(x):
    return "x = {0}".format(x)

print(func(10))

#Обернем функцию в два декоратора
#то же самое что и func = deco1(deco2(func))
print("Обернем функцию в два декоратора\n>>\n")
def deco1(f):
    print("Вызвана функция deco1")
    return f

def deco2(f):
    print("Вызвана функция deco2")
    return f

@deco1
@deco2
def func(x):
    return "x = {0}".format(x)

print(func(10))

#Ограничение доступа при помощи декоратора
passw = input("\n\nВведите пароль:... ")

def test_passw(p):
    def deco(f):
        if str(p) == "10": #тут сравниваем пароли
            return f
        else:
            return lambda: "Доступ завпрещен! "
    return deco #возвращаем функцию-декоратор

@test_passw(passw)
def func():
    return "Добро пожаловать!"

print(func())
