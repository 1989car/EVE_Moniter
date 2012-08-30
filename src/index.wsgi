#!/usr/env/python 
#!-*- encoding: utf-8 -*-  

import os

import sae
import web

import server

urls = ("/","Index",
        "","re",
        "/server",server.app_server)

app = web.application( urls, globals() )

class re:
    def GET(self): raise web.seeother('/')


    
class Index:
    
    def GET(self):
        render = web.template.render("templates")
        '''serverstat = ServerStat()'''
        '''return serverstat.getServerStats'''
        return render.index()
        
app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)