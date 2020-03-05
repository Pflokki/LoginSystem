# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EnterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnterWindow(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(282, 222)
        self.verticalLayoutWidget = QtWidgets.QWidget(widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 231, 182))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pB_photo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_photo.setObjectName("pB_photo")
        self.verticalLayout.addWidget(self.pB_photo)
        self.l_photo_path = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_photo_path.setObjectName("l_photo_path")
        self.verticalLayout.addWidget(self.l_photo_path)
        self.pB_fingerprint = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_fingerprint.setObjectName("pB_fingerprint")
        self.verticalLayout.addWidget(self.pB_fingerprint)
        self.l_fingerprint_path = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_fingerprint_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.l_fingerprint_path.setObjectName("l_fingerprint_path")
        self.verticalLayout.addWidget(self.l_fingerprint_path)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pB_enter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_enter.setObjectName("pB_enter")
        self.verticalLayout.addWidget(self.pB_enter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.l_error = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.l_error.setText("")
        self.l_error.setObjectName("l_error")
        self.horizontalLayout.addWidget(self.l_error)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(6, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Войти"))
        self.pB_photo.setText(_translate("widget", "Выбрать фотографию"))
        self.l_photo_path.setText(_translate("widget", "Файл:"))
        self.pB_fingerprint.setText(_translate("widget", "Выбрать отпечаток"))
        self.l_fingerprint_path.setText(_translate("widget", "Файл: "))
        self.pB_enter.setText(_translate("widget", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
