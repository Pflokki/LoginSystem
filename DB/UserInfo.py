from sqlalchemy import Column, Integer, String
from DB.SQLAlchemyConfig import Base


class UserInfo(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    photo_path = Column(String)
    fingerprint_path = Column(String)

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def set_photo_path(self, photo_path):
        self.photo_path = photo_path

    def set_fingerprint_path(self, fingerprint_path):
        self.fingerprint_path = fingerprint_path

    def __repr__(self):
        return "<User [{}]('{}','{}', '{}')>".format(self.id, self.name, self.surname, self.patronymic)
