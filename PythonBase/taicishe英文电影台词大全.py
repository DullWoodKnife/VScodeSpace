import math

import requests
from lxml import etree
import re
# 定义一个函数用来获取网页源代码
def getsource(pagelink):
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    # 获取源码
    response = requests.get(pagelink, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html

# 定义一个函数用于解析我们的网页源代码并获取我们想要的数据
def geteveryitem(pagelink):
    html = getsource(pagelink)
    element = etree.HTML(html)
    # 获取总数
    print('总数文本', element.xpath('//*[@id="main"]/div/div[2]/div[2]/div/h1/small/text()')[0])
    totalmovies = re.findall(r'\d+', element.xpath('//*[@id="main"]/div/div[2]/div[2]/div/h1/small/text()')[0])[0]
    print('电影总数', totalmovies, type(totalmovies))
    pagecount = math.ceil(int(totalmovies)/100)
    print('电影总页数', pagecount)
    # 拿到[class="info"]的所有div
    movieitemlist = element.xpath('//div[@class="col-sm-9"]//div[@class="tv"]//ul/li')
    # print(movieitemlist,len(movieitemlist))
    mainurl = 'https://www.taicishe.com'
    # 定义一个列表
    itemlist = []
    for item in movieitemlist:
        # 定义一个字典
        itemdict = {}
        # 标题
        title = item.xpath('.//a//text()')[0]
        # 详情页的url
        link = item.xpath('.//a/@href')[0]
        # print(link)


        # 将数据存放到字典中
        itemdict['title'] = title
        itemdict['link'] = mainurl + link
        # print(itemdict)
        itemlist.append(itemdict)
    # print(itemlist)
    return itemlist


if __name__ == '__main__':
    url = 'https://www.taicishe.com/Others/movie/p/'
    # html = getsource(url)
    itemlist = geteveryitem(url)

    print(itemlist)