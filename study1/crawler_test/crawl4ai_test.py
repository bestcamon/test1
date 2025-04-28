import json
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.baidu.com")
        print(result.markdown)


# async def fetch_stock_data():
#     url = "https://finance.yahoo.com/quote/AAPL"
#     async with AsyncWebCrawler(verbose=True) as crawler:
#         result = await crawler.arun(url=url, css_selector="div#quote-header-info")
#         print(result.markdown)
#
# def save_to_json(data, filename="stock_data.json"):
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)
#
# stock_data = {"symbol": "AAPL", "price": 150.75, "change": "+1.25"}
# save_to_json(stock_data)

if __name__ == "__main__":
    asyncio.run(fetch_stock_data())
if __name__ == "__main__":
    asyncio.run(main())
