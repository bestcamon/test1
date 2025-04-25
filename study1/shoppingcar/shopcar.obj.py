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

    def init(self, id, name, money):
        self.id = id
        self.name = name
        self.money = money

    def check(self, product):
        self.money = self.money - product.price * 1.1
        self.product_list.append(product)


#     product = product(1, "牙刷", 10, 10)
#     返回客户信息 = 查找用户方法()
#               使用客户信息替换临时用户变量
# user1 = user_temp()
# user2 = user_vip(1, "sam", 100)
# user1 = user2
# print(user1.check(product))


def init():
    user_init()
    return product_init()


def product_init():
    return []


def user_init():
    return []


def print_product_list(product_list):
    for product in product_list:
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


if __name__ == '__main__':
    main()
