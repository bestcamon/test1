import asyncio
from crawl4ai import AsyncWebCrawler

async def fetch_url_content(url):
    """
    使用 AsyncWebCrawler 抓取指定 URL 的内容。
    """
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url)
        return result.markdown
# NY301S1040
# aa198222
async def main():
    # 要抓取的 URL 列表
    urls = [
        "https://www.ps3838.com/zh-cn/spor34"
        "2190-=ts/soccer",
    ]

    # 并发抓取多个 URL  install
    tasks = [fetch_url_content(url) for url in urls]
    results = await asyncio.gather(*tasks)

    # 打印抓取结果
    for i, content in enumerate(results):
        print(f"--- 内容来自 URL {i + 1} ---")
        print(content)
        print("\n")

if __name__ == "__main__":
    asyncio.run(main())