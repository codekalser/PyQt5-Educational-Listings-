from PyQt5 import QtCore, QtWidgets, QtWinExtras
import sys, time

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Список быстрого доступа")
        # Создаем сам список быстрого доступа и очищаем его
        jumpList = QtWinExtras.QWinJumpList(parent=self)
        jumpList.clear()
        # Получаем категорию последних открывавшихся документов
        recent = jumpList.recent()
        # Создаем пункт "Лицензия Python" и добавляем его в эту категорию
        item1 = QtWinExtras.QWinJumpListItem(QtWinExtras.QWinJumpListItem.Link)
        item1.setFilePath(r"C:\Windows\notepad.exe")
        item1.setTitle("Лицензия Python")
        item1.setArguments([r"C:\Windows"])
        recent.addItem(item1)
        # Делаем категорию видимой
        recent.setVisible(True)
        # Получаем категорию часто открываемых документов, добавляем в
        # нее пункт "Новости Python" и делаем видимой
        frequent = jumpList.frequent()
        frequent.addLink("Новости Python", r"C:\totalcmd")
        frequent.setVisible(True)
        # Получаем категорию задач, добавляем в нее пункт "Блокнот",
        # разделитель, пункт "Write" и делаем видимой
        tasks = jumpList.tasks()
        tasks.addLink("Блокнот", r"C:\Windows\notepad.exe")
        tasks.addSeparator()
        tasks.addLink("Write", r"C:\Windows\write.exe")
        tasks.setVisible(True)
        # Создаем произвольную категорию "Инструменты"
        otherCat = QtWinExtras.QWinJumpListCategory()
        otherCat.setTitle("Инструменты")
        # Добавляем в нее пункт "Python" и также делаем видимой
        otherCat.addLink("Флэшечка", r"C:\бэкапфлешки19янв2020")
        otherCat.setVisible(True)
        jumpList.addCategory(otherCat)
        self.resize(200, 50)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())