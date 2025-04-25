import sys


class product():
    id = 0
    name = ""
    price = 0
    num = 0

    def __init__(self, id, name, price, num):
        self.id = id
        self.name = name
        self.price = price
        self.num = num

    def __print__(self):
        return "id " + str(self.id) + " name " + self.name + " price " + str(self.price)


class user():
    id = 0
    name = ""
    money = 0
    product_list = []

    def check(self, product):
        self.money = self.money - product.price


class user_vip(user):
    def __init__(self, id, name, money):
        self.id = id
        self.name = name
        self.money = money

    def check(self, product):
        self.money = self.money - product.price * 0.8
        self.product_list.append(product)


class user_temp(user):
    def __init__(self):
        self.id = 0
        self.name = "temp"
        self.money = 0

    def __init__(self, id, name, money):
        self.id = id
        self.name = name
        self.money = money

    def check(self, product_price):
        self.money = self.money - product_price * 1.1
        self.product_list.append(product)


def init():
    user_init()
    return product_init()


def product_init():
    return []


def user_init():
    return []


def print_product_list(product_list):
    for product  in product_list :
        product.__print__()


def shopping(user, product_list):
    pass


def main():
    product_list = init()
    temp_user = user_temp()
    while True:
        print_product_list(product_list)
        print("用户是否购物y/n")
        input_var = input().upper()
        if input_var == "Y":
            temp_user = shopping(temp_user, product_list)
            if len(temp_user.product_list) != 0:
                print_product_list(temp_user.product_list)
                print(temp_user.money)
        else:
            print("退出程序")
            sys.exit(0)
