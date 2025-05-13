import requests
from bs4 import BeautifulSoup
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Cookie': 'bid=zRNGYnptpG4; douban-fav-remind=1; viewed="35035944"; gr_user_id=184492c6-aeef-4982-901f-1b09c2068705; ap_v=0,6.0; _pk_id.100001.4cf6=074e6710f58c43d9.1689427734.; __utmc=30149280; __utmz=30149280.1689427737.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; ll="108088"; __yadk_uid=CiTsJsC2AkO8osEEuxsxgH6aSpdU3hJF; __gads=ID=45e9ee92cf4ec1b5-22fb1d284fdc006e:T=1680781559:RT=1689427756:S=ALNI_MYITBoTB0r8a8JzXtf9AAGAyofW6w; __gpi=UID=00000bfc2637c48e:T=1680781559:RT=1689427756:S=ALNI_Mb5gSJq3sFe87EZ8i9AAS4pTEK98g; _vwo_uuid_v2=D3D419E1B418DCC4CD5D70BA518A20948|a16e6c827b6f325ea0acbef2466a9c40; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1689431498%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.1385780288.1680781559.1689427737.1689431498.4; __utmt=1; dbcl2="264274455:bzQqX8oD3K8"; ck=OlkX; __utmt_douban=1; __utma=223695111.1736987962.1689427737.1689427737.1689431546.2; __utmb=223695111.0.10.1689431546; __utmz=223695111.1689431546.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26427; __utmb=30149280.7.10.1689431498'
}
main_url = 'https://www.51shucheng.net/wangluo/longzu'


# 把打开网页获取页面的步骤写成函数
def open_page(url):
    """
    html: url地址
    return : html的page页面
    """
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    html = html.text

    return html


# 把构建soup找到页面对应内容的步骤写成函数
def find_content(html, selector, class_):
    """
    html: 网页page页面
    selector: 对应的页面元素
    class_: 对应类名
    return : 想要的页面内容
    """
    soup = BeautifulSoup(html, features='lxml')
    wanted_content = soup.find_all(selector, class_=class_)

    return wanted_content


# 把小说内容写入文件中
def write_content(name, chapter_name, content):
    """
    name: 小说名称
    chapter_name: 章节名称
    content: 章节内容
    """

    # 如果小说的目录不存在，则创建目录；如果存在则删除重建一个
    path = os.path.join(f"./{name}")
    if os.path.exists(path):
        file = os.path.join(path, f"{chapter_name + '.txt'}")
        print(file)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        os.mkdir(path)
        file = os.path.join(path, f"{chapter_name + '.txt'}")
        print(file)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)


# 获取网页
main_html = open_page(main_url)

# 获得每部小说的url
fictions = find_content(main_html, "div", "mulu-list quanji")
fiction_names = find_content(main_html, 'div', 'mulu-title')  # 每部小说的名称
fiction_urls = []  # 以列表形式存储小说第几部，第几部的名称，第几章，章节名称

for i in range(len(fictions)):
    urls = fictions[i].find_all("a")
    name = fiction_names[i].text
    for j in range(len(urls)):
        url, title = urls[j]['href'], urls[j].text
        fiction_urls.append([i + 1, name, title, url])

# 获取每章节的内容
for i in range(len(fiction_urls)):
    num = fiction_urls[i][0]  # 属于第几部小说
    if num == 1 or num == 2:
        continue
    name = fiction_urls[i][1]
    title = fiction_urls[i][2]  # 章节名称
    print(f"{'*' * 5}开始第{num}部小说《{name}》的  {title}  爬取{'*' * 5}")

    html = open_page(fiction_urls[i][3])
    content = find_content(html, "div", 'neirong')[0].text
    write_content(name, title, content)
    time.sleep(num)
