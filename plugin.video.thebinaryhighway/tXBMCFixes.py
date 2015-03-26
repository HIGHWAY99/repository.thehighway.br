### ############################################################################################################
###	#	
### # Project: 			#		XBMC Fixes
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
from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile,isPath,isFile,popYN,_SaveFile,popOK,CopyAFile,RefreshList,DownloadThis,getFileExtension,_debugging)

### ############################################################################################################
### ############################################################################################################
SiteName='XBMC Fixes  [2013-12-09]'
SiteTag='XBMCFixes'
mainSite=''
iconSite='http://i.imgur.com/XMClMrQ.png' #'http://xbmc.org/wp-content/themes/paradise/Paradise/images/logo.png' #_artIcon
fanartSite='http://s9.postimg.org/uy7tu92jz/1013960_471938356223940_1093377719_n.jpg' #'http://xbmc.org/wp-content/uploads/xbmc-eden-announce-2-650-1-600x336.jpg' #_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan'}

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

workingUrl='http://github.com/HIGHWAY99/repository.thehighway/raw/master/repo/thebinaryhighway/packs/'
workingPath=xbmc.translatePath(os.path.join(_addonPath,'resources','misc'))
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
		#m+=CR+'Age:  Please make sure you are of a valid age to watch the material shown.'
		#m+=CR+CR+'Known Hosts for Videos:  '
		#m+=CR+'videofun.me | video44.net | novamov.com | yourupload.com' # | play44.net | vidzur.com'
		#m+=CR+CR+'Valid Folders:  '
		#m+=CR+'script.module.urlresolver | script.module.urlresolver-master | script.module.urlresolver-2.0.9 | script.module.urlresolver-1.0.0'
		m+=CR+CR+'Features:  '
		m+=CR+'* Tools Related to XBMC.'
		m+=CR+CR+'Notes:  '
		m+=CR+'* A Restart of XBMC may be needed after using some fixes before you notice changes.'
		#m+=CR+'* '
		#m+=CR+'* '
		m+=CR+''
		m+=CR+ps('ReferalMsg')
		m+=CR+''
		m+=CR+''
		m+=CR+''
	String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
	#RefreshList()

def TP(s): return xbmc.translatePath(s)



### ############################################################################################################
### ############################################################################################################











### ############################################################################################################
### ############################################################################################################
def Tool_FixMouseMoveA():
	#ttFileName='mouse.xml'; 
	eMsgHead='Copy File: '+'mouse.xml'
	destPath=xbmc.translatePath(os.path.join('special://home','system'))
	if isPath(destPath)==False: myNote(eMsgHead,'Making Folder: '+'system'); os.mkdir(destPath)
	destPath=xbmc.translatePath(os.path.join(destPath,'keymaps'))
	if isPath(destPath)==False: myNote(eMsgHead,'Making Folder: '+'keymaps'); os.mkdir(destPath)
	fromFile='mouse.xml'; tFrom=xbmc.translatePath(os.path.join(workingPath,fromFile))
	toFile='mouse.xml'; tTo=xbmc.translatePath(os.path.join(destPath,toFile))
	r=popYN('Would you like to copy this File?',fromFile,'to:  '+tTo,'',n='Cancel',y='Copy It')
	if r==False: popOK('File could not be copied.',title=eMsgHead,line2='',line3='')
	elif (isFile(tFrom)==True) and (isFile(tTo)==False): CopyAFile(tFrom,tTo)
### ############################################################################################################
### ############################################################################################################
def Tool_Fix_1Channel_Remove_HostHandledCheck():
	eMsgHead='Fixing: '+'(plugin.video.1channel/default.py)'
	StringOld="if urlresolver.HostedMediaFile(item['url']).valid_url():"
	StringNew="if item==item: #urlresolver.HostedMediaFile(item['url']).valid_url():"
	destPath=xbmc.translatePath(os.path.join('special://home','addons','plugin.video.1channel'))
	if isPath(destPath)==False: myNote(eMsgHead,'Folder not found.'); return
	destFile=xbmc.translatePath(os.path.join(destPath,'default.py'))
	if isFile(destFile)==False: myNote(eMsgHead,'File not found.'); return
	CopyAFile(destFile,destFile+'.bup'); 
	tt=_OpenFile(destFile); 
	tt=tt.replace(StringOld,StringNew); 
	_SaveFile(destFile,tt); 
	myNote(eMsgHead,'File should now be fixed.')

def Tool_Fix_1Channel_Restore_HostHandledCheck():
	eMsgHead='Fixing: '+'(plugin.video.1channel/default.py)'
	StringOld="if item==item: #urlresolver.HostedMediaFile(item['url']).valid_url():"
	StringNew="if urlresolver.HostedMediaFile(item['url']).valid_url():"
	destPath=xbmc.translatePath(os.path.join('special://home','addons','plugin.video.1channel'))
	if isPath(destPath)==False: myNote(eMsgHead,'Folder not found.'); return
	destFile=xbmc.translatePath(os.path.join(destPath,'default.py'))
	if isFile(destFile)==False: myNote(eMsgHead,'File not found.'); return
	CopyAFile(destFile,destFile+'.bup'); 
	tt=_OpenFile(destFile); 
	tt=tt.replace(StringOld,StringNew); 
	_SaveFile(destFile,tt); 
	myNote(eMsgHead,'File should now be fixed.')

def Tool_Fix_LastFM_Remove_AccountNotice():
	eMsgHead='Fixing: '+'(plugin.audio.lastfm/utils.py)'
	StringOld=" xbmc.executebuiltin('Notification(%s,%s,%i)' % (LANGUAGE(32011), LANGUAGE(32027), 7000))"
	StringNew=" ttTempFixTT='' #xbmc.executebuiltin('Notification(%s,%s,%i)' % (LANGUAGE(32011), LANGUAGE(32027), 7000))"
	destPath=xbmc.translatePath(os.path.join('special://home','addons','plugin.audio.lastfm'))
	if isPath(destPath)==False: myNote(eMsgHead,'Folder not found.'); return
	destFile=xbmc.translatePath(os.path.join(destPath,'utils.py'))
	if isFile(destFile)==False: myNote(eMsgHead,'File not found.'); return
	CopyAFile(destFile,destFile+'.bup'); 
	tt=_OpenFile(destFile); 
	tt=tt.replace(StringOld,StringNew); 
	_SaveFile(destFile,tt); 
	myNote(eMsgHead,'File should now be fixed.')

def Tool_Fix_LastFM_Restore_AccountNotice():
	eMsgHead='Fixing: '+'(plugin.audio.lastfm/utils.py)'
	StringOld=" ttTempFixTT='' #xbmc.executebuiltin('Notification(%s,%s,%i)' % (LANGUAGE(32011), LANGUAGE(32027), 7000))"
	StringNew=" xbmc.executebuiltin('Notification(%s,%s,%i)' % (LANGUAGE(32011), LANGUAGE(32027), 7000))"
	destPath=xbmc.translatePath(os.path.join('special://home','addons','plugin.audio.lastfm'))
	if isPath(destPath)==False: myNote(eMsgHead,'Folder not found.'); return
	destFile=xbmc.translatePath(os.path.join(destPath,'utils.py'))
	if isFile(destFile)==False: myNote(eMsgHead,'File not found.'); return
	CopyAFile(destFile,destFile+'.bup'); 
	tt=_OpenFile(destFile); 
	tt=tt.replace(StringOld,StringNew); 
	_SaveFile(destFile,tt); 
	myNote(eMsgHead,'File should now be fixed.')

def Tool_Fix_Fixit(AddonFolder,AddonFile,StringOld,StringNew):
	if (len(AddonFolder)==0) or (len(AddonFile)==0) or (len(StringOld)==0): myNote(eMsgHead,'Missing Fixit Data.'); return
	eMsgHead='Fixing: '+'('+AddonFolder+'/'+AddonFile+')'
	destPath=xbmc.translatePath(os.path.join('special://home','addons',AddonFolder))
	if isPath(destPath)==False: myNote(eMsgHead,'Folder not found.'); return
	destFile=xbmc.translatePath(os.path.join(destPath,AddonFile))
	if isFile(destFile)==False: myNote(eMsgHead,'File not found.'); return
	CopyAFile(destFile,destFile+'.bup'); 
	tt=_OpenFile(destFile); 
	tt=tt.replace(StringOld,StringNew); 
	_SaveFile(destFile,tt); 
	myNote(eMsgHead,'File should now be fixed.')


### ############################################################################################################
### ############################################################################################################

def Updater(url,filename,destpath,iszip=True):
	#
	_FE=getFileExtension(filename)
	if (_FE.lower()=='txt') or (_FE.lower()=='log') or (_FE.lower()=='py') or (_FE.lower()=='png') or (_FE.lower()=='jpg') or (_FE.lower()=='gif'): iszip=False
	elif (_FE.lower()=='zip') or (_FE.lower()=='z7') or (_FE.lower()=='ace'): iszip=True
	#try: _addon.resolve_url(addpr('url',''))
	try: _addon.resolve_url(filename)
	except: pass
	try:
		import shutil
		debob(['url:',url,'filename:',filename,'destpath:',destpath])
		zippath=xbmc.translatePath(os.path.join(_addonPath,'zips'))
		zipfile=xbmc.translatePath(os.path.join(zippath,filename))
		if isPath(zippath)==False: os.mkdir(zippath); deb('Path Made',zippath)
		common.DownloadThis(url,filename,zippath,useResolver=False)
		if isPath(destpath)==False: os.mkdir(destpath); deb('Path Made',destpath)
		if isFile(zipfile)==True:
			if iszip==False: shutil.copy(zipfile,xbmc.translatePath(os.path.join(destpath,filename)))
			else: ee=ExtractThis(zipfile,destpath)
		else: deb('File not found',zipfile); myNote('Updater','may have failed.'); return
		try: 
			os.remove(zipfile)
			shutil.rmtree(zippath)
			#os.rmdir (zippath)
			#os.remove(zippath)
		except: pass
		#checkedFileList=_OpenFile(checkedFileWP)
		#checkedFileList+="\n'"+filename+"'"
		#_SaveFile(checkedFileWP,checkedFileList)
		myNote('Updater','Completed')
		RefreshList()
	except:
		debob('error during updater process.')
		myNote('Updater','may have failed.')

def Update_CustomUpdate2(path,filename,urlpath=workingUrl):
	if (len(path)==0) or (len(filename)==0): return
	if (len(urlpath)==0): urlpath=workingUrl
	url=urlpath+filename
	if   (path.lower()=='/addon/') or (path.lower()=='/'): destpath=xbmc.translatePath(_addonPath)
	elif (path.lower()=='/addons/'): destpath=xbmc.translatePath(os.path.join('special://home','addons'))
	elif (path.lower()=='/addon/resources/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources'))
	elif (path.lower()=='/addon/resources/misc/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','misc'))
	elif (path.lower()=='/addon/resources/urlresolver/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','urlresolver'))
	elif (path.lower()=='/addon/resources/repos/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','repos'))
	elif (path.lower()=='/addon/art/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'art'))
	#elif (path.lower()=='/addon/'): 
	else: return
	Updater(url,filename,destpath)

def Update_CustomUpdate(path,filename):
	if (len(path)==0) or (len(filename)==0): return
	##filename='art.zip'
	url=workingUrl+filename
	if   (path.lower()=='/addon/') or (path.lower()=='/'): destpath=xbmc.translatePath(_addonPath)
	elif (path.lower()=='/addons/'): destpath=xbmc.translatePath(os.path.join('special://home','addons'))
	elif (path.lower()=='/addon/resources/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources'))
	elif (path.lower()=='/addon/resources/misc/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','misc'))
	elif (path.lower()=='/addon/resources/urlresolver/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','urlresolver'))
	elif (path.lower()=='/addon/resources/repos/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','repos'))
	elif (path.lower()=='/addon/art/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'art'))
	#elif (path.lower()=='/addon/'): 
	else: return
	##destpath=xbmc.translatePath(os.path.join(_addonPath,'art'))
	Updater(url,filename,destpath)

def Updater4Fixes(FixName):
	if FixName=='elementtree': 				Update_CustomUpdate('/addons/','script.module.elementtree-1.2.7.zip')
	if FixName=='httplib2': 					Update_CustomUpdate('/addons/','script.module.httplib2-0.7.1.zip')
	if FixName=='metahandler203': 		Update_CustomUpdate('/addons/','script.module.metahandler-2.0.3.zip')
	if FixName=='metahandler20302': 	Update_CustomUpdate('/addons/','script.module.metahandler-2.0.3.02.zip')
	if FixName=='metahandler210': 		Update_CustomUpdate('/addons/','script.module.metahandler-2.1.0.zip')
	if FixName=='metahandler231': 		Update_CustomUpdate2('/addons/','script.module.metahandler-2.3.1.zip','http://ftp.heanet.ie/mirrors/xbmc/addons/frodo/script.module.metahandler/')
	if FixName=='universal': 					Update_CustomUpdate('/addons/','script.module.universal-1.0.1.zip')
	if FixName=='commonplugincache': 	Update_CustomUpdate('/addons/','script.common.plugin.cache-2.1.0.zip')
	if FixName=='urlresolver112': 		Update_CustomUpdate('/addons/','script.module.urlresolver-1.1.2.zip')
	if FixName=='urlresolver21001': 	Update_CustomUpdate('/addons/','script.module.urlresolver-2.1.0.01.zip')
	if FixName=='urlresolver212': 		Update_CustomUpdate('/addons/','script.module.urlresolver-2.1.2.zip')
	#if FixName=='urlresolver212': 		Update_CustomUpdate2('/addons/','script.module.urlresolver-2.1.2.zip','http://ftp.heanet.ie/mirrors/xbmc/addons/frodo/script.module.urlresolver/')
	if FixName=='solarmovieso029':		Update_CustomUpdate('/addons/','plugin.video.solarmovie.so-0.2.9.zip')
	if FixName=='1channel202':				Update_CustomUpdate('/addons/','plugin.video.1channel-2.0.2.zip')
	if FixName=='1channel2026':				Update_CustomUpdate('/addons/','plugin.video.1channel-2.0.2.6.zip')
	if FixName=='1channel2027':				Update_CustomUpdate('/addons/','plugin.video.1channel-2.0.2.7.zip')
	if FixName=='1channel2028':				Update_CustomUpdate('/addons/','plugin.video.1channel-2.0.2.8.zip')
	if FixName=='1channel210':				Update_CustomUpdate('/addons/','plugin.video.1channel-2.1.0.zip')
	if FixName=='1channel2101':				Update_CustomUpdate('/addons/','plugin.video.1channel-2.1.0.1.zip')
	if FixName=='myconnpy':						Update_CustomUpdate('/addons/','script.module.myconnpy-0.3.2.zip')
	#if FixName=='myconnpy':						Update_CustomUpdate2('/addons/','script.module.myconnpy-0.3.2.zip','http://ftp.heanet.ie/mirrors/xbmc/addons/frodo/script.module.myconnpy/')
	if FixName=='requests':						Update_CustomUpdate('/addons/','script.module.requests-1.1.0.zip')
	if FixName=='simplejson':					Update_CustomUpdate('/addons/','script.module.simplejson-3.3.0.zip')
	if FixName=='xbmcswift2':					Update_CustomUpdate('/addons/','script.module.xbmcswift2-2.4.0.zip')
	if FixName=='delete.textures.db': ### indowsError: (32, 'The process cannot access the file because it is being used by another process', '\\userdata\\Database\\Textures13.db')
		path=TP('special://database'); myNote('Fixer','Reading Folder: special://database'); files=os.listdir(path); debob(files); 
		for file in files:
			if ('Textures' in file) and (file.endswith(".db")): 
				fnamef=os.path.join(path,file); deb('Found',fnamef); myNote('Fixer','Found: '+fnamef)
				#try: 
				#os.unlink(fnamef); os.remove(fnamef); deb('removing',fnamef); myNote('Fixer','Removing: '+fnamef)
				#except: deb('error during removing',fnamef); myNote('Fixer','may have failed.')
		xbmc.executebuiltin("XBMC.UpdateLocalAddons()"); RefreshList()
	if FixName=='empty.folder.packages':
		path=TP(os.path.join('special://home','addons','packages'))
		RemovingPath(path)
		RefreshList()
	if FixName=='empty.folder.thumbnails':
		path=TP(os.path.join('special://thumbnails'))
		RemovingPath(path)
		RefreshList()
	if FixName=='clean.slate.it':
		sFs=[TP(os.path.join('special://home','addons')),TP('special://database'),TP('special://userdata'),TP('special://thumbnails'),TP('special://temp'),TP(os.path.join('special://home','cache'))]
		for path in sFs:
			if isPath(path)==True:
				myNote("Clean Slate Tool","Path:  "+path.replace(TP('special://home'),''),delay=100); xbmc.sleep(1000); directories=os.listdir(path)
				for d in directories:
					if d not in ["plugin.video.thebinaryhighway"]:
						dPath=TP(os.path.join(path,d))
						try: RemovingPath(dPath,False,False,False)
						except: deb('Error removing',dPath)
		popOK("Most Folders should now be cleaned out [CR]and ready for reinstalling addons","Clean Slate Tool")
		popOK("Try using the installers above [CR]to get you back on track.","Clean Slate Tool")
		XBMC_UpdateLocalAddons(); RefreshList()
	#################################
	#	#Updater(url,filename,destpath)
	#

#def RemovingFlie(path): return

def RemovingPath(path,z1=True,z2=True,z3=True):
	if isPath(path)==True: 
		deb('Found',path); 
		try: 
			import shutil; shutil.rmtree(path); deb('removing',path); 
			if z1==True: myNote('Fixer','Removing: '+path)
		except: 
			deb('Erored on',path); 
			if z2==True: myNote('Fixer','Failed: '+path)
	else: 
		deb('couldn\'t find',path); 
		if z3==True: myNote('Fixer','Failed to find path: '+path)

### ############################################################################################################
### ############################################################################################################



### ############################################################################################################
### ############################################################################################################






### ############################################################################################################
### ############################################################################################################


### ############################################################################################################
### ############################################################################################################
def SectionMenu():
	cNumber ='8'; cNumber2='2'; cNumber3='4'; 
	_addon.add_directory({'mode':'About','site':site},{'title':cFL_('About',colors['9'])},is_folder=False,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	#
	#_addon.add_directory({'mode':'1CHHostCheckRemove','site':site},{'title':cFL_('1CH - Remove Host Check (Faster Display)[CR]Thx for this fix goes to: HIGHWAY99',colors['9'])},is_folder=False,fanart='http://s9.postimg.org/w2vvcentb/primewire.jpg',img='http://i2.ytimg.com/vi/i_yPxLAlKzg/mqdefault.jpg')
	#_addon.add_directory({'mode':'1CHHostCheckRestore','site':site},{'title':cFL_('1CH - Restore Host Check',colors['9'])},is_folder=False,fanart='http://s9.postimg.org/w2vvcentb/primewire.jpg',img='http://i2.ytimg.com/vi/i_yPxLAlKzg/mqdefault.jpg')
	
	#_addon.add_directory({'mode':'LastFMAccountNoticeRemove','site':site},{'title':cFL_('LastFM - Remove Notice of username/pasword[CR]Thx for this fix goes to: vict0r',colors['9'])},is_folder=False,fanart='http://s9.postimg.org/w2vvcentb/primewire.jpg',img='http://i2.ytimg.com/vi/i_yPxLAlKzg/mqdefault.jpg')
	#_addon.add_directory({'mode':'LastFMAccountNoticeRestore','site':site},{'title':cFL_('LastFM - Restore Notice of username/pasword',colors['9'])},is_folder=False,fanart='http://s9.postimg.org/w2vvcentb/primewire.jpg',img='http://i2.ytimg.com/vi/i_yPxLAlKzg/mqdefault.jpg')
	
	### Set these if you want dif art.
	t_Fanart=fanartSite
	t_Icon=iconSite
	###
	
	### Set these for each String-Type File Fix.
	t_Fanart="http://s9.postimg.org/w2vvcentb/primewire.jpg"
	t_Icon="http://i2.ytimg.com/vi/i_yPxLAlKzg/mqdefault.jpg"
	t_FixBy="HIGHWAY99"; t_FixName="1CH"; t_FixLabel="Host Check"
	t_Addon_Folder="plugin.video.1channel"; t_Addon_File="default.py"
	t_Old="if urlresolver.HostedMediaFile(item['url']).valid_url():"
	t_New="if item==item: #urlresolver.HostedMediaFile(item['url']).valid_url():"
	_addon.add_directory({'AddonFolder':t_Addon_Folder,'AddonFile':t_Addon_File,'StringOld':t_Old,'StringNew':t_New,'mode':'Tool_Fix_Fixit','site':site},{'title':cFL_(t_FixName+' - Fix/Remove '+t_FixLabel+'[CR]Thx for this fix goes to: '+t_FixBy,colors['9'])},is_folder=False,fanart=t_Fanart,img=t_Icon)
	_addon.add_directory({'AddonFolder':t_Addon_Folder,'AddonFile':t_Addon_File,'StringOld':t_New,'StringNew':t_Old,'mode':'Tool_Fix_Fixit','site':site},{'title':cFL_(t_FixName+' - Restore '+t_FixLabel,colors['9'])},is_folder=False,fanart=t_Fanart,img=t_Icon)
	###
	
	### Set these for each String-Type File Fix.
	t_Fanart="http://shaneatkins.co.uk/wp-content/uploads/2012/07/lastfm.jpg"
	t_Icon="http://cdn.last.fm/flatness/community/xmas_monster.png"
	t_FixBy="vict0r"; t_FixName="LastFM"; t_FixLabel="Notice of username/pasword"
	t_Addon_Folder="plugin.audio.lastfm"; t_Addon_File="utils.py"
	t_Old=" xbmc.executebuiltin('Notification(%s,%s,%i)' % (LANGUAGE(32011), LANGUAGE(32027), 7000))"
	t_New=" ttTempFixTT='' #xbmc.executebuiltin('Notification(%s,%s,%i)' % (LANGUAGE(32011), LANGUAGE(32027), 7000))"
	_addon.add_directory({'AddonFolder':t_Addon_Folder,'AddonFile':t_Addon_File,'StringOld':t_Old,'StringNew':t_New,'mode':'Tool_Fix_Fixit','site':site},{'title':cFL_(t_FixName+' - Fix/Remove '+t_FixLabel+'[CR]Thx for this fix goes to: '+t_FixBy,colors['9'])},is_folder=False,fanart=t_Fanart,img=t_Icon)
	_addon.add_directory({'AddonFolder':t_Addon_Folder,'AddonFile':t_Addon_File,'StringOld':t_New,'StringNew':t_Old,'mode':'Tool_Fix_Fixit','site':site},{'title':cFL_(t_FixName+' - Restore '+t_FixLabel,colors['9'])},is_folder=False,fanart=t_Fanart,img=t_Icon)
	###
	
	### Set these for each String-Type File Fix.
	#t_Fanart=fanartSite
	#t_Icon=iconSite
	#t_FixBy="vict0r"; t_FixName="AutoUpdate"; t_FixLabel="Notice of username/pasword"
	#t_Addon_Folder="plugin.audio.lastfm"; t_Addon_File="utils.py"
	#t_Old="<addonautoupdate>true</addonautoupdate>"
	#t_New="<addonautoupdate>false</addonautoupdate>"
	#_addon.add_directory({'AddonFolder':t_Addon_Folder,'AddonFile':t_Addon_File,'StringOld':t_Old,'StringNew':t_New,'mode':'Tool_Fix_Fixit','site':site},{'title':cFL_(t_FixName+' - Disable '+t_FixLabel+'[CR]Thx for this fix goes to: '+t_FixBy,colors['9'])},is_folder=False,fanart=t_Fanart,img=t_Icon)
	#_addon.add_directory({'AddonFolder':t_Addon_Folder,'AddonFile':t_Addon_File,'StringOld':t_New,'StringNew':t_Old,'mode':'Tool_Fix_Fixit','site':site},{'title':cFL_(t_FixName+' - Enable '+t_FixLabel,colors['9'])},is_folder=False,fanart=t_Fanart,img=t_Icon)
	###
	#gui_home = xbmc.translatePath(os.path.join('special://home/userdata',''))
	#guisettings = os.path.join(gui_home, 'guisettings.xml')
	#input_xml = open(guisettings)
	#xmlgui = input_xml.read()
	#input_xml.close()
	#xmlgui = xmlgui.replace('<addonautoupdate>true</addonautoupdate>', '<addonautoupdate>false</addonautoupdate>')
	#newgui = open(guisettings, 'w')
	#newgui.write(xmlgui)
	#newgui.close()
	###
	
	_addon.add_directory({'FixName':'commonplugincache','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.common.'+cFL('plugin.cache',colors['9'])+'-2.1.0.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'elementtree','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('elementtree',colors['9'])+'-1.2.7.zip'},is_folder=False,fanart=fanartSite,img='http://www.mybonsaibuddy.com/Japanese_Red_Maple_Bonsai_Tree.jpg')
	_addon.add_directory({'FixName':'httplib2','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('httplib2',colors['9'])+'-0.7.1.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'metahandler203','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('metahandler',colors['9'])+'-2.0.3.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'metahandler20302','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('metahandler',colors['9'])+'-2.0.3.02.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'metahandler210','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('metahandler',colors['9'])+'-2.1.0.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'metahandler231','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('metahandler',colors['9'])+'-2.3.1.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'myconnpy','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('myconnpy',colors['9'])+'-0.3.2.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'requests','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('requests',colors['9'])+'-1.1.0.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'simplejson','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('simplejson',colors['9'])+'-3.3.0.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'xbmcswift2','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('xbmcswift2',colors['9'])+'-2.4.0.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'universal','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('universal',colors['9'])+'-1.0.1.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'urlresolver112','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('urlresolver',colors['9'])+'-1.1.2.zip (Not for Gotham)'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'urlresolver21001','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('urlresolver',colors['9'])+'-2.1.0.01.zip (Frodo)'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'urlresolver212','mode':'Updater4Fixes','site':site},{'title':'Install: '+'script.module.'+cFL('urlresolver',colors['9'])+'-2.1.2.zip (Frodo)'},is_folder=False,fanart=fanartSite,img=iconSite)
	
	_addon.add_directory({'FixName':'solarmovieso029','mode':'Updater4Fixes','site':site},{'title':'Install: '+'plugin.video.'+cFL('solarmovie.so',colors['9'])+'-0.2.9.zip'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'1channel202','mode':'Updater4Fixes','site':site},{'title':'Install: '+'plugin.video.'+cFL('1channel',colors['9'])+'-2.0.2.zip[CR] (By Bstrdsmkr)'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'1channel2026','mode':'Updater4Fixes','site':site},{'title':'Install: '+'plugin.video.'+cFL('1channel',colors['9'])+'-2.0.2.6.zip[CR] (Custom Version By The Highway)'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'1channel2027','mode':'Updater4Fixes','site':site},{'title':'Install: '+'plugin.video.'+cFL('1channel',colors['9'])+'-2.0.2.7.zip[CR] (Custom Version By The Highway)'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'1channel2028','mode':'Updater4Fixes','site':site},{'title':'Install: '+'plugin.video.'+cFL('1channel',colors['9'])+'-2.0.2.8.zip[CR] (Custom Version By The Highway)'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'1channel210','mode':'Updater4Fixes','site':site},{'title':'Install: '+'plugin.video.'+cFL('1channel',colors['9'])+'-2.1.0.zip[CR] (Current Version)'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'1channel2101','mode':'Updater4Fixes','site':site},{'title':'Install: '+'plugin.video.'+cFL('1channel',colors['9'])+'-2.1.0.1.zip[CR] (Custom Version By The Highway)'},is_folder=False,fanart=fanartSite,img=iconSite)
	
	#_addon.add_directory({'AddonFolder':'','mode':'Updater4Fixes','site':site},{'title':cFL_('',colors['9'])},is_folder=False,fanart=fanartSite,img=iconSite)
	#Updater4Fixes(addpr('FixName',''))
	
	# ### Can't remove file as it's in use. ###
	# ##_addon.add_directory({'FixName':'delete.textures.db','mode':'Updater4Fixes','site':site},{'title':'Remove: '+cFL_('Textures*.db',colors['9'])+CR+' (Possible Fix for Missing Icons. Restart.)'},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'FixName':'empty.folder.packages','mode':'Updater4Fixes','site':site},{'title':'Empty: '+'/'+cFL('packages',colors['9'])+'/ Folder'+CR+' (For use when you know what your doing.)'},is_folder=False,fanart='http://montanaesgr.org/wp-content/uploads/2013/09/empty-room-backgrounddownload-floor-3d-wallpaper-1600x1200-wallpoper-dfefomro.jpg',img='http://1.bp.blogspot.com/-4uffc2V-8BE/T1Oz9mwaeII/AAAAAAAAAKc/J5bz23oy8uw/s1600/Empty.jpg')
	_addon.add_directory({'FixName':'empty.folder.thumbnails','mode':'Updater4Fixes','site':site},{'title':'Empty: '+'/'+cFL('Thumbnails',colors['9'])+'/ Folder'+CR+' (For use when you know what your doing.)'},is_folder=False,fanart='http://montanaesgr.org/wp-content/uploads/2013/09/empty-room-backgrounddownload-floor-3d-wallpaper-1600x1200-wallpoper-dfefomro.jpg',img='http://1.bp.blogspot.com/-4uffc2V-8BE/T1Oz9mwaeII/AAAAAAAAAKc/J5bz23oy8uw/s1600/Empty.jpg')
	# ### Testing for FreshStart Addon ###
	if _debugging==True: _addon.add_directory({'FixName':'clean.slate.it','mode':'Updater4Fixes','site':site},{'title':''+cFL_('Clean Slate Tool',colors['9'])+' ('+cFL('Will Delete Files.','red')+')'+CR+' (Check the Forum or Live Chat @ XBMCHUB or for information on this tool.)'},is_folder=True,fanart='http://thefathershouse.com/~thefathe/cms-assets/images/313934.clean-slate-board.jpg',img='http://dengitsjoe.com/wp-content/uploads/et_temp/CleanSlate-91513_220x220.jpeg')
	
	
	
	
	
	#_addon.add_directory({'AddonFolder':'','AddonFile':'','StringOld':"",'StringNew':"",'mode':'Tool_Fix_Fixit','site':site},{'title':cFL_('LastFM - Restore Notice of username/pasword',colors['9'])},is_folder=False,fanart='http://s9.postimg.org/w2vvcentb/primewire.jpg',img='http://i2.ytimg.com/vi/i_yPxLAlKzg/mqdefault.jpg')
	### Tool_Fix_Fixit(addpr('AddonFolder',''),addpr('AddonFile',''),addpr('StringOld',''),addpr('StringNew',''))
	
	
	#
	#
	#
	if isFile(TP(os.path.join(workingPath,'mouse.xml')))==True: _addon.add_directory({'mode':'FixMouseMove','site':site},{'title':cFL_('Prevent exiting FullScreen due to Mouse Movement [CR]while watching a video. (Mouse.xml) [restart]',colors['9'])},is_folder=False,fanart='http://i00.i.aliimg.com/wsphoto/v1/673900382_2/T2-Air-Fly-Mouse-2-4G-3D-Motion-Stick-Remote-PC-Mouse-for-TV-Box-TV.jpg',img='http://i138.photobucket.com/albums/q260/Ygdrassil/stuff/Mouse-Keyboard-B-1815.jpg')
	#
	eod()

### ############################################################################################################
### ############################################################################################################

def mode_subcheck(mode='',site='',section='',url=''):
	if (mode=='SectionMenu'): 		SectionMenu()
	elif (mode=='SubMenu'): 			SubMenu()
	elif (mode=='CopyPlugin'): 		CopyPlugin(addpr('title',''))
	elif (mode=='List'): 					Browse_List(url,page)
	elif (mode=='Hosts'): 				Browse_Hosts(url)
	elif (mode=='AZ'): 						Browse_AZ()
	elif (mode=='Genres'): 				Browse_Genres()
	elif (mode=='PlayFromHost'): 	PlayFromHost(url)
	elif (mode=='Search'): 				Search_Site(title=addpr('title',''),url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
	elif (mode=='SearchLast'): 		Search_Site(title=addst('LastSearchTitle'+SiteTag),url=url,page=page,metamethod=addpr('metamethod',''),endit=tfalse(addpr('endit','true'))) #(site,section)
	elif (mode=='FixMouseMove'): 	Tool_FixMouseMoveA()
	elif (mode=='1CHHostCheckRemove'):	Tool_Fix_1Channel_Remove_HostHandledCheck()
	elif (mode=='1CHHostCheckRestore'):	Tool_Fix_1Channel_Restore_HostHandledCheck()
	elif (mode=='LastFMAccountNoticeRemove'):	Tool_Fix_LastFM_Remove_AccountNotice()
	elif (mode=='LastFMAccountNoticeRestore'):	Tool_Fix_LastFM_Restore_AccountNotice()
	elif (mode=='Tool_Fix_Fixit'):	Tool_Fix_Fixit(addpr('AddonFolder',''),addpr('AddonFile',''),addpr('StringOld',''),addpr('StringNew',''))
	elif (mode=='Updater4Fixes'):	Updater4Fixes(addpr('FixName',''))
	elif (mode=='About'): 				About()
	#elif (mode=='FavList'): 			Fav_List(site,section)
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
	
	#

mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
