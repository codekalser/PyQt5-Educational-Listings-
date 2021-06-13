import sys
tmp_in = sys.stdin #созраняем ссылку на sys.stdin
f = open(r"file.txt", "r") #файл открыт на чтение
sys.stdin = f #перенаправляем ввод

while True:
    try:
        line = input() #читаем сроку из файла
        print(line)    #выводим строку
    except EOFError:   #если достигнут конец файла
        break          #выходим из цикла
sys.stdin = tmp_in     #восстан стандартный ввод
f.close()

