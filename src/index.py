#!/usr/env/python 
#!-*- encoding: utf-8 -*-  

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
        '''serverstat = ServerStat()'''
        '''return serverstat.getServerStats'''
        return "EVE Server Stats"
    
    
if __name__ == "__main__":
    app.run()