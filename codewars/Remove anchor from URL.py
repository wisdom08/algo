# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
# 회고: url.split('#')[0]

def remove_url_anchor(url):
    res = ""
    for s in url:
        if s == '#':
            return res
        else:
            res += s

    return res
