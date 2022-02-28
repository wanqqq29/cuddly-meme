# Generated by Django 4.0 on 2022-01-18 01:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Original_Product',
            fields=[
                ('productID', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('product_Link', models.CharField(max_length=300, verbose_name='产品链接')),
            ],
            options={
                'verbose_name': '产品信息',
                'verbose_name_plural': '产品信息',
            },
        ),
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgLink', models.CharField(max_length=300, verbose_name='图片链接')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review_spyder.original_product', verbose_name='产品ID')),
            ],
        ),
        migrations.CreateModel(
            name='Original_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentID', models.CharField(max_length=100, verbose_name='评论ID')),
                ('comment_content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('comment_score', models.IntegerField(verbose_name='用户评分')),
                ('trip_time', models.CharField(max_length=50, verbose_name='出行日期')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期')),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改日期')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review_spyder.original_product', verbose_name='产品ID')),
            ],
            options={
                'verbose_name': '原始评论',
                'verbose_name_plural': '原始评论',
            },
        ),
    ]
