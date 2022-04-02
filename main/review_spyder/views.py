from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token

# Create your views here.
import json
import review_spyder.spyder.xc_utils as xc
from review_spyder.models import Original_Comments, Original_Product, picture


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
        page = postdata.get('page')
        if site == 'ctrip':
            if len(pid) != 0:
                # totalnum = xc.xc_spyder(pid)
                reviewlist = []
                for i in Original_Comments.objects.all().filter(productID=pid).values():
                    reviewlist.append(i['comment_content'])
                piclist = []
                for i in picture.objects.all().filter(productID=pid).values():
                    piclist.append(i['imgLink'])
                return JsonResponse({'totalnum': 11, 'reviewlist': reviewlist, 'piclist': piclist})
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
                print(res)
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


# 返回echarts数据
def api2(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        return JsonResponse(request.body)
