# -*- coding: utf-8 -*-
# feimengjuan
# 
# reģ����Ҫ������������ʽ
import re

#urllib.requestģ���ṩ�˶�ȡWebҳ�����ݵĽӿ�
import urllib.request


#ץȡ��ҳͼƬ


#���ݸ�������ַ����ȡ��ҳ��ϸ��Ϣ���õ���html������ҳ��Դ����
def getHtml(url):
    page = urllib.request.urlopen(url) # urllib.request.urlopen()�������ڴ���һ��URL��ַ
    html = page.read().decode() # read().decode() ���ڶ�ȡURL�ϵ����ݲ�����
    return html

def getImg(html):
    #����������ʽ��Դ�����е�ͼƬ��ַ���˳���
    reg = r'src="(.+?\.jpg)" pic_ext'   # pic_ext=jpeg ��������ƥ��ͼƬ��ʽ
    imgre = re.compile(reg) # re.compile() ���԰�������ʽ�����������ʽ���󣬿����ظ�ʹ��
    imglist = imgre.findall(html) #��ʾ��������ҳ�й��˳�����ͼƬ�ĵ�ַ������imglist��

    x = 0
    for imgurl in imglist:
    	print(imgurl)
    	# urllib.request.urlretrieve()������ֱ�ӽ�Զ���������ص����أ�ͼƬͨ��xһ�ε�������
        urllib.request.urlretrieve(imgurl,'%s.jpg' %x) #��imglist�б����ͼƬ��ַ��������ͼƬ�����ڱ���
        x = x + 1

html = getHtml("http://tieba.baidu.com/p/2460150866")#��ȡ����ַ��ҳ��ϸ��Ϣ���õ���html������ҳ��Դ����
getImg(html)#����ҳԴ�����з��������ر���ͼƬ
