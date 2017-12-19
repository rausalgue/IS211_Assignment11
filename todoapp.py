#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week 11 - Flask App"""

from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)

"""
list_data = {
    '1': ['Get Run in','rlasso@aol.com.com','high'],
    '2': ['Make Bfas', 'class@aol.com','low']
}
"""

list_data = {}

@app.route('/')
def index():
    return render_template('index.html', list_data=list_data)

@app.route('/submit', methods = ['POST'])
def submission():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    print list_data
    print len(list_data)



    #Validate the Email
    if priority != '' and task != '' and re.search('@', email):
        iteration = len(list_data)
        iteration += 1

        list_data[iteration] = [task,email,priority]

    print len(list_data)
    print list_data

    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    print len(list_data)
    list_data.clear()
    print len(list_data)

    return redirect('/')


if __name__ == '__main__':
    app.run()