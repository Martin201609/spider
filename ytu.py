# -*- coding:utf-8 -*-
from Tkinter import *
from ScrolledText import ScrolledText #滚动文本框
import urllib
import re

url_name =[ ] #url + name

a = 1
def get():
    global  a
    url = 'http://www.budejie.com/video/'+str(a)
    #var1.set('已经获取到第%s页的视频视频'%(a))
    print url
    html = urllib.urlopen(url).read()
    a += 1
    url_reg = r'data-mp4="(.*?)"'
    url_items = re.findall(url_reg,html)
    name_reg = re.compiel('<div class="j-r-list-c-desc"(.*?)</div>',re.S)
    name_items = re.findall(name_reg,html)
    for i,k in zip(name_items,url_items):
        url_name.append([i,k])

id =1 #视频个数
def write():
    global id
    while id < 100:
        get(id)
        for i in url_name:
            text.insert(END,str(id)+'.'+i[1]+'\n'+i[0]) #i[1] url, i[0]视频名称，END在末尾
            url_name.pop(0)
            id += 1



#########################################
root = Tk()
root.title("文件标题")
root.geometry('+300+100') #+300+100窗口左边

text = ScrolledText(root,font=('微软雅黑',10)) #文本框文字
text.grid()

button = Button(root,text='开始爬取',font=('微软雅黑',10),command = write)
button.grid()
var1 = StringVar()
label = Label(root,font=('微软雅黑',10),fg='red',textvariable = var1)
label.grid()
var1.set('准备中...')


root.mainloop()
