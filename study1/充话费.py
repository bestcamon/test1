import os
import sys

user_file_path = r"E:\workspace\githubDownloads\test1\data\user_data.txt"


class user():
    number = 0
    money = 0

    def __init__(self, number, money):
        self.number = number
        self.money = money

    def __print__(self):
        return "number " + str(self.number) + "  money  " + str(self.money)

    def update_money(self, rmb):
        self.money = rmb + self.money


def find_user_by_number(number, user_list):
    for user in user_list:
        if user.number == number:
            return user


def top_up(user, money):
    user.update_money(money)
    print(user.__print__())
    return user


def user_init():
    user_list = []
    user1 = user(12345, 50)
    user2 = user(23456, 20)
    user3 = user(34567, 80)
    user_list.append(user1)
    user_list.append(user2)
    user_list.append(user3)
    return user_list


def read_user_file():
    a = os.path.exists(user_file_path)
    user_data_list = []

    # case 1
    # with 语句：当使用 with 语句打开文件时，Python 自动管理文件的打开和关闭过程。一旦执行流离开 with 代码块（无论是正常结束还是因为异常而提前退出），文件将自动关闭。
    with  open(user_file_path, "r") as file:
        for line in file:
            user_value = line.strip()  # 使用 strip() 去除行末的换行符和空白字符
            user_data_list.append(user_value)

    # case 2
    # 传统方式，手动打开和关闭文件
    # user_file = None
    # try:
    #     user_file = open(user_file_path, "r")
    #     for line in user_file:
    #         user_value = line.strip()  # 使用 strip() 去除行末的换行符和空白字符
    #         user_data_list.append(user_value)
    # finally:
    #     if user_file is not None:
    #         user_file.close()

    return user_data_list


# 110,50
# 119,100
# 120,200
def init():
    user_data_list = read_user_file()
    user_list = []
    for user_value in user_data_list:
        user_value_arr = user_value.split(',')
        user_obj = user(int(user_value_arr[0]), int(user_value_arr[1]))
        user_list.append(user_obj)
    return user_list


def save_data(user_list):
    a = os.path.exists(user_file_path)
    user_data_list = []
    for user in user_list:
        data_user = str(user.number) + "," + str(user.money) + "\n"
        user_data_list.append(data_user)

    user_file = open(user_file_path, "w")
    with user_file:
        user_file.writelines(user_data_list)
    user_file.close()


if __name__ == '__main__':
    user_list = init()
    while True:
        print("用户是否充值？y/n")
        input_var = input().upper()
        if input_var == "Y":
            print("输入电话号码")
            input_number = int(input())
            user_temp = find_user_by_number(input_number, user_list)
            print(user_temp.__print__())
            print("请输入充值金额")
            input_money = int(input())
            top_up(user_temp, input_money)
            print("是否继续充值y/n")
            input_var = input().upper()
            if input_var == "Y":
                continue
            else:
                save_data(user_list)
                sys.exit()
        else:
            sys.exit()
