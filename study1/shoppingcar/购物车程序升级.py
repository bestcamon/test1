import os
import sys


class user():
    username = 0
    password = 0
    id = 0
    name = ""
    money = 0
    shopping_car = None

    def __init__(self):
        self.shopping_car = shopping_car()

    def add_product(self, product):
        self.shopping_car.add_product(product)

    def delete_product(self, product):
        self.shopping_car.delete_product(product)

    def update_money(self, new_money):
        self.money = self.money + new_money
        print(self.name + " 充值成功 " + str(new_money) + "元，现有余额为" + str(self.money) + "元")


class product():
    id = 0
    name = ""
    price = 0
    stock = 0
    shopping_car_product_count = 1

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __print__(self):
        return "id " + str(self.id) + " name " + self.name + " price " + str(self.price)

    def __copy__(self):
        copy = product(self.id, self.name, self.price, self.stock)
        copy.shopping_car_product_count = self.shopping_car_product_count
        return copy


class user_vip(user):
    def __init__(self, username, password, id, name, money):
        super().__init__()
        self.username = username
        self.password = password
        self.id = id
        self.name = name
        self.money = money

    def check(self):
        self.money = self.money - self.shopping_car.check() * 0.8


class user_temp(user):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.name = "temp"
        self.money = 0

    def init(self, id, name, money):
        self.id = id
        self.name = name
        self.money = money

    def check(self):
        self.money = self.money - self.shopping_car.check() * 1.1


class shopping_car():

    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        product_temp = self.find_product(product.id)
        if product_temp != None:
            product_temp.shopping_car_product_count = \
                product_temp.shopping_car_product_count + \
                product.shopping_car_product_count
        else:
            self.product_list.append(product)

    def delete_product(self, product):
        product_temp = self.find_product(product.id)
        if product_temp == None:
            return
        if product_temp.shopping_car_product_count >= 2:
            product_temp.shopping_car_product_count = \
                product_temp.shopping_car_product_count - 1
        else:
            self.product_list.remove(product_temp)

    def delete_product_by_id(self, product_id):
        product_temp = self.find_product(product_id)
        self.delete_product(product_temp)

    def find_product(self, product_id):
        for product in self.product_list:
            if product.id == product_id:
                return product
        return None

    def check(self):
        all_price = 0
        for product in self.product_list:
            all_price = all_price + product.price * product.shopping_car_product_count
        return all_price

    def print_shopping_car(self):
        for product in self.product_list:
            print(product.__print__())


def user_init():
    users = []
    users.append(user_vip("1234", "2345", 1234, "张三", 100))
    users.append(user_vip("1235", "2346", 1235, "张三1", 100))
    users.append(user_vip("1236", "2347", 1236, "张三2", 100))
    users.append(user_vip("1237", "2348", 1237, "张三3", 100))
    users.append(user_vip("1238", "2349", 1238, "张三4", 100))
    users.append(user_vip("1239", "2350", 1239, "张三5", 100))
    return users


user_list_file_path = r"D:\python workspace\test1\data\product_list.txt"
product_list_file_path = r"D:\python workspace\test1\data\user_list.txt"


# def read_sys_shoppingcar():
#     a = os.path.exists(user_list_file_path)
#     b = os.path.exists(product_list_file_path)
#
#     user_list = []
#     product_list =[]
#     x = user_list
#     y = product_list
#     read_sys_shoppingcar =[x,y]
#     with  open(user_list_file_path, "r") as file:
#         for line in file:
#             user_value = line.strip()
#             user_list.append(user_value)
#             return user_list
#     with  open(product_list_file_path, "r") as file:
#         for line in file:
#             product_value = line.strip()
#             product_list.append(product_value)
#             return product_list
## def init():
#     user_list = read_sys_shoppingcar[1]
#
#     product_list  = read_sys_shoppingcar[2]
#     for user_value in user_data_list:
#         user_value_arr = user_value.split(',')
#         user_obj = user(int(user_value_arr[0]), int(user_value_arr[1]))
#         user_list.append(user_obj)
#     return user_list
#     return product_init()
def read_user_list():
    a = os.path.exists(user_list_file_path)
    user_list = []
    with open(user_list_file_path, "r") as file:
        for line in file:
            user_value = line.strip()
            user_list.append(user_value)
            return user_list


def read_product_list():
    product_list = []
    with open(product_list_file_path, "r") as file:
        for line in file:
            product_value = line.strip()
            product_list.append(product_value)
            return product_list


def init():
    user_data_list = read_user_list()
    user_list = []
    for user_value in user_data_list:
        user_value_arr = user_value.split(",")
        user_obj = user_vip(str(user_value_arr[0]), str(user_value_arr[1]), int(user_value_arr[2]),
                            str(user_value_arr[4]), int(user_value_arr[5]))
        user_list.append(user_obj)
        return user_list

    product_data_list = read_product_list()
    product_list = []
    for product_value in product_data_list:
        product_value_arr = product_value.split(",")
        product_obj = product(int(product_value_arr[1]), str(product_value_arr[2]),
                              int(product_value_arr[3]),
                              int(product_value_arr[4]))
        product_list.append(product_obj)
        return product_list


def save_user_data(user_list):
    a = os.path.exists(user_list_file_path)
    user_data_list = []
    for user_vip in user_list:
        user_data = str(user_vip.username) + "," + str(user_vip.password) + "," + str(user_vip.name) + "," + str(
            user_vip.id) + "," + str(user_vip.money) + "\n"
        user_data_list.append(user_data)

    user_file = open(user_list_file_path, "w")
    with user_file:
        user_file.writelines(user_data_list)
    user_file.close()


def save_product_data(product_list):
    a = os.path.exists(product_list_file_path)
    product_data_list = []
    for product in product_list:
        product_data = str(product.id) + "," + str(product.name) + "," + str(product.price) + "," + str(
            product.stock) + "\n"
        product_data_list.append(product_data)

    product_file = open(product_list_file_path, "w")
    with product_file:
        product_file.writelines(product_data_list)
    product_file.close()


def find_user(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user


def login():
    atemp_login = 0
    max_atemp_login = 3
    while True:
        if atemp_login < max_atemp_login:
            users = user_init()
            input_name = input("请输入用户名: ")
            input_pwd = input("请输入密码: ")
            user_temp = find_user(users, input_name, input_pwd,user.name,users.money)
            if user_temp != None:
                print("欢迎登录")
                return user_temp
            else:
                atemp_login = atemp_login + 1
                print("密码错误，请重新输入")
        elif atemp_login >= max_atemp_login:
            print("多次输入错误，账户已经锁定")
            sys.exit()


def product_init():
    product_list = []
    product_1 = product(1, "牙膏", 10, 10)
    product_2 = product(2, "牙刷", 8, 10)
    product_3 = product(3, "水杯", 8, 10)
    product_list.append(product_1)
    product_list.append(product_2)
    product_list.append(product_3)
    return product_list


def print_product_list(product_list):
    for product in product_list:
        print(product.__print__())


def find_product(product_list, product_id):
    for product in product_list:
        if product.id == product_id:
            return product


def shopping(user, product_list):
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
        if product.stock <= 0:
            print("商品已售罄")
            continue
        print(product.__print__())
        print("客户是否购加入购物车?y/n")

        input1 = input()
        if input1.upper() != "Y":
            continue
        else:
            print("请输入商品数量")
            var1 = int(input())
            product_temp = product.__copy__()
            if var1 > 1:
                product_temp.shopping_car_product_count = var1
            user.add_product(product_temp)

            print("是否继续购物？y/n")
            input1 = input()
            if input1.upper() == "Y":
                continue
            else:
                print("开始结账")
                user.shopping_car.print_shopping_car()
                all_prince = user.shopping_car.check()
                print("本次购物总价" + str(all_prince) + "元")
                print("用户钱包" + str(user.money) + "元")
                print("开始结账")
                user.check()
                product.stoke = product_temp.stock - product_temp.shopping_car_product_count
                if user.money > 0:

                    print("感谢本次购物，账户余额还剩" + str(user.money) + "元")
                    return user
                    save_user_data(user)
                    save_product_data(product)
                    sys.exit()
                else:
                    print("本次购物还需充值" + abs(user.money) + "元")
                    print("账户余额不足，请问是否充值")
                    print("请输入充值金额")
                    var1 = int(input())
                    user.update_money(var1)
                    user.check()
                    product.stock = product.stock - product_temp.shopping_car_product_count
                    print("感谢本次购物，账户余额还剩" + str(user.money) + "元")
                    return user
                    save_user_data(user)
                    save_product_data(product)
                    sys.exit()


def main():
    user = login()
    product_list = init()
    while True:
        print_product_list(product_list)
        print("用户是否购物y/n")
        input_var = input().upper()
        if input_var == "Y":
            shopping(user, product_list)
            if len(user.product_list) != 0:
                print_product_list(user.product_list)
                print(user.money)
                print("用户是否继续购物y/n")
                input_var = input().upper()
                if input_var == "Y":
                    continue
                else:
                    sys.exit()


#


if __name__ == '__main__':
    main()
