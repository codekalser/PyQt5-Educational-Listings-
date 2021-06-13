import os
try:
    os.rename(r"file4.txt", "file.txt")
except OSError:
    print("Файл не удалось переименовать")
else:
    print("Файл успешно переименован")
