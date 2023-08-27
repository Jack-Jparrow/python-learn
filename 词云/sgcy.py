# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:16:26 2019

@author: Administrator
"""

# GovRptWordCloudV3B
import jieba
import wordcloud
import imageio
import os

# 读取txt文件，获取需要统计词汇的文本
f = open("三国演义.txt", "r", encoding="utf-8")
t = f.read()
f.close()

# 设置图像遮罩
mask = imageio.imread("guanyu.jpg")

# 请在下列exludes集合中，自行补充其他需要排除的词汇
excludes = {"将军", "却说", "二人", "不可", "荆州", "不能", "如此", "商议", "如何", "主公", "军士", "左右","军马", "引兵", "次日", "大喜", "天下", "东吴", "于是", "今日", "不敢", "魏兵", "陛下", "一人","人马", "不知", "汉中", "只见", "众将", "蜀兵", "上马", "大叫", "太守", "此人", "夫人", "先主",
   "后人", "背后", "城中", "天子", "一面", "何不", "大军", "忽报", "先生", "百姓", "何故", "然后",
    "先锋", "不如", "赶来", "原来", "令人", "江东", "下马", "喊声", "正是", "徐州", "忽然", "因此",
    "成都", "不见", "未知", "大败", "大事", "之后", "一军", "引军", "起兵", "军中", "接应", "进兵",
    "大惊", "可以", "以为", "大怒", "不得", "心中"
}

words = jieba.lcut(t)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "孔明曰" or word == "诸葛亮":
        rword = "孔明"
    elif word == "丞相" or word == "孟德":
        rword = "曹操"
    elif word == "都督" or word == "公瑾":
        rword = "周瑜"
    elif word == "翼德" or word == "三将军":
        rword = "张飞"
    elif word == "刘禅":
        rword = "后主"
    elif word == "奉先":
        rword = "吕布"
    elif word == "仲达":
        rword = "司马懿"        
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
    
# 实现删除干扰词汇功能（此处约2行代码）    
for word in excludes:
    del counts[word]

# 使用列表和lambda功能实现 词汇的排序 （此处约2行代码）
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

# 将替代名词转换为正式姓名
items[items.index(("孔明", 1383))] = ("诸葛亮", 1383)
items[items.index(("后主", 217))] = ("刘禅", 217)

txt = " ".join(dict(items).keys())

w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, \
    background_color="white", mask = mask)
w.generate(txt)

# 判断输出文件夹是否存在，如果不存在则创建
outputFileFolder = "output"
if os.path.exists(outputFileFolder) == False:
    os.mkdir(outputFileFolder)

# 输出打印生成的图片到指定文件夹
w.to_file("SanGuoWordCloudV1.png")