# coding:utf8

from urllib.request import urlopen
# json解析库,对应到lxml
import json
# json的解析语法，对应到xpath
import jsonpath

url = "http://py4e-data.dr-chuck.net/comments_42.json"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}

# request = urllib.request(url, headers=header)

response = urlopen(url)

# 取出json文件里的内容，返回的格式是字符串
html = response.read()

# 把json形式的字符串转换成python形式的Unicode字符串进行存储
unicodestr = json.loads(html)

# python形式的列表
city_list = jsonpath.jsonpath(unicodestr, "$..name")

print(unicodestr)
print(type(city_list))
print(city_list)

# 打印每个城市
for i in city_list:
    print(i)

# dumps()默认中文伟ascii编码格式，ensure_ascii默认为Ture
# 禁用ascii编码格式，返回Unicode字符串
array = json.dumps(city_list, ensure_ascii=False)

# 把结果写入到lagouCity.json文件中
with open("lagouCity.json", "wb") as f:
    f.write(array.encode("utf-8"))
