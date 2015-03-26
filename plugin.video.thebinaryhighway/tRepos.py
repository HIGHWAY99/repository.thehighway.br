### ############################################################################################################
###	#	
### # Project: 			#		Respository Tool
### # Author: 			#		The Highway
### # Description: 	#		
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
SiteName='Add Repositories'
SiteTag='urlResolver'
mainSite=''
iconSite='http://www.xbmchub.com/blog/wp-content/uploads/Screen-Shot-2013-06-30-at-1.13.58-PM.jpg' #_artIcon
fanartSite='http://xbmc.org/wp-content/uploads/zappy-frodo-background-680-600x336.jpg' #_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan'}

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

workingPath=xbmc.translatePath(os.path.join(_addonPath,'resources','repos'))
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
		m+=CR+'* Create a folder for a repository and copy  it\'s .xml (sometimes fanart.jpg, icon.png, and changelog.txt) to the folder.'
		m+=CR+CR+'Notes:  '
		m+=CR+'* This tool will allow the isntalling of Repositories.'
		m+=CR+'* A Restart of XBMC might be needed before the Repository shows up within xbmc.'
		m+=CR+'* I\'m not responsible for the any Repository(s) on this list may have.'
		m+=CR+'* Those Repositories on this list are either chosen by me because I like them, or cause they were asked to be included and slightly looked at minorly by me.'
		m+=CR+'* If you would like your repository added to this list, I\'ll consider it, but it\'ll most likely be a addon.xml file only, possibly with a lower version number edited in so that it\'ll be able to update to your own current version with changelog, fanart, and icon by the user by after they have it.  This is obviously to save space for sake of filesize of my overall project.'
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
	debob([fomPath,fromFile,toPath])
	eMsgHead='Copy File'+fromFile
	destPath=xbmc.translatePath(toPath) #xbmc.translatePath(os.path.join(toPath,'lib','urlresolver','plugins'))
	if isPath(destPath)==True: myNote(eMsgHead,'Repository seems to already be installed: '+destFolder1); #return
	if isFile(xbmc.translatePath(os.path.join(destPath,fromFile)))==True: 
		myNote(eMsgHead,'filename already exists.')
		_SaveFile(xbmc.translatePath(os.path.join(destPath,fromFile+'.bup')),_OpenFile(xbmc.translatePath(os.path.join(destPath,fromFile))))
	r=popYN('Would you like to copy this File?',fromFile,'to:  '+destPath,'',n='Cancel',y='Copy It')
	#myNote(eMsgHead,'r='+str(r))
	if r==False: popOK('File could not be copied.',title=eMsgHead,line2='',line3='')
	else:
		if isPath(destPath)==False: os.mkdir(destPath)
		if isPath(destPath)==False: myNote(eMsgHead,'Could not create folder: '+destFolder1); #return
		#
		ttFileName='fanart.jpg'; tFrom=xbmc.translatePath(os.path.join(fomPath,fromFile[:-4]+'.'+ttFileName)); tTo=xbmc.translatePath(os.path.join(destPath,ttFileName))
		if (isFile(tFrom)==True) and (isFile(tTo)==False): CopyAFile(tFrom,tTo)
		ttFileName='icon.png'; tFrom=xbmc.translatePath(os.path.join(fomPath,fromFile[:-4]+'.'+ttFileName)); tTo=xbmc.translatePath(os.path.join(destPath,ttFileName))
		if (isFile(tFrom)==True) and (isFile(tTo)==False): CopyAFile(tFrom,tTo)
		ttFileName='changelog.txt'; tFrom=xbmc.translatePath(os.path.join(fomPath,fromFile[:-4]+'.'+ttFileName)); tTo=xbmc.translatePath(os.path.join(destPath,ttFileName))
		if (isFile(tFrom)==True) and (isFile(tTo)==False): CopyAFile(tFrom,tTo)
		ttFileName='addon.xml'; tFrom=xbmc.translatePath(os.path.join(fomPath,fromFile)); tTo=xbmc.translatePath(os.path.join(destPath,ttFileName))
		if (isFile(tFrom)==True) and (isFile(tTo)==False): CopyAFile(tFrom,tTo); popOK('File should now be copied.',title=eMsgHead,line2='',line3='')
	#

def CopyPlugin(title):
	try: _addon.resolve_url(url)
	except: t=''
	#workingPath
	#isPath
	#isFile
	eMsgHead='Copy File'+title
	if isPath(workingPath)==False: myNote(eMsgHead,'can not find path to copy file from.')
	if isFile(xbmc.translatePath(os.path.join(workingPath,title)))==False: myNote(eMsgHead,'can not find file to copy from.')
	#if isPath(workingPath)==False: myNote(eMsgHead,'can not find path to copy file from.')
	
	destFolder1=title[:-4]; destPath=xbmc.translatePath(os.path.join(ps('special.home.addons'),destFolder1))
	debob(destPath); myNote(eMsgHead,'looking for folder: '+destFolder1)
	if isPath(destPath)==False: CopyPlugin2(workingPath,title,destPath); return
	myNote(eMsgHead,'Repository seems to already be installed: '+destFolder1)
	popOK('File could not be copied.',title=eMsgHead,line2='',line3='')
	#

def SectionMenu():
	cNumber ='8'; cNumber2='2'; cNumber3='4'; cNumber4='12'; 
	_addon.add_directory({'mode':'About','site':site},{'title':cFL_('About',colors['9'])},is_folder=False,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	_addon.add_directory({'site':site,'mode':'UpdateLocalAddons'},{'title':cFL_('Update Local Addons (XBMC) [CR][Run after select a Repository(s)]',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'site':site,'mode':'UpdateAddonRepos'},{'title':cFL_('Check Repositories Addon Updates (XBMC)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	for root, d, names in os.walk(workingPath):
		if root==workingPath:
			#deb('root',root); deb('dir',str(len(d))) #; debob(names)
			for filename in names:
				fe=getFileExtension(filename); fullF=xbmc.translatePath(os.path.join(root,filename))
				if (fe=='xml') and (isFile(fullF)==True):
					pyName=filename[:-4]; pyTitle=filename[:-4]; img=_artIcon; fimg=_artFanart
					if pyTitle[:1] is not '[': pyTitle=cFL_(pyTitle,colors[cNumber])
					if isFile(fullF[:-4]+'.icon.png')==True: __img=fullF[:-4]+'.icon.png'
					else: __img='http://www.xbmchub.com/forums/images/styles/ShinyBlue/style/logo.png'
					if isFile(fullF[:-4]+'.fanart.jpg')==True: __fanart=fullF[:-4]+'.fanart.jpg'
					else: __fanart='https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash4/c0.32.851.315/p851x315/1052535_473020589449050_121345808_o.jpg'
					_addon.add_directory({'mode':'CopyPlugin','site':site,'title':filename,'url':filename},{'title':pyTitle+ps('filemarker')},is_folder=False,fanart=__fanart,img=__img)
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
	elif (mode=='UpdateAddonRepos'): 		xbmc.executebuiltin("XBMC.UpdateAddonRepos()")
	elif (mode=='UpdateLocalAddons'): 	xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
	#elif (mode=='FavList'): 			Fav_List(site,section)
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
	
	#

mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
