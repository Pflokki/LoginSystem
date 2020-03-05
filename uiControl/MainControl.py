import sys
from PyQt5 import QtWidgets
from ui.ui_MainWindow import Ui_MainWindow
from uiControl.CreateUserControl import CreateUserControl
from uiControl.UserListControl import UserListControl
from uiControl.EnterControl import EnterControl


class MainControl(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pB_add_user.clicked.connect(self.on_clicked_pb_add_user)
        self.create_user_window = CreateUserControl()
        self.create_user_list_window = UserListControl()
        self.enter_window = EnterControl()

        self.pB_search_user.clicked.connect(self.on_clicked_pb_search_user)
        self.pB_enter.clicked.connect(self.on_clicked_enter_btn)

    def on_clicked_pb_add_user(self):
        self.create_user_window = CreateUserControl()
        self.create_user_window.show()

    def on_clicked_pb_search_user(self):
        self.create_user_list_window = UserListControl()
        self.create_user_list_window.show()
        self.create_user_list_window.print_all_users()

    def on_clicked_enter_btn(self):
        self.enter_window = EnterControl()
        self.enter_window.show()


def test():
    app = QtWidgets.QApplication(sys.argv)
    window = MainControl()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test()
