import requests

proxies = {
	"http": "http://125.40.79.66:8118",  # 代理ip
    "http": "http://180.118.240.148:808",
    "http": "http://222.94.150.111:61234"
}

headers = {
	"User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
}

http_url = "http://2018.ip138.com/ic.asp"
res = requests.post(url=http_url, headers=headers, proxies= proxies, timeout=30)
res.encoding = "gb2312"
html = res.text
# 打印出来页面上如果显示的ip是上面设置的代理ip则设置成功
print(html)
if res.status_code == 200:
	print("访问网页成功")
else:
	print ("代理ip错误")
