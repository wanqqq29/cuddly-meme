# import utils.mfw_utils as mfw
# import utils.xc_utils as xc
#
#
# #   TODO:
# #   爬取结搜索结果页 比如搜索丽江,爬取搜索结果,统计哪个团去的人多 价格排序 评价排序
# #   爬取评论时间 画折线图分析哪个月份去的人多  从而 推荐去的月份
# #   顺便保存评分 作为训练标识
#
# # if __name__ == '__main__':
# #     # mfw.mfw_spyder('2623139')
# #     # mfw.mfw_spyder('5122707')
# #     # xc.xc_spyder('16799198')
# #     xc.xc_spyder('10798720')

import json,re,requests,time
from review_spyder.models import Original_Comments, Original_Product, picture

