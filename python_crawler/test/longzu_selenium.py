import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# https://googlechromelabs.github.io/chrome-for-testing/#stable
# 创建webDriver对象，指明使用chrome浏览器驱动
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 设置为无头
options.add_argument('--disable-gpu')  # 设置没有使用gpu
options.add_argument("--ignore-certificate-errors")  # 可选，忽略证书错误
options.add_argument("--no-sandbox")  # 可选，禁用沙盒模式

# 1.创建浏览器对象
chrome_driver_path = 'E:\\Tools\\chrome-win64\\chromedriver.exe'
Service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=Service, options=options)


# 把打开网页获取页面的步骤写成函数
def open_url(url):
    driver.get(url)


# 大段落名称
def find_title():  # 每部小说的名称
    return driver.find_element(By.CLASS_NAME, 'catalog').find_element(By.TAG_NAME, "h1").text


# 获取每章的名字和url
def find_chapter_name_and_url():
    chapter_name_and_url_dict = dict()
    xpath_options = [
        "//div[@class='mulu-list']",
        "//div[@class='mulu-list quanji']",
        "//div[@class='mulu-list-2 quanji']"
    ]
    chapter_list = []
    for xpath_option in xpath_options:
        chapter_list = driver.find_elements(By.XPATH, xpath_option)
        if chapter_list:
            break

    for chapter_item in chapter_list:
        table_element = chapter_item.find_elements(By.TAG_NAME, "li")  # 使用类的示例
        for item in table_element:
            chapter_name = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('title')
            chapter_url = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            chapter_name_and_url_dict[chapter_name] = chapter_url
            print(chapter_name, chapter_url)
    return chapter_name_and_url_dict


# 获取本章的内容
def get_chapter_value_by_url(chapter_url):
    open_url(chapter_url)
    return driver.find_element(By.CLASS_NAME, "neirong").text


# 文件写出
def write_book(file_path, chapter_name, book_dict):
    # 如果目录不存在，则创建目录；如果存在则删除重建一个
    path = os.path.join(f"{file_path}")
    file = os.path.join(path, f"{chapter_name + '.txt'}")
    print(file)
    with open(file, 'w', encoding='utf-8') as f:
        for book_key in book_dict:
            f.write(book_key)
            f.write("\r\n")
            f.write(book_dict[book_key])
            f.write("\r\n")
        # 关闭文件
        f.close()


# 获取网页
if __name__ == '__main__':
    # 隐式等待,防止程序过快而网页反应不过来(10s)
    driver.implicitly_wait(10)

    main_url = 'https://www.51shucheng.net/guanchang/zuzhibuzhang'

    # 打开网页
    open_url(main_url)
    # 定义一个字典， 存放每章的名字和内容
    book_dict = dict()

    # 获取小说名字
    title = find_title()
    # 获取每章的名字和url
    chapter_name_and_url = find_chapter_name_and_url()

    # 循环获取每章的内容并保存
    for key in chapter_name_and_url:
        chapter_url = chapter_name_and_url[key]
        chapter_value = get_chapter_value_by_url(chapter_url)
        book_dict[key] = chapter_value

    file_path = os.getcwd()
    # 写出到文本
    write_book(file_path, title, book_dict)

    # 关闭浏览器
    driver.quit()
