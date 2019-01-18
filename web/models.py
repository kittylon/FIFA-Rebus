# from mongoengine import *
# import datetime
#
#
# class Country(Document):
#     name = StringField(unique=True, max_length=100, required=True)
#     nationality = StringField(max_length=100, required=True)
#
#
# class Team(Document):
#     team_name = StringField(unique=True, max_length=100, required=True)
#     flag_image = StringField(max_length=100, required=True)
#     team_emblema = StringField(max_length=100, required=True)
#
#
# class Player(Document):
#     POSITIONS = ('portero', 'defensa', 'librero', 'lateral', 'carrilero', 'mediocentro defensivo', 'centrocampista',
#                  'exterior', 'delantero')
#     team = ReferenceField(Team)
#     first_name = StringField(max_length=100, required=True)
#     last_name = StringField(max_length=100, required=True)
#     birth_date = DateTimeField(default=datetime.datetime.utcnow, required=True)
#     position = StringField(max_length=100, choices=POSITIONS)
#     shirt_number = IntField(required=True)
#     is_titular = db.BoolField(default=False, required=True)
#
#
# class Coach(Document):
#     team = ReferenceField(Team)
#     first_name = StringField(max_length=100, required=True)
#     last_name = StringField(max_length=100, required=True)
#     birth_date = DateTimeField(default=datetime.datetime.utcnow, required=True)
#     nationality = StringField(max_length=100, required=True)
#     role = StringField(max_length=200, required=True)
