#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week 11 - Flask App"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()