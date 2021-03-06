# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 352)
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        Dialog.setModal(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_4.addWidget(self.dateEdit, 0, 0, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Flight No")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        
        self.gridLayout_4.addWidget(self.comboBox, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 3)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

        regex = QtCore.QRegExp("^[0-9A-Za-z]{4}")
        validator = QtGui.QRegExpValidator(regex)
        self.lineEdit_2.setValidator(validator)
        self.lineEdit_3.setValidator(validator)

        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_3)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_3.addWidget(self.timeEdit, 0, 0, 1, 1)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.groupBox_3)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.gridLayout_3.addWidget(self.timeEdit_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.groupBox_4)
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.gridLayout.addWidget(self.timeEdit_4, 0, 0, 1, 1)
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.groupBox_4)
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.gridLayout.addWidget(self.timeEdit_3, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.dateEdit, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.timeEdit)
        Dialog.setTabOrder(self.timeEdit, self.timeEdit_4)
        Dialog.setTabOrder(self.timeEdit_4, self.timeEdit_3)
        Dialog.setTabOrder(self.timeEdit_3, self.timeEdit_2)
        Dialog.setTabOrder(self.timeEdit_2, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_3)
        Dialog.setTabOrder(self.pushButton_3, self.pushButton_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("New Leg", "New Leg"))
        self.pushButton.setText(_translate("Dialog", "Add Leg"))
        self.comboBox.setItemText(0, _translate("Dialog", "AL-ISA"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "From"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "To"))
        self.groupBox_3.setTitle(_translate("Dialog", "Block"))
        self.groupBox_4.setTitle(_translate("Dialog", "Flight"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Done"))
