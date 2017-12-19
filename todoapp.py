#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week 11 - Flask App"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

list_data = {
    '1': ['Get Run in','rlasso@aol.com.com','high'],
    '2': ['Make Bfas', 'class@aol.com','low']
}

@app.route('/')
def index():
    return render_template('index.html', list_data=list_data)

if __name__ == '__main__':
    app.run()