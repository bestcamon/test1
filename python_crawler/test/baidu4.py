from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

MMC_BATCH_ADDRESS = "https://www.baidu.com/"
#https://googlechromelabs.github.io/chrome-for-testing/#stable
#创建webDriver对象，指明使用chrome浏览器驱动
chrome_driver_path = 'E:\\Tools\\chrome-win64\\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)
wd = webdriver.Chrome(service=service)

#关闭页面退出
#wd.close()

def execute():
    wd.find_element(By.ID, 'execute_button').click()

if __name__ == '__main__':
    # 隐式等待,防止程序过快而网页反应不过来(10s)
    wd.implicitly_wait(10)

    # 调用webDriver 对象的get方法，可以让浏览器打开指定网址
    wd.get(MMC_BATCH_ADDRESS)

    wd.find_element(By.ID, 'kw').send_keys('hello')
    # 根据id选择元素，返回的就是该元素对应的WebElement对象
    element = wd.find_element(By.ID, 'su')

    element.click()


    # 通过该WebElement对象，就可以对页面元素进行操作
    # 比如输入字符串到这个输入框里
    wd.find_element(By.ID, 'i1Yy').send_keys('23')
    wd.find_element(By.ID, 'i1Mm').send_keys('03')
    wd.find_element(By.ID, 'i1Dd').send_keys('23')
    wd.find_element(By.ID, 'i1Nisu').send_keys('9')
    execute()





