import re
import json
import requests

# 读取 HTML 文件
url = input("请输入要获取 HTML 的 URL: ")
    # 使用 GET 方法获取 HTML 内容
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url,headers=headers)
response.raise_for_status()  # 检查请求是否成功
print(response)
html_content = response.text

# 匹配包含 JSON 的部分
pattern = r'var firstPageData = \s*({[\s\S]*?"taogeData":\s*{[\s\S]*?}}});'
match = re.search(pattern, html_content)

if match:
    json_text = match.group(0)  # 提取 JSON 文本
    json_text2 = json_text.strip().lstrip('var firstPageData = ').rstrip(';')
    # 预处理 JSON 文本
    # json_text = json_text.replace("undefined", "null")  # 替换 undefined 为 null
    # json_text = json_text.replace(r"\\u002F", "/")  # 替换转义的斜杠为标准斜杠

    try:
        # 加载 JSON 数据
        data = json.loads(json_text2)
        # 从 JSON 数据中提取 songList
        data_2 = data.get("taogeData")
        song_list = data_2.get('songlist', [])

        # 解析所需的数据并格式化输出
        for index,song in enumerate(song_list, start=1):
            song_name = song.get('name', 'Unknown')
            singers = song.get('singer', [])
            singer_names = ' / '.join([singer.get('name', 'Unknown') for singer in singers])
            print(f"{index}. {song_name}    {singer_names}")
    except json.JSONDecodeError as e:
        print(f"JSON 解码错误: {e}")
        print("预处理后的 JSON 文本：")
        print(json_text)  # 打印错误字符
else:
    print("未找到 JSON 数据，请检查正则表达式是否正确。")