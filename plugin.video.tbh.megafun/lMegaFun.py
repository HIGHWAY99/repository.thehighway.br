### ############################################################################################################
###	#	
### # Project: 			#		Url Tester
### # Author: 			#		The Highway
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re
import common
from common import *
from common import (_debugging,_addon,_artIcon,_artFanart,_addonPath,_OpenFile,isPath,isFile,popYN,_SaveFile,popOK,CopyAFile,RefreshList,DownloadThis,getFileExtension)
### ############################################################################################################
### ############################################################################################################
SiteName='MegaFun Channel Guide  (v0.0.3)  [Streams]'
SiteTag='MegaFun'
mainSite='megafun.vn'
iconSite="http://megafun.vn/common/v3/image/logo.png" #_artIcon
fanartSite=_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan'}

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

#workingPath=xbmc.validatePath(xbmc.translatePath(os.path.join(_addonPath,'resources')))
workingPath=xbmc.validatePath(xbmc.translatePath(_addonPath))
workingFile='lMegaFun_UrlList.txt'
workingFileWP=xbmc.validatePath(xbmc.translatePath(os.path.join(workingPath,workingFile)))
### ############################################################################################################
### ############################################################################################################
site=addpr('site','')
section=addpr('section','')
url=addpr('url','')
thumbnail=addpr('img','')
fanart=addpr('fanart','')
page=addpr('page','')
### ############################################################################################################
### ############################################################################################################
def About(head=''+cFL(SiteName,'blueviolet')+'',m=''):
	m=''
	if len(m)==0:
		m+='Site Name:  '+SiteName+CR+'Site Tag:  '+SiteTag+CR+'Site Domain:  '+mainSite+CR+'Site Icon:  '+iconSite+CR+'Site Fanart:  '+fanartSite
		m+=CR+'Age:  Please make sure you are of a valid age to watch the material shown.'
		#m+=CR+CR+'Known Hosts for Videos:  '
		#m+=CR+''
		m+=CR+CR+'Features:  '
		#m+=CR+'* Right Click Menu Access @ About or Url(s).'
		#m+=CR+'* Menu Items: Add Url | Remove Url'
		#m+=CR+'* Extra:  If you got the addon\'s Debugging to file setting turned on, you can view an Add Url link in the menu as well.'
		#m+=CR+'* Attempt to Play the Url(s) that you supply.'
		#m+=CR+'* Attempt to Play the Url(s) that you supply with both Direct-Link and UrlResolver Support via ContextMenu.'
		m+=CR+CR+'Notes:  '
		#m+=CR+'* This tool is still being worked on, so things may not be perfect yet.'
		#m+=CR+'* This tool is mainly meant to help devs check links to see if they\'re playable or not.'
		#m+=CR+'* '
		m+=CR+''
		m+=CR+ps('ReferalMsg')
		m+=CR+''
		m+=CR+''
		m+=CR+''
	String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
	#RefreshList()
### ############################################################################################################
### ############################################################################################################
def AddUrlToList(url=''):
	if (url==''): url=showkeyboard(txtMessage=url,txtHeader="Add URL:  ")
	if (url=='') or (url=='none') or (url==None) or (url==False): return
	url=url.replace("'","")
	deb('Adding url for',url)
	dd=_OpenFile(workingFileWP)
	dd+="\n'"+url+"'\n"
	_SaveFile(workingFileWP,dd)
	RefreshList()
def RemoveUrlToList(url=''):
	if (url==''): url=showkeyboard(txtMessage=url,txtHeader="Add URL:  ")
	if (url=='') or (url=='none') or (url==None) or (url==False): return
	url=url.replace("'","")
	deb('Removing url for',url)
	dd=_OpenFile(workingFileWP)
	dd=dd.replace("\n'"+url+"'\n","")
	_SaveFile(workingFileWP,dd)
	RefreshList()
### ############################################################################################################
### ############################################################################################################
def TP(s): return xbmc.translatePath(s)
def TPap(s,fe='.py'): return xbmc.translatePath(os.path.join(_addonPath,s+fe))

def SectionMenuEnglish(tag=''):
	cNumber ='8'; cNumber2='2'; cNumber3='0'; cNumber4='9'; 
	contextMenuItems=[]; 
	#contextMenuItems.append(('Add URL','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'site':site,'mode':'AddUrlToList'}) ))
	_addon.add_directory({'mode':'About','site':site},{'title':cFL_('About',colors['9'])},is_folder=False,contextmenu_items=contextMenuItems,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	if isFile(workingFileWP)==False: _SaveFile(workingFileWP,'\n')
	else:
		s1=[]; dd=_OpenFile(workingFileWP); deb('length of workingfile',str(len(dd))); #debob(dd)
		##s="\n+'(.*?)':'([A-Za-z0-9]+)':'(.+?)'\n+"; #deb('s',s); 
		##s1.append("\n+#EN'(.*?\s+\[EN\])':'([A-Za-z0-9]+)':'(.+?)'"); 
		if tag=="english": s1.append("\n+#EN'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+'(.*?\s+\[EN\])':'([A-Za-z0-9]+)':'(.+?)'"); 
		if tag=="premium": s1.append("\n+#P'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+#'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		if tag=="foriegn": s1.append("\n+#F'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+##'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		for s in s1:
			try: matches=re.compile(s).findall(dd); debob(matches); #,re.DOTALL
			except: matches=''; 
			ItemCount=len(matches); deb('# of matches',str(ItemCount)); i=1
			if ItemCount > 0:
				for name,tag,cid in matches:
					if   tag=='megafun':
						match='http://m24.megafun.vn/live.vs?c=%s&q=%s' % (cid,'high'); 
						_title=cFL('[HTTP] '+cid+'.)  ',colors[cNumber4])+cFL(name,colors[cNumber])#+CR+match; 
					elif tag=='megafun2':
						match='rtmp://m22.megafun.vn/hctv//%s' % (cid); 
						_title=cFL('[RTMP] '+cid+'.)  ',colors[cNumber4])+cFL(name,colors[cNumber])#+CR+match; 
					elif tag=='megafun3':
						#rtmp://$OPT:rtmp-raw=rtmp://m22.megafun.vn/hctv playpath=vstv009?token=CQ0T1Xvn0YlJQibmvBPpaA&time=1375431732&q=rtmp swfUrl=http://megafun.vn/common/player/player.swf live=1 pageUrl=http://baoquangninh.com.vn/truyen-hinh/?c=12
						match='rtmp://m22.megafun.vn/hctv playpath=%s swfUrl=http://megafun.vn/common/player/player.swf live=1' % (cid); 
						_title=cFL(cid+'.)  ',colors[cNumber4])+cFL(name,colors[cNumber])#+CR+match; 
					else:
						match=cid; _title=str(i)+'.)  '+cFL_(name,colors[cNumber])+CR+match; 
					contextMenuItems=[]; img=iconSite; fimg=fanartSite; pars={'mode':'PlayURL','url':match,'site':site,'section':section}; 
					#contextMenuItems.append(('Try URL With UrlResolver','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'site':site,'mode':'PlayURLs','url':match}) ))
					#contextMenuItems.append(('Remove URL','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'site':site,'mode':'RemoveUrlToList','url':match})))
					#contextMenuItems.append(('Add URL','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'site':site,'mode':'AddUrlToList'}) ))
					try: _addon.add_directory(pars,{'title':_title},is_folder=False,contextmenu_items=contextMenuItems,total_items=ItemCount,fanart=fimg,img=img); i=i+1; 
					except: pass
	eod()

def SectionMenu():
	cNumber ='8'; cNumber2='2'; cNumber3='0'; cNumber4='9'; 
	contextMenuItems=[]; 
	#contextMenuItems.append(('Add URL','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'site':site,'mode':'AddUrlToList'}) ))
	_addon.add_directory({'mode':'About','site':site},{'title':cFL_('About',colors['9'])},is_folder=False,contextmenu_items=contextMenuItems,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	#if (_debugging==True): _addon.add_directory({'mode':'AddUrlToList','site':site},{'title':cFL_('Add Url',colors[cNumber3])},is_folder=True,contextmenu_items=contextMenuItems,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	_addon.add_directory({'tag':'english','mode':'SectionMenuEnglish','site':site},{'title':'['+cFL('English',colors[cNumber3])+']'},is_folder=True,contextmenu_items=contextMenuItems,fanart=fanartSite,img=iconSite); 
	#_addon.add_directory({'tag':'premium','mode':'SectionMenuEnglish','site':site},{'title':'['+cFL('Premium',colors[cNumber3])+']'},is_folder=True,contextmenu_items=contextMenuItems,fanart=fanartSite,img=iconSite); 
	_addon.add_directory({'tag':'foriegn','mode':'SectionMenuEnglish','site':site},{'title':'['+cFL('Foriegn',colors[cNumber3])+']'},is_folder=True,contextmenu_items=contextMenuItems,fanart=fanartSite,img=iconSite); 
	
	if isFile(workingFileWP)==False: _SaveFile(workingFileWP,'\n')
	else:
		s1=[]; dd=_OpenFile(workingFileWP); deb('length of workingfile',str(len(dd))); #debob(dd)
		##s="\n+'(.*?)':'([A-Za-z0-9]+)':'(.+?)'\n+"; #deb('s',s); 
		##s1.append("\n+#EN'(.*?\s+\[EN\])':'([A-Za-z0-9]+)':'(.+?)'"); 
		s1.append("\n+#[A-Z\#]*'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+#EN'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+'(.*?\s+\[EN\])':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+#P'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+#'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+#F'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		#s1.append("\n+##'(.*?)':'([A-Za-z0-9]+)':'(.+?)'"); 
		for s in s1:
			try: matches=re.compile(s).findall(dd); debob(matches); #,re.DOTALL
			except: matches=''; 
			ItemCount=len(matches); deb('# of matches',str(ItemCount)); i=1
			if ItemCount > 0:
				for name,tag,cid in matches:
					if   tag=='megafun':
						match='http://m24.megafun.vn/live.vs?c=%s&q=%s' % (cid,'high'); 
						_title=cFL('[HTTP] '+cid+'.)  ',colors[cNumber4])+cFL(name,colors[cNumber])#+CR+match; 
					elif tag=='megafun2':
						match='rtmp://m22.megafun.vn/hctv//%s' % (cid); 
						_title=cFL('[RTMP] '+cid+'.)  ',colors[cNumber4])+cFL(name,colors[cNumber])#+CR+match; 
					elif tag=='megafun3':
						#rtmp://$OPT:rtmp-raw=rtmp://m22.megafun.vn/hctv playpath=vstv009?token=CQ0T1Xvn0YlJQibmvBPpaA&time=1375431732&q=rtmp swfUrl=http://megafun.vn/common/player/player.swf live=1 pageUrl=http://baoquangninh.com.vn/truyen-hinh/?c=12
						match='rtmp://m22.megafun.vn/hctv playpath=%s swfUrl=http://megafun.vn/common/player/player.swf live=1' % (cid); 
						_title=cFL(cid+'.)  ',colors[cNumber4])+cFL(name,colors[cNumber])#+CR+match; 
					else:
						match=cid; _title=str(i)+'.)  '+cFL_(name,colors[cNumber])+CR+match; 
					contextMenuItems=[]; img=iconSite; fimg=fanartSite; pars={'mode':'PlayURL','url':match,'site':site,'section':section}; 
					#contextMenuItems.append(('Try URL With UrlResolver','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'site':site,'mode':'PlayURLs','url':match}) ))
					#contextMenuItems.append(('Remove URL','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'site':site,'mode':'RemoveUrlToList','url':match})))
					#contextMenuItems.append(('Add URL','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'site':site,'mode':'AddUrlToList'}) ))
					try: _addon.add_directory(pars,{'title':_title},is_folder=False,contextmenu_items=contextMenuItems,total_items=ItemCount,fanart=fimg,img=img); i=i+1; 
					except: pass
	eod()
### ############################################################################################################
### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
	deb('mode',mode); 
	if (mode=='SectionMenu'): 		SectionMenu()
	elif (mode=='') or (mode=='main') or (mode=='MainMenu'): SectionMenu()
	elif (mode=='SectionMenuEnglish'): 	SectionMenuEnglish(addpr('tag',''))
	elif (mode=='AddUrlToList'): 	AddUrlToList(url=url)
	elif (mode=='RemoveUrlToList'): 	RemoveUrlToList(url=url)
	elif (mode=='About'): 				About()
	elif (mode=='CustomUpdate'): 	Update_CustomUpdate(addpr('path',''),addpr('filename',''))
	##
	elif (mode=='PlayURL'): 						PlayURL(url)
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
	elif (mode=='cFavoritesEmpty'):  	fav__COMMON__empty( site=site,section=section,subfav=addpr('subfav','') ); xbmc.executebuiltin("XBMC.Container.Refresh"); 
	elif (mode=='cFavoritesRemove'):  fav__COMMON__remove( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year','') )
	elif (mode=='cFavoritesAdd'):  		fav__COMMON__add( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year',''),img=addpr('img',''),fanart=addpr('fanart',''),plot=addpr('plot',''),commonID=addpr('commonID',''),commonID2=addpr('commonID2',''),ToDoParams=addpr('todoparams',''),Country=addpr('country',''),Genres=addpr('genres',''),Url=url ) #,=addpr('',''),=addpr('','')
	elif (mode=='AddVisit'):							
		try: visited_add(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='RemoveVisit'):							
		try: visited_remove(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='EmptyVisit'):						
		try: visited_empty(); RefreshList(); 
		except: pass
	elif (mode=='refresh_meta'):			refresh_meta(addpr('video_type',''),TagAnimeName(addpr('title','')),addpr('imdb_id',''),addpr('alt_id',''),addpr('year',''))
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
	#

mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
