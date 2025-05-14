import os
from playwright.sync_api import sync_playwright

# 获取当前文件的文件夹
out_dir = os.getcwd()
# Playwright 配置
PLAYWRIGHT_ARGS = [
    "--no-sandbox",  # 禁用沙箱（适用于 Docker 或 CI 环境）
    "--disable-gpu",  # 禁用 GPU 加速
    "--ignore-certificate-errors",  # 忽略 SSL 证书错误
    "--user-agent=MyBot/1.0",  # 自定义 User-Agent
    "--lang=zh-CN",  # 设置语言/地区
    "--timezone=Asia/Shanghai"  # 设置时区
]


def open_url(page, url: str):
    page.goto(url, wait_until="domcontentloaded")


def main():
    base_url = 'https://www.ps3838.com/zh-cn/sports/soccer'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=PLAYWRIGHT_ARGS)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        # 打开主页面
        open_url(page, base_url)
        # 打开体育页面  //*[@id='oddspage']/div[2]/div[1]/div[2]/div
        container_div = page.locator("//*[@id='oddspage']/div[2]/div[1]/div[2]/div")
        container_div.wait_for(state="visible", timeout=10000)  # 等待元素可见
        # 查找div_obj下的，所有divd class是league，获取其中的span内容

        # 查找所有 class="league" 的子元素
        league_divs = container_div.locator("div.league")

        print(league_divs.count())
        # 遍历并提取每个 league div 中的 span 内容
        for i in range(league_divs.count()):
            league_div = league_divs.nth(i)
            # 获取 league_div 的所有直接子元素
            child_elements = league_div.locator("> *")

            # 遍历所有子元素
            title(i, child_elements.nth(3))
        # 获取标签名（如 "SPAN", "DIV" 等）

        browser.close()


def title(i, child):
    print(f"子元素 {i + 1} (span): {child.text_content()}")


if __name__ == '__main__':
    main()
