# -*- coding: utf-8 -*-
from flask import Flask, render_template
from pymongo import Connection

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

app = Flask(__name__)
app.config.from_object(__name__)

connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])

import songs.index
#import songs.songs


