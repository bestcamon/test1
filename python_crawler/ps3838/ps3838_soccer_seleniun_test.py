import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 创建webDriver对象，指明使用chrome浏览器驱动
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 设置为无头
options.add_argument('--disable-gpu')  # 设置没有使用gpu
options.add_argument("--ignore-certificate-errors")  # 可选，忽略证书错误
options.add_argument("--no-sandbox")  # 可选，禁用沙盒模式

# 1.创建浏览器对象
chrome_driver_path = 'E:\\Tools\\chrome-win64\\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


def find_title(leagues_list):
    for league in leagues_list:
        # 在每个 league 元素内部查找所有 <span> 子元素
        id = league.get_attribute("id")
        children = league.find_elements(By.XPATH, "./*")
        title_dict[id] = children[3].text  # 索引从 0 开始，第 4 个是 index=3


def main(main_url):
    # 打开网页
    driver.get(main_url)
    driver.implicitly_wait(5)
    # 定义一个字典， 存放每章的名字和内容
    odds_container_all_div = driver.find_elements(By.CLASS_NAME, 'odds-container')
    for my_leagues_div in odds_container_all_div:
        leagues_list = my_leagues_div.find_elements(By.CLASS_NAME, "league")
        find_title(leagues_list)
        # 获取league下的下一个下标的容器
        all_element_list = find_all_leagues(my_leagues_div)
        for index in range(len(all_element_list)):
            element = all_element_list[index]
            class_name = element.get_attribute("class")
            if class_name != None and class_name != '' and class_name == 'league':
                div_arr = all_element_list[index + 1].find_elements(By.XPATH, "./*")
                get_body_div(div_arr[0])


title_dict = {}


def get_body_div(body_div):
    body_div.get_attribute("id")


def find_all_leagues(body_div):
    all_element_list = body_div.find_elements(By.XPATH, "./*")
    if len(all_element_list) > 1:
        return all_element_list
    else:
        return find_all_leagues(all_element_list[0])


def find_all_leagues_while(body_div):
    while True:
        all_element_list = body_div.find_elements(By.XPATH, "./*")
        if len(all_element_list) <= 1:
            body_div = all_element_list[0]
            continue
        return all_element_list


# 获取网页
def div_click():
    # more_1609805765
    driver.get(main_url)
    driver.implicitly_wait(5)
    # 定义一个字典， 存放每章的名字和内容
    odds_container_all_div = driver.find_element(By.ID, 'more_1609805765')
    odds_container_all_div.click()
    time.sleep(10)


if __name__ == '__main__':
    # 隐式等待,防止程序过快而网页反应不过来(10s)
    # driver.implicitly_wait(10)
    main_url = 'https://www.ps3838.com/zh-cn/sports/soccer'
    try:
        main(main_url)
    except Exception as e:
        print(e)
    finally:
        driver.close()
