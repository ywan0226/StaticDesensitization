# coding: utf8
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import re

db = SQLAlchemy()


class BaseModel:
    id = db.Column(db.Integer, primary_key=True)
    createTime = db.Column(db.DateTime, default=datetime.now())
    updateTime = db.Column(db.DateTime, default=datetime.now())


class User(db.Model, BaseModel):
    __tablename__ = 'user'

    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    grant = db.Column(db.Integer, nullable=False, default=0)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(32))

    @validates('phone')
    def validate_phone(self, phone):
        if not re.match(r"^1[3-9][0-9]\d{8}$", phone):
            return "phone invalidate"
        return phone

    @validates('email')
    def validate_email(self, email):
        assert '@' in email, "failed simple email validation"
        return email


class DB(db.Model, BaseModel):
    __tablename__ = 'db'

    name = db.Column(db.String(32), nullable=False)
    userName = db.Column(db.String(50), nullable=False)
    password = db.Column(db.Integer, nullable=False, default=0)
    addr = db.Column(db.String(15))
    port = db.Column(db.String(32))
    type = db.Column(db.Enum('mysql', 'oracle'))
    tables = db.relationship("TableName", backref="db")

    @validates('addr')
    def validate_addr(self, addr):
        if not re.match(r'^((2((5[0-5])|([0-4]\d)))|([0-1]?\d{1,2}))(\.((2((5[0-5])|([0-4]\d)))|([0-1]?\d{1,2}))){3}$',
                        addr):
            return "addr invalidate"
        return addr

    @validates('port')
    def validate_port(self, port):
        if not re.match(r'^((6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])|[0-5]?\d{0,4})$',
                        port):
            return "port invalidate"
        return port


class TableName(db.Model, BaseModel):
    __tablename__ = 'table'

    name = db.Column(db.String(32), nullable=False)
    db_id = db.Column(db.Integer, db.ForeignKey(DB.id))


class Rule(db.Model, BaseModel):
    __tablename__ = 'rule'

    name = db.Column(db.String(32), nullable=False)
    expression = db.Column(db.String(256), nullable=False)
    info = db.Column(db.Enum('name', 'id', 'phone', 'card', 'addr', 'fixed', 'pwd'))  # 脱敏对象
    method = db.Column(db.Enum('replace', 'invalid', 'scrambled', 'sea'))  # 替换、无效化、乱序、对称加密
    flag = db.Column(db.Integer, default=0)  # 0:内置 1:自定义


class ScanTask(db.Model, BaseModel):
    __tablename__ = 'scan_task'

    name = db.Column(db.String(32), nullable=False)
    table = db.Column(db.String(32), db.ForeignKey(TableName.id))
    result = db.relationship("ScanResult", backref="scan_task")


class ScanResult(db.Model, BaseModel):
    __tablename__ = 'scan_result'

    result = db.Column(db.String(32), nullable=False)
    task = db.Column(db.String(32), db.ForeignKey(ScanTask.id))
