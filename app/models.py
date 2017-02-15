# -*- coding=utf-8 -*-

from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash  # 引入密码加密 验证方法
from flask_login import UserMixin  # 引入flask-login用户模型继承类方�?


class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DATETIME, default=datetime.utcnow())
    user = db.Column(db.String(5))
    phone = db.Column(db.String(64))
    problem = db.Column(db.Text)
    computer_type = db.Column(db.String(64))
    computer_password = db.Column(db.String(64))
    split = db.Column(db.Boolean, default=False)
    solve = db.Column(db.Boolean, default=False)
    mender = db.Column(db.String(64))
    verify = db.Column(db.Boolean, default=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class User(UserMixin, db.Model):
    # 在使用Flask-Login作为登入功能�?在user模型要继承UserMimix�?
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    # real_name = db.Column(db.String(64), unique=True)
    # record = db.relationship('Record', backref='user')

    @property
    def password(self):
        raise AttributeError(u'不是可获取信息')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        # 增加password会通过generate_password_hash方法来加密储�?

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
        # 在登入时,我们需要验证明文密码是否和加密密码所吻合


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
