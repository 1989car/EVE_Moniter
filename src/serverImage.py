#!/usr/bin/env python
# coding: utf-8
'''
Created on 2012-8-30

@author: Administrator
'''
import sae

import os,time,re,socket,StringIO

from PIL import Image, ImageDraw,ImageFont


startr = re.compile('Starting\ up\.\.\.\((\d+)\ sec\.\)')

HOST='211.144.214.68'
PORT=26000

dat = ''.join([ chr(x) for x in [0x23, 0x00, 0x00, 0x00, 0x7E, 0x00, 0x00, 0x00,
                        0x00, 0x14, 0x06, 0x04, 0xE8, 0x99, 0x02, 0x00,
                        0x05, 0x8B, 0x00, 0x08, 0x0A, 0xCD, 0xCC, 0xCC,
                        0xCC, 0xCC, 0xCC, 0x00, 0x40, 0x05, 0x49, 0x0F,
                        0x10, 0x05, 0x42, 0x6C, 0x6F, 0x6F, 0x64 ]])
    
def getTime():
        Time =  time.strftime("UpdateTime %Y-%m-%d  %H:%M:%S",time.localtime())
        '''print Time'''
        return Time
        
def getNum(cin ):
        return sum([ ord(n) * ( 256 ** p )  for (n ,p )  in zip( cin , range(4))]) 
    
def getServer():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send(dat )
        idat =  s.recv( 4096 )       
            
        if startr.search( idat ):
            '''m = startr.search( idat )           
            print 'Starting:%s' % (m.groups(1)[0])'''
            return -99
            
        else:        
            v = ord( idat[19] )
            if v == 4:
                cnt = getNum( idat[20:25] )
            elif v == 5:
                cnt = getNum(  idat[20:22])
            elif v == 6:
                cnt = getNum( idat[20])
            else:
                cnt = 0
                
            '''print 'EVE Server Online:%u' % ( cnt )'''
            return cnt
    except:
            '''return "Offline"'''
            return -1 

def createImage():
    img = Image.open(os.path.join("static", "server.png"))
    
    if getServer()==-1:
            player = str(0)
            stats = u"OFFLINE"
    elif getServer()==-99:
            player = str(0)
            stats = u"starting"
    else:
            player = str( getServer() )
            stats = u"ONLINE"
    
    
    
    ctime = unicode( getTime(),"utf-8") 
    
    
    '''print ctime'''
	

    
    imgdraw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype( os.path.join("static", "MT.ttf"), 28) 
    timefont = ImageFont.truetype( os.path.join("static", "MT.ttf"), 12) 
    signfont = ImageFont.truetype( os.path.join("static", "sign.ttf"),16)
    
    '''print img.format, img.size, img.mode'''
    
    imgdraw.text( (20,8),"Server",font=font,fill="#FFFFFF")
    
    imgdraw.text( (50, 40), stats, font=font, fill="#FFFFFF" )
    
    imgdraw.text( (420,8),"Player",font=font,fill="#FFFFFF")

    imgdraw.text( (470, 40), player, font=font, fill="#FFFFFF" )
    
    imgdraw.text( (20, 118), unicode("Mars CN"), font=signfont, fill="#FFFFFF" )
    
    imgdraw.text( (350, 118), ctime, font=timefont, fill="#FFFFFF" )
    
    '''
    img.show()
    '''
    '''img.save(os.path.join("static","output.png"))'''
    
    buff = StringIO.StringIO()
    
    img.save(buff,"png")
    '''buff.close()'''
    '''img.save("stats.png")'''
    return buff.getvalue()
    
