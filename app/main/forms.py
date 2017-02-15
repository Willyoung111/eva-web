#-*- coding=utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, length, Regexp


class AddRecordForm(FlaskForm):
    """
    用户提交维修记录的表单
    """
    user = StringField(u'物主姓名:', validators=[Required(), length(6, 18)])
    phone = StringField(u'联系方式:', validators=[Required(), length(6, 13), Regexp('[0-9]')])
    problem = TextAreaField(u'简要描述您的问题:', validators=[Required()])
    computer_type = StringField(u'您的电脑型号:', validators=[Required()])
    computer_password = StringField(u'您的电脑密码（可不填）:')
    submit = SubmitField(u'提交')


class GetIdForm(FlaskForm):
    """
        序号相关的表单
        """
    id = StringField(u'请输入您的序列号：', validators=[Required()])
    submit = SubmitField(u'提交')


