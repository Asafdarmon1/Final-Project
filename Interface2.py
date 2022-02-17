# Final Projet
# Asaf Darmon - 205404080
# Liran Hersh - 203955299
# Doctor's Interface - Page 2

# imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


# Creating the user interface
# this code was generate by Qt5 software
class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 40, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(70, 120, 300, 300))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(470, 150, 255, 205))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "X-Ray Program"))
        self.label.setText(_translate("SecondWindow", "Detection Complete!"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SecondWindow", "Disease:"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SecondWindow", "Probability:"))
        qpixmap = QPixmap('C:/Final Project Liran/cam.png')
        self.imageLabel.setPixmap(qpixmap)
        self.predictions = []
        
    # Open Prediction Txt File and insert the prediction
    # information to the patient final table
        with open('predictions.txt', 'r') as f:
            my_text = f.read()
            lst = my_text.split((" "))
            for i in lst:
                if i != "":
                    self.predictions.append(i)
            self.tableWidget.setRowCount(4)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Effusion"))
            self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(round((float(self.predictions[0]) * 100),3)) + "%"))
            self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Infiltartion"))
            self.tableWidget.setItem(1 ,1, QtWidgets.QTableWidgetItem(str(round((float(self.predictions[1]) * 100),3)) + "%"))
            self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem("Normal"))
            self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(str(round((float(self.predictions[2]) * 100),3)) + "%"))
            self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem("Pneumonia"))
            self.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(str(round((float(self.predictions[3]) * 100),3)) + "%"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
