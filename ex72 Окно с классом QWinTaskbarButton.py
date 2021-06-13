from PyQt5 import QtCore, QtWidgets, QtGui, QtWinExtras
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window |
                                                       QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Класс QWinTaskbarButton")
        # Создаем оба значка
        self.icon1 = QtGui.QIcon("icon1.png")
        self.icon2 = QtGui.QIcon("icon2.png")
        # Создаем кнопку панели задач
        self.taskbarButton = QtWinExtras.QWinTaskbarButton(parent=self)
        # Создаем все три кнопки
        hbox = QtWidgets.QHBoxLayout()
        btnIcon1 = QtWidgets.QPushButton(self.icon1, "Значок &1")
        btnIcon1.clicked.connect(self.setIcon1)
        hbox.addWidget(btnIcon1)
        btnIcon2 = QtWidgets.QPushButton(self.icon2, "Значок &2")
        btnIcon2.clicked.connect(self.setIcon2)
        hbox.addWidget(btnIcon2)
        btnClearIcon = QtWidgets.QPushButton("&Убрать значок")
        btnClearIcon.clicked.connect(self.taskbarButton.clearOverlayIcon)
        hbox.addWidget(btnClearIcon)
        self.setLayout(hbox)
        self.resize(200, 50)
        # После вывода окна на экран привязываем его к кнопке панели задач
    def showEvent(self, evt):
        self.taskbarButton.setWindow(self.windowHandle())
        # Выполняем задание новых значков для кнопки панели задач при нажатии
        # кнопок
    def setIcon1(self):
        self.taskbarButton.setOverlayIcon(self.icon1)
    def setIcon2(self):
        self.taskbarButton.setOverlayIcon(self.icon2)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())