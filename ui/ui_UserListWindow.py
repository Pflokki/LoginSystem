# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserListWIndow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserListWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Список пользователей")
        Form.resize(706, 439)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 691, 421))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.l_surname = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.l_surname.setObjectName("l_surname")
        self.verticalLayout.addWidget(self.l_surname)
        self.le_surname = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.le_surname.setObjectName("le_surname")
        self.verticalLayout.addWidget(self.le_surname)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.l_name = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.l_name.setObjectName("l_name")
        self.verticalLayout_2.addWidget(self.l_name)
        self.le_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.le_name.setObjectName("le_name")
        self.verticalLayout_2.addWidget(self.le_name)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.l_patronymic = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.l_patronymic.setObjectName("l_patronymic")
        self.verticalLayout_3.addWidget(self.l_patronymic)
        self.le_patronymic = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.le_patronymic.setObjectName("le_patronymic")
        self.verticalLayout_3.addWidget(self.le_patronymic)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pb_Search = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pb_Search.setObjectName("pb_Search")
        self.horizontalLayout_2.addWidget(self.pb_Search)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tw_Users = QtWidgets.QTableWidget(self.verticalLayoutWidget_4)
        self.tw_Users.setObjectName("tw_Users")
        self.verticalLayout_4.addWidget(self.tw_Users)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Поиск пользователей"))
        self.l_surname.setText(_translate("Form", "Фамилия"))
        self.l_name.setText(_translate("Form", "Имя"))
        self.l_patronymic.setText(_translate("Form", "Отчество"))
        self.pb_Search.setText(_translate("Form", "Поиск пользователя"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_UserListWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
