from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

MMC_BATCH_ADDRESS = "https://www.baidu.com/"
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 设置为无头
options.add_argument('--disable-gpu')  # 设置没有使用gpu
options.add_argument("--ignore-certificate-errors")  # 可选，忽略证书错误
options.add_argument("--no-sandbox")  # 可选，禁用沙盒模式
# 创建webDriver对象，指明使用chrome浏览器驱动
chrome_driver_path = 'E:\\Tools\\chrome-win64\\chromedriver.exe'
Service = Service(chrome_driver_path)
wd = webdriver.Chrome(service=Service, options=options)


# 关闭页面退出
# wd.close()

def execute():
    wd.find_element(By.ID, 'execute_button').click()


if __name__ == '__main__':
    # 隐式等待,防止程序过快而网页反应不过来(10s)
    wd.implicitly_wait(1)

    # 调用webDriver 对象的get方法，可以让浏览器打开指定网址
    wd.get(MMC_BATCH_ADDRESS)

    wd.find_element(By.ID, 'kw').send_keys('hello')
    # 根据id选择元素，返回的就是该元素对应的WebElement对象
    element = wd.find_element(By.ID, 'su')
    element.click()

    wd.close()
