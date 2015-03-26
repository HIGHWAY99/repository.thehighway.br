### ############################################################################################################
###	#	
### # Project: 			#		Menu - Misc, Tools, ....
### # Author: 			#		The Highway
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re

from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile)

### ############################################################################################################
### ############################################################################################################
SiteName='Misc. (Tools and such)'
SiteTag='misc'
mainSite=''
iconSite='' #_artIcon
fanartSite='' #_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan'}
collartag='t'

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']
### ############################################################################################################
### ############################################################################################################
site=addpr('site','')
section=addpr('section','')
url=addpr('url','')
sections={'series':'series','movies':'movies'}
thumbnail=addpr('img','')
fanart=addpr('fanart','')
page=addpr('page','')
### ############################################################################################################
### ############################################################################################################
def XBMCHUB(head=''+cFL(SiteName,'blueviolet')+'',m=''):
	m=''
	if len(m)==0:
		##m+='Site Name:  '+SiteName+CR+'Site Tag:  '+SiteTag+CR+'Site Domain:  '+mainSite+CR+'Site Icon:  '+iconSite+CR+'Site Fanart:  '+fanartSite
		m+=cFL('XBMCHUB','blue')
		m+=CR+cFL('Url:  ',colors['11'])+cFL('http://www.xbmchub.com',colors['10'])
		m+=CR+cFL('Forum:  ',colors['11'])+cFL('http://www.xbmchub.com/forums/',colors['10'])
		m+=CR+cFL('Fusion:  ',colors['11'])+cFL('http://www.xbmchub.com/fusion/',colors['10'])
		m+=CR+cFL('Fusion (old):  ',colors['11'])+cFL('http://fusion.xbmchub.com/',colors['10'])
		m+=CR+cFL('IRC Chat - Channel:  ',colors['11'])+cFL('#XBMCHUB',colors['1'])
		m+=CR+cFL('IRC Chat - Server:  ',colors['11'])+cFL('irc.freenode.net',colors['10'])
		m+=CR+cFL('IRC Chat - WebApp:  ',colors['11'])+cFL('http://webchat.freenode.net/?channels=xbmchub&uio=d4',colors['10'])
		m+=CR+cFL('IRC Chat - Regular Idlers:  ',colors['11'])+cFL(cFL('TwiztedZero','green')+' | '+cFL('HIGHWAY99','tan'),colors['10'])
		m+=CR+''
		#m+=CR+'Age:  Please make sure you are of a valid age to watch the material shown.'
		m+=CR+''
		m+=CR+''
		m+=CR+''
		#m+=CR+'* '
		#m+=CR+'* '
		m+=CR+''
		m+=CR+CR+ps('ReferalMsg')
		m+=CR+''
		m+=CR+''
		m+=CR+CR+CR+CR+CR+CR+CR+CR+CR+CR+'[COLOR black].[/COLOR]'
	String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
	#RefreshList()






### ############################################################################################################
### ############################################################################################################
def TP(s): return xbmc.translatePath(s)
def TPap(s,fe='.py'): return xbmc.translatePath(os.path.join(_addonPath,s+fe))


def Menu_CustomMenu():
	#AnimeGet
	#Anime44
	#AnimePlus
	#AnimeZone
	#DubbedAnimeOn
	#DubHappy.eu
	#WatchDub
	#GoodDrama
	#
	#
	cNumber ='8'; cNumber2='2'; cNumber3='4'; cNumber4='12'
	#_addon.add_directory({'mode':'SectionMenu','site':'AnimeGet'},{'title':cFL_('AnimeGet',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'Anime44'},{'title':cFL_('Anime44',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'AnimePlus'},{'title':cFL_('AnimePlus *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'AnimeZone'},{'title':cFL_('AnimeZone *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'DubbedAnimeOn'},{'title':cFL_('DubbedAnimeOn *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'DubHappyeu'},{'title':cFL_('DubHappy.eu *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'WatchDub'},{'title':cFL_('WatchDub *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'GoodDrama'},{'title':cFL_('GoodDrama *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'iLiveTo'},{'title':cFL_('iLiveTo',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#
	#_addon.add_directory({'mode':'SectionMenu','site':'ResolverPlugins'},{'title':cFL_('Attempt to Fix/Add [CR]Resolver Host Plugins',colors[cNumber3])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#
	#
	for root, d, names in os.walk(_addonPath):
		if root==_addonPath:
			#deb('root',root); deb('dir',str(len(d))) #; debob(names)
			for filename in names:
				fe=getFileExtension(filename); fullF=xbmc.translatePath(os.path.join(root,filename))
				if (filename[:1]==collartag) and (fe=='py') and (isFile(fullF)==True):
					pyName=filename[:-3]
					tt=_OpenFile(fullF)
					try: 
						if   "SiteName='" in tt: pyTitle=re.compile("SiteName='(.+?)'").findall(tt)[0]
						elif 'SiteName="' in tt: pyTitle=re.compile('SiteName="(.+?)"').findall(tt)[0]
						elif "SiteName = '" in tt: pyTitle=re.compile("SiteName = '(.+?)'").findall(tt)[0]
						elif 'SiteName = "' in tt: pyTitle=re.compile('SiteName = "(.+?)"').findall(tt)[0]
						else: pyTitle=filename[1:-3]
					except: pyTitle=filename[1:-3]
					try: 
						if   "iconSite='" in tt: img=re.compile("iconSite='(.+?)'").findall(tt)[0]
						elif 'iconSite="' in tt: img=re.compile('iconSite="(.+?)"').findall(tt)[0]
						elif "iconSite = '" in tt: img=re.compile("iconSite = '(.+?)'").findall(tt)[0]
						elif 'iconSite = "' in tt: img=re.compile('iconSite = "(.+?)"').findall(tt)[0]
						else: img=_artIcon
					except: img=_artIcon
					try: 
						if   "fanartSite='" in tt: fimg=re.compile("fanartSite='(.+?)'").findall(tt)[0]
						elif 'fanartSite="' in tt: fimg=re.compile('fanartSite="(.+?)"').findall(tt)[0]
						elif "fanartSite = '" in tt: fimg=re.compile("fanartSite = '(.+?)'").findall(tt)[0]
						elif 'fanartSite = "' in tt: fimg=re.compile('fanartSite = "(.+?)"').findall(tt)[0]
						else: fimg=_artFanart
					except: fimg=_artFanart
					MiscTag=''
					if (pyName=='tUpdater2') or (pyName=='tUpdater2b'):
						if isFile(TPap('updating','.txt'))==False: MiscTag='  '+cFL('<<','red')+'  ['+cFL('Use Updater','blue')+']'
						else: MiscTag=''
					elif (pyName=='tUpdater_4_SubAddons_[DropBox]') or (pyName=='tUpdater_4_SubAddons_[GitHub]'):
						if isFile(TPap('subaddons','.txt'))==False: MiscTag='  '+cFL('<<','red')+'  ['+cFL('Use Updater','blue')+']'
						else: MiscTag=''
					if pyTitle[:1] is not '[': pyTitle=cFL_(pyTitle,colors['0'])
					_addon.add_directory({'mode':'SectionMenu','site':pyName},{'title':pyTitle+ps('filemarker')+MiscTag},is_folder=True,fanart=fimg,img=img)
	#
	_addon.add_directory({'mode':'XBMCHUB','site':site},{'title':cFL_('#'+cFL('XBMCHUB','blue')+' @ '+cFL('irc.freenode.net','red')+' [CR]www.'+cFL('XBMCHUB','blue')+'.com',colors['9'])},is_folder=False,fanart=ps('fiHubIrc'),img=ps('iiHubIrc'))
	_addon.add_directory({'mode':'TextBoxFile','site':site,'title':'XBMC.Log [File]','url':xbmc.translatePath(os.path.join('special://logpath','xbmc.log'))},{'title':cFL_('View XBMC.Log',colors['9'])},is_folder=False,fanart='http://s9.postimg.org/6izlt73n3/1011445_473021149448994_84427075_n.jpg',img='http://s9.postimg.org/uy7tu92jz/1013960_471938356223940_1093377719_n.jpg')
	_addon.add_directory({'mode':'TextBoxFile','site':site,'title':'XBMC.old.Log [File]','url':xbmc.translatePath(os.path.join('special://logpath','xbmc.old.log'))},{'title':cFL_('View XBMC.old.Log',colors['9'])},is_folder=False,fanart='http://s9.postimg.org/6izlt73n3/1011445_473021149448994_84427075_n.jpg',img='http://s9.postimg.org/uy7tu92jz/1013960_471938356223940_1093377719_n.jpg')
	#
	#
	_addon.add_directory({'mode':'TextBoxFile','url':xbmc.translatePath(os.path.join(_addonPath,'resources','urlresolver','list.txt')),'title':cFL('My list.txt for (UrlResolver) related information.',colors['9'])},{'title':cFL_('List.txt [Local]',colors[cNumber2])},is_folder=False,fanart='https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash4/c0.32.851.315/p851x315/1052535_473020589449050_121345808_o.jpg',img='http://provoketive.com/wp-content/uploads/2012/02/list5.jpg')
	_addon.add_directory({'mode':'TextBoxFile','url':xbmc.translatePath(os.path.join(_addonPath,'changelog.txt')),'title':cFL('ChangeLog',colors['9'])},{'title':cFL_('ChangeLog  [Local]',colors[cNumber2])},is_folder=False,fanart='https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash4/c0.32.851.315/p851x315/1052535_473020589449050_121345808_o.jpg',img='http://www.carando.com/images/utility/paper.png')
	_addon.add_directory({'mode':'Settings'}, 			 {'title':  cFL_('Plugin Settings',colors[cNumber2])}			,is_folder=False,fanart=_artFanart,img=_artIcon)
	_addon.add_directory({'mode':'ResolverSettings'},{'title':  cFL_('Url-Resolver Settings',colors[cNumber3])},is_folder=False,fanart='http://i1204.photobucket.com/albums/bb404/ThisRoger/screenshot022.png',img='http://i887.photobucket.com/albums/ac80/Abrasher1/SkinnySidnature5WHEREHAVEYOUBEEN.png')
	#_addon.add_directory({'mode':'ResolverUpdateHostFiles'},{'title':  cFL_('Url-Resolver Update Host Files',colors[cNumber3])},is_folder=False,img=_artIcon,fanart=_artFanart)
	#_addon.add_directory({'site':site,'mode':'Settings'},{'title':cFL_('',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'site':site,'mode':'Settings'},{'title':cFL_('',colors[cNumber4])},is_folder=False,fanart=_artFanart,img=_artIcon)
	
	
	#
	eod()

### ############################################################################################################
### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
	if (mode=='SectionMenu'): 		Menu_CustomMenu()
	elif (mode=='SubMenu'): 			SubMenu() #(site,section)
	#elif (mode=='Listings'): 			Browse_List(url)
	#
	#elif (mode=='Search'): 				Search_Site(title=addpr('title',''),url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
	#elif (mode=='SearchLast'): 		Search_Site(title=addst('LastSearchTitle'+SiteTag),url=url,page=page,metamethod=addpr('metamethod',''),endit=tfalse(addpr('endit','true'))) #(site,section)
	#elif (mode=='About'): 				About()
	elif (mode=='XBMCHUB'): 			XBMCHUB()
	elif (mode=='XBMCLOG'): 			XBMCLOG(url,addpr('title',''))
	#
	#
	#elif (mode=='FavList'): 			Fav_List(site,section)
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
		
	#

mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))

### ############################################################################################################
### ############################################################################################################
