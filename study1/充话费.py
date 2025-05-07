import sys


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


def init():
    user_list = []
    user1 = user(12345, 50)
    user2 = user(23456, 20)
    user3 = user(34567, 80)
    user_list.append(user1)
    user_list.append(user2)
    user_list.append(user3)
    return user_list


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
                sys.exit()
        else:
            sys.exit()