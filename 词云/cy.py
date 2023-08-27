##对于NLP（自然语言处理）来说，分词是一步重要的工作,这里使用jieba分词
##对你输入的文章进行分词然后统计等等操作
import jieba
##导入用于用于制作词云图的wordcloud
from wordcloud import WordCloud,ImageColorGenerator
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
##打开刚刚的info.txt,并且把得到的句柄内容复制给content
with open('三国演义.txt','r',encoding="UTF-8") as file1:
    content = "".join(file1.readlines())
##然后使用jieba模块进行对文本分词整理
content_after = "".join(jieba.cut(content,cut_all=True))

##font_path
##使用worldCloud模块对刚刚整理好的分词信息进行处理.
##max_font_size参数是可以调整部分当个词语最大尺寸
##max_words是最大可以允许多少个词去组成这个词云图
##height高度,width宽度,
##background_color背景颜色
wc = WordCloud(font_path="msyh.ttc",background_color="black",max_words=1000,max_font_size=100,
                width=1500,height=1500).generate(content)
##使用matplotlib的pyplot来进行最后的渲染出图.
plt.imshow(wc)
##目标文件另存为这个名录下
wc.to_file('wolfcodeTarget.png')
