import json, re, requests
import review_spyder.utils.TimeFormat as tf
from review_spyder.models import Original_Comments, Original_Product, picture
from lxml import etree


# TODO:
#   携程爬虫
#   获取到了评论跟图片数据 只打印了出来 还没做处理
#   每次获取50条，基本两三次就能全部获取到，所以不需要代理

# 携程爬虫
def xc_spyder(id):
    res = xc_getdata(id)
    review_list = res['review_list']
    img_list = res['img_list']
    return res['previewnum']

##携程旅游信息爬虫
def xc_info_spyder(id):
    url = 'https://vacations.ctrip.com/travel/detail/p' + id + '/?city=144'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://vacations.ctrip.com/grouptravel/",
    }
    html = requests.get(url, headers=headers).text
    html_tree = etree.HTML(html)
    pname = html_tree.xpath(
        "//html/body[@class='bg_white_color']/div[@id='root']/div[@class='imvc-view-item']/div[@id='base_bd']/div[@class='header_wrap']/div[@class='header_inner']/div[@class='detail_header']/div[@class='detail_summary']/h1/text()")
    pdesc = html_tree.xpath(
        "//html/body[@class='bg_white_color']/div[@id='root']/div[@class='imvc-view-item']/div[@id='base_bd']/div[@class='header_wrap']/div[@class='header_inner']/div[@class='detail_header']/div[@class='detail_summary']/p[@class='detail_title_subhead']/text()")
    ppeoplenum = \
        html_tree.xpath("//*[@id='base_bd']/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div/span/text()")[0]
    poffer = html_tree.xpath("//*[@id='grp-0-hint-supplier']/div/a/span/text()")
    pfeatures = html_tree.xpath(
        "/html/body[@class='bg_white_color']/div[@id='root']/div[@class='imvc-view-item']/div[@id='base_bd']/div[@class='header_wrap']/div[@class='header_inner']/div[@class='detail_header']/div[@class='detail_summary']/div[@class='pro_det_inf']/dl[1]/dd[@class='pro_det_tags']/span[@class='tag_com']/text()")
    poffer = html_tree.xpath("//div[@class='pro_det_inf']/dl[3]/dd/div/a/text()")
    pmd = html_tree.xpath("//div[@class='pro_det_inf']/dl[4]/dd/ul/li/text()")
    return {'pname': pname, 'pdesc': pdesc, 'ppeoplenum': ppeoplenum, 'poffer': poffer, 'pfeatures': pfeatures,
            'pmd': pmd}


# requestspost获取数据 返回j
def xc_reqpost(id, page):
    url = 'https://m.ctrip.com/restapi/soa2/20047/listComments'
    post_data = json.dumps({
        "head": {"cid": "09031157310830874764", "ctok": "", "cver": "1.0", "lang": "01", "sid": "8888", "syscode": "09",
                 "auth": "", "extension": []}, "ucpBizId": 2, "scene": "PRODUCT_QUERY", "queryId": id,
        "paging": {"pageSize": 50, "pageNo": page}, "sortType": 2, "tagTerms": []})
    content = requests.post(url, data=post_data).text
    j = json.loads(content)
    print(j)
    # Original_Product
    OP = Original_Product()
    OP.productID = id  # 添加产品id
    OP.product_Link = 'https://vacations.ctrip.com/travel/detail/p' + id + '/'  # 添加产品链接
    OP.save()  # 保存
    return j


def xc_getdata(id):
    review_list = []  # 评论列表
    img_list = []  # 图片列表
    j = xc_reqpost(id, 1)  # 获取第一页内容，主要获取总条数 用来分页，顺便把第一页的内容存起来
    totalCount = j['totalCount']
    if totalCount > 50:
        page_num = totalCount // 50 + 2  # 总数除50 +1 为分页数，用来循环;+1是因为剩余不到1页的;因为循环从1开始，故再+1
    else:
        page_num = 1
    print(page_num)
    total_comments = j['comments']
    ptid = Original_Product.objects.get(productID=id)
    print(ptid)
    res = xc_getfistinfo(total_comments, review_list, img_list, ptid)
    review_list = res['reviewlist']
    img_list = res['imglist']
    if page_num > 1:  # 若条数少于50条 则不爬下一页
        res = xc_getotherinfo(id, page_num, review_list, img_list, ptid)
        review_list = res['reviewlist']
        img_list = res['imglist']
    return {'review_list': review_list, 'img_list': img_list, 'previewnum': totalCount}


# 获取page=1的数据
def xc_getfistinfo(data, reviewlist, imglist, ptid):
    # data为[comments]
    for i in data:
        comment_content = i['content']  # 评论数据
        comment_content = re.sub("\n| |\r", '', comment_content)
        reviewlist.append(comment_content)
        # 声明Original_Comments模型实例
        OC = Original_Comments()
        OC.comment_content = comment_content  ## 想数据库中添加评论数据
        OC.commentID = i['commentId']  # 评论id
        OC.trip_time = tf.formatTime(i['commentTime'])  # 评论时间
        OC.comment_score = i['score']  # 用户评分
        OC.productID = ptid  # 产品id
        try:
            OC.save()
        except:
            pass
        try:
            img_content = i['attachments']
            for ii in img_content:
                imglist.append(ii['url'])
                pc = picture()
                pc.productID = ptid  # 产品id
                pc.imgLink = ii['url']  # 产品链接
                try:
                    pc.save()
                except:
                    pass
        except:
            pass

    return {'reviewlist': reviewlist, 'imglist': imglist}


# 获取page!=1的数据
def xc_getotherinfo(id, pagenum, reviewlist, imglist, ptid):
    for ii in range(2, pagenum):
        j = xc_reqpost(id, ii)
        total_comments = j['comments']
        for i in total_comments:
            comment_content = i['content']
            comment_content = re.sub("\n| |\r", '', comment_content)
            reviewlist.append(comment_content)
            # 声明Original_Comments模型实例
            OC = Original_Comments()
            OC.comment_content = comment_content  ## 想数据库中添加评论数据
            OC.commentID = i['commentId']  # 评论id
            OC.trip_time = tf.formatTime(i['commentTime'])  # 评论时间
            OC.comment_score = i['score']  # 用户评分
            OC.productID = ptid  # 产品id
            try:
                OC.save()
            except:
                pass
            try:
                img_content = i['attachments']
                for iii in img_content:
                    imglist.append(iii['url'])
                    pc = picture()
                    pc.productID = ptid  # 产品id
                    pc.imgLink = ii['url']  # 产品链接
                    try:
                        pc.save()
                    except:
                        pass
            except:
                pass
    return {'reviewlist': reviewlist, 'imglist': imglist}
