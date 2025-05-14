import os
import json
from playwright.sync_api import sync_playwright

# Playwright 配置
PLAYWRIGHT_ARGS = [
    '--no-sandbox',
    '--disable-gpu',
    '--ignore-certificate-errors'
]


def open_url(page, url: str):
    page.goto(url, wait_until="domcontentloaded")


def find_title(page) -> str:
    return page.locator('.catalog h1').inner_text()


def find_chapter_name_and_url(page) -> dict:
    xpath_options = [
        "//div[@class='mulu-list']",
        "//div[@class='mulu-list quanji']",
        "//div[@class='mulu-list-2 quanji']"
    ]
    for xp in xpath_options:
        items = page.locator(f"{xp}//li")
        if items.count() > 0:
            result = {}
            for i in range(items.count()):
                el = items.nth(i).locator('a')
                title = el.get_attribute('title')
                href = el.get_attribute('href')
                result[title] = href
                print(title, href)
            return result
    return {}


def get_chapter_value_by_url(page, url: str) -> str:
    open_url(page, url)
    return page.locator('.neirong').inner_text()


def write_book(directory: str, book_name: str, book_dict: dict):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"{book_name}.txt")
    with open(file_path, 'w', encoding='utf-8') as f:
        for chapter, content in book_dict.items():
            f.write(chapter + "\n")
            f.write(content + "\n\n")
    print(f"Saved: {file_path}")


def main():
    main_url = 'https://www.51shucheng.net/guanchang/zuzhibuzhang'
    out_dir = os.getcwd()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=PLAYWRIGHT_ARGS)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()

        # 打开主页面
        open_url(page, main_url)

        # 获取小说标题
        title = find_title(page)
        print("Book title:", title)

        # 获取章节列表
        chapters = find_chapter_name_and_url(page)

        # 遍历下载每一章
        book_dict = {}
        for chap_name, chap_url in chapters.items():
            content = get_chapter_value_by_url(page, chap_url)
            book_dict[chap_name] = content

        # 写入文件
        write_book(out_dir, title, book_dict)

        browser.close()


if __name__ == '__main__':
    main()
