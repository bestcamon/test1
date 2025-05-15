import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建webDriver对象，指明使用chrome浏览器驱动
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 设置为无头
options.add_argument('--disable-gpu')  # 设置没有使用gpu
options.add_argument("--ignore-certificate-errors")  # 可选，忽略证书错误
options.add_argument("--no-sandbox")  # 可选，禁用沙盒模式

# 1.创建浏览器对象
chrome_driver_path = 'E:\\Tools\\chrome-win64\\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


# 大段落名称
def find_title():  # 每部小说的名称
    return driver.find_element(By.CLASS_NAME, 'catalog').find_element(By.TAG_NAME, "h1").text


# 获取网页
if __name__ == '__main__':
    # 隐式等待,防止程序过快而网页反应不过来(10s)
    # driver.implicitly_wait(10)

    main_url = 'https://www.ps3838.com/zh-cn/sports/soccer'

    # 打开网页
    driver.get(main_url)
    driver.implicitly_wait(5)
    # 定义一个字典， 存放每章的名字和内容
    odds_container_all_div = driver.find_elements(By.CLASS_NAME, 'odds-container')
    for my_leagues_div in odds_container_all_div:
        leagues_list = my_leagues_div.find_elements(By.CLASS_NAME, "league")
        for league in leagues_list:
            # 在每个 league 元素内部查找所有 <span> 子元素
            children = league.find_elements(By.XPATH, "./*")
            span_text = children[3].text  # 索引从 0 开始，第 4 个是 index=3
            print(span_text)
