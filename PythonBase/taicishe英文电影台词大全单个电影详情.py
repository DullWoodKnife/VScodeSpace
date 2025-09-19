import requests
from lxml import etree

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


def geteveryitem(pagelink):
    html = geteveryitem(pagelink)
    element = etree.HTML(html)
    pagecount = int(element.xpath('//*[@id="main"]/div/div/div[2]/div/h2/small/b[2]//text()')[0])
    print("totalcount", pagecount)
    dialogue = []
    for item in range(1, pagecount+1):
        print("singlecount",item)
        print("CompleteUrl", pagelink + str(item))
        sourceurl = pagelink + str(item)
        element1 = etree.HTML(getsource(sourceurl))

        itemlist = element1.xpath('//div[@class="entry"]')
        for piece in itemlist:
            fragment = piece.xpath('//div[@class="entry"]//text()')
            dialogue.append(fragment)
        # print(dialogue)
    print('dialogue length', len(dialogue))
    return dialogue


if __name__ == '__main__':
    url = 'https://www.taicishe.com/movie-twenty-years-with-the-dolphins-2004?page='
    # html = getsource(url)
    dialoguelist = geteveryitem(url)
    print(dialoguelist)