# Final Projet
# Asaf Darmon - 205404080
# Liran Hersh - 203955299
# Doctor's Interface - Page 1


# imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget
import numpy as np
import json
from generator import AugmentedImageSequence
from Interface2 import Ui_SecondWindow
import tensorflow as tf
from keras.models import load_model
import cv2
from keras import backend as kb



# Creating the user interface
# this code was generate by Qt5 software
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 622)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setWindowIcon(QtGui.QIcon("docXray.icon"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(230, 20, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setScaledContents(True)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(140, 100, 531, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.addPhotoLabel = QtWidgets.QLabel(self.centralwidget)
        self.addPhotoLabel.setGeometry(QtCore.QRect(270, 440, 311, 31))
        self.addPhotoLabel.setFont(font)
        self.addPhotoLabel.setStyleSheet("color: rgb(0, 170, 0);")
        self.addPhotoLabel.setObjectName("addPhotoLabel")
        self.addPhotoLabel.setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.vLabel = QtWidgets.QLabel(self.centralwidget)
        self.vLabel.setGeometry(QtCore.QRect(230, 430, 71, 51))
        self.vLabel.setFont(font)
        self.vLabel.setStyleSheet("color: rgb(0, 170, 0);")
        qpixmap = QPixmap('C:/Final Project Liran/v.png')
        self.vLabel.setPixmap(qpixmap)
        self.vLabel.setObjectName("vLabel")
        self.vLabel.setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 160, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.searchType = QtWidgets.QComboBox(self.centralwidget)
        self.searchType.setGeometry(QtCore.QRect(270, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchType.setFont(font)
        self.searchType.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchType.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchType.setObjectName("searchType")
        self.searchType.addItem("")
        self.searchType.addItem("")
        self.clientEditText = QtWidgets.QTextEdit(self.centralwidget)
        self.clientEditText.setGeometry(QtCore.QRect(390, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.clientEditText.setFont(font)
        self.clientEditText.setAutoFillBackground(False)
        self.clientEditText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clientEditText.setObjectName("clientEditText")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(330, 240, 101, 41))
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton.setObjectName("okButton")
        self.clientTable = QtWidgets.QTableWidget(self.centralwidget)
        self.clientTable.setGeometry(QtCore.QRect(70, 307, 647, 69))
        self.clientTable.setObjectName("clientTable")
        self.clientTable.setColumnCount(5)
        self.clientTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setHorizontalHeaderItem(4, item)
        self.addPhotoButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPhotoButton.setGeometry(QtCore.QRect(330, 400, 111, 31))
        self.addPhotoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addPhotoButton.setObjectName("addPhotoButton")
        self.classifyButton = QtWidgets.QPushButton(self.centralwidget)
        self.classifyButton.setGeometry(QtCore.QRect(630, 480, 111, 31))
        self.classifyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.classifyButton.setObjectName("classifyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.stop_threads = False
        
        # Load our Model
        self.model = load_model('./DenseNet121-model.h5')
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "X-Ray Program"))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome Doctor"))
        self.label_2.setText(_translate("MainWindow", "Choose Type:"))
        self.label.setText(_translate("MainWindow", "Search Client:"))
        self.addPhotoLabel.setText(_translate("MainWindow", "Photo was added successfully"))
        self.searchType.setItemText(0, _translate("MainWindow", "ID"))
        self.searchType.setItemText(1, _translate("MainWindow", "Full Name"))
        self.okButton.setText(_translate("MainWindow", "OK"))
        self.okButton.clicked.connect(self.pressed)
        item = self.clientTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "First Name:"))
        item = self.clientTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name:"))
        item = self.clientTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID:"))
        item = self.clientTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Age:"))
        item = self.clientTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Previous Diseases"))
        self.clientTable.setVisible(False)
        self.addPhotoButton.setText(_translate("MainWindow", "Add Photo"))
        self.addPhotoButton.setVisible(False)
        self.addPhotoButton.clicked.connect(self.openFileDialog)
        self.classifyButton.setText(_translate("MainWindow", "Classify"))
        self.classifyButton.setDisabled(True)
        self.classifyButton.clicked.connect(self.predict)

        # Global variables
        self.lst = []
        self.filePath = ""
        self.output_path = 'C:/Final Project Liran/cam.png'
        self.predictions = []


# This function is responsible of checking user input 
# and insert the information from "patient.json" file
# into the patient table on the doctors inteface
    def pressed(self):
        temp = []
        self.found = 0
        self.lst.clear()
        textValue = self.clientEditText.toPlainText()
        if textValue == "":
            self.showErrorPopUp("Please Fill Up The Form!")
        else:
            with open('patient.json') as f:
                data = json.load(f)

            if self.searchType.currentText() == "Full Name":
                # Search patient via Full Name
                for client in data['clients']:
                    if client['First_Name'] + " " + client['Last_Name'] == textValue:
                        temp.append(json.dumps(client['First_Name']))
                        temp.append(json.dumps(client['Last_Name']))
                        temp.append(json.dumps(client['Id']))
                        temp.append(json.dumps(client['Age']))
                        temp.append(json.dumps(client['Previous_Diseases']))
                if len(temp) == 0:
                    self.showErrorPopUp("There is no client with the name: " + textValue)
                else:
                    self.found = 1

            else:
                # Search patient by ID
                for client in data['clients']:
                    if client['Id'] == textValue:
                        self.classifyButton.setDisabled(False)
                        temp.append(json.dumps(client['First_Name']))
                        temp.append(json.dumps(client['Last_Name']))
                        temp.append(json.dumps(client['Id']))
                        temp.append(json.dumps(client['Age']))
                        temp.append(json.dumps(client['Previous_Diseases']))
                if len(temp) == 0:
                    self.showErrorPopUp("There is no client with the ID: " + textValue)
                else:
                    self.found = 1

            # Here we found a client by id or full name, insert data to client table
            if self.found == 1:
                for i in range(len(temp)):
                    s = temp[i]
                    x = s.rfind("'")
                    y = s[:x].rfind("'")
                    self.lst.append(s[y + 2:x])
                self.clientTable.setRowCount(1)
                self.clientTable.setItem(0, 0, QtWidgets.QTableWidgetItem(self.lst[0]))
                self.clientTable.setItem(0, 1, QtWidgets.QTableWidgetItem(self.lst[1]))
                self.clientTable.setItem(0, 2, QtWidgets.QTableWidgetItem(self.lst[2]))
                self.clientTable.setItem(0, 3, QtWidgets.QTableWidgetItem(self.lst[3]))
                self.clientTable.setItem(0, 4, QtWidgets.QTableWidgetItem(self.lst[4]))
                self.clientTable.setVisible(True)
                self.addPhotoButton.setVisible(True)
                
                

# function to show error if values are empty
    def showErrorPopUp(self, String):
        msg = QMessageBox()
        msg.setWindowTitle("Error Message!")
        msg.setText(String)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Retry)
        msg.exec_()
        
        
# this function opens Doctor Interface - page 2
    def openPage2(self):
        self.lst = []
        predx = str(self.prediction)
        predy = predx.replace("[", "")
        pred = predy.replace("]", "")
        # save predictions to txt file
        with open('predictions.txt', 'w') as f:
            my_text = pred
            f.write(my_text)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()


# This function opens the file explorer in the doctor's computer
    def openFileDialog(self):

        self.fname = QFileDialog.getOpenFileName(self, 'open file', 'C:\Final Project Liran\Test')
        self.filePath = self.fname[0]
        if self.filePath == "":
            self.showErrorPopUp("Please Choose Photo")
        else:
            self.addPhotoLabel.setVisible(True)
            self.vLabel.setVisible(True)
            self.classifyButton.setDisabled(False)
            
            
        
# Prediction and Grad-Cam Task
# Load image, classify it using our model and color the infected
# area with heat map.
# this function is the backend of our model classification
       
    def predict(self):
        
        # Prediction
        def get_output_layer(model, layer_name):
            # get the symbolic outputs of each "key" layer (we gave them unique names).
            layer_dict = dict([(layer.name, layer) for layer in model.layers])
            layer = layer_dict[layer_name]
            return layer

        # Switch Case
        def disease_index(argument):
            switcher = {
                0: "Effusion",
                1: "Infiltration",
                2: "Normal",
                3: "Pneumonia"
            }
            return switcher.get(argument, "nothing")


        self.class_names = ["Effusion", "Infiltration", "Normal", "Pneumonia"]
        self.output_path = 'C:/Final Project Liran/cam.png'
        
        # Load image and process it to create prediction
        img_transformed = tf.keras.preprocessing.image.img_to_array(
            tf.keras.preprocessing.image.load_img(self.filePath,
                                                  target_size=(224, 224)), dtype=np.float32)
        # create predictions
        predict_img = img_transformed
        predict_img = np.expand_dims(predict_img, axis=0)
        predict_img = predict_img / 255
        
        # Prediction Task
        self.prediction = self.model.predict(predict_img)
        np.set_printoptions(suppress=True)
        
        # Get max value from the result array
        result = np.argmax(self.prediction)
        
        # Replace's Switch Case
        label = disease_index(result)

        # Load original photo
        original = cv2.imread(self.filePath)

        # If label is Normal, we do not want to create heatmap on it.
        if label == "Normal":
            print("Image Is Normal, GradCam Not Necessary")
            img = original
            cv2.putText(img, text=label, org=(150, 150), fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(255, 255, 67), thickness=1)
            img = cv2.resize(img, dsize=(300, 300))
            cv2.imwrite(self.output_path, img)
        else:
            index = self.class_names.index(label)
            
        # Classification preprocessing, augment and target size
            cam_sequence = AugmentedImageSequence(
                class_names=self.class_names,
                batch_size=1,
                target_size=(224, 224),
                augmenter=None,
                steps=1,
            )
            
            # CAM overlay
            # Get the input weights from the softmax layer.
            # The final conv layer is "conv5_block16_2_conv"
            img_transformed = cam_sequence.load_image(self.filePath)
            class_weights = self.model.layers[-1].get_weights()[0]
            final_conv_layer = get_output_layer(self.model, "conv5_block16_2_conv")
            get_output = kb.function([self.model.layers[0].input],
                                     [final_conv_layer.output, self.model.layers[-1].output])
            [conv_outputs, self.predictions] = get_output([np.array([img_transformed])])
            conv_outputs = conv_outputs[0, :, :, :]

            # Create the class activation map.
            cam = np.zeros(dtype=np.float32, shape=(conv_outputs.shape[:2]))
            for i, w in enumerate(class_weights[index]):
                cam += w * conv_outputs[:, :, i]
            cam /= np.max(cam)
            width = original.shape[0]
            height = original.shape[1]
            cam = cv2.resize(cam, dsize=(height, width))
            
            # Create the heatmap on the original image and label it 
            # with the name of the disease
            heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)
            heatmap[np.where(cam < 0.4)] = 0
            img = heatmap * 0.5 + original
            cv2.putText(img, text=label, org=(150, 150), fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(255, 255, 67), thickness=1)
            img = cv2.resize(img, dsize=(300, 300))
            cv2.imwrite(self.output_path, img)
        self.openPage2()
        
        
        

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
