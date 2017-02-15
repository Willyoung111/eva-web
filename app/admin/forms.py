# -*- coding=utf-8 -*-
from flask_wtf import FlaskForm
# from ..models import
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Required, length, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class LoginForm(FlaskForm):
    username = StringField(u'帐号', validators=[Required(), length(6, 64)])
    password = PasswordField(u'密码', validators=[Required()])
    submit = SubmitField(u'登入')


class RegistrationForm(FlaskForm):
    username = StringField(u'用户名', validators=[Required(), length(6, 18), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, u'用户名只允许字母')])
    password = PasswordField(
        u'密码', validators=[Required(), EqualTo('password2', message=u'两次密码不一致')])
    password2 = PasswordField(u'重复密码', validators=[Required()])
    # real_name = StringField(u'昵称', validators=[Required()])
    registerkey = StringField(u'注册码', validators=[Required()])
    submit = SubmitField(u'注册')


class EditRecodeForm(FlaskForm):
    user = StringField(u'物主姓名:', validators=[Required(), length(2, 5)])
    phone = StringField(u'手机号或QQ号:', validators=[Required(), length(6, 11), Regexp('[0-9]')])
    problem = TextAreaField(u'请描述您的问题:')
    computer_type = StringField(u'您的电脑型号:')
    computer_password = StringField(u'您的电脑密码（可不填）:')
    split = BooleanField(u'是否拆机：')
    solve = BooleanField(u'是否解决：')
    mender = StringField(u'维修者姓名：')
    verify = BooleanField(u'是否取回：')
    submit = SubmitField(u'提交')


class ModifyForm(FlaskForm):
    id = StringField(u'id')
    submit = SubmitField(u'修改')