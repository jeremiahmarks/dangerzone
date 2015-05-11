#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-10 16:56:45
# @Last Modified 2015-05-10
# @Last Modified time: 2015-05-10 17:00:33
from flask import Flask, request
app = Flask(__name__)

from flask.ext.script import Manager
manager = Manager(app)

# @app.route('/') # this makes any request to just the domain return the next function
# def index():
#     ua = request.headers.get('User-Agent')
#     return """<h1>Hello World</h1>\n
#     <p>It appears you are using %s today.</p>""" %ua

# # Note that the path can also include variables

# @app.route('/won/<name>')
# def winner(name):
#     return "%s totally just won, yay!" %name

if __name__ == '__main__':
    manager.run()