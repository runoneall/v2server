# V2ray Server Maintenance
## 注意：此仓库不维护clash！
收集并整理互联网上的免费节点
持续更新......


# 文件说明
1. `latest.txt` 最新订阅文件
2. `latest_base64.txt` 最新订阅文件, 经过base64编码
3. `old*.txt` 历史版本订阅文件
4. `old*_base64.txt` 历史版本订阅文件, 经过base64编码
5. `subs.txt` 使用的订阅源
6. `all_server.txt` 整合的订阅文件, 用于制作可用订阅
7. `one.txt` 零散节点

因所有人的网络环境不同, 我不能考虑到所有人的环境, 所以提供 `all_server.txt` 文件, 请自行测速使用

从2024.8.17开始, 不再提供 `latest.txt` 和 `latest_base64.txt` 文件

授人以鱼不如授人以渔, 我决定将订阅工具开源, 使用 `python3` 和 `requests` 完成. 将 `subs.txt` 放入项目目录并运行 `tool.py` 以启动, 产出文件在 `resource` 文件夹内