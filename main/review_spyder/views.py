from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token

# Create your views here.
import json, datetime, collections
import review_spyder.spyder.xc_utils as xc
from review_spyder.models import Original_Comments, Original_Product, picture
from review_spyder.sentiments.Bayes.bayes_train import 单条API, load_corpus, pos_stl


def test(request):
    return HttpResponse('1')


# 获取Csrf_token
def foo(request):
    if request.method == 'GET':
        csrf_token = get_token(request)
        return HttpResponse(csrf_token, content_type="application/json,charset=utf-8")


def get_index_page(request):
    return render(request, template_name='index.html')


def spyder(request):
    site = request.GET.get('site')
    procuctid = request.GET.get('productid')
    if site == '携程':
        if len(procuctid) != 0:
            # 总评论数量，调用方法开始爬取评论并存数据库
            previewnum = xc.xc_spyder(procuctid)
            r = Original_Comments.objects.all().filter(productID=procuctid)
            return render(request, 'result.html', {'re': r, 'productid': procuctid})


# 获取评论信息（爬虫）
def getreview(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        site = postdata.get('type')  # 网站类型：携程|马蜂窝
        pid = postdata.get('pid')  # 产品id
        if site == 'ctrip':
            if len(pid) != 0:
                # totalnum = xc.xc_spyder(pid)
                data = Original_Comments.objects.all().filter(productID=pid).values()
                reviewlist = []
                tokScorelist = []
                good = 0
                for i in data:
                    reviewlist.append(i['comment_content'])
                    tokScorelist.append(i['tokScore'])
                    if i['tokScore'] == '0':
                        good += 1
                goodrate = str((good / len(tokScorelist)) * 100)[0:4]
                print(goodrate)
                reviewdata = []
                for i in range(0, len(reviewlist)):
                    reviewdata.append({'item': reviewlist[i], 'score': tokScorelist[i]})
                piclist = []
                for i in picture.objects.all().filter(productID=pid).values():
                    piclist.append(i['imgLink'])
                return JsonResponse(
                    {'totalnum': len(reviewlist), 'reviewlist': reviewdata, 'piclist': piclist, 'goodrate': goodrate})
    else:
        return HttpResponse('method is NotAllowd! x_x!')


# 获取信息
def getinfo(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        site = postdata['type']
        pid = postdata['pid']
        if site == 'ctrip':
            if len(pid) != 0:
                res = xc.xc_info_spyder(pid)
                return JsonResponse(res)
            else:
                return HttpResponse('method is NotAllowd! x_x!')
    else:
        return HttpResponse('method is NotAllowd! x_x!')


# 单条分析接口（不重要）
def api1(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        return JsonResponse(request.body)


# 返回WordCloud数据
def WordCloud(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        site = postdata.get('type')  # 网站类型：携程|马蜂窝
        pid = postdata.get('pid')  # 产品id
        if site == 'ctrip':
            if len(pid) != 0:
                reviewlist = []
                for i in Original_Comments.objects.all().filter(productID=pid).values():
                    reviewlist.append(i['comment_content'])
                wordCloud = []
                for j in load_corpus(reviewlist):
                    j = j.split()
                    for x in j:
                        if len(x) > 1:
                            wordCloud.append(x)
                wordCloud = pos_stl(wordCloud)
                # 词频统计
                word_counts = collections.Counter(wordCloud)  # 对分词做词频统计
                word_counts = dict(word_counts)
                word_list = []
                for i in word_counts:
                    word_list.append({'name': i, 'value': word_counts[i]})
                return JsonResponse({'score': 80, 'charts': {'wordCloud': word_list}})
    else:
        return HttpResponse('method is NotAllowd! x_x!')


# 月份分类
def bartool(data):
    list = [0 for i in range(12)]
    for i in data:
        list[int(i[5:7]) // 1 - 1] += 1  # 月份除1再-1确定元素位置 从0开始+1
    return list


def bar(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        site = postdata.get('type')  # 网站类型：携程|马蜂窝
        pid = postdata.get('pid')  # 产品id
        if site == 'ctrip':
            if len(pid) != 0:
                data = Original_Comments.objects.all().filter(productID=pid).values()
                good = []
                bad = []
                for i in data:
                    if i['tokScore'] == '0':
                        good.append(i['trip_time'])
                    elif i['tokScore'] == '1':
                        bad.append(i['trip_time'])
                gooddata = bartool(good)
                baddata = bartool(bad)
                return JsonResponse({'good': gooddata, 'bad': baddata})
    else:
        return HttpResponse('method is NotAllowd! x_x!')
# 返回pie数据
