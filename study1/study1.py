dataclasses = "张三"
dataclasses2 = """
hello 
word
"""
flag = True
flag2 = False
data = None
data2 = ""
print(type(data2))
print(type(data))
numbers = 2
numbers2 = 0.2
print(type(numbers))
print(type(numbers2))
# print(1111)
a = ["zhangsan","lisi"]
a1 = {}
print(type(a))
print(type(a1))
a1["zhangsan"]="张三"
a1["lisi"]="李四"
# print(a1)
# print(a1.get("lisi"))
# print(a)

value = a[0]
print(value)
value = a[1]
print(value)

for value in a:
    print(value)
for index in range(0,a.__len__()):
    print(index)