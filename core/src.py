from interface import user_interface, bank_interface
from lib import common
from core import func_admin

login_user = None
'''
存放用户视图层
'''


# 1、注册功能
# 拆分版
def register():
    while True:
        # 1、让用户输入用户名与密码进行校验
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        re_password = input('请重新确认密码:').strip()
        # 小的逻辑处理：比如两次密码输入是否一致
        if password == re_password:
            flag, msg = user_interface.register_interface(
                username, password
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)

        # 面条版
    '''

    while True:
      # 1、让用户输入用户名与密码进行校验
      username = input('请输入用户名:').strip()
      password = input('请输入密码:').strip()
      re_password = input('请重新确认密码:').strip()
      # 小的逻辑处理：比如两次密码输入是否一致
      if password == re_password:
          # 接收到注册之后的结果，并打印

          import json
          import os
          from conf import settings

          user_path = os.path.join(
              settings.USER_DATA_PATH, f'{username}.json'
          )
          # 2、查看用户是否存在
          # 2.1若用户存在，则提醒用户重新注册
          if os.path.exists(user_path):
              print('该用户已存在，请重新输入')
              continue

          # 2.2若用户不存在，则保存
          # 2.2.1组织用户的数据的字典信息
          else:
              user_dic = {
                  'username': username,
                  'password': password,
                  'balance': 15000,
                  'flow': [],
                  'shop_car': [],
                  'locker': False  # 用于记录用户是否被冻结，False为没有,True为有
              }

              # 文件名：用户名.json
              # 拼接存储用户数据的json文件路径
              with open(user_path, mode='wt', encoding='utf-8') as f:
                  # ensure_ascii=False 让文件中的中文显示更直观
                  json.dump(user_dic, f, ensure_ascii=False)

   '''


# 2、登录功能
def login():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        flag, msg = user_interface.login_interface(
            username, password
        )
        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)


# 3、查看余额
@common.login_auth
def check_balance():
    balance = user_interface.check_bal_interface(
        login_user
    )

    print(f'用户{login_user}账户余额为:{balance}')


# 4、提现功能
@common.login_auth
def withdraw():
    while True:
        input_money = input('请输入提现金额:').strip()
        if not input_money.isdigit():
            print('请输入正确的数字')
            continue

        flag, msg = bank_interface.withdraw_interface(
            login_user, input_money
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 5、 还款功能
@common.login_auth
def repay():
    while True:
        input_money = input('请输入需要还款的金额:').strip()
        if not input_money.isdigit():
            print('请输入正确的金额')
            continue
        input_money = int(input_money)

        if input_money > 0:
            flag, msg = bank_interface.repay_interface(
                login_user, input_money
            )
            if flag:
                print(msg)
                break
        else:
            print('输入的金额不能小于0')


# 6、转账功能
@common.login_auth
def transfer():
    while True:
        input_money = input('请输入转账金额:').strip()
        input_username = input('请输入转账的用户:').strip()

        if not input_money.isdigit():
            print('请输入正确的金额')
            continue
        input_money = int(input_money)

        if input_money > 0:
            flag, msg = bank_interface.transfer_interface(
                login_user, input_money, input_username
            )

            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('余额不足')


# 7、查看流水
@common.login_auth
def check_flow():
    flow_list = bank_interface.check_flow_interface(
        login_user
    )

    if flow_list:
        for flow in flow_list:
            print(flow)

    else:
        print('无流水可查看')


# 10、管理员功能
def admin():
    func_admin.run_admin()


# 创建函数功能字典

func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': admin,
}


def run():
    while True:
        print(
            '''
            =========ATM========
                1、注册功能
                2、登录功能
                3、查看余额
                4、提现功能
                5、还款功能
                6、转账功能
                7、查看流水
                8、管理员功能
            =======end=======
            '''
        )

        choice = input('请输入功能编号：').strip()

        if choice not in func_dic:
            print('请输入正确的功能编号！')
            continue
        func_dic.get(choice)()  # func_dic.get('1') ----->register()
