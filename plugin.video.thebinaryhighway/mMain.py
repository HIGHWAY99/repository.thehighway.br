### ############################################################################################################
###	#	
### # Project: 			#		Menu - Main Menu by default
### # Author: 			#		The Highway
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re

from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,_OpenFile,isFile)

### ############################################################################################################
### ############################################################################################################
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan'}
collartag='m'

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
### ############################################################################################################
### ############################################################################################################










### ############################################################################################################
### ############################################################################################################
def TP(s): return xbmc.translatePath(s)
def TPap(s,fe='.py'): return xbmc.translatePath(os.path.join(_addonPath,s+fe))

def Menu_MainMenu():
	tcntr={}
	for aletter in MyAlphabet: tcntr[aletter]='0'
	for root, d, names in os.walk(_addonPath):
		if root==_addonPath:
			#deb('root',root); deb('dir',str(len(d))) #; debob(names)
			for filename in names:
				fe=getFileExtension(filename); fullF=xbmc.translatePath(os.path.join(root,filename))
				if (fe=='py') and (isFile(fullF)==True):
					for aletter in MyAlphabet:
						if (filename[:1]==aletter): tcntr[aletter]=str(int(tcntr[aletter])+1)
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
	cNumber ='8'; cNumber2='2'; cNumber3='4'; cNumber4='9'
	
	if isFile(TPap('mLiveStreams'))==True: _addon.add_directory({'mode':'SectionMenu','site':'mLiveStreams'},{'title':cFL_('Live Streams'+'  ['+cFL(tcntr['l'],colors['10'])+']',colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuLiveStreams'))
	if isFile(TPap('mMovies_and_TV'))==True: _addon.add_directory({'mode':'SectionMenu','site':'mMovies_and_TV'},{'title':cFL_('Movies and TV'+'  ['+cFL(tcntr['s'],colors['10'])+']',colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuMoviesTV'))
	if isFile(TPap('mAnime'))==True: _addon.add_directory({'mode':'SectionMenu','site':'mAnime'},{'title':cFL_('Anime and Cartoons'+'  ['+cFL(tcntr['a'],colors['10'])+']',colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuAnime'))
	if isFile(TPap('mSports'))==True: _addon.add_directory({'mode':'SectionMenu','site':'mSports'},{'title':cFL_('Sports'+'  ['+cFL(tcntr['r'],colors['10'])+']',colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuSports'))
	if isFile(TPap('mAudio'))==True: _addon.add_directory({'mode':'SectionMenu','site':'mAudio'},{'title':cFL_('Audio, Music, Radio...'+'  ['+cFL(tcntr['u'],colors['10'])+']',colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuAudio'))
	if isFile(TPap('mImage'))==True: _addon.add_directory({'mode':'SectionMenu','site':'mImage'},{'title':cFL_('Graphic, Image, Manga...'+'  ['+cFL(tcntr['i'],colors['10'])+']',colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuImages'))
	if isFile(TPap('mOthers'))==True: _addon.add_directory({'mode':'SectionMenu','site':'Others'},{'title':cFL_('Others'+'  ['+cFL(tcntr['v'],colors['10'])+']',colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuOthers'))
	if isFile(TPap('mAdult'))==True: _addon.add_directory({'mode':'SectionMenu','site':'mAdult'},{'title':cFL_('Adult (18+)'+'  ['+cFL(tcntr['p'],colors['10'])+']'+'[CR](Make sure your ove appropriate age to legally view such content in your area.)',colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuAdult'))
	if isFile(TPap('updating','.txt'))==False: MiscTag='  '+cFL('<<','red')+'  ['+cFL('Use Updater','blue')+']'
	else: MiscTag=''
	if isFile(TPap('mMisc'))==True: _addon.add_directory({'mode':'SectionMenu','site':'Misc'},{'title':cFL_('Misc. (Tools and such)'+'  ['+cFL(tcntr['t']+'+',colors['10'])+']'+MiscTag,colors[cNumber4])},is_folder=True,fanart=_artFanart,img=ps('iiMenuMisc'))
	if isFile(TPap('mMisc'))==True: _addon.add_directory({'mode':'XBMCHUB','site':'mMisc'},{'title':cFL_('#'+cFL('XBMCHUB','blue')+' @ '+cFL('irc.freenode.net','red')+' [CR]www.'+cFL('XBMCHUB','blue')+'.com',colors['9'])},is_folder=False,fanart=ps('fiHubIrc'),img=ps('iiHubIrc'))
	#
	#_addon.add_directory({'mode':'SectionMenu','site':'Others'},{'title':cFL_('Others'+'  ['+cFL(tcntr['v'],colors['10'])+']',colors[cNumber4])},is_folder=True,fanart='http://s9.postimg.org/6izlt73n3/1011445_473021149448994_84427075_n.jpg',img='http://s9.postimg.org/uy7tu92jz/1013960_471938356223940_1093377719_n.jpg')
	#
	#_addon.add_directory({'mode':'SectionMenu','site':'AnimeGet'},{'title':cFL_('AnimeGet',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'Anime44'},{'title':cFL_('Anime44',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'AnimePlus'},{'title':cFL_('AnimePlus *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'AnimeZone'},{'title':cFL_('AnimeZone *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'DubbedAnimeOn'},{'title':cFL_('DubbedAnimeOn *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'DubHappyeu'},{'title':cFL_('DubHappy.eu *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	#_addon.add_directory({'mode':'SectionMenu','site':'WatchDub'},{'title':cFL_('WatchDub *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	##_addon.add_directory({'mode':'SectionMenu','site':'GoodDrama'},{'title':cFL_('GoodDrama *',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
	##_addon.add_directory({'mode':'SectionMenu','site':'iLiveTo'},{'title':cFL_('iLiveTo',colors[cNumber])},is_folder=True,fanart=_artFanart,img=_artIcon)
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

Menu_MainMenu()
### ############################################################################################################
### ############################################################################################################
