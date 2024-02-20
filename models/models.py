from mongoengine import Document, StringField, IntField


class User(Document):
    name = StringField(required=True, max_length=200)
    email = StringField(required=True)
    password = StringField(required=True)
    image = StringField(required=False)


