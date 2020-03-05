# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInfoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

IMAGE_LABEL_HEIGHT = 300
IMAGE_LABEL_WIDTH = 250


class Ui_UserInfoWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("User Info")
        Form.resize(679, 369)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 651, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_face_picture = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_face_picture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.l_face_picture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.l_face_picture.setObjectName("l_face_picture")
        self.l_face_picture.setFixedSize(IMAGE_LABEL_WIDTH, IMAGE_LABEL_HEIGHT)
        self.horizontalLayout.addWidget(self.l_face_picture)
        self.l_fingerprint_image = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_fingerprint_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.l_fingerprint_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.l_fingerprint_image.setObjectName("l_fingerprint_image")
        self.l_fingerprint_image.setFixedSize(IMAGE_LABEL_WIDTH, IMAGE_LABEL_HEIGHT)

        self.horizontalLayout.addWidget(self.l_fingerprint_image)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.l_user_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_user_info.setObjectName("l_user_info")
        self.horizontalLayout_2.addWidget(self.l_user_info)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pB_delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_delete.setObjectName("pB_delete")
        self.pB_delete.setText("Удалить")
        self.horizontalLayout_3.addWidget(self.pB_delete)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Инфомация о пользователе"))
        self.l_user_info.setText(_translate("Form", "Фамилия Имя Отчество"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_UserInfoWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
