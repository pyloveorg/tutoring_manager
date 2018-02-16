#!/usr/bin/env python
# encoding: utf-8
from main import app
from main import db
from main import bcrypt
from main import lm

from flask import render_template, request, redirect, url_for
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

        return redirect('/')