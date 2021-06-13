#Суммирование неопределенного количества чисел

print("Введите слово 'stop' для получения результата\n")
summa = 0
while True:
    x = input("Введите число: \n")
    
    if x == "stop":
        break
    try:
        x = int(x)
    except ValueError:
        print("Необходимо ввести целое число!")
    else:
        summa += x
print("Сумма чисел равна: ", summa)
