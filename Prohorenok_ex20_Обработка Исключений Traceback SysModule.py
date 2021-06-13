import sys, traceback
try:
    x = 1/0
except ZeroDivisionError:
    Type, Value, Trace = sys.exc_info()
    print("Type: ", Type)
    print("Value: ", Value)
    print("Trace: ", Trace)

    print("\n","print_tb()".center(40,"-"))
    traceback.print_tb(Trace, limit=1, file=sys.stdout)
    print("\n", "format_exception()".center(40,"-"))
    print(traceback.format_exception(Type, Value, Trace))
    print("\n","format_exception_only()".center(40, "-"))
    print(traceback.format_exception_only(Type, Value))

#Блоки else и finally
print("\n\n\n")
print("Блоки else и finally".center(40, "*"))
try:
    x = 10 / 2
    #x = 10 / 0
except ZeroDivisionError:
    print("Деление на ноль!")
else:
    print("It's else block ")
finally:
    print("It's finally block ")
print("\n\n\n")
