# IP地址取自国内髙匿代理IP网站：整合旗云代理网
# 部分代码来源于互联网
# @author ahao

from bs4 import BeautifulSoup
import requests
from urllib import request
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}


def get_ip_list(url):
    web_data = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(web_data, 'html')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        httpType = tds[3].text
        if httpType == "HTTPS":
            httpType = "https://"
        else:
            httpType = "http://"
        ip_list.append(httpType + tds[0].text + ':' + tds[1].text)
#检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
          proxy_host = "https://" + ip
          proxy_temp = {"https": proxy_host}
          res = requests.get(url, proxies=proxy_temp)
        except Exception as e:
          ip_list.remove(ip)
          continue
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append(ip)
    proxy_ip = random.choice(proxy_list)
    proxy_type = proxy_ip[0:4]
    proxies = {proxy_type : proxy_ip}
    return proxies


if __name__ == '__main__':
    url = 'http://www.qydaili.com/free/?page=1'
    ip_list = get_ip_list(url)
    print(ip_list)
    proxies = get_random_ip(ip_list)
    print(proxies)
