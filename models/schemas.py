from pydantic import BaseModel
from mongoengine import Document, StringField, IntField, ListField, EmbeddedDocumentField, EmbeddedDocument


class User(BaseModel):
    _id: IntField
    name: StringField
    email: StringField
    password: StringField
    blogs: ListField
