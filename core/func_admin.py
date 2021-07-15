from core import src
from interface import admin_interface


def add_user():
    src.register()


def set_money():
    while True:
        change_user = input('请输入需要修改的用户:').strip()
        money = input('请输入需要修改的额度数量:').strip()
        if not money.isdigit():
            print('额度数量出错，请重新输入！')
            continue
        flag, msg = admin_interface.change_balance_interface(
            change_user, money
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


def lock_user():
    while True:
        lock_username = input('请输入需要修改的用户:').strip()
        lock_or_unlock = input('请输入将用户冻结("1")或解冻("0"):')

        flag, msg = admin_interface.lock_user_interface(
            lock_username, lock_or_unlock
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


admin_func_dic = {
    '1': add_user,
    '2': set_money,
    '3': lock_user,
}


def run_admin():
    while True:
        print(
            '''
            1、添加用户
            2、修改额度
            3、冻结账户
            '''
        )
        choice = input('请输入管理员功能编号:').strip()

        if choice not in admin_func_dic:
            print('请输入正确的功能编号！')
            continue
        admin_func_dic.get(choice)()
