#-*- coding=utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, length, Regexp


class AddRecordForm(FlaskForm):
    """
    用户提交维修记录的表单
    """
    user = StringField(u'物主姓名:', validators=[Required(), length(2, 5, message=u'姓名只允许2-5个字符！')])
    phone = StringField(u'手机号（QQ）:', validators=[Required(), length(6, 11, message=u'只允许6-11位数字'), Regexp('[0-9]')])
    problem = TextAreaField(u'简要描述您的问题:', validators=[Required()])
    computer_type = StringField(u'您的电脑型号:', validators=[Required()])
    computer_password = StringField(u'您的电脑密码（可不填）:')
    submit = SubmitField(u'提交')


class GetRandomIdForm(FlaskForm):
    """
    序号相关的表单
    """
    random_id = StringField(u'请输入您的序列号：', validators=[Required()])
    submit = SubmitField(u'提交')


