#-*- coding=utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from . import main
from .forms import AddRecordForm, GetIdForm
from ..models import Record
from .. import db



@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/user/amend', methods=['GET', 'POST'])
def user_amend():
    """
    用户添加维修记录
    :return:
    """
    form = AddRecordForm()
    # alist = Record.query.all()
    if form.validate_on_submit():
        record = Record(user=form.user.data, phone=form.phone.data, problem=form.problem.data,
                        computer_type=form.computer_type.data, computer_password=form.computer_password.data)
        db.session.add(record)
        db.session.commit()
        flash(u'记录添加成功,您的维修序号是 %s ,请务必截图保存' % record.id )
        return redirect(url_for('main.index'))
    return render_template('main/amend.html', form=form)


@main.route('/user/verify', methods=['GET', 'POST'])
def user_verify():
    """
    用户确认物品取回
    :return:
    """
    form = GetIdForm()
    if form.validate_on_submit():
        id = form.id.data
        record = Record.query.get_or_404(id)
        record.verify = True
        db.session.add(record)
        db.session.commit()
        flash(u'已确认取回')
        return render_template('main/index.html')
    return render_template('main/verify.html', form=form)


