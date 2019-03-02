"""
    验证代理IP的有效性
"""
import urllib.request

def verify_proxy(ip):
    # 设置请求头信息
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
    }
    # 使用百度来验证代理IP的有效性
    url = 'http://www.baidu.com'
    # 填写代理IP地址
    proxy = {'http': ip}
    # 创建proxyHandler
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 创建opener
    proxy_opener = urllib.request.build_opener(proxy_handler)
    # 安装opener
    urllib.request.install_opener(proxy_opener)

    try:
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req, timeout=5.0)  # 设置请求超时时长5秒
        return res.getcode()  # 返回状态码
    except Exception as e:
        print('Exception:', e)

