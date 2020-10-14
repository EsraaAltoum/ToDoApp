# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database import Base


class STATUS(Base):
    __tablename__ = 'STATUS'

    status_id = Column(Integer, primary_key=True)
    name = Column(String(100))


class USERDATUM(Base):
    __tablename__ = 'USERDATA'

    user_data_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(255))
    email = Column(String(100))


class TODO(Base):
    __tablename__ = 'TODO'

    todo_id = Column(Integer, primary_key=True)
    task = Column(String(255))
    due_date = Column(TIMESTAMP)
    note = Column(String(500))
    priority = Column(Integer)
    status_id = Column(ForeignKey('STATUS.status_id'), index=True)
    user_data_id = Column(ForeignKey('USERDATA.user_data_id'), index=True)

    status = relationship('STATUS')
    user_data = relationship('USERDATUM')
