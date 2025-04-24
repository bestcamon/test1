#定义总金额
#定义商品参数（"名称"，编号，价格）然后打印
#输入商品编号 获得总价格
#判断总金额减去总价格，如果小于  提示“余额额不足”
#如果大于则付款 提示还剩余额
gold_data = []
牙膏_price = 11
牙刷_price = 13
水杯_price =  8
牙膏_id = "001"
牙刷_id = "002"
水杯_id = "003"

牙膏 = str(牙膏_id)+" "+"牙膏"+" "+str(牙膏_price)
牙刷 = str(牙刷_id)+" "+"牙刷"+" "+str(牙膏_price)
水杯 = str(水杯_id)+" "+"水杯"+" "+str(水杯_price)
id_data = [str(牙刷_id),str(牙膏_id),str(水杯_id)]
price_data =[str(牙膏_price),str(牙刷_price),str(水杯_price)]

good_list=[str(牙膏),str(牙刷),str(水杯)]
id_data = [str(牙刷_id),str(牙膏_id),str(水杯_id)]
def 进入列表(gold_data):
    if gold_data!=None:
        return print(good_list)
    else:print("余额不足，请充值!")
tempvar = 0
payment = 0
def select_goods(id_data):
    if   type=="001":
        print("牙膏"+"  "+str(牙膏_price)+"元")
        tempvar=str(牙膏_price)
    elif type=="002":
        print("牙刷"+"  "+str(牙刷_price)+"元")
        tempvar = str(牙刷_price)
    elif type=="003":
        print("水杯"+"  "+str(水杯_price)+"元")
        tempvar = str(水杯_price)
    else:return print("查询不到此商品")

def pay_goods (gold_data,tempvar):
    if gold_data >= str(tempvar) : True
    balance = gold_data - str(tempvar)
    print("付款成功，余额还剩"+str(balance)+"元")



. = ()




