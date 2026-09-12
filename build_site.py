# -*- coding: utf-8 -*-
"""金银全景图 · GitHub Actions 构建脚本
从 kimi.link 拉取的 base.html（自包含单文件，含内嵌 echarts + 旧数据），
把其中的数据块替换为本次计算出的 data/dashboard.js，生成新的自包含 index.html。
"""
import sys

base = open("base.html", encoding="utf-8").read()
dj = open("data/dashboard.js", encoding="utf-8").read().replace("</script", "<\\/script")

i = base.find("window.DASHBOARD_DATA=")
if i < 0:
    sys.exit("base.html 中未找到 window.DASHBOARD_DATA 数据块，终止")
s = base.rindex("<script>", 0, i)
e = base.index("</script>", i)
out = base[:s] + "<script>\n" + dj + "\n" + base[e:]

open("index.html", "w", encoding="utf-8").write(out)
print("index.html written,", len(out), "bytes")
