# 打印乘法口诀
# 思路 递增 递减  两个for循环
# 须有两个三个变量  乘数 被乘数  和积数
# 乘数每循环1轮+1 被乘数每次+1 每次得来的积打印出来
# 第一个for循环我们打印的是行  第二个for循环打的列


# number1+1  * number2+1
# for numbers1 in range(1, 10):
#     for numbers2 in range(1,numbers1+1):
#         data = str(numbers1) + " * " + str(numbers2) + " = " + str(numbers1 * numbers2) + "  "
#         print(data, end="")
#     print()
def 乘法口诀():
    for numbers1 in range(1, 100):
        for numbers2 in range(1, numbers1 + 1):
            data = str(numbers1) + " * " + str(numbers2) + " = " + str(numbers1 * numbers2) + "  "
            print(data, end="")
        print()
if __name__ == '__main__':
    乘法口诀()

