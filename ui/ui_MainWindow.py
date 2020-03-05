# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 294)
        MainWindow.setMinimumSize(QtCore.QSize(500, 250))
        MainWindow.setMaximumSize(QtCore.QSize(500, 294))
        self.widget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(500, 250))
        self.widget.setMaximumSize(QtCore.QSize(500, 250))
        self.widget.setBaseSize(QtCore.QSize(500, 250))
        self.widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.widget.setObjectName("widget")
        self.gridWidget = QtWidgets.QWidget(self.widget)
        self.gridWidget.setGeometry(QtCore.QRect(0, 0, 501, 251))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pB_search_user = QtWidgets.QPushButton(self.gridWidget)
        self.pB_search_user.setMinimumSize(QtCore.QSize(250, 30))
        self.pB_search_user.setObjectName("pB_search_user")
        self.verticalLayout.addWidget(self.pB_search_user)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pB_add_user = QtWidgets.QPushButton(self.gridWidget)
        self.pB_add_user.setMinimumSize(QtCore.QSize(250, 30))
        self.pB_add_user.setObjectName("pB_add_user")
        self.verticalLayout.addWidget(self.pB_add_user)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pB_enter = QtWidgets.QPushButton(self.gridWidget)
        self.pB_enter.setMinimumSize(QtCore.QSize(250, 30))
        self.pB_enter.setObjectName("pB_enter")
        self.verticalLayout.addWidget(self.pB_enter)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(3, 3)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 5)
        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 5)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LoginSystem"))
        self.pB_search_user.setText(_translate("MainWindow", "Поиск пользователя"))
        self.pB_add_user.setText(_translate("MainWindow", "Добавить пользователя"))
        self.pB_enter.setText(_translate("MainWindow", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
