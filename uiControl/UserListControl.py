import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAbstractItemView
from ui.ui_UserListWindow import Ui_UserListWindow

from DB.UserInfo import UserInfo
from DB.AlchemyDBInit import Session

from uiControl.UserInfoControl import UserInfoControl


class UserListControl(QtWidgets.QMainWindow, Ui_UserListWindow):
    def __init__(self):
        super().__init__()
        self.user_info_control = UserInfoControl()
        self.setupUi(self)
        self.tw_Users.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_Users.itemClicked.connect(self.on_clicked_cell)
        self.pb_Search.clicked.connect(self.on_clicked_search_btn)

    def print_data(self, users: list):
        self.tw_Users.setRowCount(0)
        self.tw_Users.setColumnCount(5)
        for index, name in enumerate(["Фамилия", "Имя", "Отчество", "Отпечаток", "Фотография"]):
            self.tw_Users.setHorizontalHeaderItem(index, QtWidgets.QTableWidgetItem(name))
        for row, record in enumerate(users):
            self.tw_Users.insertRow(row)
            self.tw_Users.setItem(row, 0, QtWidgets.QTableWidgetItem(record.surname))
            self.tw_Users.setItem(row, 1, QtWidgets.QTableWidgetItem(record.name))
            self.tw_Users.setItem(row, 2, QtWidgets.QTableWidgetItem(record.patronymic))
            self.tw_Users.setItem(row, 3, QtWidgets.QTableWidgetItem(record.fingerprint_path))
            self.tw_Users.setItem(row, 4, QtWidgets.QTableWidgetItem(record.photo_path))
        for record in users:
            print(record)

    def print_all_users(self):
        session = Session()
        users = list(session.query(UserInfo).all())
        self.print_data(users)

    def on_clicked_cell(self):
        items = self.tw_Users.selectedItems()

        session = Session()
        user = session.query(UserInfo) \
            .filter(UserInfo.surname == items[0].text(),
                    UserInfo.name == items[1].text(),
                    UserInfo.patronymic == items[2].text(),
                    UserInfo.fingerprint_path == items[3].text(),
                    UserInfo.photo_path == items[4].text()) \
            .first()

        self.user_info_control.set_info(user.id, user.surname, user.name, user.patronymic,
                                        user.fingerprint_path, user.photo_path)
        self.user_info_control.show()

    def on_clicked_search_btn(self):
        name_pattern = self.le_name.text()
        surname_pattern = self.le_surname.text()
        patronymic_pattern = self.le_patronymic.text()

        session = Session()
        users = list(session.query(UserInfo).filter(UserInfo.name.like("%{}%".format(name_pattern)),
                                                    UserInfo.surname.like("%{}%".format(surname_pattern)),
                                                    UserInfo.patronymic.like("%{}%".format(patronymic_pattern))).all())
        self.print_data(users)


def test():
    app = QtWidgets.QApplication(sys.argv)
    window = UserListControl()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test()
