#-*- coding=utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from . import main
from .forms import AddRecordForm, GetRandomIdForm
from ..models import Record
from .. import db
from datetime import datetime
import random
import string


@main.route('/')
def index():
    return redirect(url_for('main.user_amend'))


@main.route('/user/amend', methods=['GET', 'POST'])
def user_amend():
    """
    用户添加维修记录
    :return:
    """
    form = AddRecordForm()
    # alist = Record.query.all()
    if form.validate_on_submit():
        record = Record(user=form.user.data, phone=form.phone.data, problem=form.problem.data, create_time=datetime.now(),
                        computer_type=form.computer_type.data, computer_password=form.computer_password.data)
        record.random_id = string.join(
            random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 8)).replace(' ', '')
        i = 1
        while(i):
            try:
                db.session.add(record)
                db.session.commit()
                flash(u'记录添加成功,您的随机码是 %s ,现在时间是 %s ,请务必截图保存' % (record.random_id, record.create_time))
                i = 0
                return redirect(url_for('main.index'))
            except:
                db.session.rollback()
                record.random_id = string.join(
                    random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 8)).replace(' ', '')
    return render_template('main/amend.html', form=form)


@main.route('/user/verify', methods=['GET', 'POST'])
def user_verify():
    """
    用户确认物品取回
    :return:
    """
    form = GetRandomIdForm()
    if form.validate_on_submit():
        random_id = form.random_id.data
        record = Record.query.filter(Record.random_id == random_id).first()
        try:
            record.verify = True
            db.session.add(record)
            db.session.commit()
            flash(u'已确认取回')
        except:
            db.session.rollback()
            flash(u'未知错误')
        return render_template('main/amend.html')
    return render_template('main/verify.html', form=form)

