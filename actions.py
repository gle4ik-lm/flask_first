from models import *

def is_user_exist(username: str) -> bool:
    return User.select().where(User.username == username).exists()

def add_user(username: str, password: str):
    User.create(username=username, password=password)

def get_user_by_name(name: str) -> User:
    return User.get_or_none(name=name)

def is_tea_exist(title: str) -> bool:
    return TeaPageDb.select().where(TeaPageDb.title == title).exists()

def add_tea(title: str, province: str, type: str):
    TeaPageDb.create(title=title, province=province, type=type)