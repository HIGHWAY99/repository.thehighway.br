### ############################################################################################################
###	#	
### # Project: 			#		The Binary Highway - by The Highway 2013.
### # Author: 			#		The Highway
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re

from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile,isFile,tfalse,addpr,addst,DownloadThis,fav__COMMON__add,fav__COMMON__remove,fav__COMMON__empty)

### ############################################################################################################
### ############################################################################################################











### ############################################################################################################
### ############################################################################################################
def do_MainMenu(): import mMain
def check_mode(mode='',site='',section='',url=''):
	deb('Mode',mode); deb('param >> site',site); deb('param >> section',section); deb('param >> url',url); deb('param >> title',addpr('title',''))
	if (mode=='') or (mode=='main') or (mode=='MainMenu'):
		if (site==''): import mMain; return
	if   (mode=='PlayURL'): 						PlayURL(url)
	elif (mode=='PlayURLs'): 						PlayURLs(url)
	elif (mode=='PlayURLstrm'): 				PlayURLstrm(url)
	elif (mode=='PlayFromHost'): 				PlayFromHost(url)
	elif (mode=='PlayVideo'): 					PlayVideo(url)
	elif (mode=='PlayItCustom'): 				PlayItCustom(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='PlayItCustomL2A'): 		PlayItCustomL2A(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='Settings'): 						_addon.addon.openSettings() # Another method: _plugin.openSettings() ## Settings for this addon.
	elif (mode=='ResolverSettings'): 		import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='ResolverUpdateHostFiles'):	import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='TextBoxFile'): 				TextBox2().load_file(url,addpr('title','')); #eod()
	elif (mode=='TextBoxUrl'):  				TextBox2().load_url(url,addpr('title','')); #eod()
	elif (mode=='Download'): 						
		try: _addon.resolve_url(url)
		except: pass
		debob([url,addpr('destfile',''),addpr('destpath',''),str(tfalse(addpr('useResolver','true')))])
		DownloadThis(url,addpr('destfile',''),addpr('destpath',''),tfalse(addpr('useResolver','true')))
	elif (mode=='toJDownloader'): 			SendTo_JDownloader(url,tfalse(addpr('useResolver','true')))
	elif (mode=='cFavoritesEmpty'):  	fav__COMMON__empty( site=site,section=section,subfav=addpr('subfav','') )
	elif (mode=='cFavoritesRemove'):  fav__COMMON__remove( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year','') )
	elif (mode=='cFavoritesAdd'):  		fav__COMMON__add( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year',''),img=addpr('img',''),fanart=addpr('fanart',''),plot=addpr('plot',''),commonID=addpr('commonid',''),commonID2=addpr('commonid2',''),ToDoParams=addpr('todoparams',''),Country=addpr('country',''),Genres=addpr('genres',''),Url=url ) #,=addpr('',''),=addpr('','')
	else: 
		### Handle importing .py file for the right site.
		siteL=site.lower()
		debob(xbmc.translatePath(os.path.join(_addonPath,site+'.py')))
		if   (siteL=='others'):					import mOthers
		elif (siteL=='misc'):						import mMisc
		elif (siteL=='mMovies_and_TV'):	import mMovies_and_TV
		elif (siteL=='mAnime'):					import mAnime
		elif (siteL=='mLiveStreams'):					import mLiveStreams
		elif (siteL=='resolverplugins'):	import mResolverPlugins
		#
		elif isFile(xbmc.translatePath(os.path.join(_addonPath,site+'.py')))==True: __import__(site)
		else: myNote(header='Mode:  "'+mode+'"',msg=site+' (site) not found.'); import mMain; return
		#mode_subcheck(mode,site,section,url)



check_mode(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url','')) ### Runs the function that checks the mode and decides what the plugin should do. This should be at or near the end of the file.


### ############################################################################################################
### ############################################################################################################
