# 爬取89免费ip代理网
# @author ahao

from urllib import request
from bs4 import BeautifulSoup
import csv


def getIpAgent():
    # 爬取前10页的数据
    urls = [
        "http://www.89ip.cn/index_{}.html".format(str(i)) for i in range(1, 10)]
    # 导入csv newline='' 解决隔行空的问题
    with open('F:/pythonReptile/ipAgent.csv', 'a', newline='') as file:
        for url in urls:
            html = request.urlopen(url).read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            writer = csv.writer(file)
            writer.writerow(["ip地址", "端口", "地理位置", "运营商", "最后检测时间"])
            for idx, tr in enumerate(soup.find_all("tr")):
                if idx != 0:
                    tds = tr.find_all('td')
                    writer.writerow([tds[0].contents[0], tds[1].contents[0],
                                     tds[2].contents[0], tds[3].contents[0], tds[4].contents[0]])
       

if __name__ == '__main__':
    getIpAgent()
