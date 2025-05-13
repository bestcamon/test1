import playwright
from playwright.sync_api import Playwright

from playwright.sync_api import sync_playwright

def run(playwright):
    # 启动浏览器
    browser = playwright.chromium.launch(headless=False)  # 如果不需要图形界面，请将 headless 设置为 True
    context = browser.new_context()

    # 打开新页面
    page = context.new_page()
    page.goto("https://www.baidu.com/")

    # 在搜索框中输入文本
    page.fill('input[name="wd"]', '漂亮小姐姐')  # 注意百度首页的搜索框 name 属性是 "wd"

    # 模拟按下回车键提交搜索
    page.press('input[name="wd"]', 'Enter')

    # 等待搜索结果加载完成
    page.wait_for_selector('.result')  # 假设 '.result' 是搜索结果的一个通用选择器

    # 抓取搜索结果的标题
    results = page.query_selector_all('.result')
    for item in results:
        title = item.query_selector('h3').text_content()
        print(title)

    # 关闭浏览器
    context.close()
    browser.close()

# 使用同步API运行Playwright
with sync_playwright() as playwright:
    run(playwright)