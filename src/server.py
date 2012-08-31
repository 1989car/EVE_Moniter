#!/usr/bin/env python
# coding: utf-8
'''
Created on 2012-8-28

@author: Administrator
'''
import time

import pylibmc

import web

import serverImage

urls = (
  "", "redirect",
  "/*","Server",

)

class redirect:
    def GET(self): raise web.seeother('/')
    
    
class Server:

    waittime = 60
                   
    def GET(self):
    
    mc = pylibmc.Client()
        
    currenttime = int(time.time())
    if currenttime%self.waittime == 0:
        serverImage.createImage()
    return mc.get("output")
            

app_server = web.application(urls, locals())