try:
    x = 1/0
except ZeroDivisionError:
    print("Delenie na nol'!11")
    x = 0
print(x)

#вложенные исключения
try:
    try:
        x = 1 / 0
    except NameError:
        print("Hernya kakaya-to")
    except IndexError:
        print("Indexa netu!")
    print("Ololo")
except ZeroDivisionError:
    print("Horosh blin delit' na nol'!")
    x = 0
print(x)

#Обработка нескольких исключений
try:
    x = 1 / 0
except (NameError, IndexError, ZeroDivisionError):
    x = 0
print(x)    

try:
    x = 1 / 0
except (NameError, IndexError,
        ZeroDivisionError) as err:
    print(err.__class__.__name__)
    print(err)
    x = 0
print(x)    
