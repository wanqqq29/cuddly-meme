from django.db import models
from datetime import datetime


# Create your models here.

class Original_Comments(models.Model):
    commentID = models.CharField(max_length=100, verbose_name=u'评论ID', unique=True)
    comment_content = models.TextField(max_length=1000, verbose_name=u'评论内容')
    comment_score = models.IntegerField(verbose_name=u'用户评分')
    trip_time = models.CharField(max_length=50, verbose_name=u'出行日期')
    created_date = models.DateTimeField(verbose_name=u'创建日期', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=u'修改日期', default=datetime.now)
    productID = models.ForeignKey('Original_Product', verbose_name=u'产品ID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'原始评论'
        verbose_name_plural = u'原始评论'


class Original_Product(models.Model):
    productID = models.CharField(max_length=100, verbose_name=u'产品ID', primary_key=True)
    product_Link = models.CharField(max_length=300, verbose_name=u'产品链接')

    class Meta:
        verbose_name = u'产品信息'
        verbose_name_plural = u'产品信息'


class picture(models.Model):
    productID = models.ForeignKey('Original_Product', verbose_name=u'产品ID', on_delete=models.CASCADE)
    imgLink = models.CharField(max_length=300, verbose_name=u'图片链接', unique=True)
