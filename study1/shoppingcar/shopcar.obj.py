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
#     使用客户信息替换临时用户变量
# user1 = user_temp()
# user2 = user_vip(1, "sam", 100)
# user1 = user2
# print(user1.check(product))


def init():
    a = product_init()
    b = user_init()
    data_list = [a, b]
    return data_list


def product_init():
    product_list = []
    product_1 = product(1, "牙膏", 10, 10)
    product_2 = product(2, "牙刷", 8, 10)
    product_3 = product(3, "水杯", 8, 10)
    product_list.append(product_1)
    product_list.append(product_2)
    product_list.append(product_3)
    return product_list
    # return [
    #     {"id": 1, "name": "牙膏", "price": 12, "num": 10},
    #     {"id": 2, "name": "牙刷", "price": 5, "num": 10},
    #     {"id": 3, "name": "水杯", "price": 8, "num": 10}
    # ]


def user_init():
    user_list = []
    user1 = user_vip(1, "张三", 100)
    user2 = user_vip(2, "李四", 100)
    user3 = user_vip(3, "王五", 100)
    user_list.append(user1)
    user_list.append(user2)
    user_list.append(user3)
    return user_list

    # return [
    # ={"id": 1, "name": "张三", "money": 1500, "product_list": product},
    #     {"id": 2, "name": "李四", "money": 500, "product_list": product},
    #     {"id": 3, "name": "王五", "money": 600, "product_list": product}
    # ]


def print_product_list(product_list):
    for product in product_list:
        print(product.__print__())


def find_product(product_list, product_id):
    for product in product_list:
        if product.id == product_id:
            return product


def find_user(user_list, user_id):
    for user in user_list:
        if user.id == user_id:
            return user


def shopping(user, product_list, user_list):
    while True:
        print("客户输入商品编号")
        inputvar = input()
        if int(inputvar) == 0:
            return user
        elif inputvar == "exit":
            sys.exit()
        try:
            input_int_var = int(inputvar)
        except ValueError:
            print("输入错误，重新输入")
            continue
        product = find_product(product_list, input_int_var)
        if product == None:
            print("商品不存在")
            continue
        if product.num <= 0:
            print("商品已售罄")
            continue

        print(product.__print__())
        print("客户是否购买商品?y/n")

        input1 = input()
        if input1.upper() != "Y":
            continue
        else:
            print("请输入客户id")
            var1 = int(input())
            user1 = find_user(user_list, var1)
            if user1 == None:
                print("输入付款金额")
                var2 = int(input())
                user.money = var2
            else:
                user = user1
            if user.money >= product.price:
                user.check(product)
                product.num = product.num - 1
                print("商品购买成功！余额还剩" + str(user.money) + "元。")
            else:
                print("当前余额不足")
                print("是否继续购物y/n")
                var3 = input()
                if var3.upper() != "Y":
                    continue
                else:
                    return user


def main():
    print()
    list = init()
    product_list = list[0]
    user_list = list[1]
    temp_user = user_temp()
    while True:
        print_product_list(product_list)
        print("用户是否购物y/n")
        input_var = input().upper()
        if input_var == "Y":
            temp_user = shopping(temp_user, product_list, user_list)
            if len(temp_user.product_list) != 0:
                print_product_list(temp_user.product_list)
                print(temp_user.money)
        else:
            print("退出程序")
            sys.exit(0)


if __name__ == '__main__':
    main()
