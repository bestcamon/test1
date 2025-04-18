# 定义两个数字
# 两个数字之间运算符号
# 用str字符串保存计算符号
# 判断运算符号+—*/ 调用不同的运算方法
# 计算表达式的返回值

# var 变量1
# var 变量2
# var 运算符号
#
# 主入口方法(变量1，变量2，运算符号)：
#     判断 运算符号 等于 加号
#         执行加法(变量1，变量2)
#     如果不是，继续判断，运算符号 等于 减号
#         执行减法(变量1.变量2)
#     如果不是，继续判断，运算符号 等于 乘号
#         执行乘法(变量1.变量2)
#     如果不是，继续判断，运算符号 等于 除号
#         执行除法(变量1.变量2)
#     以上都不是的运算符号
#         输出， 不符合运算符号
#
# 定义加法（变量1，变量2）
#     临时变量 等于 变量1 加 变量2
#       返回临时变量

# 计算两数
def mian_method(num1, str_type):
    if str_type == "+":
        return jiafa(num1, num2)
    elif str_type == "-":
        return jianfa(num1, num2)
    elif str_type == "*":
        return chengfa(num1, num2)
    elif str_type == "/":
        return chufa(num1, num2)
    else:
        print("不符合的运算符号")

# range() 只在for 使用，用来显示下标
# len()  返回当前变量的长度
# 计算多个数累加
def mian_method2(num, str_type):
    if str_type == "+":
        temp_var = 0
        for i in range(0, len(num)):
            if temp_var == 0:
                temp_var = jiafa(num[i], num[i + 1])
            elif i == len(num) - 1:
                return temp_var
            else:
                temp_var = jiafa(temp_var, num[i + 1])


def jiafa(num1, num2):
    temp_var = num1 + num2
    return temp_var


def jianfa(num1, num2):
    temp_var = num1 - num2
    return temp_var


def chengfa(num1, num2):
    temp_var = num1 * num2
    return temp_var


def chufa(num1, num2):
    temp_var = num1 / num2
    return temp_var


if __name__ == '__main__':
    num1 = 8
    num2 = 4

    # print(jiafa(num1, num2))
    # print(jianfa(num1, num2))
    # print(chengfa(num1, num2))
    # print(chufa(num1, num2))
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = ["张三","李四", 3, 4, 5, 6, 7, 8, 9]

    strwq="zhangsan"
    print(len(strwq))
    number = mian_method2(num, "+")
    print(number)
