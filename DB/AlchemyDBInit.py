# add DB to create metadata
from DB.UserInfo import UserInfo

from sqlalchemy import create_engine
from DB.SQLAlchemyConfig import DB_PATH, Base
from sqlalchemy.orm import sessionmaker


engine = create_engine(DB_PATH, echo=True)
Session = sessionmaker(bind=engine)
# Создание таблицы
Base.metadata.create_all(engine)
