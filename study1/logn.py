import sys


class user():
    username = 0
    password = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password


def user_init():
    users = []
    users.append(user("1234", "2345"))
    users.append(user("1235", "2346"))
    users.append(user("1236", "2347"))
    users.append(user("1237", "2348"))
    users.append(user("1238", "2349"))
    users.append(user("1239", "2350"))
    return users


def find_user(user_list, username, password):
    for user in user_list:
        if user.username == username and user.password == password:
            return user


def login():
    users = user_init()
    load_user_list(users)


def load_user_list(users):
    attempts_longin = 0
    max_attempts_login = 3
    while attempts_longin < max_attempts_login:
        # 尝试过不用int  但是我明明已经设置atemp_longin已经定义了等于0
        # 报错显示为解析到这个定义函数
        input_name = input("请输入用户名: ")
        input_pwd = input("请输入密码: ")
        user_temp = find_user(users, input_name, input_pwd)
        if user_temp != None:
            print("欢迎登录")
            sys.exit()
        else:
            attempts_longin = attempts_longin + 1
            print("密码错误，请重新输入")
    else:
        print("用户多次输入错误，账户已经锁定")
        sys.exit()


if __name__ == '__main__':
    login()
