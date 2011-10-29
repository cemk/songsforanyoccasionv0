# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from pymongo import Connection


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

app = Flask(__name__)
app.config.from_object(__name__)

render_template = render_template
request = request

connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

import songs.render
import songs.index
import songs.form

#import songs.songs

