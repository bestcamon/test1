# 定义总金额
# 定义商品参数（"名称"，编号，价格）然后打印
# 输入商品编号 获得总价格
# 判断总金额减去总价格，如果小于  提示“余额额不足”
# 如果大于则付款 提示还剩余额
import sys

gold_data = []


def init():
    obj = {}
    obj["id"] = 1
    obj["name"] = "牙膏"
    obj["price"] = 12
    obj["num"] = 10

    gold_data.append(obj)

    obj1 = {}
    obj1["id"] = 2
    obj1["name"] = "牙刷"
    obj1["price"] = 5
    obj1["num"] = 10
    gold_data.append(obj1)

    obj2 = {}
    obj2["id"] = 3
    obj2["name"] = "水杯"
    obj2["price"] = 8
    obj2["num"] = 10
    gold_data.append(obj2)


def print_gold_data():
    for data in gold_data:
        print(data)
    print("商品展示玩成！")


def print_data(data):
    print("id: " + str(data["id"]))
    print("商品名: " + data["name"])
    print("商品价格: " + str(data["price"]))
    print("------------------------------")


# 牙膏 = str(牙膏_id) + " " + "牙膏" + " " + str(牙膏_price)
# 牙刷 = str(牙刷_id) + " " + "牙刷" + " " + str(牙膏_price)
# 水杯 = str(水杯_id) + " " + "水杯" + " " + str(水杯_price)
# # id_data = [str(牙刷_id), str(牙膏_id), str(水杯_id)]
# price_data = [str(牙膏_price), str(牙刷_price), str(水杯_price)]
#
# good_list = [牙膏, str(牙刷), str(水杯)]
# id_data = [牙刷_id, 牙膏_id, 水杯_id]

#
# def 进入列表(gold_data):
#     if gold_data != None:
#         return print(good_list)
#     else:
#         print("余额不足，请充值!")
#

tempvar = 0
payment = 0


def pay_goods(gold_data, tempvar):
    if gold_data >= str(tempvar): True
    balance = gold_data - str(tempvar)
    print("付款成功，余额还剩" + str(balance) + "元")


def select_goods(id):
    pass
    # if id == 1:
    #     print("牙膏" + "  " + str(牙膏_price) + "元")
    #     tempvar = str(牙膏_price)
    # elif id == 2:
    #     print("牙刷" + "  " + str(牙刷_price) + "元")
    #     tempvar = str(牙刷_price)
    # elif id == 3:
    #     print("水杯" + "  " + str(水杯_price) + "元")
    #     tempvar = str(水杯_price)
    # else:
    #     return print("查询不到此商品")
    # print(tempvar)


#
# for id in id_data:
#     select_goods(id)
# pay_goods(gold_data, tempvar)

# 指定启动口情况下，所有程序以时序方式执行
# 时序，流程化执行，

if __name__ == '__main__':
    # 商品初始化
    init()
    print("商品初始化玩成！")
    print("输入exit推出！")
    # 打印商品
    print_gold_data()
    money = 500
    # 1,循环调用，除非输入exit推出
    # 1,用户选择商品，输入id
    # 2,显示商品信息
    # 3，用户输入支付金额
    # 4，结账，第一个，扣款成功，商品库存数量-1，显示付款成功，显示余额，询问是否继续购买，如果继续，就输入所有商品信息
    # ，扣款失败，显示扣款失败，金额不够
    # 5，用户推出
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
                    data = gold_data[gold_id]
                    print("商品信息：")
                    print_data(data)
                    print("是否购买商品？Y/N")
                    input_value = input()
                    if input_value == "Y" or input_value == "y":
                        print("输入金额：")
                        input_value = input()
                        new_money = int(input_value)
                        if new_money >= data.get("price"):
                            print("购买成功！")
                            data["num"] = data["num"] - 1
                        elif new_money < data.get("price"):
                            print("购买失败！金额不够!,返回上一层")
                    else:
                        print("返回上一层")
                        break
        else:
            print("推出程序")
            sys.exit()

        if input_value == "exit":
            sys.exit()

# print("输入金额：")
# input_value = input()
# new_money = int(input_value)
# if new_money >= data.get("price"):
#     print("购买成功！")
#     data["num"] = data["num"] - 1
# elif new_money < data.get("price"):
#     print("购买失败！金额不够")
# else:
#     print("是否继续浏览商品？ Y/N")
#     input_value = input()
#     if input_value == "Y" or input_value == "y":
#         continue
