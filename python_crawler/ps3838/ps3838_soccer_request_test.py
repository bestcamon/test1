import requests
import json
import time


def get_compact_events(sp=29, max_retry=3):
    """
    获取 PS3838 紧凑赛事列表（compact events）
    sp: 体育项目 ID，29 表示足球
    """
    # 动态 timestamp 防止缓存
    timestamp = int(time.time() * 1000)
    url = (
        "https://www.ps3838.com/sports-service/sv/compact/events"
        f"?btg=1&c=&cl=3&d=&ec=&ev=&g=&hle=false&ic=false"
        f"&ice=false&inl=false&l=3&lang=&lg=&lv=&me=0&mk=1"
        f"&more=false&o=1&ot=1&pa=0"
        f"&pimo=0,1,8,39,2,3,6,7,4,5&pn=-1&pv=1&sp={sp}&tm=0&v=0"
        f"&locale=zh_CN&_={timestamp}&withCredentials=true"
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/136.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,eo;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://www.ps3838.com/zh-cn/sports/soccer",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Sec-Ch-Ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "X-App-Data": (
            "dW5=kcNYvyFkAgkJ;"
            "pctag=f0874e8d-7797-4eef-941e-112e26d61dc7;"
            "directusToken=tKl5CpR1Zc7GoCHbKmW8eRixdIsGLZG7"
        )
    }
    cookies = {
        "_sig": "Dcy1NbUkxTURka1lXUmpNakV5TXpOaFpBOkpod08zMGtoZ2E1VUpPRndTZ3dnNldKQ3I6LTE3MzY0MDU0MDA6NzQ1NTA1MjQxOjIuMTAuMDo5Q0NFQTlvSVhE",
        "_apt": "9CCEA9oIXD",
        "pctag": "f0874e8d-7797-4eef-941e-112e26d61dc7",
        "dW5": "kcNYvyFkAgkJ",
        "40f11e4504d1cb907f41211f225c2bd6": "ceqmag21fujtic5tom6ssdv6g6",
        "skin": "ps3838",
        "lang": "en_US",
    }

    for attempt in range(1, max_retry + 1):
        try:
            with requests.Session() as sess:
                sess.get("https://www.ps3838.com/zh-cn/sports/soccer", headers=headers, cookies=cookies)
                resp = sess.get(url, headers=headers, cookies=cookies, timeout=10)
                if resp.status_code == 200:
                    return resp.json()
                elif resp.status_code == 429:
                    print(f"[Attempt {attempt}] 速率限制，等待重试...")
                    time.sleep(30)
                else:
                    print(f"[Attempt {attempt}] 请求失败: {resp.status_code}")
                    return None
        except requests.RequestException as e:
            print(f"[Attempt {attempt}] 异常: {e}")
            time.sleep(5)
    return None


if __name__ == "__main__":
    # 获取赛事数据
    events_data = get_compact_events(sp=29)
    if events_data:
        # 保存到 JSON 文件
        output_file = "compact_events.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(events_data, f, ensure_ascii=False, indent=2)
        print(f"已将数据保存到 {output_file}")
    else:
        print("未能获取到赛事数据")
