'''import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
buff = response.read()
html = buff.decode("utf8")
print(html)
'''
import threading
import time
from threading import Thread


# import urllib.request
#
# request = urllib.request.Request('http://www.baidu.com')
# response = urllib.request.urlopen(request)
# buff = response.read()
# html = buff.decode("utf8")
# print(html)

# 定义一个模拟长时间运行的任务的函数
def print_numbers():
    for i in range(5):
        print(f"数字: {i}")
        time.sleep(1)  # 模拟耗时操作


# 定义另一个模拟长时间运行的任务的函数
def print_letters():
    for letter in 'ABCDE':
        print(f"字母: {letter}")
        time.sleep(1)  # 模拟耗时操作


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()
