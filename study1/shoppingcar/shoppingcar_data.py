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
class product():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __print__(self):
        return "id " + str(self.id) + " name " + self.name + " price " + str(self.price)


def find_product(good_data, good_id):
    for good in good_data:
        if good.id == good_id:
            return good


def init():
    product_data = []
    a = product(1, "牙膏", 11)
    b = product(2, "牙刷", 13)
    c = product(3, "水杯", 8)
    product_data.append(a)
    product_data.append(b)
    product_data.append(c)
    for var in product_data:
        print(var.__print__())
    return product_data


if __name__ == '__main__':
    product_data = init()
    balance = 500

    print("欢迎来到自动售货系统！")
    print(f"您的初始余额：{balance}元")
    print("退出系统请输入 exit\n")
    while True:
        print("是否购买商品？Y/N")
        input_value = input()
        if input_value == "Y" or input_value == "y":
            while True:
                print("选择商品id：，返回上一层输入0")
                input_value = input()
                gold_id = int(input_value)
                if input_value == "0":
                    break
                else:
                    var = find_product(product_data, gold_id)
                    print(var.__print__())
