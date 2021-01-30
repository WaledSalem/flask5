#!/usr/bin/python3

from app import db, Users, Person

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot')
db.session.add(testuser)
db.session.commit()
