from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME
capabilities['pageLoadTimeout'] = None  # 禁用隐式页面加载超时
capabilities['implicit_timeout'] = None  # 禁用隐式元素等待超时



if __name__ == '__main__':
    # 设置 Chrome WebDriver 的路径
    chrome_driver_path = 'C:\\Program Files\\Tools\\chrome-win64\\chromedriver.exe'

    # 创建 Chrome WebDriver 对象
    wd = webdriver.Chrome(executable_path=chrome_driver_path, desired_capabilities=capabilities)
    # wd = webdriver.Chrome(executable_path=chrome_driver_path)

    # 打开百度首页
    wd.get("https://www.baidu.com/")

    # 获取百度首页标题
    title = wd.title
    print("百度首页标题：", title)

    # 关闭浏览器
    wd.quit()

