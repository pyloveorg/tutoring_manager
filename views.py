#!/usr/bin/env python
# encoding: utf-8
from main import app
from main import db
from main import bcrypt
from main import lm

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from models import User


@app.route('/', methods=['GET', 'POST'])
def info():
    return render_template('info.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email and password:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash('User successfully registered')

        return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email and password:
            registered_user = User.query.filter_by(email=email, password=password).first()
            if registered_user is None:
                flash('Username or password is invalid')
                return redirect(url_for('login'))

            login_user(registered_user)
            flash('Logged in successfully')
            return redirect(request.args.get('next') or url_for('home'))

        return redirect(url_for('info'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('info'))


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')