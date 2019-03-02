"""
    爬虫程序入口
"""
import getproxy
import time
import random

if __name__ == '__main__':
    page_count = 100  # 分页数量, 这里就爬100页看看吧
    anony_url = 'https://www.xicidaili.com/nn/'  # 高匿代理链接
    ip_list = []
    for page in range(1, page_count+1):
        page_url = anony_url + str(page)
        ip = getproxy.get_proxy_ip(page_url)
        ip_list = ip_list + ip

        time.sleep(random.random() * 5)  # 线程挂起一个随机时间

