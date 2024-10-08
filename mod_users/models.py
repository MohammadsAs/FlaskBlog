from werkzeug.security import generate_password_hash
from sqlalchemy import Column, Integer, String
from app import db


class User(db.Model):
    __tablename__= 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(256), nullable=False, unique=False)
    role = Column(Integer(), nullable=False, default=0)
    full_name = Column(String(128), nullable=True, unique=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)