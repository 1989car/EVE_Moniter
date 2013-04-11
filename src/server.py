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
  "/status.png","Server",

)



class redirect:
    def GET(self): raise web.seeother('/')
	
	
class Server:


    def GET(self):
	
	mc = pylibmc.Client()
        
        last_time = mc.get("last_time")
        
        if not last_time:
        	return serverImage.createImage()
		
	current_time = int(time.time())
        
        print current_time,"/",last_time
       
	if current_time-last_time > 10:
        	'''web.header('Cache-Control:',' no-cache, no-store, max-age=0, must-reva lidate')'''
                
		return	serverImage.createImage()
        else:
        	return mc.get("output")
            

app_server = web.application(urls, locals())