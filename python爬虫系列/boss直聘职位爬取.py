# boss直聘郑州java职位数据爬取
# @author ahao

from urllib import request
from bs4 import BeautifulSoup
import bs4
import requests



def getJobInfo():

    proxies = {
	    "http": "http://125.40.79.66:8118",  # 代理ip
        "http": "http://180.118.240.148:808",
        "http": "http://222.94.150.111:61234"
    }

    header = {
        'Accept': "*/*",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Connection': "keep-alive",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }

    urls = [
        "https://m.zhipin.com/c101180100/?page={}&query=java".format(str(i)) for i in range(1, 3)]
    
    for url in urls:
        response = requests.get(
            url, headers=header, proxies=proxies, timeout=30)
        print(response.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        datas = soup.find_all(name="li", attrs={"class": "item"})
        print(len(datas))
        for lines in datas:
            # 标题
            title = lines.find("h4")
            # 薪资
            money = lines.find("span")
            # 公司名称
            companyName = lines.find("div", attrs={"class": "name"})
            info = lines.find_all("em")
            # 地点
            address = info[0]
            # 年限
            nianXian = info[1]
            # 学历
            education = info[2]
            print(title.text, money.text, companyName.text,
                  address.text, nianXian.text, education.text)

if __name__ == '__main__':
    getJobInfo()
