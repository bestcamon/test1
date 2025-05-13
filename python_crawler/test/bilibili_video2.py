import re
import subprocess  # 用于执行FFmpeg命令
import time

import requests
from tqdm import tqdm

ffmpeg_path = r'E:\tools\FFmpeg\bin'
HEADERS = {
    "Cookie": "buvid3=2DD49D62-AEB5-3F6B-2FCD-7BEA4FD38A9C50262infoc; b_nut=1705813350; _uuid=9285CD66-3E85-1010E7-45A9-B7BA831CC810F51717infoc; buvid4=A4712DF2-AFD3-83F2-E246-EC1FFDC0495D50717-024012105-Z8mq4OUSKequZeMKPr6m5g%3D%3D; buvid_fp=6e4f72b9547414ce4cd6eb06b7991ef6; DedeUserID=472989906; DedeUserID__ckMd5=be7588f12a173e3e; rpdid=|(YuRl~)kR|0J'u~|l)uJJ)R; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDY4Mzk3NDcsImlhdCI6MTcwNjU4MDQ4NywicGx0IjotMX0.7CFmOwpj_xN6qZLOBdLfTe-HSXA7a72AiyQr3_4A8N8; bili_ticket_expires=1706839687; SESSDATA=f87f5c89%2C1722132549%2Cc84db%2A11CjDhRAbv3bvKuRn8vh15N7581zO30bJ4tAwcVmv9qXJ77Lw9vfBLXW0SaLuc6fcVCyoSVmNFQWJFY3FVT1RVcDU0V25NSWVuS1I2Mm5QaWZwQldtX21ENUVXSnk1a05ISmgwdTNBWUFBel9WYjFSMXJIa3RNcUZVV25WakxwLTZMWjk4b2liTDRBIIEC; bili_jct=895eef74844efe9bc38a4682575f1235; sid=8rkekw66; CURRENT_FNVAL=16; enable_web_push=DISABLE; header_theme_version=CLOSE; home_feed_column=4; browser_resolution=777-879; PVID=9; b_lsid=4CD525F5_18D58732163",
    'Referer': 'https://www.bilibili.com/video/BV1xQ4y1c7Qj/?spm_id_from=333.1007.tianma.2-1-3.click&vd_source=3aba1ea1013958c3f37c6e933f7f3875',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

}


def get_response(url):
    resp = requests.get(url=url, headers=HEADERS, stream=True, proxies=None)
    return resp


def get_video_info(html_url):
    html_data = get_response(html_url)
    aid = re.findall(f'"aid":(.*?),"', html_data.text)[0]
    bvid = re.findall(f'"bvid":"(.*?)",', html_data.text)[0]
    cid = re.findall(f'"cid":(.*?),"', html_data.text)[0]
    w_rid = re.findall(f'"session":"(.*?)"', html_data.text)[0]
    title = re.findall(f'"title":"(.*?)"', html_data.text.replace("|", " "))[0]
    qn = re.findall(f'"accept_quality":(.*?)', html_data.text)[0]
    video_info = [aid, bvid, cid, w_rid, title, qn]
    return video_info


def get_video_content(video_info):
    api_url = 'https://api.bilibili.com/x/player/playurl'
    params = {
        'avid': video_info[0],
        'bvid': video_info[1],
        'cid': video_info[2],
        'qn': video_info[5],
        'type': '',
        'otype': 'json',
        'fourk': '1',
        'fnver': '0',
        'fnval': '16',
        'platform': 'pc',
        'down': '0',
        'cross_domain': 'true',
        'ss': '1',
        'nobase64': '1',
        'sign': '66f1d42fc44a7b3b8f554f74fda14e10',
    }
    json_data = requests.get(url=api_url, params=params, headers=HEADERS).json()

    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']

    video_content = [audio_url, video_url]
    return video_content


def download_file(url, filename, description):
    with tqdm(total=get_file_size(url), unit='B', unit_scale=True, desc=description) as pbar:
        with open(filename, mode="wb") as file:
            response = get_response(url)
            for chunk in response.iter_content(chunk_size=2048):
                file.write(chunk)
                pbar.update(len(chunk))


def get_file_size(url):
    response = get_response(url)
    size = int(response.headers.get('Content-Length', 0))
    return size


def merge_audio_video(video_path, audio_path, output_path):
    # 使用FFmpeg合并音频和视频
    ffmpeg_cmd = f'ffmpeg --enable-decoder=h264 -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac -strict experimental "{output_path} 2> log.txt"'
    subprocess.run(ffmpeg_cmd, shell=True)
    # os.remove(video_path)
    # os.remove(audio_path)


if __name__ == '__main__':
    # 完成于2024年1月31日00:26:38
    # html_url = input("请输入B站视频的链接地址:")
    html_url = "https://www.bilibili.com/video/BV1ZH4y1A7Xb/?spm_id_from=333.934.0.0"
    video_info = get_video_info(html_url)
    video_content = get_video_content(video_info)
    start_time = time.time()

    audio_filename = f"{video_info[1]}.mp3"
    video_filename = f"{video_info[1]}.mp4"

    download_file(video_content[0], audio_filename, f"{video_info[1]} - 音频")
    download_file(video_content[1], video_filename, f"{video_info[1]} - 视频")

    output_filename = f"{video_info[1]}_merged.mp4"
    merge_audio_video(video_filename, audio_filename, output_filename)

    end_time = time.time()

    elapsed_time = end_time - start_time

    audio_size_mb = get_file_size(video_content[0]) / (1024 * 1024)
    video_size_mb = get_file_size(video_content[1]) / (1024 * 1024)

    print("\n下载完成！")
    print(f"每个文件的大小：音频 - {round(audio_size_mb, 2)} MB, 视频 - {round(video_size_mb, 2)} MB")
    print(f"文件的名称：{video_info[4]}")
    print(f"下载和合成所有文件耗时：{round(elapsed_time, 2)} 秒")
