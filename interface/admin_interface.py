from db import db_handler


def change_balance_interface(username, money):
    user_dic = db_handler.select(username)

    if user_dic:
        user_dic['balance'] = int(money)

        db_handler.save(user_dic)

        return True, '额度修改成功！'

    return False, '修改失败！'


def lock_user_interface(username, lock_or_unlock):
    user_dic = db_handler.select(username)
    lock_or_unlock = int(lock_or_unlock)
    if user_dic:
        if lock_or_unlock == 1:
            user_dic['locked'] = True

            db_handler.save(user_dic)

            return True, f'用户{username}冻结成功！'
        user_dic['locked'] = False

        db_handler.save(user_dic)

        return True, f'用户{username}解冻成功！'

    return False, '冻结用户不存在！'
