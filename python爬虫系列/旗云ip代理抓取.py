# 爬取旗云代理网
# @author ahao

from urllib import request
from bs4 import BeautifulSoup
import csv


def getIpAgent():
    # 爬取前10页的数据
    urls = [
        "http://www.qydaili.com/free/?page={}".format(str(i)) for i in range(1, 3)]
    # 导入csv newline='' 解决隔行空的问题
    with open('F:/pythonReptile/ipAgent2.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ip地址", "端口", "匿名度", "类型", "位置", "响应速度", "最后验证时间"])
        for url in urls:
            html = request.urlopen(url).read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            tr = soup.find_all("tr")
            for idx, tr in enumerate(soup.find_all("tr")):
                if idx != 0:
                    tds = tr.find_all('td')
                    writer.writerow([tds[0].contents[0], tds[1].contents[0],
                                     tds[2].contents[0], tds[3].contents[0], 
                                     tds[4].contents[0], tds[5].contents[0], 
                                     tds[6].contents[0]])
       

if __name__ == '__main__':
    getIpAgent()
