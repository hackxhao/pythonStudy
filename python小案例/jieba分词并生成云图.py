import jieba
from wordcloud import WordCloud, STOPWORDS


def generateImg():
    # 文件路径
    path = r"C:\Users\ahao\Downloads"
    # 读取文件内容 encoding需与文件编码保持一致
    text = (open(path+r'\岗位需求.txt', 'r', encoding='UTF-8')).read()
    # jieba分词 cut_all=False 精确模式
    words = jieba.cut(text, cut_all=False)
    words = " ".join(words)
    # 引入字体路径
    fontPath = r'C:\Windows\Fonts\STXIHEI.TTF'
    wc = WordCloud(font_path=fontPath,  # 如果是中文必须要添加这个，否则会显示成框框
                   background_color='black',
                   width=1000,
                   height=800,
                   stopwords=STOPWORDS.add('单位')
                   ).generate(words)
    wc.to_file('F://生成.png')  # 保存图片


if __name__ == '__main__':
    generateImg()
