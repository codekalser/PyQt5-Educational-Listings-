#Перечисления с элементами произвольного
#типа

from enum import Enum, IntEnum, unique

#при помощи декоратора unique объявляем, что
#переменая хранит только уникальные значения

@unique
class Versions(Enum):
    V2_7 = "2.7"
    V3_9 = "3.9"
    MostFresh = "3.9.1"

class Colors(IntEnum):
    Red = 1
    Green = 2
    Blue = 3

print(Colors.Blue,"\n",
      Colors["Red"],"\n",
      Colors(2),"\n",
      Colors.Red.name,"\n",
      Colors.Red.value, "\n",
      list(Colors))
for c in Colors:
    print(c.value, end = " ")
