"""
    保存ip信息到指定文件
"""


def save_txt(str_ip, filename):
    try:
        with open(filename, 'a') as fn:
            fn.write(str_ip + '\n')
    except Exception as e:
        print('except:', e)
