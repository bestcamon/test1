import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# https://googlechromelabs.github.io/chrome-for-testing/#stable

# 创建webDriver对象，指明使用chrome浏览器驱动
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 设置为无头
options.add_argument('--disable-gpu')  # 设置没有使用gpu
options.add_argument("--ignore-certificate-errors")  # 可选，忽略证书错误
options.add_argument("--no-sandbox")  # 可选，禁用沙盒模式
options.add_argument("--disable-dev-shadow")

# 1.创建浏览器对象
chrome_driver_path = 'E:\\tools\\chrome_test_123.0.6312.122\\chromedriver.exe'
driver = webdriver.Chrome(options=options)


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
            # print(chapter_name, chapter_url)
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


def write_json(file_path, chapter_name, json_str):
    # 如果目录不存在，则创建目录；如果存在则删除重建一个
    path = os.path.join(f"{file_path}")
    file = os.path.join(path, f"{chapter_name}")
    print(file)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(json_str)
        # 关闭文件
        f.close()


# 主要逻辑
def spacer_book(url, title, file_directory_path):
    # 打开网页
    open_url(url)
    # 定义一个字典， 存放每章的名字和内容
    book_dict = dict()

    # 获取小说名字
    # title = find_title()
    # 获取每章的名字和url
    chapter_name_and_url = find_chapter_name_and_url()

    # 循环获取每章的内容并保存
    for key in chapter_name_and_url:
        chapter_url = chapter_name_and_url[key]
        chapter_value = get_chapter_value_by_url(chapter_url)
        book_dict[key] = chapter_value

    # 写出到文本
    write_book(file_directory_path, title, book_dict)


def create_directory(directory, new_directory_name):
    # 如果你想避免已存在目录引发异常，可以使用 os.path.exists() 来检查目录是否存在
    path = os.path.join(directory, new_directory_name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


# 获取目录分类
def get_dir_name_and_url():
    table_of_contents_dict = dict()
    chapter_list = driver.find_elements(By.XPATH, "//div[@class='cat-list']")
    for chapter_item in chapter_list:
        tar_name = chapter_item.find_element(By.TAG_NAME, 'h2').text
        table_of_contents_dict[tar_name] = dict()
        table_element = chapter_item.find_elements(By.TAG_NAME, "li")
        for item in table_element:
            chapter_name = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('title')
            h3_chapter_url = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            table_of_contents_dict[tar_name][chapter_name] = h3_chapter_url
    return table_of_contents_dict


# 获取book链接
def get_book_name_and_url(table_of_contents_dict):
    chapter_dict = dict()
    for tar_name_item in table_of_contents_dict:
        h2_path = create_directory(mian_path, tar_name_item)
        for chapter_name_item in table_of_contents_dict[tar_name_item]:
            h3_path = create_directory(h2_path, chapter_name_item)
            h3_chapter_url_item = table_of_contents_dict[tar_name_item][chapter_name_item]
            open_url(h3_chapter_url_item)
            h4_book_list = driver.find_elements(By.XPATH, "//div[@class='mulu-list']/ul/li")

            if (len(h4_book_list) == 1 and h4_book_list[0].text == "没有分类") or (len(h4_book_list) == 0):
                continue
            for h4_book_item in h4_book_list:
                book_name = h4_book_item.find_element(By.CSS_SELECTOR, 'a').text
                book_url = h4_book_item.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
                chapter_dict[book_name] = [book_url, h3_path]
                print(tar_name_item, chapter_name_item, book_name, book_url)
    return chapter_dict


def read_json(mian_path, json_file_name):
    path = os.path.join(mian_path, json_file_name)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


# 获取网页
if __name__ == '__main__':
    # 隐式等待,防止程序过快而网页反应不过来(10s)
    driver.implicitly_wait(10)
    # 主目录
    mian_path = os.path.dirname(os.path.abspath(__file__))

    create_directory(mian_path, "")
    # 下载无忧书城所有分类下的小说
    main_url = 'https://www.51shucheng.net/fenlei'
    # chapter_dict_json = read_json(mian_path, "chapter_dict.json")
    chapter_dict_json = {}
    chapter_dict = dict() if len(chapter_dict_json) == 0 else chapter_dict_json
    if not chapter_dict_json:
        open_url(main_url)
        # 获取目录分类
        table_of_contents_dict = get_dir_name_and_url()
        # 获取book链接
        chapter_dict = get_book_name_and_url(table_of_contents_dict)
        # json写出备份
        write_json(mian_path, "chapter_dict.json", json.dumps(chapter_dict))

    breakpoint_download_chapter_dict_json = read_json(mian_path, "breakpoint_download_chapter_dict.json")
    # 断点下载
    breakpoint_download_chapter_dict = dict() if len(
        breakpoint_download_chapter_dict_json) == 0 else breakpoint_download_chapter_dict_json

    # 循环下载book数据
    try:
        for book_name in chapter_dict:
            if breakpoint_download_chapter_dict.get(book_name) is None:
                breakpoint_download_chapter_dict[book_name] = chapter_dict.get(book_name)
            else:
                print(book_name, "已下载")
                continue

            print(book_name, chapter_dict[book_name])
            spacer_book(chapter_dict[book_name][0], book_name, chapter_dict[book_name][1])
            write_json(mian_path, "breakpoint_download_chapter_dict.json", json.dumps(breakpoint_download_chapter_dict))
    except Exception as e:
        print(e)
        last_key, last_value = breakpoint_download_chapter_dict.popitem()
        breakpoint_download_chapter_dict.pop(last_key)
        write_json(mian_path, "breakpoint_download_chapter_dict.json", json.dumps(breakpoint_download_chapter_dict))
    finally:
        breakpoint_download_chapter_dict_file = os.path.join(mian_path, f"{breakpoint_download_chapter_dict.json}")
        if os.path.exists(breakpoint_download_chapter_dict_file):
            # 删除文件
            os.remove(breakpoint_download_chapter_dict_file)
    # 关闭浏览器
    driver.quit()
