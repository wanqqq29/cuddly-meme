from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json
import review_spyder.spyder.xc_utils as xc
from review_spyder.models import Original_Comments, Original_Product, picture


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
        if site == '携程':
            if len(pid) != 0:
                totalnum = xc.xc_spyder(pid)
                reviewlist = Original_Comments.objects.all().filter(productID=pid)
                piclist = picture.objects.all().filter(productID=pid)
                return JsonResponse({'totalnum': totalnum, 'reviewlist': reviewlist, 'piclist': piclist})
    else:
        return HttpResponse('method is NotAllowd! x_x!')


def getinfo(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        site = postdata.get('type')
        pid = postdata.get('pid')
        if site == '携程':
            if len(pid) != 0:
                res = xc.xc_info_spyder(pid)
                return JsonResponse(res)
    else:
        return HttpResponse('method is NotAllowd! x_x!')
