#鸡兔同笼
#鸡有一个头两个脚
#兔子有一个头四个脚  数头有36个，数脚有94个，问鸡兔数量
#设鸡有x  兔子为y

#x+y=36
#2x+4y=94
#2x+2y=72
#94-72=2y
# y =11  x=25

def jitutonglong(head,foot):
    return (foot - head * 2) / 2

y=jitutonglong(36,94)
x=36-y
print(x,y)
