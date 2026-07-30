from select import select

from models import TeaPageDb, User, UserTeaPage


def is_user_exist(username: str) -> bool:
    return User.select().where(User.username == username).exists()

def add_user(username: str, password: str):
    User.create(username=username, password=password)

def add_tea_in_list(title: str, province: str, type: str, user):
    UserTeaPage.create(title=title, province=province, type=type, user = user)

def get_user_by_name(username: str):
    return User.get_or_none(username=username)

def is_tea_exist(title: str) -> bool:
    return TeaPageDb.select().where(TeaPageDb.title == title).exists()

def add_tea(title: str, province: str, type: str):
    TeaPageDb.create(title=title, province=province, type=type)

def get_types():
    teas = TeaPageDb.select(TeaPageDb.type).distinct().order_by(
        TeaPageDb.type)
    types = [tea.type for tea in teas]
    return types

def get_teas():
    return TeaPageDb.select()

def get_tea_by_type(type: str):
    return TeaPageDb.select().where(TeaPageDb.type == type)

def get_tea_info(title: str):
    return  TeaPageDb.get(TeaPageDb.title == title)

def get_tea_by_user(user_id: int):

    return UserTeaPage.select().where(UserTeaPage.user == user_id)

def get_types_for_page(user_id: int):
    teas = UserTeaPage.select(UserTeaPage.type).where(UserTeaPage.user == user_id).distinct().order_by(
        UserTeaPage.type)
    types = [tea.type for tea in teas]
    return types

def get_tea_by_type_for_user(type: str, user_id):
    return UserTeaPage.select().where((TeaPageDb.type == type) & (UserTeaPage.user == user_id))

def get_teas_for_user(user_id: int):
    return UserTeaPage.select().where(UserTeaPage.user == user_id)

def delete_tea(title: str, user_id: int):
    UserTeaPage.delete().where((UserTeaPage.title == title) & (UserTeaPage.user == user_id)).execute()