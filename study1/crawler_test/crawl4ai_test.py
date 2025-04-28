from crawl4ai import AsyncWebCrawler
import asyncio
from crawl4ai import WebCrawler
from crawl4ai.extractor import *
import json

# 百度爬取
async def baidu():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.baidu.com")
        print(result.markdown)


# 股票数据爬取
async def fetch_stock_data():
    url = "https://finance.yahoo.com/quote/AAPL"
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url, xpath="//*[@id='nimbus-app']/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span")
        print(result.markdown)




async def scrape_aapl_stock():
    url = "https://finance.yahoo.com/quote/AAPL"

    # 初始化带缓存的爬虫（避免重复请求）
    crawler = WebCrawler(
        enable_caching=True,
        cache_expiry=3600  # 1小时缓存
    )

    # 使用混合模式加载页面（静态+动态）
    result = await crawler.run(
        url=url,
        extractor=CombinedExtractor(
            extractors=[
                # 1. 使用CSS选择器提取关键数据
                CSSExtractor(
                    selectors={
                        "current_price": 'fin-streamer[data-test="qsp-price"]',
                        "change": 'fin-streamer[data-test="qsp-price-change"] > span:nth-child(1)',
                        "change_percent": 'fin-streamer[data-test="qsp-price-change-percent"] > span:nth-child(1)',
                        "previous_close": 'td[data-test="PREV_CLOSE-value"]',
                        "open": 'td[data-test="OPEN-value"]',
                        "volume": 'td[data-test="TD_VOLUME-value"]',
                        "market_cap": 'td[data-test="MARKET_CAP-value"]'
                    }
                ),
                # 2. 使用正则表达式提取JSON中的深度数据
                RegexExtractor(
                    pattern=r'"APP\.context":\s*({.*?})\s*;\s*\n',
                    group=1,
                    output_type="json"
                )
            ]
        ),
        # 使用无头浏览器渲染
        use_browser=True,
        # 设置浏览器参数
        browser_args={
            "headless": True,
            "viewport": {"width": 1280, "height": 800},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    )

    # 处理提取结果
    structured_data = {}

    # 合并CSS提取结果
    if result.css_data:
        structured_data.update({
            "current_price": result.css_data.get("current_price", {}).get("text"),
            "change": result.css_data.get("change", {}).get("text"),
            "change_percent": result.css_data.get("change_percent", {}).get("text"),
            "previous_close": result.css_data.get("previous_close", {}).get("text"),
            "open": result.css_data.get("open", {}).get("text"),
            "volume": result.css_data.get("volume", {}).get("text"),
            "market_cap": result.css_data.get("market_cap", {}).get("text")
        })

    # 处理正则提取的JSON数据
    if result.regex_data:
        json_data = json.loads(result.regex_data[0])
        quote_data = json_data.get("dispatcher").get("stores").get("QuoteSummaryStore")

        # 提取关键指标
        structured_data.update({
            "pe_ratio": quote_data.get("summaryDetail").get("trailingPE").get("raw"),
            "eps": quote_data.get("defaultKeyStatistics").get("trailingEps").get("raw"),
            "dividend_yield": quote_data.get("summaryDetail").get("dividendYield").get("raw"),
            "beta": quote_data.get("defaultKeyStatistics").get("beta").get("raw"),
            "52_week_range": f"{quote_data.get('summaryDetail').get('fiftyTwoWeekLow').get('raw')} - {quote_data.get('summaryDetail').get('fiftyTwoWeekHigh').get('raw')}"
        })

    return structured_data


# 执行异步函数
if __name__ == "__main__":
    data = asyncio.run(scrape_aapl_stock())
    print(json.dumps(data, indent=2))

