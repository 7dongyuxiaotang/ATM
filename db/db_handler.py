'''
数据处理层
    专门用户处理数据
'''

import json
import os
from conf import settings


# 查看数据
def select(username):
    # 接收接口层传过来的username用户名，拼接用户json文件路径
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )
    if os.path.exists(user_path):
        with open(user_path, mode='rt', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic


def save(user_dic):
    username = user_dic.get('username')
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )

    with open(user_path, mode='wt', encoding='utf-8') as f:
        # ensure_ascii=False 让文件中的中文显示更直观
        json.dump(user_dic, f, ensure_ascii=False)
