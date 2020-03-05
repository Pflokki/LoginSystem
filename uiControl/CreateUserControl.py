import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from ui.ui_CreateUserWindow import Ui_CreateUserWindow
from pathlib import Path

from DB.UserInfo import UserInfo
from DB.AlchemyDBInit import Session


class CreateUserControl(QtWidgets.QMainWindow, Ui_CreateUserWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_create.clicked.connect(self.on_clicked_pb_create)
        self.pB_load_photo.clicked.connect(self.on_clicked_open_photo_dialog)
        self.pB_load_fingerprint.clicked.connect(self.on_clicked_open_fingerprint_dialog)

        self._fingerprint_path = ""
        self._photo_path = ""

    def on_clicked_pb_create(self):
        name = self.le_name.text()
        surname = self.le_surname.text()
        patronimyc = self.le_patronimyc.text()

        user = UserInfo(name, surname, patronimyc)
        user.set_fingerprint_path(self._fingerprint_path)
        user.set_photo_path(self._photo_path)

        session = Session()
        session.add(user)
        session.flush()

        self.close()

    def on_clicked_open_photo_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        full_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "All Files (*);;", options=options)
        file_name = Path(full_path).parts[-1]

        if full_path:
            print(full_path)
        self.l_image_path.setText("Фотография: {}".format(file_name))

        self._photo_path = full_path

    def on_clicked_open_fingerprint_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        full_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "All Files (*);;", options=options)
        file_name = Path(full_path).parts[-1]

        if full_path:
            print(full_path)
        self.l_fingerprint_path.setText("Отпечаток: {}".format(file_name))

        self._fingerprint_path = full_path


def test():
    app = QtWidgets.QApplication(sys.argv)
    window = CreateUserControl()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test()
