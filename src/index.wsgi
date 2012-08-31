import os
import pylibmc

import sae
import web

import server

urls = ("/","Index",
        "","re",
        "/test","test",
        "/server",server.app_server)

app = web.application( urls, globals() )

class re:
    def GET(self): raise web.seeother('/')
    
class test:
    def GET(self):
    	mc = pylibmc.Client()
        return mc.get("output")
    
class Index:
    
    def GET(self):
        render = web.template.render("templates")
        '''serverstat = ServerStat()'''
        '''return serverstat.getServerStats'''
        return render.index()
		
app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)