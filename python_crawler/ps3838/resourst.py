import re
import requests

respose = requests.get('https://www.ps3838.com/zh-cn/sports/soccer')
# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
# print(respose.text)  #返回文本内容 //*[@id='lg8584']/span
urls = re.findall(r"xpath='//*[@id='lg8584']/span'", respose.text, re.S)  # re.S 把文本信息转换成1行匹配
url = urls[5]
result = requests.get(url)
mp4_url = re.findall(r'id="media".*?src="(.*?)"', result.text, re.S)[0]

video = requests.get(mp4_url)

with open('D:\\a.mp4', 'wb') as f:
    f.write(video.content)