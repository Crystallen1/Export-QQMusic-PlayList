# Export QQMusic PlayList

## 简介

导出QQ音乐的歌单为文本格式，可以用于迁移到其他各种音乐软件，如使用：
https://www.tunemymusic.com/zh-CN/features/transfer

tips: 看了几个别人的开源项目都是使用了QQ音乐的开发者工具提供的api查询，但是QQ音乐的开发者工具似乎关闭了注册入口，只有一个登录入口了。
而不使用api的话只能拿到歌单的前30条数据

## 步骤
### 0. 安装python环境（如果没有）

### 1. 克隆仓库
``` 
https://github.com/Crystallen1/Export-QQMusic-PlayList.git
```
### 2. 将QQ音乐歌单分享到任意地方（如微信）并复制链接
![image](https://github.com/user-attachments/assets/93e23532-26ec-435d-9e31-86af5dec18f8)
![image](https://github.com/user-attachments/assets/542a8809-5329-422e-a18c-75daef882164)

### 3.运行python脚本

```python
python export.py
```
再根据提示信息将复制到链接输入
<img width="234" alt="image" src="https://github.com/user-attachments/assets/42235b65-b275-488f-b990-33a6f53cc9eb" />

就可以在控制台中得到歌单信息（歌曲+歌手），复制信息

