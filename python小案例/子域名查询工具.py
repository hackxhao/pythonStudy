# 子域名查询工具
# @author ahao

from urllib import request
from bs4 import BeautifulSoup
import csv
import bs4

def getSubdomain(domain):
    url = "http://webscan.360.cn/sub/index/?url={}".format(str(domain))
    html = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.find_all(name="dd")
    for line in datas:
        content = line.find("strong")
        # 解决AttributeError: 'NoneType' object has no attribute 'text' 问题
        if isinstance(content, bs4.element.Tag):
            print(content.text)


if __name__ == '__main__':
    getSubdomain("www.baidu.com")

