f1 = lambda: 10 + 20
f2 = lambda x, y: x + y
f3 = lambda x, y, z: x + y + z

print(f1(),
      f2(5,10),
      f3(5,10,30)
    )

arr = ["единица1","Единый","Единица2"]
arr.sort(key=lambda s: s.lower())

for i in arr:
    print(i, end="\n")

#Пример функции-генератора
def func(x,y):
    for i in range(1, x+1):
        yield i**y

for n in func(10,2):
    print(n, end=" ")

#или
i = func(3,3)
print('\n',i.__next__())
print(i.__next__())
print(i.__next__())
