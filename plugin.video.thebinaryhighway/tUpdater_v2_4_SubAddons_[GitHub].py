### ############################################################################################################
###	#	
### # Project: 			#		Updater Tool for Sub-Addons
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
from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile,isPath,isFile,popYN,_SaveFile,popOK,CopyAFile,RefreshList,DownloadThis,getFileExtension)

### ############################################################################################################
### ############################################################################################################
SiteName='Updater v2b For Sub-Addons  [GitHub]'
SiteTag='file updater v2b for Sub-Addons'
mainSite=''
iconSite='http://i.imgur.com/ZpOLr1h.png' #'http://i.imgur.com/0zsWiGB.png' #_artIcon
fanartSite='http://s9.postimg.org/6izlt73n3/1011445_473021149448994_84427075_n.jpg' #_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan'}
#fanart='http://i.imgur.com/UtL1F8j.png',img='http://i.imgur.com/0zsWiGB.png')

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

workingPath=xbmc.translatePath(os.path.join(_addonPath,'resources','zips'))
#workingUrl='https://dl.dropboxusercontent.com/u/2259047/xbmc/theanimehighwayremake/packs/'
workingUrl='http://github.com/HIGHWAY99/repository.thehighway/raw/master/repo/thebinaryhighway/packs/'
workingFile='subaddons.txt'
workingFileWP=xbmc.translatePath(os.path.join(_addonPath,workingFile))
checkedFile='subaddons__.txt'
checkedFileWP=xbmc.translatePath(os.path.join(_addonPath,checkedFile))

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
		m+=CR+'* This tool is to allow you to update peices handled within this addon.'
		m+=CR+'* This version of the my Updater Tool allows the downloading of a file that contains a list of the updates with their filename and a path tag which this tool uses to determine where to send the file(s) to.'
		m+=CR+'* Hides filenames from the list after you\'ve downloaded them.'
		m+=CR+CR+'Notes:  '
		m+=CR+'* This tool is still being worked on, so things may not be perfect yet.'
		m+=CR+'* If you need to redownload the same file, you may via "Updater v2b", or simply edit the updating__.txt / subaddons__.txt to remove the file or empty/delete the file... thus making it available on the list again.'
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
		checkedFileList=_OpenFile(checkedFileWP)
		checkedFileList+="\n'"+filename+"'"
		_SaveFile(checkedFileWP,checkedFileList)
		myNote('Updater','Completed')
		RefreshList()
	except:
		debob('error during updater process.')
		myNote('Updater','may have failed.')

def Update_CustomUpdate(path,filename):
	if (len(path)==0) or (len(filename)==0): return
	##filename='art.zip'
	url=workingUrl+filename
	if   (path.lower()=='/addon/') or (path.lower()=='/'): destpath=xbmc.translatePath(_addonPath)
	elif (path.lower()=='/addon/resources/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources'))
	elif (path.lower()=='/addon/resources/misc/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','misc'))
	elif (path.lower()=='/addon/resources/urlresolver/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','urlresolver'))
	elif (path.lower()=='/addon/resources/repos/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'resources','repos'))
	elif (path.lower()=='/addon/art/'): destpath=xbmc.translatePath(os.path.join(_addonPath,'art'))
	#elif (path.lower()=='/addon/'): 
	else: return
	##destpath=xbmc.translatePath(os.path.join(_addonPath,'art'))
	Updater(url,filename,destpath)

def TP(s): return xbmc.translatePath(s)
def TPap(s,fe='.py'): return xbmc.translatePath(os.path.join(_addonPath,s+fe))

def SectionMenu():
	cNumber ='8'; cNumber2='2'; cNumber3='4'; 
	_addon.add_directory({'mode':'About','site':site},{'title':cFL_('About',colors['9'])},is_folder=False,fanart=fanartSite,img='http://i.imgur.com/0h78x5V.png') # iconSite
	if isFile(checkedFileWP)==False: _SaveFile(checkedFileWP,'')
	checkedFileList=_OpenFile(checkedFileWP)
	if isFile(workingFileWP)==False: MiscTag='  '+cFL('<<','red')+'  ['+cFL('Use Updater','blue')+']'
	else: MiscTag=''
	_addon.add_directory({'mode':'CustomUpdate','path':'/addon/','filename':workingFile,'url':workingFile,'site':site},{'title':cFL(cFL_('Click to update the data file for updates.'+MiscTag,colors['9']),colors['0'])+'[CR][May Take a few moments.]'},is_folder=False,fanart=fanartSite,img=iconSite)
	if isFile(workingFileWP)==True: _addon.add_directory({'mode':'TextBoxFile','url':workingFileWP,'title':cFL('Updates',colors['9'])},{'title':cFL_('Read Update\' documentation',colors[cNumber2])},is_folder=False,fanart=fanartSite,img=iconSite)
	#DownloadThis(workingUrl+workingFile,workingFile,_addonPath,useResolver=False)
	#if isFile(workingFileWP)==False: DownloadThis(workingUrl+workingFile,workingFile,_addonPath,useResolver=False)
	if isFile(workingFileWP)==True:
		dd=_OpenFile(workingFileWP)
		debob(dd)
		s="'(.*?)'\s*:\s*'([A-Za-z0-9\.\-_\[\]\(\)]*)'"; 
		try: matches=re.compile(s).findall(dd) #,re.DOTALL
		except: matches=''
		ItemCount=len(matches)
		if ItemCount > 0:
			debob(matches)
			for _path,_name in matches:
				if not _name in checkedFileList:
					img=iconSite; fimg=fanartSite; 
					_title=cFL(_name,colors[cNumber])+CR+' ['+_path+']'
					pars={'mode':'CustomUpdate','path':_path,'filename':_name,'site':site,'section':section,'url':_name}
					_addon.add_directory(pars,{'title':_title},is_folder=False,fanart=fimg,img=img,total_items=ItemCount)
		#
	#
	#
	eod()
	return
	#
	_addon.add_directory({'mode':'TextBoxUrl','site':site,'title':'Updater Info','url':workingUrl+'updater.txt'},{'title':cFL_('Check Updater Info',colors['9'])},is_folder=False,fanart='http://s9.postimg.org/6izlt73n3/1011445_473021149448994_84427075_n.jpg',img='http://s9.postimg.org/uy7tu92jz/1013960_471938356223940_1093377719_n.jpg')
	#
	_addon.add_directory({'mode':'UpdateURPlugs','site':site,'url':'URPlugs'},{'title':cFL_('Update: Host Plugins List [Sub-Folder]',colors[cNumber])},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'mode':'UpdateRepos','site':site,'url':'Repos'},{'title':cFL_('Update: Repo List',colors[cNumber])},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'mode':'UpdateMisc','site':site,'url':'Misc'},{'title':cFL_('Update: Misc [Sub-Folder]',colors[cNumber])},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'mode':'UpdateArt','site':site,'url':'Art'},{'title':cFL_('Update: Art [Sub-Folder]',colors[cNumber])},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'mode':'UpdateRes','site':site,'url':'Res'},{'title':cFL_('Update: Resources [Sub-Folder]',colors[cNumber])},is_folder=False,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'mode':'UpdateAddon','site':site,'url':'Addon'},{'title':cFL_('Update: Addon [This Addon]',colors[cNumber])},is_folder=False,fanart=fanartSite,img=iconSite)
	#_addon.add_directory({'mode':'Update','site':site},{'title':cFL_('Update: Repo List',colors[cNumber])},is_folder=False,fanart=fanartSite,img=iconSite)
	#
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
	elif (mode=='UpdateRepos'): 	Update_Repos()
	elif (mode=='UpdateURPlugs'): Update_UrlResolverPlugins()
	elif (mode=='UpdateMisc'): 		Update_Misc()
	elif (mode=='UpdateAddon'): 	Update_Addon()
	elif (mode=='UpdateRes'): 		Update_Resources()
	elif (mode=='UpdateArt'): 		Update_Art()
	elif (mode=='CustomUpdate'): 	Update_CustomUpdate(addpr('path',''),addpr('filename',''))
	#elif (mode=='FavList'): 			Fav_List(site,section)
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
	
	#

mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
