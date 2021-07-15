from db import db_handler
from lib import common

'''
逻辑接口层
    用户接口  453466500
'''


def register_interface(username, password, balance=15000):
    user_dic = db_handler.select(username)

    if user_dic:
        return False, f'{username} 用户名已存在'

    password = common.get_pwd_md5(password)
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        'flow': [],
        'shop_car': [],
        'locker': False  # 用于记录用户是否被冻结，False为没有,True为有
    }

    # 保存数据
    db_handler.save(user_dic)
    return True, f'{username} 注册成功'


def login_interface(username, password):
    user_dic = db_handler.select(username)
    if user_dic:
        if user_dic.get('locked'):
            return False, '当前用户已经被冻结，无法登录！'

        password = common.get_pwd_md5(password)
        if password == user_dic.get('password'):
            return True, f'用户{username}登录成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户不存在，请重新输入！'


def check_bal_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']
