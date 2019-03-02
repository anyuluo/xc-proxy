"""
    给定一个url，获取链接下相关的代理IP信息
"""

from bs4 import BeautifulSoup
import urllib.request
import random
import verify
import save


def get_proxy_ip(url):
    # 初始化代理IP列表
    # 至于这些IP哪儿来的你就别问我了，出门左转，你要爬的地方不就有么
    agent = ['39.137.168.229:8080', '118.89.52.23:3128',
             '124.93.201.59:42672', '116.209.54.16:9999',
             '183.6.130.6:8118', '59.62.164.116:9999']
    ip_list = []
    try:
        # 设置请求头信息
        headers = {
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            # 'Host': 'www.xicidaili.com',
            # # Referer属性：一些网站中加入的防盗链功能，
            # # 经过观察，当请求下一页时，Referer属性的值为当点页的链接，在这里为了方便随机生成一页的链接
            # 'Referer': 'https://www.xicidaili.com/nn/{}'.format(random.randint(1, 500)),
            # 'Upgrade-Insecure-Requests': '1',
            # 设置用户代理
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        }

        # 从agent列表中随机选择一个IP地址做为代理
        proxy = {'http': random.choice(agent)}
        # 创建proxyHandler
        proxy_handler = urllib.request.ProxyHandler(proxy)
        # 创建opener
        proxy_opener = urllib.request.build_opener(proxy_handler)
        # 安装opener
        urllib.request.install_opener(proxy_opener)

        # 构造请求对象
        req = urllib.request.Request(url, headers=headers)
        # 打开网页链接，获取网页源码
        res = urllib.request.urlopen(req)
        # 使用BeautifulSoup解析html页面
        soup = BeautifulSoup(res, 'html.parser')

        # 通过CSS选择器选中表格中所有的tr元素
        ip_items = soup.select('#ip_list tr')
        # 在遍历IP列表时去掉表头
        for item in ip_items[1:]:
            item = item.select('td')
            ip = item[1].text  # ip地址
            port = item[2].text  # 端口
            address = item[3].text.strip()  # 服务器地址
            anony = item[4].text  # 匿名
            protocl = item[5].text  # 协议
            speed = item[6].select('.bar')[0]['title']  # 服务器响应速度
            time = item[9].text  # 服务器最后验证时间
            # 验证IP的有效性
            if 200 == verify.verify_proxy(ip + ':' + port):
                print('发现可用IP：{}:{}'.format(ip, port))
                agent.append(ip + ':' + port)  # 将IP加入代理列表中
                # 将ip信息拼接成一个字符串
                ip_info = ip + ' ' + port + ' ' + anony + ' ' + protocl + ' ' + address + ' ' + speed + ' ' + time
                save.save_txt(ip_info, 'xc-ip.txt')  # 将IP信息暂存到列表中
            else:
                print('很遗憾！这个ip：{} 不可用'.format(ip))
        print(ip_list)
        return ip_list
    except Exception as e:
        print('expect:', e)
