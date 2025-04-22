import sys


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
