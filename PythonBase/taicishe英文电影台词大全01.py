import requests
from lxml import etree
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# 获取源码
pagelink = 'https://www.taicishe.com/Others/movie/p/545'
response = requests.get(pagelink, headers=headers)
response.encoding = 'utf-8'
html = response.text

element = etree.HTML(html)
# 拿到[class="info"]的所有div
movieitemlist = element.xpath('//div[@class="col-sm-9"]//div[@class="tv"]//ul/li')
# print(movieitemlist,len(movieitemlist))
# 定义一个列表
itemlist = []
for item in movieitemlist:
    # 定义一个字典
    itemdict = {}
    # 标题
    title = item.xpath('.//a//text()')
    # print(title)
    # 详情页的url
    link = item.xpath('.//a[@href]')
    # print(link)


    # 将数据存放到字典中
    itemdict['title'] = title
    itemdict['link'] = link
    # print(itemdict)
    itemlist.append(itemdict)
    print(itemlist)
