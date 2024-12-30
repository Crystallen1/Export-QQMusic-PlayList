import re
import json

# 读取 HTML 文件
with open("data.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# 匹配包含 JSON 的部分
pattern = r"window\.__INITIAL_DATA__\s*=\s*({[\s\S]*})"
match = re.search(pattern, html_content)

if match:
    json_text = match.group(1)  # 提取 JSON 文本

    # 预处理 JSON 文本
    json_text = json_text.replace("undefined", "null")  # 替换 undefined 为 null
    json_text = json_text.replace(r"\\u002F", "/")  # 替换转义的斜杠为标准斜杠

    try:
        # 加载 JSON 数据
        data = json.loads(json_text)
        # 从 JSON 数据中提取 songList
        song_list = data.get('songList', [])

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