from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from ui.ui_EnterWindow import Ui_EnterWindow
from uiControl.UserInfoControl import UserInfoControl

from DB.AlchemyDBInit import Session
from DB.UserInfo import UserInfo

from pathlib import Path


class EnterControl(QtWidgets.QMainWindow, Ui_EnterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pB_photo.clicked.connect(self.on_clicked_choice_photo_btn)
        self.pB_fingerprint.clicked.connect(self.on_clicked_choice_fingerprint_btn)
        self.pB_enter.clicked.connect(self.on_clicked_enter_btn)

        self.user_info_control = UserInfoControl()
        self._photo_path = ""
        self._fingerprint_path = ""

    def on_clicked_choice_photo_btn(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        full_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "All Files (*);;", options=options)
        self._photo_path = full_path

        file_name = Path(full_path).parts[-1]

        if full_path:
            print(full_path)
        self.l_photo_path.setText("Файл: {}".format(file_name))

    def on_clicked_choice_fingerprint_btn(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        full_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "All Files (*);;", options=options)
        self._fingerprint_path = full_path

        file_name = Path(full_path).parts[-1]

        if full_path:
            print(full_path)
        self.l_fingerprint_path.setText("Файл: {}".format(file_name))

    def on_clicked_enter_btn(self):
        self.l_error.setText("")

        if self._photo_path or self._fingerprint_path:
            session = Session()
            user = session.query(UserInfo) \
                .filter(UserInfo.photo_path.like("%{}%".format(self._photo_path)),
                        UserInfo.fingerprint_path.like("%{}%".format(self._fingerprint_path))) \
                .first()

            if user:
                self.user_info_control = UserInfoControl()
                self.user_info_control.set_info(user.id, user.surname, user.name, user.patronymic,
                                                user.fingerprint_path, user.photo_path)
                self.user_info_control.show()
                print(user)
            else:
                self.l_error.setText("Пользователь не найден")

        else:
            self.l_error.setText("Пользователь не найден")

