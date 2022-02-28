# 代理池的使用
import requests


def get_proxy():
    return requests.get("http://101.35.14.95:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://101.35.14.95:5010/delete/?proxy={}".format(proxy))
