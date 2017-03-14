# -*- coding: utf-8 -*-
# feimengjuan
# 
# re模块主要包含了正则表达式
import re

#urllib.request模块提供了读取Web页面数据的接口
import urllib.request


#抓取网页图片


#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    page = urllib.request.urlopen(url) # urllib.request.urlopen()方法用于打开了一个URL地址
    html = page.read().decode() # read().decode() 用于读取URL上的数据并解码
    return html

def getImg(html):
    #利用正则表达式把源代码中的图片地址过滤出来
    reg = r'src="(.+?\.jpg)" pic_ext'   # pic_ext=jpeg 用于正则匹配图片格式
    imgre = re.compile(reg) # re.compile() 可以把正则表达式编译成正则表达式对象，可以重复使用
    imglist = imgre.findall(html) #表示在整个网页中过滤出所有图片的地址，放在imglist中

    x = 0
    for imgurl in imglist:
    	print(imgurl)
    	# urllib.request.urlretrieve()方法，直接将远程数据下载到本地，图片通过x一次递增命名
        urllib.request.urlretrieve(imgurl,'%s.jpg' %x) #打开imglist中保存的图片网址，并下载图片保存在本地
        x = x + 1

html = getHtml("http://tieba.baidu.com/p/2460150866")#获取该网址网页详细信息，得到的html就是网页的源代码
getImg(html)#从网页源代码中分析并下载保存图片
