# -*- coding=utf-8 -*-
from . import admin
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user, login_user, logout_user
from forms import LoginForm, RegistrationForm, EditRecodeForm, ModifyForm
from ..models import User, Record
from .. import db


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('admin.index'))
        flash(u'用户密码不正确')
    return render_template('admin/login.html', form=form)


@admin.route('/register', methods=['GET', 'POST'])
def register():
    register_key = 'zhucema'
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.registerkey.data != register_key:
            flash(u'注册码不符，请返回重试')
            return redirect(url_for('admin.register'))
        else:
            if form.password.data != form.password2.data:
                flash(u'两次输入密码不一')
                return redirect(url_for('admin.register'))
            else:
                user = User(username=form.username.data, password=form.password.data)
                db.session.add(user)
                db.session.commit()
                flash(u'您已经成功注册')
                return redirect(url_for('admin.login'))
    return render_template('admin/register.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已经登出了系统')
    return redirect(url_for('admin.index'))


@admin.route('/record', methods=['GET', 'POST'])
@login_required
def record():
    results = db.session.query(Record).order_by(-Record.id)
    form = ModifyForm()
    if form.validate_on_submit():
        return redirect(url_for('admin.modify', id=form.id.data))
    return render_template('admin/record.html', results=results, form=form)


@admin.route('/modify/<int:id>', methods=['GET', 'POST'])
@login_required
def modify(id):
    re = db.session.query(Record).filter(Record.id == id).one()
    form = EditRecodeForm(user=re.user, phone=re.phone, problem=re.problem, computer_type=re.computer_type,
                          computer_password=re.computer_password, split=re.split, solve=re.solve, mender=re.mender,
                          verify=re.verify)
    if form.validate_on_submit():
        cord = Record.query.get_or_404(id)
        cord.user = form.user.data
        cord.phone = form.phone.data
        cord.problem=form.problem.data
        cord.computer_type=form.computer_type.data
        cord.computer_password=form.computer_password.data
        cord.mender=form.mender.data
        if form.split.data:
            cord.split = True
        else:
            cord.split = False
        if form.solve.data:
            cord.solve = True
        else:
            cord.solve = False
        if form.verify.data:
            cord.verify = True
        else:
            cord.verify = False
        db.session.add(cord)
        db.session.commit()
        return redirect(url_for('admin.record'))
    return render_template("admin/modify.html", form=form, id=re.id, time=re.create_time)
