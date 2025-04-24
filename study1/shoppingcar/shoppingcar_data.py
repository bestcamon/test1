# 类
# 人
class good():
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
    good_data = []
    a = good(1, "牙膏", 11)
    b = good(2, "牙刷", 13)
    c = good(3, "水杯", 8)
    good_data.append(a)
    good_data.append(b)
    good_data.append(c)
    for var in good_data:
        print(var.__print__())
    return good_data


if __name__ == '__main__':
    good_data = init()
    while True:
        print("是否购买商品?Y/N")
        input_id = input()
        if input_id == "Y" or input_id == "y":
            print("选择商品id，输入 8 返回上一层。")
            input_id = input()
            good_id = int(input_id)
            if input_id == "8":
                break
            else:
                var = find_product(good_data, good_id)
                print(var.__print__())
                print("是否购买商品？Y/N")
                input_var = input()
                if input_var == "y" or input_var == "y":
                    print("请输入金额")
                    input_money = input()
                    input_money = int(input_money)
                    if input_money >= var.price:
                        balance = input_money - var.price
                        print("购买成功，余额还剩" + str(balance) + "元")
                        print("是否继续购买？Y/N")
                        input_a =input()
                        if input_a=="Y" or input_a =="y":
                            continue
                    else:
                        print("余额不足，返回上一层")
                        continue
