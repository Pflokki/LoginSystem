from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from ui.ui_UserInfoWindow import Ui_UserInfoWindow, IMAGE_LABEL_HEIGHT, IMAGE_LABEL_WIDTH
from DB.AlchemyDBInit import Session
from DB.UserInfo import UserInfo


class UserInfoControl(QtWidgets.QMainWindow, Ui_UserInfoWindow):
    def __init__(self):
        super().__init__()
        self.id_ = 0
        self.name = ""
        self.surname = ""
        self.patronymic = ""
        self.photo_path = ""
        self.fingerprint_path = ""

        self.setupUi(self)
        self.pB_delete.clicked.connect(self.delete_user)

    def set_info(self, id_, surname, name, patronymic, fingerprint_path, photo_path):
        self.id_ = id_
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.photo_path = photo_path
        self.fingerprint_path = fingerprint_path

    def show(self):
        self.l_user_info.setText("{} {} {}".format(self.surname, self.name, self.patronymic))
        _pixmap = QPixmap(self.photo_path).scaled(IMAGE_LABEL_WIDTH, IMAGE_LABEL_HEIGHT)
        self.l_face_picture.setPixmap(_pixmap)

        _pixmap_2 = QPixmap(self.fingerprint_path).scaled(IMAGE_LABEL_WIDTH, IMAGE_LABEL_HEIGHT)
        self.l_fingerprint_image.setPixmap(_pixmap_2)

        super().show()

    def delete_user(self):
        session = Session()
        user = session.query(UserInfo).filter(UserInfo.id == self.id_).first()
        session.delete(user)
        session.flush()

        super().close()
