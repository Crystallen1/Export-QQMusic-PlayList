# exportQQMusic

## 简介
有点笨的QQ音乐歌单转网易云音乐歌单，就是通过解析HTML来获取歌单。QQ音乐的开发者工具似乎关闭了注册入口，所以可能只能用这种笨方法了。

## 步骤
### 0. 安装python环境（如果没有）

### 1. 克隆仓库
``` 
git clone https://github.com/Crystallen1/exportQQMusic.git
```
### 2. 打卡QQ音乐网页版，并进入想转移的歌单界面
![image](https://github.com/user-attachments/assets/6933021f-0986-4206-93ae-7e48192013de)
![image](https://github.com/user-attachments/assets/ffdc32fd-d990-4beb-b3c2-6026445f6077)


### 3. 获取歌单信息

#### 方法1

在键盘输入 ctrl+s(windows)/command+s(mac),保存网站的html，命名为data.html

<img width="410" alt="image" src="https://github.com/user-attachments/assets/d66257be-5103-4b52-86e1-cc2cc912ad7c" />

#### 方法2

打开浏览器的开发者工具（F12等），点击Network中的第一个名字是一串数字的（你的歌单的id），复制其中的Response，保存为一个data.html文件

![image](https://github.com/user-attachments/assets/0c6098d8-df21-44fd-9112-e4b50ac2f628)


将获取到的html文件放在第一步中得到的文件夹中


### 4.运行python脚本

```python
python export.py
```

就可以在控制台中得到歌单信息（歌曲+歌手），复制信息

### 5.将复制到的信息粘贴到网易云歌单的文字导入中
![image](https://github.com/user-attachments/assets/2e699a0f-f064-4875-90b8-ba4abb0c2ebf)

