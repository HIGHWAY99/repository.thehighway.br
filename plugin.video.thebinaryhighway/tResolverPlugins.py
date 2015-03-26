### ############################################################################################################
###	#	
### # Project: 			#		Host Plugin Tool
### # Author: 			#		The Highway
### # Description: 	#		Adds Host Plugins to UrlResolver's Plugin Folder to provide support for sources
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re

from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile,isPath,isFile,popYN,_SaveFile,popOK,CopyAFile)

### ############################################################################################################
### ############################################################################################################
SiteName='[COLOR yellow]A[/COLOR]ttempt to Fix/Add [CR]Resolver Host Plugins' #'[COLOR white]url[COLOR yellow]Resolver[/COLOR][/COLOR]  [script.module.urlresolver]'
SiteTag='urlResolver'
mainSite='script.module.urlresolver\lib\urlresolver\plugins'
iconSite='http://i.imgur.com/XMClMrQ.png' #_artIcon
fanartSite='http://i.imgur.com/UtL1F8j.png' #_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'','6':'','7':'','8':'cornflowerblue','9':'blueviolet'}
#fanart='http://i.imgur.com/UtL1F8j.png',img='http://i.imgur.com/0zsWiGB.png')

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

workingPath=xbmc.translatePath(os.path.join(_addonPath,'resources','urlresolver'))
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
		m+=CR+CR+'Valid Folders:  '
		m+=CR+'script.module.urlresolver | script.module.urlresolver-master | script.module.urlresolver-2.0.9 | script.module.urlresolver-1.0.0'
		m+=CR+CR+'Features:  '
		m+=CR+'* Browse Hosts Files available with this project.'
		#m+=CR+'* Uses urlResolver().'
		#m+=CR+'* Play Videos via Handled Hosts.'
		#m+=CR+'* Browse Genres and A-Z - Browse Item Pages by A-Z/Others or by Genres (fetched from the site with item count for each genre.'
		#m+=CR+'* Search - Just a normal Title Search was available for this site, though it uses a Post-method and their site search seems to have some problems at times.'
		#m+=CR+'* Repeat Last Search - Like it says, this shows up once you\'ve done a Search for the first time and allows you to repeat the last search term you used for this Site.  Yes, it\'s setup to save the setting for each site seperately.'
		m+=CR+CR+'Notes:  '
		m+=CR+'* This meant to help you update Host Plugin .py files in for script.module.urlresolver.'
		m+=CR+'* Existing file(s) will be renamed from  [B].py[/B]  to  [B].py.bup[/B].'
		m+=CR+'* If you have a working Host Plugin and would like it added to this, please get ahold of me and I\'ll see about taking a look at it and getting it added.'
		#m+=CR+'* '
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











### ############################################################################################################
### ############################################################################################################
def CopyPlugin2(fomPath,fromFile,toPath):
	eMsgHead='Copy Plugin'+fromFile
	destPath=xbmc.translatePath(os.path.join(toPath,'lib','urlresolver','plugins'))
	if isPath(destPath)==False: myNote(eMsgHead,'sub-path not found'); return
	if isFile(xbmc.translatePath(os.path.join(destPath,fromFile)))==True: 
		myNote(eMsgHead,'filename already exists.')
		#_SaveFile(xbmc.translatePath(os.path.join(destPath,fromFile+'.bup')),_OpenFile(xbmc.translatePath(os.path.join(destPath,fromFile))))
		CopyAFile(xbmc.translatePath(os.path.join(destPath,fromFile)),xbmc.translatePath(os.path.join(destPath,fromFile+'.bup')))
	r=popYN('Would you like to copy this plugin?',fromFile,'to:  '+destPath,'',n='Cancel',y='Copy It')
	#myNote(eMsgHead,'r='+str(r))
	if r==False: 
		popOK('Plugin could not be copied.',title=eMsgHead,line2='',line3='')
	else:
		if isFile(xbmc.translatePath(os.path.join(fomPath,fromFile)))==True:
			## \/ this method doesn't seem to work for graphics, so I've changed it over both in this tool and in tRepos.py.
			#_SaveFile(xbmc.translatePath(os.path.join(destPath,fromFile)),_OpenFile(xbmc.translatePath(os.path.join(fomPath,fromFile))))
			CopyAFile(xbmc.translatePath(os.path.join(fomPath,fromFile)),xbmc.translatePath(os.path.join(destPath,fromFile)))
			popOK('File should now be copied.',title=eMsgHead,line2='',line3='')
	
	
	#

def CopyPlugin(title):
	try: _addon.resolve_url(url)
	except: t=''
	#workingPath
	#isPath
	#isFile
	eMsgHead='Copy Plugin'+title
	if isPath(workingPath)==False: myNote(eMsgHead,'can not find path to copy file from.')
	if isFile(xbmc.translatePath(os.path.join(workingPath,title)))==False: myNote(eMsgHead,'can not find file to copy from.')
	#if isPath(workingPath)==False: myNote(eMsgHead,'can not find path to copy file from.')
	
	destFolder1='script.module.urlresolver'; destPath=xbmc.translatePath(os.path.join(ps('special.home.addons'),destFolder1))
	debob(destPath); myNote(eMsgHead,'looking for folder: '+destFolder1)
	if isPath(destPath)==True: CopyPlugin2(workingPath,title,destPath); return
	myNote(eMsgHead,'not found: '+destFolder1)
	destPath=xbmc.translatePath(os.path.join(ps('special.home.addons'),'script.module.urlresolver-master'))
	debob(destPath); myNote(eMsgHead,'looking for folder: '+destFolder1)
	if isPath(destPath)==True: CopyPlugin2(workingPath,title,destPath); return
	myNote(eMsgHead,'not found: '+destFolder1)
	destPath=xbmc.translatePath(os.path.join(ps('special.home.addons'),'script.module.urlresolver-2.0.9'))
	debob(destPath); myNote(eMsgHead,'looking for folder: '+destFolder1)
	if isPath(destPath)==True: CopyPlugin2(workingPath,title,destPath); return
	myNote(eMsgHead,'not found: '+destFolder1)
	destPath=xbmc.translatePath(os.path.join(ps('special.home.addons'),'script.module.urlresolver-1.0.0'))
	debob(destPath); myNote(eMsgHead,'looking for folder: '+destFolder1)
	if isPath(destPath)==True: CopyPlugin2(workingPath,title,destPath); return
	myNote(eMsgHead,'not found: '+destFolder1)
	popOK('Plugin could not be copied.',title=eMsgHead,line2='',line3='')
	#

def SectionMenu():
	cNumber ='8'; cNumber2='2'; cNumber3='4'; 
	_addon.add_directory({'mode':'About','site':site},{'title':cFL_('About',colors['9'])},is_folder=False,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	for root, d, names in os.walk(workingPath):
		if root==workingPath:
			#deb('root',root); deb('dir',str(len(d))) #; debob(names)
			for filename in names:
				fe=getFileExtension(filename); fullF=xbmc.translatePath(os.path.join(root,filename))
				if (fe=='py') and (isFile(fullF)==True):
					pyName=filename[:-3]; pyTitle=filename[:-3]; img=_artIcon; fimg=_artFanart
					if pyTitle[:1] is not '[': pyTitle=cFL_(pyTitle,colors[cNumber])
					_addon.add_directory({'mode':'CopyPlugin','site':site,'title':filename,'url':filename},{'title':pyTitle+ps('filemarker')},is_folder=False,fanart='https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash4/c0.32.851.315/p851x315/1052535_473020589449050_121345808_o.jpg',img='http://www.xbmchub.com/forums/images/styles/ShinyBlue/style/logo.png')
	#
	#
	#
	#
	#_addon.add_directory({'mode':'TextBoxFile','url':xbmc.translatePath(os.path.join(_addonPath,'resources','urlresolver','list.txt')),'title':cFL('My list.txt for (UrlResolver) related information.',colors['9'])},{'title':cFL_('List.txt [Local]',colors[cNumber2])},is_folder=False,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'TextBoxFile','url':xbmc.translatePath(os.path.join(_addonPath,'changelog.txt')),'title':cFL('ChangeLog',colors['9'])},{'title':cFL_('ChangeLog  [Local]',colors[cNumber2])},is_folder=False,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'Settings'}, 			 {'title':  cFL_('Plugin Settings',colors[cNumber2])}			,is_folder=False,img=_artIcon,fanart=_artFanart)
	#_addon.add_directory({'mode':'ResolverSettings'},{'title':  cFL_('Url-Resolver Settings',colors[cNumber3])},is_folder=False,img=_artIcon,fanart=_artFanart)
	#_addon.add_directory({'mode':'ResolverUpdateHostFiles'},{'title':  cFL_('Url-Resolver Update Host Files',colors[cNumber3])},is_folder=False,img=_artIcon,fanart=_artFanart)
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
	elif (mode=='About'): 				About()
	#elif (mode=='FavList'): 			Fav_List(site,section)
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
	
	#

mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
