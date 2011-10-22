from flask import Flask
from mongokit import Connection, Document

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

app = Flask(__name__)
app.config.from_object(__name__)

import songs.index
#import songs.songs


connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])