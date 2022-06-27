import urllib.request
import http.cookiejar



# import requests
#
#
# response = requests.get("https://uat.yaoud.com:9030/report")
#
# print(response.status_code)

import requests
from lxml import etree
import time

url = "https://www.baidu.com/"
# url_1 = "http://www.htqyy.com/"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",'Connection': 'close'
}
resp = requests.get(url,headers=headers)
text = resp.text
# html = etree.HTML(text)
print(text)










# url = 'https://uat.yaoud.com:9030/'
#
# # 方法一
# print('方法一')
# req_one = urllib.request.Request(url)
# req_one.add_header('User-Agent', 'Mozilla/6.0')
# res_one = urllib.request.urlopen(req_one)
# code_one = res_one.getcode()
# html_one = res_one.read().decode('utf-8')
# res_one.close()
# print('方法一网页状态码：%s' % (code_one))
# print('方法一网页内容：' + html_one)


# print('方法二')
# res_two = urllib.request.urlopen(url)
# code_two = res_two.getcode()
# html_two = res_two.read().decode('utf-8')
# print('方法二网页状态码：%s' % (code_two))
# print('方法二网页内容：'+html_two)



import sys
import requests

# https://uat.yaoud.com:9030/report
# https://uat.yaoud.com:9030/wms
# https://uat.yaoud.com:9030/operation

# a = eval(sys.argv[1])
# b = eval(sys.argv[2])
# c = eval(sys.argv[3])

# print(requests.get(a).status_code)
# print(requests.get(b).status_code)
# print(requests.get(c).status_code)

# print(a+b+c)


# print(requests.get('https://uat.yaoud.com:9030/report').status_code)

# import requests
# import sys
#
#
# gpus = sys.argv[1]
# html2 = requests.get(gpus).status_code
# gpus2 = sys.argv[2]
# html3 = requests.get(gpus2).status_code
# print(html2)
# print(html3)

