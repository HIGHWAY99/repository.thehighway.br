### ############################################################################################################
###	#	
### # Project: 			#		XBMC Commands
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
SiteName='XBMC Commands  [2013-10-17]'
SiteTag='XBMCCommands'
mainSite=''
iconSite='http://i.imgur.com/XMClMrQ.png' #'http://s9.postimg.org/uy7tu92jz/1013960_471938356223940_1093377719_n.jpg' #_artIcon
fanartSite='http://s9.postimg.org/6izlt73n3/1011445_473021149448994_84427075_n.jpg' #_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan'}

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

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


def SectionMenu():
	cNumber ='8'; cNumber2='2'; cNumber3='4'; cNumber4='12'
	_addon.add_directory({'mode':'About','site':site},{'title':cFL_('About',colors['9'])},is_folder=False,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	_addon.add_directory({'mode':'FixMouseMove','site':site},{'title':cFL_('Prevent exiting FullScreen due to Mouse Movement [CR]while watching a video. (Mouse.xml) [restart]',colors[cNumber])},is_folder=False,fanart='http://i00.i.aliimg.com/wsphoto/v1/673900382_2/T2-Air-Fly-Mouse-2-4G-3D-Motion-Stick-Remote-PC-Mouse-for-TV-Box-TV.jpg',img='http://i138.photobucket.com/albums/q260/Ygdrassil/stuff/Mouse-Keyboard-B-1815.jpg')
	#_addon.add_directory({'mode':'TextBoxFile','url':xbmc.translatePath(os.path.join(_addonPath,'resources','urlresolver','list.txt')),'title':cFL('My list.txt for (UrlResolver) related information.',colors['9'])},{'title':cFL_('List.txt [Local]',colors[cNumber2])},is_folder=False,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'TextBoxFile','url':xbmc.translatePath(os.path.join(_addonPath,'changelog.txt')),'title':cFL('ChangeLog',colors['9'])},{'title':cFL_('ChangeLog  [Local]',colors[cNumber2])},is_folder=False,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'Settings'}, 			 {'title':  cFL_('Plugin Settings',colors[cNumber2])}			,is_folder=False,img=_artIcon,fanart=_artFanart)
	#_addon.add_directory({'mode':'ResolverSettings'},{'title':  cFL_('Url-Resolver Settings',colors[cNumber3])},is_folder=False,img=_artIcon,fanart=_artFanart)
	#_addon.add_directory({'mode':'ResolverUpdateHostFiles'},{'title':  cFL_('Url-Resolver Update Host Files',colors[cNumber3])},is_folder=False,img=_artIcon,fanart=_artFanart)
	#
	_addon.add_directory({'site':site,'mode':'Mute'},{'title':cFL_('Mute/unMute Volume (XBMC)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'EjectTray'},{'title':cFL_('Eject/Close Tray',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'RefreshRSS'},{'title':cFL_('RefreshRSS (XBMC) *',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'System.Exec','url':'notepad'},{'title':cFL_('Notepad (Windows-Only)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'System.Exec','url':xbmc.translatePath(os.path.join('c:\\windows\\system32\\','notepad.exe'))+' "'+xbmc.translatePath(os.path.join(_addonPath,'changelog.txt'))+'"'},{'title':cFL_('Notepad /w XBMC.log (Windows-Only)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'System.Exec','url':xbmc.translatePath(os.path.join(_addonPath,'changelog.txt'))+'"'},{'title':cFL_('Open XBMC.log /w Default App (Windows-Only)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'PlayDVD'},{'title':cFL_('PlayDVD (XBMC) *',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'ReloadSkin'},{'title':cFL_('ReloadSkin (XBMC)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'UpdateAddonRepos'},{'title':cFL_('Update Addon Repositories (XBMC)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'UpdateLocalAddons'},{'title':cFL_('Update Local Addons (XBMC)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'Weather.Refresh'},{'title':cFL_('Weather.Refresh *',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'ToggleDebug'},{'title':cFL_('Toggle Debug (XBMC)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'Minimize'},{'title':cFL_('Minimize (XBMC)',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'site':site,'mode':'ActivateScreensaver'},{'title':cFL_('Activate Screensaver',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	##_addon.add_directory({'site':site,'mode':'XBMCHelp'},{'title':cFL_('XBMCHelp',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
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
	elif (mode=='About'): 				About()
	#
	elif (mode=='RefreshRSS'): 					xbmc.executebuiltin("XBMC.RefreshRSS()")
	elif (mode=='EjectTray'): 					xbmc.executebuiltin("XBMC.EjectTray()")
	elif (mode=='Mute'): 								xbmc.executebuiltin("XBMC.Mute()")
	elif (mode=='System.Exec'): 				xbmc.executebuiltin("XBMC.System.Exec(%s)" % url)
	elif (mode=='System.ExecWait'): 		xbmc.executebuiltin("XBMC.System.ExecWait(%s)" % url)
	elif (mode=='PlayDVD'): 						xbmc.executebuiltin("XBMC.PlayDVD()")
	elif (mode=='ReloadSkin'): 					xbmc.executebuiltin("XBMC.ReloadSkin()")
	elif (mode=='UpdateAddonRepos'): 		xbmc.executebuiltin("XBMC.UpdateAddonRepos()")
	elif (mode=='UpdateLocalAddons'): 	xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
	elif (mode=='Weather.Refresh'): 		xbmc.executebuiltin("XBMC.Weather.Refresh()")
	elif (mode=='ToggleDebug'): 				xbmc.executebuiltin("XBMC.ToggleDebug()")
	elif (mode=='Minimize'): 						xbmc.executebuiltin("XBMC.Minimize()")
	elif (mode=='ActivateScreensaver'): xbmc.executebuiltin("XBMC.ActivateScreensaver()")
	#elif (mode=='XBMCHelp'): 						xbmc.executebuiltin("XBMC.Help()")
	#elif (mode=='RefreshRSS'): 					xbmc.executebuiltin("XBMC.RefreshRSS()")
	#
	##_addon.add_directory({'site':site,'mode':'XBMCHelp'},{'title':cFL_('XBMCHelp',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	#elif (mode=='FavList'): 			Fav_List(site,section)
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
	
	#

mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
