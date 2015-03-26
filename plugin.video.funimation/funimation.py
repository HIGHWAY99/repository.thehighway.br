#Funimation - by The Highway 2013.

import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
#import requests ### (Removed in v0.2.1b to fix scripterror on load on Mac OS.) ### 
try: import requests ### <import addon="script.module.requests" version="1.1.0"/> ### 
except: t=''				 ### See https://github.com/kennethreitz/requests ### 
import urllib,urllib2,re,os,sys,htmllib,string,StringIO,logging,random,array,time,datetime
import urlresolver
import copy
###
#import cookielib
#import base64
#import threading
###
#import unicodedata ### I don't want to use unless I absolutely have to. ### 
#import zipfile ### Removed because it caused videos to not play. ### 
import HTMLParser, htmlentitydefs
try: 		import StorageServer
except: import storageserverdummy as StorageServer
try: 		from t0mm0.common.addon 				import Addon
except: from t0mm0_common_addon 				import Addon
try: 		from t0mm0.common.net 					import Net
except: from t0mm0_common_net 					import Net
try: 		from sqlite3 										import dbapi2 as sqlite; print "Loading sqlite3 as DB engine"
except: from pysqlite2 									import dbapi2 as sqlite; print "Loading pysqlite2 as DB engine"
try: 		from script.module.metahandler 	import metahandlers
except: from metahandler 								import metahandlers
### 
from teh_tools 		import *
from config 			import *


#import stream_hulu as mHulu
#from stream_hulu import *
#from stream_hulu import main as mHulu

##### /\ ##### Imports #####
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
__plugin__=ps('__plugin__'); __authors__=ps('__authors__'); __credits__=ps('__credits__'); _addon_id=ps('_addon_id'); _domain_url=ps('_domain_url'); _database_name=ps('_database_name'); _plugin_id=ps('_addon_id')
_database_file=os.path.join(xbmc.translatePath("special://database"),ps('_database_name')+'.db'); 
### 
_addon=Addon(ps('_addon_id'), sys.argv); addon=_addon; _plugin=xbmcaddon.Addon(id=ps('_addon_id')); cache=StorageServer.StorageServer(ps('_addon_id'))
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
##### Paths #####
### # ps('')
_addonPath	=xbmc.translatePath(_plugin.getAddonInfo('path'))
_artPath		=xbmc.translatePath(os.path.join(_addonPath,ps('_addon_path_art')))
_datapath 	=xbmc.translatePath(_addon.get_profile()); _artIcon		=_addon.get_icon(); _artFanart	=_addon.get_fanart()
##### /\ ##### Paths #####
##### Important Functions with some dependencies #####
def art(f,fe=ps('default_art_ext')): return xbmc.translatePath(os.path.join(_artPath,f+fe)) ### for Making path+filename+ext data for Art Images. ###
def artMF(f,fe=ps('default_art_ext')): return xbmc.translatePath(os.path.join(_addonPath,f+fe)) ### 
##### /\ ##### Important Functions with some dependencies #####
##### Settings #####
_setting={}; _setting['enableMeta']	=	_enableMeta			=tfalse(addst("enableMeta"))
_setting['debug-enable']=	_debugging			=tfalse(addst("debug-enable")); _setting['debug-show']	=	_shoDebugging		=tfalse(addst("debug-show"))
_setting['meta.movie.domain']=ps('meta.movie.domain'); _setting['meta.movie.search']=ps('meta.movie.search')
_setting['meta.tv.domain']   =ps('meta.tv.domain');    _setting['meta.tv.search']   =ps('meta.tv.search')
_setting['meta.tv.page']=ps('meta.tv.page'); _setting['meta.tv.fanart.url']=ps('meta.tv.fanart.url'); _setting['meta.tv.fanart.url2']=ps('meta.tv.fanart.url2'); _setting['label-empty-favorites']=tfalse(addst('label-empty-favorites'))
CurrentPercent=0; CancelDownload=False
##### /\ ##### Settings #####
##### Variables #####
ICON=  ['',artMF('icon','.png'),artMF('icon2','.png'),artMF('icon3','.png'),artMF('icon4','.png')]
fanart=['',artMF('fanart','.jpg'),artMF('fanart2','.jpg')]

_default_section_=ps('default_section'); net=Net(); DB=_database_file; BASE_URL=_domain_url;
##### /\ ##### Variables #####
deb('Addon Path',_addonPath);  deb('Art Path',_artPath); deb('Addon Icon Path',_artIcon); deb('Addon Fanart Path',_artFanart)
### ############################################################################################################
def eod(): _addon.end_of_directory()
def messupText(t,_html=False,_ende=False,_a=False,Slashes=False):
	if (_html==True): t=ParseDescription(HTMLParser.HTMLParser().unescape(t))
	if (_ende==True): t=t.encode('ascii', 'ignore'); t=t.decode('iso-8859-1')
	if (_a==True): t=_addon.decode(t); t=_addon.unescape(t)
	if (Slashes==True): t=t.replace( '_',' ')
	return t
def name2path(name):  return (((name.lower()).replace('.','-')).replace(' ','-')).replace('--','-')
def name2pathU(name): return (((name.replace(' and ','-')).replace('.','-')).replace(' ','-')).replace('--','-')
### ############################################################################################################
### ############################################################################################################
##### Queries #####
_param={}
_param['mode']=addpr('mode',''); _param['url']=addpr('url',''); _param['pagesource'],_param['pageurl'],_param['pageno'],_param['pagecount']=addpr('pagesource',''),addpr('pageurl',''),addpr('pageno',0),addpr('pagecount',1)
_param['img']=addpr('img',''); _param['fanart']=addpr('fanart',''); _param['thumbnail'],_param['thumbnail'],_param['thumbnail']=addpr('thumbnail',''),addpr('thumbnailshow',''),addpr('thumbnailepisode','')
_param['section']=addpr('section','movies'); _param['title']=addpr('title',''); _param['year']=addpr('year',''); _param['genre']=addpr('genre','')
_param['by']=addpr('by',''); _param['letter']=addpr('letter',''); _param['showtitle']=addpr('showtitle',''); _param['showyear']=addpr('showyear',''); _param['listitem']=addpr('listitem',''); _param['infoLabels']=addpr('infoLabels',''); _param['season']=addpr('season',''); _param['episode']=addpr('episode','')
_param['pars']=addpr('pars',''); _param['labs']=addpr('labs',''); _param['name']=addpr('name',''); _param['thetvdbid']=addpr('thetvdbid','')
_param['plot']=addpr('plot',''); _param['tomode']=addpr('tomode',''); _param['country']=addpr('country','')
_param['thetvdb_series_id']=addpr('thetvdb_series_id',''); _param['dbid']=addpr('dbid',''); _param['user']=addpr('user','')
_param['subfav']=addpr('subfav',''); _param['episodetitle']=addpr('episodetitle',''); _param['special']=addpr('special',''); _param['studio']=addpr('studio','')

#_param['']=_addon.queries.get('','')
#_param['']=_addon.queries.get('','')
##_param['pagestart']=addpr('pagestart',0)
##### /\
### ############################################################################################################
### ############################################################################################################




### ############################################################################################################
### ############################################################################################################
### ############################################################################################################











### ############################################################################################################




#def CATEGORIES():
###				#addDir(name,url,mode,icon)
#        addDir('Anime Episodes','Episodes','http://www.funimation.com/',2,1,ICON2,fanart2)
#        addDir('Anime Movies','Movies','http://www.funimation.com/',4,1,ICON3,fanart2)
###        addDir('Anime Clips','Clips','http://www.funimation.com/',5,1,ICON4,fanart2)
###        addDir('Anime Trailers','Trailers','http://www4.funimation.com/',6,1,ICON3,fanart2)
####        addDir('Shows','http://www.funimation.com/shows/',1)
####        addDir('','',1,'')
####        addDir( '','',1,'')
                       
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


                
#def get_params():
#        param=[]
#        paramstring=sys.argv[2]
#        if len(paramstring)>=2:
#                params=sys.argv[2]
#                cleanedparams=params.replace('?','')
#                if (params[len(params)-1]=='/'):
#                        params=params[0:len(params)-2]
#                pairsofparams=cleanedparams.split('&')
#                param={}
#                for i in range(len(pairsofparams)):
#                        splitparams={}
#                        splitparams=pairsofparams[i].split('=')
#                        if (len(splitparams))==2:
#                                param[splitparams[0]]=splitparams[1]
#                                
#        return param
#
#
#def addLink(name,url,iconimage=ICON):
#        ok=True
#        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
#        liz.setInfo( type="Video", infoLabels={ "Title": name } )
#        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
#        return ok
#
#
#def addDir(name,name2,url,type2,mode,iconimage=ICON,fanimage=fanart):
#        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&nm="+urllib.quote_plus(name2)+"&tp="+str(type2)
#        ok=True
#        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
#        liz.setInfo( type="Video", infoLabels={ "Title": name } )
#        liz.setProperty( "Fanart_Image", fanimage )
#        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
#        return ok
#
#             
#params=get_params()
#url=None
#name=None
#name2=None
#type2=None
#mode=None
#
#try:
#        url=urllib.unquote_plus(params["url"])
#except:
#        pass
#try:
#        name=urllib.unquote_plus(params["name"])
#except:
#        pass
#try:
#        name2=urllib.unquote_plus(params["nm"])
#except:
#        pass
#try:
#        type2=int(params["tp"])
#except:
#        pass
#try:
#        mode=int(params["mode"])
#except:
#        pass
#
#print "Mode: "+str(mode)
#print "URL: "+str(url)
#print "Name: "+str(name)
#print "Name2: "+str(name2)
#print "Type2: "+str(type2)
#if mode==None or url==None or len(url)<1:
#        print ""
#        CATEGORIES()
#elif mode==1:
#        print ""+url
#        INDEX(url,type2)
#elif mode==2:
#        print ""+url
#        VIDEOLINKS(url,name,name2,type2)
#elif mode==3:
#        print ""+url
#        GETLINKS(url,name,name2,type2)
#elif mode==4:
#        print ""+url
#        VIDEOLINKSmovies(url,name,name2,type2)
#elif mode==5:
#        print ""+url
#        VIDEOLINKSclips(url,name,name2,type2)
#elif mode==6:
#        print ""+url
#        VIDEOLINKStrailers(url,name,name2,type2)


### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
def getHTML(url):
	try:		return net.http_GET(url).content
	except:	return ''

def FindPlayer(url,title):
	html=getHTML(url)
	try:		guID=re.compile('<script src="http://config.hulu.com/js/hulu_global.js\?guid=([0-9A-Za-z\-]+)&partner=\D+"').findall(html)[0]
	except:	guID=''
	#try:		partner=re.compile('<script src="http://config.hulu.com/js/hulu_global.js\?guid=[0-9A-Za-z\-]+&partner=(\D+)"').findall(html)[0]
	#except:	partner=''
	partner='Funimation'
	try:		urlID=re.compile('NewSite.videoPlayerComponent.playVideo\(\s*"(\d+)"\s*\)').findall(html)[0]
	except:	urlID=''
	#try:		shows=re.compile('').findall(html)[0]
	#except:	shows=''
	if (urlID is not ''):
		#import xbmc.translatePath(os.path.join('special://home/addons/plugin.video.hulu/resources/lib/','stream_hulu')) as mHulu
		##try: from plugin.video.hulu import stream_hulu as mHulu
		##except: import stream_hulu as mHulu
		import stream_hulu as mHulu
		#mHulu.doit(video_id=vidID)
		#mHulu.play(vidID)
		#vidURL=urllib.quote_plus('http://www.hulu.com/watch/'+vidID+'')
		vidID=urlID
		vidURL=vidID
		#
		#eID=mHulu.cid2eid(guID)
		eID=guID
		deb('title',title)
		deb('page url',url)
		deb('guID',guID)
		#deb('vidID',vidID)
		deb('urlID',urlID)
		deb('eID',eID)
		### Example of what is needed: ['plugin://plugin.video.hulu/', '200', '?url="50110811"&mode="TV_play"&videoid="203921"&eid="Pgm5LA9Q85WaP2aODW2IRg"']
		xbmc.executebuiltin("XBMC.RunPlugin(plugin://plugin.video.hulu/?url=%s&mode=%s&videoid=%s&eid=%s&guid=%s)" % (urlID,'TV_play',vidID,eID,guID) )
	#
	#special://home/addons/plugin.video.
	#
	set_view('list',addst('default-view')); eod()

def Menu_ShowPage_Episodes(url):
	url=url+'/episodes'; shows2=[]; html=getHTML(url)
	### /episodes?page=3" title="Go to last page" class="active">last 
	try:		lastpage=int(re.compile('/episodes\?page=(\d+)" title="Go to last page" class="active">last').findall(html)[0])
	except:	lastpage=1
	deb('Last Page No',str(lastpage))
	if (lastpage > 1):
		for pn in range(1,(lastpage),1):
			html+=getHTML(url+'?page='+str(pn))
	s ='<a\shref="(/[0-9A-Za-z\-\_]+/episode/[0-9A-Za-z\-\_]+/\D\D\D)"\sclass=".+?"><img\ssrc="(http://www.funimation.com/sites/default/files/imagecache/81h_X_144w_typical_video_thumbnail/.+?.jpg)"\salt=".*?"\stitle=".*?"\sclass=".+?"/></a>[\n]'
	s+='<div class="video-box-words">[\n]'
	s+='<div class="show-name">(.+?)</div>[\n]'
	s+='<a href="/[0-9A-Za-z\-\_]+/episode/[0-9A-Za-z\-\_]+/\D\D\D" title=".*?"><span class="episode-no">Episode\s-\s(\d+)\s-\s<span class="sub-dub">(\D+)</span>[\n]'
	s+='<div class="title">(.*?)</div>'
	try:		shows=re.compile(s).findall(html)
	except:	shows=''
	if (shows is not ''):
		for path,img,show_name,epi_no,subdub,epi_title in shows:
			if (len(epi_no)==1):	shows2.append((path,img,show_name,'0'+epi_no,subdub,epi_title))
			else:									shows2.append((path,img,show_name,epi_no,subdub,epi_title))
		shows2=sorted(shows2, key=lambda item: item[3], reverse=True)
		shows2=sorted(shows2, key=lambda item: item[4], reverse=False)
		#print shows2
		for path,img,show_name,epi_no,subdub,epi_title in shows2:
			path=_domain_url+path; labs={}; fan=fanart[1]
			#if (len(epi_no)==1): epi_no='0'+epi_no
			labs['title'] =cFL('['+cFL(subdub,ps('cFL_color'))+']',ps('cFL_color2'))+'  '
			labs['title']+=cFL(show_name[0:1],ps('cFL_color'))+show_name[1:]
			labs['title']+=' - [E'
			labs['title']+=cFL(epi_no,ps('cFL_color2'))
			labs['title']+='] - '
			labs['title']+=cFL(epi_title[0:1],ps('cFL_color'))+epi_title[1:]
			labs['title']+=''
			labs['title'] =cFL(labs['title'],ps('cFL_color3'))
			_addon.add_directory({'mode': 'FindPlayer','title': show_name, 'url': path},labs,img=img, is_folder=False ,fanart=fan)

def Menu_ShowPage_Movies(url):
	url=url+'/videos'
	html=getHTML(url)
	s ='<a href="(/[0-9A-Za-z\-\_]+/movie/[0-9A-Za-z\-\_]+/\D\D\D)" title=".*?">[\n]'
	s+='<img src="(http://www.funimation.com/sites/default/files/imagecache/81h_X_144w_typical_video_thumbnail/.*?.jpg)" alt=".*?" title=".*?" class=".+?" width="144" height="81"/>[\n]<div class="not-exclusive"></div>[\n]'
	s+='<div class="\D\D\D"></div>[\n]</a>[\n]<div class="video-box-words clearfix">[\n]'
	s+='<div class="show-name">(.+?)</div>[\n]<div class="clip-type">[\n]'
	s+='<a href="/[0-9A-Za-z\-\_]+/movie/[0-9A-Za-z\-\_]+/\D\D\D" title=".*?">movie - <span>(\D\D\D)</span> - <span class="clip-name">(.+?)</span></a>'
	try:		shows=re.compile(s).findall(html)
	except:	shows=''
	if (shows is not ''):
		#shows=sorted(shows, key=lambda item: item[3], reverse=True)
		shows=sorted(shows, key=lambda item: item[3], reverse=False)
		print shows
		for path,img,show_name,subdub,epi_title in shows:
			path=_domain_url+path; labs={}; fan=fanart[1]
			labs['title'] =cFL('['+cFL(subdub,ps('cFL_color'))+']',ps('cFL_color2'))+'  '
			labs['title']+=cFL(show_name[0:1],ps('cFL_color'))+show_name[1:]
			labs['title']+=' - ['
			labs['title']+=cFL('Movie',ps('cFL_color2'))
			labs['title']+='] - '
			labs['title']+=cFL(epi_title[0:1],ps('cFL_color'))+epi_title[1:]
			labs['title']+=''
			labs['title'] =cFL(labs['title'],ps('cFL_color3'))
			_addon.add_directory({'mode': 'FindPlayer','title': show_name, 'url': path},labs,img=img, is_folder=False ,fanart=fan)

def Menu_ShowPage_Clips(url):
	url=url+'/videos'
	html=getHTML(url)
	s ='<a href="(/[0-9A-Za-z\-\_]+/clip/[0-9A-Za-z\-\_]+/[0-9A-Za-z\-\_]+)" class=".*?"><img src="(http://www.funimation.com/sites/default/files/imagecache/81h_X_144w_typical_video_thumbnail/.+?.jpg)" alt=".*?" title=".*?" class=".*?" width="144" height="81"/></a>[\n]'
	s+='<div class="show-name">(.+?)</div>[\n]'
	s+='<div class="clip-type">[\n]'
	s+='<a href="/[0-9A-Za-z\-\_]+/clip/[0-9A-Za-z\-\_]+/[0-9A-Za-z\-\_]+" title=".*?">Video: (\D+) - <span class="clip-name">(.+?)</span></a>'
	try:		shows=re.compile(s).findall(html)
	except:	shows=''
	if (shows is not ''):
		#shows=sorted(shows, key=lambda item: item[3], reverse=True)
		shows=sorted(shows, key=lambda item: item[4], reverse=False)
		print shows
		for path,img,show_name,subdub,epi_title in shows:
			path=_domain_url+path; labs={}; fan=fanart[1]
			labs['title'] =cFL('['+cFL('Video',ps('cFL_color'))+']',ps('cFL_color2'))+'  '
			labs['title']+=cFL(show_name[0:1],ps('cFL_color'))+show_name[1:]
			labs['title']+=' - ['
			labs['title']+=cFL(subdub,ps('cFL_color2'))
			labs['title']+='] - '
			labs['title']+=cFL(epi_title[0:1],ps('cFL_color'))+epi_title[1:]
			labs['title']+=''
			labs['title'] =cFL(labs['title'],ps('cFL_color3'))
			_addon.add_directory({'mode': 'FindPlayer','title': show_name, 'url': path},labs,img=img, is_folder=False ,fanart=fan)

def Menu_ShowPage_Trailers(url):
	url=url+'/videos'
	html=getHTML(url)
	s ='<a href="(/[0-9A-Za-z\-\_]+/trailer/[0-9A-Za-z\-\_]+/[0-9A-Za-z\-\_]+)" class=".*?"><img src="(http://www.funimation.com/sites/default/files/imagecache/81h_X_144w_typical_video_thumbnail/.+?.jpg)" alt=".*?" title=".*?" class=".*?" width="144" height="81"/></a>[\n]'
	s+='<div class="show-name">(.+?)</div>[\n]'
	s+='<div class="clip-type">[\n]'
	s+='<a href="/[0-9A-Za-z\-\_]+/trailer/[0-9A-Za-z\-\_]+/[0-9A-Za-z\-\_]+" title=".*?">(\D+) - <span></span> - <span class="clip-name">(.+?)</span></a>'
	try:		shows=re.compile(s).findall(html)
	except:	shows=''
	if (shows is not ''):
		#shows=sorted(shows, key=lambda item: item[3], reverse=True)
		shows=sorted(shows, key=lambda item: item[4], reverse=False)
		print shows
		for path,img,show_name,subdub,epi_title in shows:
			path=_domain_url+path; labs={}; fan=fanart[1]
			labs['title'] =cFL('['+cFL('Video',ps('cFL_color'))+']',ps('cFL_color2'))+'  '
			labs['title']+=cFL(show_name[0:1],ps('cFL_color'))+show_name[1:]
			labs['title']+=' - ['
			labs['title']+=cFL(subdub,ps('cFL_color2'))
			labs['title']+='] - '
			labs['title']+=cFL(epi_title[0:1],ps('cFL_color'))+epi_title[1:]
			labs['title']+=''
			labs['title'] =cFL(labs['title'],ps('cFL_color3'))
			_addon.add_directory({'mode': 'FindPlayer','title': show_name, 'url': path},labs,img=img, is_folder=False ,fanart=fan)


def Menu_ShowPage(url):
	pages=['/episodes','/movies','/clips','/trailers']
	### http://www.funimation.com/ai-yori-aoshi/
	### http://www.funimation.com/ai-yori-aoshi/episodes
	### http://www.funimation.com/ai-yori-aoshi/movies
	### http://www.funimation.com/ai-yori-aoshi/clips
	### http://www.funimation.com/ai-yori-aoshi/trailers
	### http://www.funimation.com/videos/simulcast
	### 
	### [u'rtmpe://cp39466.edgefcs.net/ondemand', u'mp4:hulu12/811/50110811/agave50110811_4168324_H264_650.mp4', u'auth=daEa1acdkcYb_cibvaNdycxa7dhacd0bgdt-bsfdYg-c0-ZnHErEnZDzu&aifp=sll02152008&slist=hulu12/811/50110811;.international=false&hgt=OZU7Pvs7j27-nhteNno7wnNUzbLXHjC_QJ6yfTlCNv74NGd97lQc_ww0vCqlyoh9Ml_p6pjN1GAJQOhMJgLDCO9bWRjQpTuoTbP6K4bcjqjCDg92zsQANnujhZwN41udY7JMUjOfhelPfJxlicQhUoWzCpLvepG25PC7XFIFeLjd6Ecd0HnXcPtuHZM-G70qibygXXLE6usqkj7CGwJm2fLr5zxosAeTSH-WaMi7eWAOcQvxJajMeOWIDx-PY2Ji&hgt_ver=331370278']
	### ['plugin://plugin.video.hulu/', '135', '?url="50110811"&mode="TV_play"&videoid="203921"&eid="Pgm5LA9Q85WaP2aODW2IRg"']
	### 
	### 
	### 
	Menu_ShowPage_Episodes(url)
	Menu_ShowPage_Movies(url)
	Menu_ShowPage_Clips(url)
	Menu_ShowPage_Trailers(url)
	#for page in pages:
	#	html=getHTML(url+page)
	#	s='<td class="col-\d+\s*\D*">[\n]<div class="views-field-markup-\d+">[\n]<span class="field-content"><div class="video-box  clearfix">[\n]'
	#	s+='<a href="(/.+?)" title="(.+?)">[\n]'
	#	s+='<div class="not-exclusive">.+?</div>[\n]'
	#	s+='<div class="(.+?)">.+?</div>[\n]</a>[\n]'
	#	s+='<div class="video-box-thumb"><img src="(http://www\.funimation\.com/sites/default/files/imagecache/81h_X_144w_typical_video_thumbnail/[0-9A-Za-z\_\-]+\.jpg)" alt="" title="" class="imagecache imagecache-81h_X_144w_typical_video_thumbnail imagecache-default imagecache-81h_X_144w_typical_video_thumbnail_default" width="144" height="81"/></div>[\n]'
	#	s+='<div class="video-box-words clearfix">[\n]'
	#	s+='<div class="show-name">(.+?)</div>[\n]'
	#	s+='<a href="/.+?" title=".+?"><span class="episode-no">Episode - 1 - <span class="sub-dub">Sub</span>[\n]'
	#	s+='<div class="title">Oneday</div>[\n]'
	#	s+='</span></a>[\n]</div>\s*[\n]</div>\s*</span>[\n]</div>[\n]</td>'
	#	try:		shows=re.compile(s).findall(html)
	#	except:	shows=''
	#	if (shows is not ''):
	#		print shows
	#		#for path,epi_title,videotype,image,show_name in shows:
	#
	set_view('list',addst('default-view')); eod()

def Menu_ShowList(url=_domain_url):
	html=getHTML(url)
	#html=net.http_GET(url).content
	#print html
	try:		shows=re.compile('<span class="field-content"><a href="(/[0-9A-Za-z\-]+)">(.+?)</a></span>').findall(html)
	except:	shows=''
	if (shows is not ''):
		print shows
		for show_url,show_name in shows:
			show_url=_domain_url+show_url
			#addDir(name,name,'http://www.funimation.com' + url2,type2,type2,'',fanart2)#addDir(name,name,'http://www4.funimation.com' + url2,type2,type2,'',fanart2)
			labs={}; img=ICON[1]; fan=fanart[1]
			labs['title'] =cFL(show_name[0:1],ps('cFL_color'))
			labs['title']+=show_name[1:]
			labs['title'] =cFL(labs['title'],ps('cFL_color3'))
			_addon.add_directory({'mode': 'GetShowPage','title': show_name, 'url': show_url},labs,img=img, is_folder=True ,fanart=fan)
	set_view('list',addst('default-view')); eod()

def Menu_MainMenu():
	_addon.add_directory({'mode': 'GetShowList','title': "", 'url': ''},{'title': cFL('S',ps('cFL_color'))+'how List'},img=ICON[1], is_folder=True ,fanart=fanart[1])
	_addon.add_directory({'mode': 'Settings'},{'title':  cFL('P',ps('cFL_color'))+'lugin Settings'},is_folder=False,img=ICON[1],fanart=fanart[1])
	set_view('list',addst('default-view')); eod()
	#
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
##### Modes #####
def check_mode(mode=''):
	deb('Mode',mode)
	if (mode=='') or (mode=='main') or (mode=='MainMenu'): Menu_MainMenu()
	elif (mode=='GetShowList'): 					Menu_ShowList()
	elif (mode=='GetShowPage'): 					Menu_ShowPage(_param['url'])
	elif (mode=='FindPlayer'): 						FindPlayer(_param['url'],_param['title'])
	#elif (mode=='PlayVideo'): 						PlayVideo(_param['url'], _param['infoLabels'], _param['listitem'])
	#elif (mode=='PlayTrailer'): 					PlayTrailer(_param['url'], _param['title'], _param['year'], _param['img'])
	#elif (mode=='Settings'): 							_addon.addon.openSettings() #_plugin.openSettings()
	#elif (mode=='ResolverSettings'): 			urlresolver.display_settings()
	#elif (mode=='LoadCategories'): 				Menu_LoadCategories(_param['section'])
	##elif (mode=='BrowseAtoZ'): 					BrowseAtoZ(_param['section'])
	#elif (mode=='BrowseYear'): 						Menu_BrowseByYear(_param['section'])
	#elif (mode=='BrowseGenre'): 					Menu_BrowseByGenre(_param['section'])
	#elif (mode=='BrowseCountry'): 				Menu_BrowseByCountry(_param['section'])
	#elif (mode=='BrowseLatest'): 				BrowseLatest(_param['section'])
	#elif (mode=='BrowsePopular'): 				BrowsePopular(_param['section'])
	#elif (mode=='GetResults'): 					GetResults(_param['section'], genre, letter, page)
	#elif (mode=='GetTitles'): 						listItems(_param['section'], _param['url'], _param['pageno'], _param['pagecount'], _param['genre'], _param['year'], _param['title'])
	#elif (mode=='GetTitlesLatest'): 			listItems(_param['section'], _param['url'], _param['pageno'], _param['pagecount'], _param['genre'], _param['year'], _param['title'], chck=ps('LI.tv.latest.check'))
	#elif (mode=='GetTitlesLatestWatched'): listItems(_param['section'],_param['url'], _param['pageno'], _param['pagecount'], _param['genre'], _param['year'], _param['title'], chck=ps('LI.tv.latest.watched.check'))
	#elif (mode=='GetTitlesPopular'): 			listItems(_param['section'], _param['url'], _param['pageno'], _param['pagecount'], _param['genre'], _param['year'], _param['title'], chck=ps('LI.tv.popular.all.check'))
	#elif (mode=='GetTitlesHDPopular'): 		listItems(_param['section'], _param['url'], _param['pageno'], _param['pagecount'], _param['genre'], _param['year'], _param['title'], chck=ps('LI.movies.popular.hd.check'))
	#elif (mode=='GetTitlesOtherPopular'): listItems(_param['section'], _param['url'], _param['pageno'], _param['pagecount'], _param['genre'], _param['year'], _param['title'], chck=ps('LI.movies.popular.other.check'))
	#elif (mode=='GetTitlesNewPopular'): 	listItems(_param['section'], _param['url'], _param['pageno'], _param['pagecount'], _param['genre'], _param['year'], _param['title'], chck=ps('LI.movies.popular.new.check'))
	#elif (mode=='GetLinks'): 							listLinks(_param['section'], _param['url'], showtitle=_param['showtitle'], showyear=_param['showyear'])
	#elif (mode=='GetSeasons'): 						listSeasons(_param['section'], _param['url'], _param['img'])
	#elif (mode=='GetEpisodes'): 					listEpisodes(_param['section'], _param['url'], _param['img'], _param['season'])
	#elif (mode=='TextBoxFile'): 					TextBox2().load_file(_param['url'],_param['title']); eod()
	#elif (mode=='TextBoxUrl'):  					TextBox2().load_url( _param['url'],_param['title']); eod()
	#elif (mode=='SearchForAirDates'):  		search_for_airdates(_param['title']); eod()
	#elif (mode=='Search'):  							doSearchNormal(_param['section'],_param['title'])
	#elif (mode=='AdvancedSearch'):  			doSearchAdvanced(_param['section'],_param['title'])
	#elif (mode=='FavoritesList'):  		  	fav__list(_param['section'],_param['subfav'])
	#elif (mode=='FavoritesEmpty'):  	 		fav__empty(_param['section'],_param['subfav'])
	#elif (mode=='FavoritesRemove'):  			fav__remove(_param['section'],_param['title'],_param['year'],_param['subfav'])
	#elif (mode=='FavoritesAdd'):  		  	fav__add(_param['section'],_param['title'],_param['year'],_param['img'],_param['fanart'],_param['subfav'])
	#elif (mode=='sunNote'):  		   				sunNote( header=_param['title'],msg=_param['plot'])
	#elif (mode=='deadNote'):  		   			deadNote(header=_param['title'],msg=_param['plot'])
	#elif (mode=='LibrarySaveMovie'):  		Library_SaveTo_Movies(_param['url'],_param['img'],_param['showtitle'],_param['showyear'])
	#elif (mode=='LibrarySaveTV'):  				Library_SaveTo_TV(_param['section'], _param['url'],_param['img'],_param['showtitle'],_param['showyear'],_param['country'],_param['season'],_param['episode'],_param['episodetitle'])
	#elif (mode=='LibrarySaveEpisode'):  	Library_SaveTo_Episode(_param['url'],_param['img'],_param['title'],_param['showyear'],_param['country'],_param['season'],_param['episode'],_param['episodetitle'])
	#elif (mode=='PlayLibrary'): 					PlayLibrary(_param['section'], _param['url'], showtitle=_param['showtitle'], showyear=_param['showyear'])
	#elif (mode=='Download'): 							print _param; DownloadRequest(_param['section'], _param['url'],_param['img'],_param['studio']); eod()
	#elif (mode=='DownloadStop'): 					DownloadStop(); eod()
	#elif (mode=='TrailersGenres'): 				Trailers_Genres(_param['section'], _param['url'])
	#elif (mode=='TrailersList'): 					Trailers_List(_param['section'], _param['url'], _param['genre'])
	#elif (mode=='LatestThreads'): 				News_LatestThreads(_param['url'],_param['title'])
	#elif (mode=='listUsers'): 						UsersList(_param['section'],_param['url'])
	#elif (mode=='UsersChooseSection'): 		UsersChooseSection(_param['section'],_param['url'])
	#elif (mode=='UsersShowFavorites'): 		UsersShowFavorites(_param['section'],_param['url'])
	#elif (mode=='UsersShowWatchList'): 		UsersShowWatchList(_param['section'],_param['url'])
	#elif (mode=='UsersShowUploads'): 			UsersShowUploads(_param['section'],_param['url'])
	#elif (mode=='PrivacyPolicy'): 				Site__PrivacyPolicy()
	#elif (mode=='TermsOfService'): 				Site__TermsOfService()
	#elif (mode=='GetLatestSearches'): 		listLatestSearches(_param['section'],_param['url'])
	#elif (mode=='UsersShowProfileAccountInfo'): UsersShowPersonInfo(mode, _param['section'],_param['url'])
	else: myNote(header='Mode:  "'+mode+'"',msg='[ mode ] not found.'); initDatabase(); Menu_MainMenu()

##### /\ ##### Modes #####
### ############################################################################################################
check_mode(_param['mode']) ### Runs the function that checks the mode and decides what the plugin should do. This should be at or near the end of the file.
#xbmcplugin.endOfDirectory(int(sys.argv[1]))
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
