#Funimation - by The Highway 2013.


import urllib,urllib2,re,os,xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
#import stream_hulu as mHulu
#from stream_hulu import *
#from stream_hulu import main as mHulu


__settings__ = xbmcaddon.Addon(id='plugin.video.funimation')
##__language__ = __settings__.getLocalizedString
__home__ = __settings__.getAddonInfo('path')
#icon = xbmc.translatePath( os.path.join( __home__, 'icon.png' ) )
#__plugin__ = "Funimation"
#__authors__ = "The Highway"
#__credits__ = ""
#home = xbmc.translatePath(addon.getAddonInfo('path'))
ICON = os.path.join(__home__, 'icon.png')
ICON2 = os.path.join(__home__, 'icon2.png')
ICON3 = os.path.join(__home__, 'icon3.png')
ICON4 = os.path.join(__home__, 'icon4.png')
fanart = os.path.join(__home__, 'fanart.jpg')
fanart2 = os.path.join(__home__, 'fanart2.jpg')




def CATEGORIES():
#				#addDir(name,url,mode,icon)
        addDir('Anime Episodes','Episodes','http://www.funimation.com/',2,1,ICON2,fanart2)
        addDir('Anime Movies','Movies','http://www.funimation.com/',4,1,ICON3,fanart2)
#        addDir('Anime Clips','Clips','http://www.funimation.com/',5,1,ICON4,fanart2)
#        addDir('Anime Trailers','Trailers','http://www4.funimation.com/',6,1,ICON3,fanart2)
##        addDir('Shows','http://www.funimation.com/shows/',1)
##        addDir('','',1,'')
##        addDir( '','',1,'')
                       
def INDEX(url,type2):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<span class="field-content"><a href="(.+?)">(.+?)</a></span>').findall(link)
        for url2,name in match:
                addDir(name,name,'http://www.funimation.com' + url2,type2,type2,'',fanart2)
                #addDir(name,name,'http://www4.funimation.com' + url2,type2,type2,'',fanart2)


def VIDEOLINKS(url,name,name2,type2):
        req = urllib2.Request(url + '/episodes/')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        addDir('[Show]: ' + name +  '','','http://www4.funimation.com/',type2,1,ICON2,fanart2)
        addDir('______ Dubs: ',name2,'http://www4.funimation.com/',type2,1,ICON2,fanart2)
        #dubs
        match=re.compile('<a href="(.+?)" class="imagecache imagecache-81h_X_144w_typical_video_thumbnail imagecache-linked imagecache-81h_X_144w_typical_video_thumbnail_linked"><img src="(.+?)" alt=".+?" title=".+?" class="imagecache imagecache-81h_X_144w_typical_video_thumbnail" \D+="\d+" \D+="\d+"\D+</a\D+\s+<div class="video-box-words"\D+\s+<div class="show-name">(.+?)</div\D+\s+<a href=".+?" title=".+?"><span class="episode-no">(.+?)<span class="sub-dub">(.+?)</span\D+\s+<div class="title">(.+?)</div\D+\s+</span').findall(link)
        for url2,imgThumb,showname,episodetn,subdub,episodename in match:
                addDir(episodetn + ' (' + subdub + ') ' + '- ' + episodename,name2,'http://www4.funimation.com' + url2 + '',type2,3,imgThumb,fanart2)
        addDir('______ Subs: ',name2,'http://www4.funimation.com/',type2,1,ICON2,fanart2)
        #subs
        matcsh=re.compile('<a href="(.+?)" class="imagecache imagecache-81h_X_144w_typical_video_thumbnail imagecache-linked imagecache-81h_X_144w_typical_video_thumbnail_linked"><img src="(.+?)" alt="" title="" class="imagecache imagecache-81h_X_144w_typical_video_thumbnail" \D+="\d+" \D+="\d+"\D+</a\D+\s+<div class="video-box-words"\D+\s+<div class="show-name">(.+?)</div\D+\s+<a href=".+?" title=".+?"><span class="episode-no">(.+?)<span class="sub-dub">(.+?)</span\D+\s+<div class="title">(.+?)</div\D+\s+</span').findall(link)
        for url2,imgThumb,showname,episodetn,subdub,episodename in matcsh:
                addDir(episodetn + ' (' + subdub + ') ' + '- ' + episodename,name2,'http://www4.funimation.com' + url2 + '',type2,3,imgThumb,fanart2)
        addDir('______ Pages: ',name2,'http://www4.funimation.com/',type2,1,ICON2,fanart2)
        #pages
        matcch=re.compile('<li class="pager-item \D+"\D+<a href="(.+?)" title="Go to .+?" class="active">(.+?)</a></li>').findall(link)
        for url3,pgName in matcch:
                addDir(name2 + ' - [Page]: ' + pgName,name2,'http://www4.funimation.com' + url3,type2,2,'',fanart2)
       

def VIDEOLINKSmovies(url,name,name2,type2):
        req = urllib2.Request(url + '/videos/')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        addDir('[Show]: ' + name +  '','','http://www4.funimation.com/',type2,1,ICON3,fanart2)
        addDir('______ Movies: ',name2,'http://www4.funimation.com/',type2,1,ICON3,fanart2)
        match=re.compile('<a href="(.+?)" title=".+?"\D+\s+<img src="(.+?)" alt="" title="" class=".+?" \D+="\d+" \D+="\d+"\D+\s+<div class="not-exclusive"\D+</div\D+\s+<div class="(.+?)"\D+</div\D+\s+</a\D+\s+<div class="video-box-words clearfix"\D+\s+<div class="show-name">(.+?)</div\D+\s+<div class="clip-type"\D+\s+<a href="(.+?)" title=".+?">(.+?)<span>(.+?)</span\D+<span class="clip-name">(.+?)</span').findall(link)
        for url2,imgThumb,subdub,showName,urlB,nameA,nameB,nameC in match:
                addDir(nameA + '' + nameB + ' - ' + nameC,name2,'http://www4.funimation.com' + url2 + '',type2,3,imgThumb,fanart2)
        #pages
        matcch=re.compile('<li class="pager-item \D+"\D+<a href="(.+?)" title="Go to .+?" class="active">(.+?)</a></li>').findall(link)
        for url3,pgName in matcch:
                addDir(name2 + ' - [Page]: ' + pgName,name2,'http://www4.funimation.com' + url3,type2,type2,'',fanart2)


def GETLINKS(url,name,name2,type2):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        #match=re.compile('<a href="(.+?)" class="imagecache imagecache-81h_X_144w_typical_video_thumbnail imagecache-linked imagecache-81h_X_144w_typical_video_thumbnail_linked"><img src="(.+?)" alt="" title="" class="(\d+)" height="81" width="144"></a>').findall(link)
        #for url,imgThumb in match:
        #	addLink(url,'http://www.funimation.com' + url,'')
        #
        vid_id=re.compile('NewSite.videoPlayerComponent.playVideo( "(.+?)" );').findall(link)[0]
        #vid_w,vid_h=re.compile('NewSite.videoPlayerComponent.setSize( "(.+?)","(.+?)" );').findall(link)[0]
        import stream_hulu as mHulu
        mHulu.doit(video_id=vid_id)
        #mHulu.play(vid_id)
        #
        #
#        match=re.compile('<a href="(.+?)" class="imagecache imagecache-81h_X_144w_typical_video_thumbnail imagecache-linked imagecache-81h_X_144w_typical_video_thumbnail_linked"><img src="(.+?)" alt="" title="" class="imagecache .+?" height="81" width="144"></a>\s<div class="video-box-words">\s<div class="show-name">(.+?)</div>\s<a href=".+?" title=".+?"><span class="episode-no">(.+?)<span class="sub-dub">(.+?)</span>\s<div class="title">(.+?)</div>\s</span>').findall(link)
#        for url,imgThumb,showname,episodetn,subdub,episodename in match:
#                addLink(showname + '(' + subdub + '): ' + episodetn + ' - ' + episodename,'','http://www4.funimation.com' + url,imgThumb)
### <script src="http://config.hulu.com/js/hulu_global.js?guid=0B1CEA04-DCCB-40cf-AD0E-5222EF66D519&partner=Funimation" id="NS_GUID_JS" type="text/javascript"></script>
### var HuluPlayer = {
### 	readyHandler: function() {
### 		NewSite.videoPlayerComponent.setSize( "980","465" );
### 		NewSite.videoPlayerComponent.playVideo( "50040810" );
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 


                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param




def addLink(name,url,iconimage=ICON):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,name2,url,type2,mode,iconimage=ICON,fanimage=fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&nm="+urllib.quote_plus(name2)+"&tp="+str(type2)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanimage )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
params=get_params()
url=None
name=None
name2=None
type2=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        name2=urllib.unquote_plus(params["nm"])
except:
        pass
try:
        type2=int(params["tp"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Name2: "+str(name2)
print "Type2: "+str(type2)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        INDEX(url,type2)
        
elif mode==2:
        print ""+url
        VIDEOLINKS(url,name,name2,type2)

elif mode==3:
        print ""+url
        GETLINKS(url,name,name2,type2)

elif mode==4:
        print ""+url
        VIDEOLINKSmovies(url,name,name2,type2)

elif mode==5:
        print ""+url
        VIDEOLINKSclips(url,name,name2,type2)

elif mode==6:
        print ""+url
        VIDEOLINKStrailers(url,name,name2,type2)




xbmcplugin.endOfDirectory(int(sys.argv[1]))
