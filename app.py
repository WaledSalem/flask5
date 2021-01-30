#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://waled:root@localhost/data"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(30), unique = True, nullable = False)
    alive = db.Column(db.Boolean, default=True)
    date = db.Column(db.DateTime)
    height = db.Column(db.Float)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')
