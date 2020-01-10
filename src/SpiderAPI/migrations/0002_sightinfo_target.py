# Generated by Django 2.1.10 on 2020-01-09 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SpiderAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SightInfo',
            fields=[
                ('Title', models.CharField(blank=True, max_length=50, verbose_name='名字')),
                ('BusinessId', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='景点id')),
                ('DistrictId', models.IntegerField(default=0, verbose_name='地区id')),
                ('Tags', models.CharField(blank=True, max_length=30, verbose_name='特点')),
                ('Texts', models.CharField(blank=True, max_length=30, verbose_name='排名')),
                ('CommentScoreReal', models.CharField(blank=True, max_length=3, verbose_name='评分')),
                ('CommentNumberText', models.IntegerField(blank=True, default=0, verbose_name='评论数')),
                ('AddressText', models.CharField(blank=True, max_length=30, verbose_name='地点')),
                ('addressWay', models.CharField(blank=True, max_length=50, verbose_name='到达方式')),
                ('DescriptorText', models.TextField(blank=True, verbose_name='描述信息')),
                ('Img', models.TextField(blank=True, verbose_name='图片地址')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=20, verbose_name='爬取景点id')),
                ('did', models.CharField(max_length=20, verbose_name='景点地区id')),
                ('cookie', models.TextField(blank=True, verbose_name='设置cookie')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '爬虫设置',
                'verbose_name_plural': '爬虫设置',
            },
        ),
    ]