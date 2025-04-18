# 实现一个充花费程序
# 1，有个电话号码
# 2,充话费的金额
# 伪代码
import sys

# 充话费主入口方法（电话号码，话费金额）
#      初始化用户数据
#     1，查询电话号码现有的话费，返回余额
#     余额 = 查询话费（电话号码）
#     现有话费余额 = 充话费方法（电话号码，余额，金额）
#     输出 现有话费

#
# 充话费主入口方法（电话号码，话费金额）
#     1，查询电话号码现有的话费，返回余额
#     余额 = 查询话费（电话号码）
#     现有话费余额 = 充话费方法（电话号码，余额，金额）
#     输出，话费是否充值成功
#     或者 话费任然不足，再请充值

map_data = {}
data_list = [1, 2, 3, 4, 5]


# 数据部分
def init():
    map_data["10086"] = 50
    map_data["10087"] = 60


# 查话费方法
def select_huafei_by_number(number):
    try:
        if map_data[number] != None:
            余额 = map_data[number]
    except KeyError:
        print("没有这个号码")
        sys.exit()
    return 余额


def updatehuafei(number, 余额, money):
    if map_data[number] != None:
        new_money = 余额 + money
        map_data[number] = new_money
    return new_money


def main_method(number, money):
    余额 = select_huafei_by_number(number)
    new_余额 = updatehuafei(number, 余额, money)
    print(new_余额)


if __name__ == '__main__':
    init()
    number = "10086"
    money = 50
    main_method(number, money)
