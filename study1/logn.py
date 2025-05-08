import sys


class user():
    admin =0
    password = 0
    def __init__(self,admin,password):
        self.admin = admin
        self.password = password
def login():
    atemp_longin = 0
    max_atemp_login = 3
    def load_user_list(admin,password):
        if int(atemp_longin) < int(max_atemp_login):
            #尝试过不用int  但是我明明已经设置atemp_longin已经定义了等于0
            #报错显示为解析到这个定义函数
            admin = input("用户名")
            password =input("密码")
            if admin == "1234" and password == "2345":
                return print("欢迎登录")
            else:
                atemp_longin = atemp_longin + 1
                print("密码错误，请重新输入")
        else:
            print("用户多次输入错误，账户已经锁定")
            sys.exit()

if __name__ == '__main__':
    login()





