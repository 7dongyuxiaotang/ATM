'''
银行相关业务的接口
'''
from db import db_handler


def withdraw_interface(username, money):
    user_dic = db_handler.select(username)
    balance = int(user_dic.get('balance'))

    money2 = int(money) * 1.05
    if balance >= money2:
        balance -= money2

        user_dic['balance'] = balance
        flow = f'用户[{username}]提现金额[{money}]元成功，手续费为[{money2 - float(money)}]元'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)

        return True, flow
    return False, '账户金额不足'


def repay_interface(username, money):
    user_dic = db_handler.select(username)
    user_dic['balance'] += money
    flow = f'用户:[{username}]还款成功，还款金额:[{money}]元，当前的账户内金额为[{user_dic["balance"]}]元'
    user_dic['flow'].append(flow)
    db_handler.save(user_dic)

    return True, flow


def transfer_interface(username, money, transfer_username):
    login_user_dic = db_handler.select(username)
    transfer_username_dic = db_handler.select(transfer_username)

    if not transfer_username_dic:
        return False, '该用户不存在'

    if login_user_dic['balance'] >= money:
        login_user_dic['balance'] -= money
        transfer_username_dic['balance'] += money

        login_user_flow = f'用户:[{username}]成功给用户:[{transfer_username}]转账[{money}]元！'
        login_user_dic['flow'].append(login_user_flow)

        transfer_username_flow = f'用户:[{transfer_username}]成功收到用户:[{username}]转账[{money}]元！'
        transfer_username_dic['flow'].append(transfer_username_flow)

        db_handler.save(login_user_dic)
        db_handler.save(transfer_username_dic)

        return True, login_user_flow

    return False, f'用户:[{username}]给[{transfer_username}]转账[{money}]元失败！'


def check_flow_interface(username):
    user_dic = db_handler.select(username)

    return user_dic.get('flow')
