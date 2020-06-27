# -*- coding: utf-8 -*-
import pymysql
import feedparser
import  json
import os
import requests

#第一次运行请注释掉下面 dowmload(url) 这个代码
#第一次运行请注释掉下面 dowmload(url) 这个代码
#第一次运行请注释掉下面 dowmload(url) 这个代码


ping_url="https://www.baidu.com/"   #heroku app 或 aria2  prc的网址，用于检测aria2是否在线
prc_password=""     #prc密码
rpc_url = "http://ip:6800/jsonrpc"      #改成自己的aria2 rpc链接
dir="/root/pan/download"     #下载地址，末尾不需要 /



def ping(url):
    print(f'{url}: Ping!')
    html=requests.get(url)
    #print(html.status_code)
    return html.status_code

def dowmload(url,title):
    down=f"{dir}/{title}"
    jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer',
                          'method': 'aria2.addUri',
                          'params': [f"token:{prc_password}", [
                              url],
                                     {
                                         "dir": down}]})

    aria = requests.post(url=rpc_url, data=jsonreq, verify=False)
    print(aria.text)

def creat_json():
    if os.path.exists('rss.json')==False:
        none_list=[]
        with open('rss.json', 'w') as f:
            json.dump(none_list, f)
        f.close()

def read_json():
    # 读取存储于json文件中的列表

    with open('rss.json', 'r') as f_obj:
        rss_list = json.load(f_obj)
    f_obj.close()
    return rss_list

def save(rss_list):
    with open('rss.json', 'w') as f_obj:
        json.dump(rss_list, f_obj)
    f_obj.close()

if __name__ == '__main__':
    creat_json()
    rss_list=read_json()
    print("开始获取Rss")
    rss_url='https://share.acgnx.se/rss-sort-2.xml'     #末日资源库网址，可换为动漫花园，之前换过记得是支持的
    d = feedparser.parse(rss_url)
    print("Rss获取完成")
    num=0

    for a in d.entries:
        pan = 0
        title=str(a["title"])
        title=title.replace("\\"," ").replace("/"," ").replace("&"," ").replace("​","")
        title.lstrip()
        url=str(a["links"][1]["href"])
        fabu=str(a["authors"][0]["name"])
        for b in rss_list:
            if b["url"]==url:
                pan=1

        if pan==0:
            info_dict={"title":title,"url":url,"fabu":fabu}

            print(f"添加：{info_dict}")
            for c in range(3):
                if ping(ping_url)==200:
                    #dowmload(url,title)  #第一次运行请注释掉下面 dowmload(url) 这个代码
                    rss_list.append(info_dict)
                    break
            else:
                print("aria2未启动")

            num=num+1




    print("更新%d磁力" % num)
    save(rss_list)
