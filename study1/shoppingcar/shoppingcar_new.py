import sys


# 初始化商品数据
# ；
def init_products():
    """初始化商品数据"""
    return [
        {"id": 1, "name": "牙膏", "price": 12, "num": 10},
        {"id": 2, "name": "牙刷", "price": 5, "num": 10},
        {"id": 3, "name": "水杯", "price": 8, "num": 10}
    ]


def print_product(data):
    """打印单个商品信息"""
    print("商品id: " + str(data["id"]))
    print("商品名称: " + data["name"])
    print("商品价格: " + str(data["price"]) + "元")
    print("剩余库存: " + str(data["num"]))
    print("-" * 30)


def show_all_products(products):
    """显示所有商品信息"""
    print("\n当前可购商品清单：")
    for product in products:
        print_product(product)
    print("商品展示玩成！")


def find_product(products, product_id):
    """根据商品编号查找商品"""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def shopping_process(balance, products):
    """处理购物流程"""
    while True:
        user_input = input("请输入商品编号进行购买 (0返回/exit退出)：").strip()

        if user_input.lower() == "exit":
            sys.exit()
        if user_input == "0":
            return balance

        try:
            product_id = int(user_input)
        except ValueError:
            print("输入错误，请重新输入！")
            continue

        product = find_product(products, product_id)

        if not product:
            print("商品不存在！")
            continue
        if product["num"] <= 0:
            print("该商品已售罄！")
            continue

        print("\n您选择的商品信息：")
        print_product(product)

        confirm = input("是否购买此商品？(Y/N) ").upper()
        if confirm != "Y":
            continue

        if balance >= product["price"]:
            balance -= product["price"]
            product["num"] -= 1
            print(f"购买成功！当前余额：{balance}元")
        else:
            print("余额不足，购买失败！")

        if input("是否继续购物？(Y/N) ").upper() != "Y":
            return balance


# 初始化数据
# 商品信息对象化  set 商品信息
# 初始化商品的id，name ，price，num
# 初始化方法():
#   商品1= 商品(id，name ，price，num)
#   商品2= 商品(id，name ，price，num)
#   商品3= 商品(id，name ，price，num)
#   商品集合=[]
#   商品集合.添加(商品1)
#   商品集合.添加(商品2)
#   商品集合.添加(商品3)
#   返回 商品集合


# 进入系统，打印商品礼表
# 循环 商品列表 定义临时变量商品：
#     输出商品信息


# 主程序入口
#   初始化商品列表 定义商品集合变量
#   定义用户余额
#   循环：
#        打印商品列表
#        询问客户是否购物   返回客户键入信息，定义变量（是或者否）
#        判定客户输入y：
#             键入购物方法（）：返回余额
#             判定用户余额是否和初始化金额是否一致
#                 把消费余额赋值给初始金额变量
#                 打印当前初始金额变量
#
#
#        判定客户输入N 或者其他
#             输出退出程序
#             退出程序
# 购物方法（）：
#   进入循环：
#      客户输如商品编号，返回客户键入信息，定义变量
#      如果用户输入0
#         跳出方法，返回余额
#      如果用户输出exit
#         退出程序
#      监控：
#           把定义的商品id变量 转化为数字型变量
#      捕获异常 ：
#           输出并返回  （输入错误重新输入）
#           ”continue“
#      返回商品  = 设置查找方法（商品集合，商品di）
#      如果商品返回为空：
#         输出（商品不存在）
#          跳出本次循环
#      如果商品库存数量小于等于0
#         输出（商品已售罄）
#         跳出本次循环
#      打印选择的商品信息
#      客户键入是否购买商品 是或者否 ，定义变量
#      如果不是y:
#         跳出本次循环#
#      如果是y：
#          如果余额>= 商品价格
#             创建临时变量 = 余额减去 -商品价格
#             余额=创建临时变量
#             商品库存-1
#             输出（商品购买成功！当前余额）
#          else：
#             输出（余额不足，购买失败）
#          询问是否购物  定义变量
#          判定y:
#             continue
#          else:
#               return 跳出方法 返回余额
#
#
#
# 退出


if __name__ == "__main__":
    """主程序逻辑"""
    products = init_products()
    balance = 500

    print("欢迎来到自动售货系统！")
    print(f"您的初始余额：{balance}元")
    print("退出系统请输入 exit\n")

    while True:
        show_all_products(products)
        choice = input("是否开始购物？(Y/N) ").upper()

        if choice == "N":
            print("感谢使用，再见！")
            sys.exit()
        if choice == "Y":
            new_balance = shopping_process(balance, products)
            if new_balance != balance:
                balance = new_balance
                print(f"\n当前剩余余额：{balance}元")
                if balance < min(p["price"] for p in products):
                    print("余额已不足以购买任何商品！")
                    sys.exit()
        else:
            print("输入无效，请重新输入！")
