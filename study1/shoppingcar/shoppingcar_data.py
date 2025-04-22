# 写个一超市收银程序，显示商品列表，用户购买商品的过程
# 1，数据初始化，构建商品列表
# 2，用户购买商品
# 1，1定义商品参数（"名称"，编号，价格）
# 以对象形式初始化所有商品

# 定义总金额
# 定义商品参数（"名称"，编号，价格）然后打印
# 输入商品编号 获得总价格
# 判断总金额减去总价格，如果小于  提示“余额额不足”
# 如果大于则付款 提示还剩余额
from django_redis.client import herd


# 类
# 人
class good():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __print__(self):
        return "id " + str(self.id) + " name " + self.name + " price " + str(self.price)


def init():
    good_data = []
    a = good(1, "牙膏", 11)
    b = good(2, "牙刷", 13)
    c = good(3, "水杯", 8)
    good_data.append(a)
    good_data.append(b)
    good_data.append(c)
    for var in good_data:
        print(var.__print__())


if __name__ == '__main__':
    init()
