import json
import re
import requests
from lxml import etree
from review_spyder.utils import proxy as p


# TODO:
#    循环：0的时候多跑了一次  |0 1 重复
#    代理问题（云函数重建）ok
#    自由行 跟团游  已实现自由行 差别在url的最后一个参数


# 马蜂窝爬虫


def mfw_spyder(id):
    res = mfw_getdata(id)
    review_list = res['review_list']
    pimg_list = res['pimg_list']
    print(review_list)
    print(pimg_list)


def mfw_img(data, pimglist):
    x = etree.HTML(data)
    try:
        pimg = x.xpath("//div[contains(@class, 'img')]/a/@data-href")
        for i in pimg:
            pimglist.append(i)
        return pimglist
    except:
        pass


def mfw_review(data, reviewlist):
    try:
        x = etree.HTML(data)
        pcontent = x.xpath("//li/p[@class='txt']/text()")[0]
        if pcontent != '此用户参与了评分，没有填写评价内容。':  # 去除默认评价
            ptxt = re.sub("\n | |\r", '', pcontent)  # 去除特殊符号
            reviewlist.append(ptxt)
            return reviewlist
        else:
            pass
    except:
        pass


def mfw_getdata(id):
    nextflag = True  # 执行第一次循环时的初始值
    review_list = []  # 评论列表
    pimg_list = []  # 图片列表
    page = 1
    r = requests
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
              "Accept": "application/json, text/javascript, */*; q=0.01", 'Connection': 'close',
              "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
              "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Connection": "close",
              "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin"}
    proxy_times = 0
    while nextflag:
        print('外层循环')
        retry_count = 10  # 连接5秒超时，重试10次
        # url = 'https://www.mafengwo.cn/sales/c/comment/api/list?star=0&has_img=&page_no=' + str(page) + '&style=html&decorate=www&spu_id=9176925'
        url = 'https://www.mafengwo.cn/sales/c/comment/api/list?star=0&has_img=&page_no=' + str(
            page) + '&style=html&decorate=www&sales_id=' + id
        while retry_count > 0:
            proxy = p.get_proxy().get("proxy")  # 获取代理
            try:
                content = r.get(url, headers=header, proxies={"http": "http://{}".format(proxy)}, timeout=5).text
                j = json.loads(content)
                jdata = j['data']['list']
                nextflag = j['data']['page']['next']  # 是否继续的标志
                for i in jdata:
                    review_list = mfw_review(i, review_list)  # 评论
                    pimg_list = mfw_img(i, pimg_list)  # 图片
                print(review_list[-1])
                proxy_times += 1
                page += 1
                break
            except Exception as e:
                print(e)
                retry_count -= 1
                print('正在重试,次数' + str(10 - retry_count))
                p.delete_proxy(proxy)  # 删除代理池中代理
    return {'review_list': review_list, 'pimg_list': pimg_list}


# if __name__ == '__main__':
#     mfw_spyder('2623139')
