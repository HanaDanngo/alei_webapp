#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Danngo Alei'


from flask import Flask 
app = Flask(__name__)

@app.route('/')
def home():
    return 'config flask'

if __name__ == '__main__':
    app.run()