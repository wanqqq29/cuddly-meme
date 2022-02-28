import time

def formatTime(timestamp):
    time_local = time.localtime(timestamp/1000) # 13位时间戳需转换为10位时间戳
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt
