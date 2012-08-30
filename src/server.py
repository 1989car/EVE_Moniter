#!/usr/bin/env python
# coding: utf-8
'''
Created on 2012-8-28

@author: Administrator
'''
import time

import web

import serverImage

urls = (
  "", "redirect",
  "/*","Server",

)

class redirect:
    def GET(self): raise web.seeother('/')


class Server:
    '''
    Server Stat
    '''
    waittime = 1
                
    def GET(self):
        '''
        render = web.template.render("templates")
        
        return render.server()
        '''
        currenttime = int(time.time())
        if currenttime%self.waittime == 0:
            '''web.header("Content-type","image/x-png")'''
            return serverImage.createImage()
        else:
            web.notmodified()
       
     
app_server = web.application(urls, locals())