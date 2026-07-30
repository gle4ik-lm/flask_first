
from peewee import *
db = SqliteDatabase('db.sqlite')

class BaseModel(Model):
    class Meta:
        database = db

class TeaPageDb(BaseModel):
    title = CharField()
    province = CharField()
    type = CharField()

class User(BaseModel):
    id = PrimaryKeyField()
    username = CharField()
    password = CharField()

class UserTeaPage(BaseModel):
    title = CharField()
    province = CharField()
    type = CharField()

    user = ForeignKeyField(User, backref='pages')


def init_db():
    db.connect()
    # db.drop_tables([TeaPageDb, UserTeaPage, User])
    db.create_tables([TeaPageDb, UserTeaPage, User])