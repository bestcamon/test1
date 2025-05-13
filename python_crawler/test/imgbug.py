from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 使用Selenium打开网页

# 创建webDriver对象，指明使用chrome浏览器驱动
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 设置为无头
options.add_argument('--disable-gpu')  # 设置没有使用gpu
options.add_argument("--ignore-certificate-errors")  # 可选，忽略证书错误
options.add_argument("--no-sandbox")  # 可选，禁用沙盒模式
options.add_argument("--disable-dev-shadow")

# 1.创建浏览器对象
driver = webdriver.Chrome(options=options)
main_url = "https://www.hippopx.com/zh/"
main_path = "image"
num = 5


def image_bug(searchfor, page):
    driver.get(main_url + "/search?q=" + str(searchfor) + "&page=" + str(page))

    # 等待页面加载
    wait = WebDriverWait(driver, 10)
    parent_element = driver.find_element(By.XPATH, "//*[@id='mainlist']")
    child_elements = parent_element.find_elements(By.XPATH, "./*")  # 使用"./*"来查找所有子节点
    if not child_elements:
        print("未找到该类型图片")
        return
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[itemprop="associatedMedia"]')))

    # 执行JavaScript代码，将页面滚动到底部，确保所有图片加载出来
    script = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(script)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[itemprop="associatedMedia"]')))

    # 找到所有目标li元素
    target_li_elements = driver.find_elements(By.CSS_SELECTOR, 'li[itemprop="associatedMedia"]')

    # 遍历所有目标li元素，找到其中的img元素并下载保存到本地
    for index, li in enumerate(target_li_elements, start=1):
        img = li.find_element(By.TAG_NAME, 'img')
        img_src = img.get_attribute('title')

        # 下载图片
        img_data = img.screenshot_as_png

        # 保存图片到本地
        with open(main_path + f'\\{img_src}.png', 'wb') as f:
            f.write(img_data)
        if index == num:
            break
    # 关闭浏览器
    driver.quit()


def create_directory(directory, new_directory_name=""):
    # 如果你想避免已存在目录引发异常，可以使用 os.path.exists() 来检查目录是否存在
    path = os.path.join(directory, new_directory_name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


if __name__ == '__main__':
    create_directory(main_path)
    index = 1
    # name = input("请输入需要的图片名(类型，如dog,cat)")
    # num = input("请输入需要的图片数")
    name = "日本美女"
    image_bug(name, index)
