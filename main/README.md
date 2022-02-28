---
title:基于XX的旅游网站评论情感分析
tags: [python,数据分析,爬虫,NLP]
hide: true
---
# 基于xx的旅游网站情感分析
# 想法：

集成各大旅游网站平台，当用户复制某个链接到系统中，自动爬取该目标中的评论并完成分析，展示给用户

## 展示维度包括：

- 评论情感分极-
- 词云图
- 机票或景点价格预测-
- 根据出行日期判断目的地天气
- 酒店价格

## 难点：
- 适应多个网站的爬虫、反爬策略
- 评论中的转折词，比如：景点态度不好，但是风景不错，还是值得一去的。这一条应该划分到情感为正面，但是很可能因为态度不好而划分到负面
  - [融合句法规则和CNN的旅游评论情感分析](https://www.cnki.com.cn/Article/CJFDTotal-SJSJ201911047.htm)
  - 是不是可以根据评论中用户自己打的标签与分析出的标签做一个权重
- 价格预测
- 酒店推荐 价格


## 设计
### 爬虫
- [x] 代理池 [云函数代理池](D:/0x0documents/MarkDown文件夹/python&爬虫/云函数代理池.md)
- [ ] 途牛
- [ ] 马蜂窝

### 前端
- 暂未设计

### 后端
- 暂时选用Django

# 笔记

## 代理池
https://proxy-pool.readthedocs.io/zh/latest/user/how_to_run.html#id5

## TensorFlow.js

- https://storage.googleapis.com/tfjs-examples/sentiment/dist/index.html



## 途牛

## 评论api(挂掉了)

- https://www.tuniu.com/papi/tour/comment/product?page=2&productId=210050902&selectedType=23&firstRequest=0&stamp=0110038120372192071638846643381
- 参数
  - page 页码
  - productid 出游项目id
  - selectedType 评论类型
    - 23 精华点评
    - 20 满意
    - 21 一般
    - 22 不满意
    - 16 有图
    - 1199 感觉不错
    - 1200 导游不错
    - ...... 可以根据接口响应看到

# 代码
## 携程
```python

```

