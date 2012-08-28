'''
Created on 2012-8-28

@author: Administrator
'''
import re
import socket

import web
urls = (
  "", "redirect",
  "/","ServerStat"
)

class redirect:
    def GET(self): raise web.seeother('/')


class ServerStat:
    '''
    Server Stat
    '''
    startr = re.compile('Starting\ up\.\.\.\((\d+)\ sec\.\)')

    HOST='211.144.214.68'
    PORT=26000

    dat = ''.join([ chr(x) for x in [0x23, 0x00, 0x00, 0x00, 0x7E, 0x00, 0x00, 0x00,
                        0x00, 0x14, 0x06, 0x04, 0xE8, 0x99, 0x02, 0x00,
                        0x05, 0x8B, 0x00, 0x08, 0x0A, 0xCD, 0xCC, 0xCC,
                        0xCC, 0xCC, 0xCC, 0x00, 0x40, 0x05, 0x49, 0x0F,
                        0x10, 0x05, 0x42, 0x6C, 0x6F, 0x6F, 0x64 ]])
    def getNum(self, cin ):
        return sum([ ord(n) * ( 256 ** p )  for (n ,p )  in zip( cin , range(4))]) 
    
    def getServer(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST, self.PORT))
            s.send(self.dat )
            idat =  s.recv( 4096 )       
            
            if self.startr.search( idat ):
                m = self.startr.search( idat )
                '''print 'Starting:%s' % (m.groups(1)[0])'''
                return 'Starting:%s' % (m.groups(1)[0])
            else:        
                v = ord( idat[19] )
                if v == 4:
                    cnt = self.getNum( idat[20:25] )
                elif v == 5:
                    cnt = self.getNum(  idat[20:22])
                elif v == 6:
                    cnt = self.getNum( idat[20])
                else:
                    cnt = 0
                
                '''print 'EVE Server Online:%u' % ( cnt )'''
                return cnt
        except:
                '''print 'Offline:'''
                return -1 
    def GET(self):
        print self.getServer()
        return self.getServer()



app_server = web.application(urls, locals())