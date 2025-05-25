from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate
from gui import Ui_MainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui      =   Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(344, 435)
        self.ui.calculateDate.setDate(QDate.currentDate())
        self.ui.endDate.setDate(QDate.currentDate())
        self.ui.equal.clicked.connect(self.equal)
        self.ui.add.clicked.connect(self.func)
        self.ui.multiplication.clicked.connect(self.func)
        self.ui.minus.clicked.connect(self.func)
        self.ui.divide.clicked.connect(self.func)
        self.ui.number_0.clicked.connect(self.func)
        self.ui.number_1.clicked.connect(self.func)
        self.ui.number_2.clicked.connect(self.func)
        self.ui.number_3.clicked.connect(self.func)
        self.ui.number_4.clicked.connect(self.func)
        self.ui.number_5.clicked.connect(self.func)
        self.ui.number_6.clicked.connect(self.func)
        self.ui.number_7.clicked.connect(self.func)
        self.ui.number_8.clicked.connect(self.func)
        self.ui.number_9.clicked.connect(self.func)
        self.ui.delete_2.clicked.connect(self.func)
        self.ui.clear.clicked.connect(self.func)
        self.ui.point.clicked.connect(self.func)
        self.ui.open.clicked.connect(self.func)
        self.ui.close.clicked.connect(self.func)
        self.ui.dateButton.clicked.connect(self.func)
        self.ui.dateButton_2.clicked.connect(self.difference)

        self.ui.choose.addItems(["Ekle","Çıkar"])

    def difference(self):
        try:
            if self.ui.choose.currentIndex() == 0:
                self.ui.result.setText("{0}-{1}-{2}".format(
                    self.ui.calculateDate.date().addDays(self.ui.days.value()).getDate()[2],
                    self.ui.calculateDate.date().addDays(self.ui.days.value()).getDate()[1],
                    self.ui.calculateDate.date().addDays(self.ui.days.value()).getDate()[0])
                )

            elif self.ui.choose.currentIndex() == 1:
                self.ui.result.setText("{0}-{1}-{2}".format(
                    self.ui.calculateDate.date().addDays(self.ui.days.value()*(-1)).getDate()[2],
                    self.ui.calculateDate.date().addDays(self.ui.days.value()*(-1)).getDate()[1],
                    self.ui.calculateDate.date().addDays(self.ui.days.value()*(-1)).getDate()[0])
                )

        except Exception:
            pass

    def equal(self):
        try:
            if not (self.ui.input.text().isalpha()):
                result  =   eval(self.ui.input.text())
                self.ui.input.clear()
                if len(str(result)) <= 15:
                    self.ui.input.setText(str(result))
                else:
                    result  =   str(result)
                    result  =   f"{result[:11]}e+{len(result[11:])}"
                    self.ui.input.setText(str(result))

        except Exception:
            pass

    def func(self):
        try:
            sender  =   self.sender().text()
            txt = self.ui.input.text()
            if sender == "+":
                self.ui.input.setText(f"{txt}+")

            elif sender == "-":
                self.ui.input.setText(f"{txt}-")

            elif sender == "x":
                self.ui.input.setText(f"{txt}*")

            elif sender == "÷":
                self.ui.input.setText(f"{txt}/")

            elif sender == "1":
                self.ui.input.setText(f"{txt}1")

            elif sender == "2":
                self.ui.input.setText(f"{txt}2")

            elif sender == "3":
                self.ui.input.setText(f"{txt}3")

            elif sender == "4":
                self.ui.input.setText(f"{txt}4")

            elif sender == "5":
                self.ui.input.setText(f"{txt}5")

            elif sender == "6":
                self.ui.input.setText(f"{txt}6")

            elif sender == "7":
                self.ui.input.setText(f"{txt}7")

            elif sender == "8":
                self.ui.input.setText(f"{txt}8")

            elif sender == "9":
                self.ui.input.setText(f"{txt}9")

            elif sender == "0":
                self.ui.input.setText(f"{txt}0")

            elif sender == "del":
                self.ui.input.setText(f"{txt[:-1]}")

            elif sender.lower() == "c":
                self.ui.input.clear()

            elif sender == ",":
                self.ui.input.setText(f"{txt}.")

            elif sender == "(":
                if self.ui.tabWidget.currentIndex() == 0:
                    self.ui.input.setText(f"{txt}(")

            elif sender == ")":
                if self.ui.tabWidget.currentIndex() == 0:
                    self.ui.input.setText(f"{txt})")

            elif sender == "Hesapla":
                result  =   self.ui.startDate.date().daysTo(self.ui.endDate.date())
                if result < 0:
                    result *= -1
                self.ui.result.setText(str(result))

        except Exception as err:
            pass

def run():
    app     =   QApplication(sys.argv)
    win     =   Window()
    win.show()
    sys.exit(app.exec_())

run()
