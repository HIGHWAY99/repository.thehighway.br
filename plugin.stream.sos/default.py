#############################################################################
#############################################################################
import common
from common import *
from common import (addon_id,addon_name,addon_path)
if (tfalse(getSet("enable-cat-all"))==True): Testing=True
else: Testing=False
#############################################################################
#############################################################################
def Menu0(): ## Main Menu ##
	try:
		AcInfo=grabAcInfo(True,True,False,False); catThumb=''; DoD=getSet("custom-url2"); 
		if len(AcInfo)==0: eod(); return
		if (tfalse(getSet("enable-custom-url2"))==False) or (len(DoD)==0): DoD=zCoDeSz('durl')
		Page=zCoDeSz('us2b')+DoD+zCoDeSz('dcat2b')+AcInfo; 
		if Testing==True: debob({'Page':Page})
		#htmlCat=nolines(getURL(Page)); #deb("Length of HTML",str(len(htmlCat))); 
		htmlCat=nolines(getURL_WithCaching(Page)); #deb("Length of HTML",str(len(htmlCat))); 
		if len(htmlCat)==0: eod(); return
		try: r=re.compile(zCoDeSz('re1')).findall(htmlCat)[0]
		except: r=[]
		if r:
				htmlCat=r; htmlCat=htmlCat.replace(zCoDeSz('rp1a'),zCoDeSz('rp1b'))
				try: r=re.compile(zCoDeSz('re2')).findall(htmlCat)
				except: r=[]
				if r:
					iC=len(r); 
					if tfalse(getSet("enable-cat-all"))==True: ##F#O#R##T#E#S#T#I#N#G##
						pars={'mode':'Browse','page':'All'}; cMI=[]; ADDON.add_directory(pars,{'title':''+'All'+''},fanart=addonFanart,img=addonIcon,is_folder=True,total_items=iC,contextmenu_items=cMI,context_replace=False)
					for catId,name,catThumb in r:
						try:
							pars={'mode':'Browse','page':name}; cMI=[]; 
							if name.lower().startswith('search'):
								pars['mode']='Search'; pars['page']=''
							if name.lower().endswith('search'):
								if name.lower().startswith('movie'):
									pars['mode']='SearchMovie'; pars['page']=''
								if name.lower().startswith('tv'):
									pars['mode']='SearchTV'; pars['page']=''
								if name.lower().startswith('mp3') or name.lower().startswith('song') or name.lower().startswith('music'):
									pars['mode']='SearchSong'; pars['page']=''
							if len(catThumb)==0: catThumb=addonIcon
							try: ADDON.add_directory(pars,{'title':''+name+'','genre':name},fanart=addonFanart,img=catThumb,is_folder=True,total_items=iC,contextmenu_items=cMI,context_replace=False)
							except: pass
						except: pass
					#name='Search*'; pars={'mode':'Search','page':''}; cMI=[]; catThumb=addonIcon; 
					#try: ADDON.add_directory(pars,{'title':''+name+''},fanart=addonFanart,img=catThumb,is_folder=True,total_items=iC,contextmenu_items=cMI,context_replace=False)
					#except: pass
					#name='Search* blue'; pars={'mode':'Search','page':'blue'}; cMI=[]; catThumb=addonIcon; 
					#try: ADDON.add_directory(pars,{'title':''+name+''},fanart=addonFanart,img=catThumb,is_folder=True,total_items=iC,contextmenu_items=cMI,context_replace=False)
					#except: pass
#		setView('movies',getSet("front-view")); eod()
	except: pass
	setView('movies',getSet("front-view")); eod()
#############################################################################
#############################################################################
def Browse(h,page=''):
	try:
		cMI=[]; htmlCh=''; htmlCat=''; chThumb=''; HasErrored=False; AcInfo=grabAcInfo(True,True,False,False); DoD=getSet("custom-url2"); 
		if len(AcInfo)==0: eod(); return
		if (tfalse(getSet("enable-custom-url2"))==False) or (len(DoD)==0): DoD=zCoDeSz('durl')
		if h=='sh':
			if page=='':
				try: UserQuery=urllib.quote_plus(showkeyboard('None','Search For:'))
				except: eod(); return
			else: UserQuery=urllib.quote_plus(page)
			#debob({'UserQuery':UserQuery})
			if UserQuery=='': eod(); return
			for a in ['&','=','?']:
				if a in UserQuery: UserQuery=UserQuery.replace(a,'')
			Page=zCoDeSz('us2b')+DoD+zCoDeSz('dsh2b')+''+UserQuery+AcInfo; 
		elif h.startswith('sh-'):
				if h=='sh-song':
					UrLaB=zCoDeSz('dsh2b').replace('type=search&','type=Mp3-Search&')
				elif h=='sh-tv':
					UrLaB=zCoDeSz('dsh2b').replace('type=search&','type=TV-Search&')
				else: #elif h=='sh-movie':
					UrLaB=zCoDeSz('dsh2b').replace('type=search&','type=Movie-Search&')
				##
				if page=='':
					try: UserQuery=urllib.quote_plus(showkeyboard('None','Search For:'))
					except: eod(); return
				else: UserQuery=urllib.quote_plus(page)
				#debob({'UserQuery':UserQuery})
				if UserQuery=='': eod(); return
				for a in ['&','=','?']:
					if a in UserQuery: UserQuery=UserQuery.replace(a,'')
				Page=zCoDeSz('us2b')+DoD+UrLaB+''+UserQuery+AcInfo; 
		else:
			Page=zCoDeSz('us2b')+DoD+zCoDeSz('dch2b')+'-'+urllib.quote_plus(page)+AcInfo; 
			if (page.lower()=='all') or (page==''):
				Page=zCoDeSz('us2b')+DoD+zCoDeSz('dch2b')+''+AcInfo; 
		
		if Testing==True: debob({'Page':Page})
		htmlCh=nolines(getURL(Page)); #deb("Length of HTML",str(len(htmlCh))); 
		if len(htmlCh)==0: eod(); return
		for m in ['Resource Limit Is Reached','The website is temporarily unable to service your request','exceeded resource limit','Please try again later.']:
			try:
				if (m in htmlCh) or (len(htmlCh)==0):
					if HasErrored==False:
						HasErrored=True; popOK(msg="Please try again later.",title="Problem",line2="Trouble connecting to list.",line3="Please be patient."); eod(); return
			except: pass
		try: r=re.compile(zCoDeSz('re3')).findall(htmlCh)[0]; #debob({"Length of 'r'":len(r)}); 
		except: r=[]
		if r:
			if ('<stream>' in htmlCh) or ('<stream/>' in htmlCh):
				htmlCh=r; htmlCh=htmlCh.replace(zCoDeSz('rp2a'),zCoDeSz('rp2b')); 
				try: r=re.compile(zCoDeSz('re4')).findall(htmlCh)
				except: r=[]
				if r:
					iC=len(r); 
					for chId,name,chCat,chPlot,chThumb,url in r:
						try:
							if (not '://' in url) and (len(url) > 18): url=DecodeUrlB64(url)
						except: pass
						if (not url=='none') and (len(url) > 0) and (len(name) > 0):
							if len(chThumb)==0: chThumb=addonIcon
							if zCoDeSz('nx1a') in chPlot: chPlot=chPlot.replace(zCoDeSz('nx1a'),zCoDeSz('nx1b'))
							pars={'mode':'Play','channel':url,'name':name}; cMI=[]; plot=''; plotoutline=''; tag=''
							if (tfalse(getSet("enable-cat-all"))==True): ##F#O#R##T#E#S#T#I#N#G##
									plotoutline=chThumb; plot+=chId+'.)  '+name+'\n'; plot+='Category:  '+chCat+'\n'; plot+=url+'\n'; plot+=chThumb+'\n'; 
									if not '://' in url: tag='[COLOR orange]**[/COLOR] '
									elif zCoDeSz('us1a') in url: tag='[COLOR orange]*[/COLOR][COLOR red]*[/COLOR] '
									elif zCoDeSz('us2a') in url: tag='[COLOR orange]*[/red][COLOR orange]*[/COLOR] '
									else: tag='[COLOR red]**[/COLOR] '
									cMI.append((tag,zCoDeSz('ai')))
							#if zCoDeSz('ap1') in url: pars['mode']='Browse'
							#elif zCoDeSz('ap2') in url: pars['mode']='Search'
							if ('://' in url) and (not url.endswith('://')):
								try: urlPartB=url.split('://')[1]
								except: urlPartB=''
							else: urlPartB=''
							if url.lower().startswith('channels://') or url.lower().startswith('cat://'):
								try: pars['mode']='Browse'; pars['page']=urlPartB
								except: pass
							elif url.lower().startswith('search://'):
								try: pars['mode']='Search'; pars['page']=urlPartB
								except: pass
							elif url.lower().startswith('movie-search://'):
								try: pars['mode']='SearchMovie'; pars['page']=urlPartB
								except: pass
							elif url.lower().startswith('tv-search://'):
								try: pars['mode']='SearchTV'; pars['page']=urlPartB
								except: pass
							elif url.lower().startswith('mp3-search://'):
								try: pars['mode']='SearchSong'; pars['page']=urlPartB
								except: pass
							else:
								cMI.append(('Channel Information',zCoDeSz('ai')))
							try: ADDON.add_video_item(pars,{'title':''+tag+''+name+'','plot':plot+chPlot,'genre':chCat,'plotoutline':plotoutline},fanart=addonFanart,img=chThumb,total_items=iC,contextmenu_items=cMI,context_replace=False)
							except: pass
			#elif ('<stream_url>' in htmlCh) or ('<stream_url/>' in htmlCh):
			#	htmlCh=r; htmlCh=htmlCh.replace(zCoDeSz('rp2a'),zCoDeSz('rp2b')); 
			#	try: r=re.compile(zCoDeSz('re5')).findall(htmlCh)
			#	except: r=[]
			#	if r:
			#		iC=len(r); 
			#		for chId,name,chCat,chPlot,chThumb,url in r:
			#			try:
			#				if (not '://' in url) and (len(url) > 18): url=DecodeUrlB64(url)
			#			except: pass
			#			if (not url=='none') and (len(url) > 0) and (len(name) > 0):
			#				if len(chThumb)==0: chThumb=addonIcon
			#				if zCoDeSz('nx1a') in chPlot: chPlot=chPlot.replace(zCoDeSz('nx1a'),zCoDeSz('nx1b'))
			#				pars={'mode':'Play','channel':url,'name':name}; cMI=[]; plot=''; plotoutline=''; tag=''
			#				if (tfalse(getSet("enable-cat-all"))==True): ##F#O#R##T#E#S#T#I#N#G##
			#						plotoutline=chThumb; plot+=chId+'.)  '+name+'\n'; plot+='Category:  '+chCat+'\n'; plot+=url+'\n'; plot+=chThumb+'\n'; 
			#						if not '://' in url: tag='[COLOR orange]**[/COLOR] '
			#						elif zCoDeSz('us1a') in url: tag='[COLOR orange]*[/COLOR][COLOR red]*[/COLOR] '
			#						elif zCoDeSz('us2a') in url: tag='[COLOR orange]*[/red][COLOR orange]*[/COLOR] '
			#						else: tag='[COLOR red]**[/COLOR] '
			#						cMI.append((tag,zCoDeSz('ai')))
			#				#if zCoDeSz('ap1') in url: pars['mode']='Browse'
			#				#elif zCoDeSz('ap2') in url: pars['mode']='Search'
			#				if url.lower().startswith('channels://'):
			#					try: pars['mode']='Browse'; pars['page']=url.split('://')[1]
			#					except: pass
			#				elif url.lower().startswith('search://'):
			#					try: pars['mode']='Search'; pars['page']=url.split('://')[1]
			#					except: pass
			#				else:
			#					cMI.append(('Channel Information',zCoDeSz('ai')))
			#				try: ADDON.add_video_item(pars,{'title':''+tag+''+name+'','plot':plot+chPlot,'genre':chCat,'plotoutline':plotoutline},fanart=addonFanart,img=chThumb,total_items=iC,contextmenu_items=cMI,context_replace=False)
			#				except: pass
	except: pass
	setView('movies',getSet("browse-view")); eod()
#############################################################################
#############################################################################
def ChooseQuality(Name='',Img='',Res='',ResSD='',ResHD=''):
	try:
		a=[]; 
		for c,d in [('Default',Res),('SD',ResSD),('HD',ResHD)]:
			if len(Res) > 0: 
				if not '://' in d:
					d=DecodeUrlB64(d); 
				a.append(('Quality: '+c,d))
		for name,Link in a:
			cMI=[]; plot=''; tag=''; 
			pars={'mode':'Play','channel':Link,'name':Name}; 
			try: ADDON.add_video_item(pars,{'title':''+tag+''+name+'','plot':plot},fanart=addonFanart,img=Img,contextmenu_items=cMI,context_replace=False)
			except: pass
		pass
	except: pass
	setView('movies',getSet("quality-view")); eod()
#############################################################################
#############################################################################
def PlayStream(URL,NAME=''):
	#try:
		if Testing==True: deb("Initial URL",URL); 
		if (not '://' in URL) and (len(URL) > 18): 
			try: 
				URL=DecodeUrlB64(URL)
				URL=URL.strip()
				if Testing==True: deb("Decoded URL",URL); 
			except: pass
		RefTag=zCoDeSz('ref1')
		if URL.lower().startswith('ref://'): RefTag='ref://'
		if (not URL=='') and (URL.lower().startswith(RefTag)) and (len(URL) > (len(RefTag)+4)):
			if Testing==True: deb("Ref URL",URL); 
			token=''; URL=URL.replace(RefTag,zCoDeSz('us2b')); 
			if 'token=' in URL:
				try: Token=re.compile('token=([0-9a-zA-Z_\-]+)').findall(URL)[0]
				except: Token=''
			AcInfo=grabAcInfo(True,True,False,False); 
			URL=URL+AcInfo
			if Testing==True: deb("Ref URL*",URL); 
			htmlPly=nolines(getURL(URL)).strip(); 
			if Testing==True: debob("==="); debob(htmlPly); 
			if '://' in htmlPly: URL=htmlPly
			else: URL=DecodeUrlB64(htmlPly)
			if Testing==True: debob("---"); debob(URL); debob("+++"); 
			URL=URL.strip()
			if (len(URL) > 10) and (len(Token) > 0): 
				if '?' in URL: URL+='&token='+Token
				else: URL+='?token='+Token
			if Testing==True: deb("Returned URL",URL); 
			if len(URL)==0: eod(); return
		play=xbmc.Player(GetPlayerCore()); AcInfo=grabAcInfo(); ddd=getSet("custom-url"); pl1=zCoDeSz("pl1"); pl2=zCoDeSz("pl2"); 
		if len(AcInfo)==0: eod(); return
		if (tfalse(getSet("enable-custom-url"))==False) or (len(ddd)==0): ddd=zCoDeSz("dot")
		if '://' in URL: 
			url=URL
			AcInfo=AcInfo.replace('\n','')
			if '?' in url: AcInfo=AcInfo.replace('?','&').replace('\n','')
			if   url.startswith(zCoDeSz('us1a')): url=url.replace(zCoDeSz('us1a'),zCoDeSz('us1b'))+AcInfo
			elif url.startswith(zCoDeSz('us2a')): 
				url=url.replace(zCoDeSz('us2a'),zCoDeSz('us2b'))
				if url.endswith(zCoDeSz('us3a')):
					url=url.replace(zCoDeSz('us3a'),'')+AcInfo+'&_='+zCoDeSz('us3a')
				else:
					url+=AcInfo
			#debob("test a "+url)
		else: url="%s%s%s%s%s"%(pl1,ddd,pl2,URL,AcInfo); 
		##
		DoD=getSet("custom-url2"); AcInfo=grabAcInfo(True,True,False,False); 
		if (tfalse(getSet("enable-custom-url2"))==False) or (len(DoD)==0): DoD=zCoDeSz('durl')
		PageS=zCoDeSz('us2b')+DoD+zCoDeSz('pb1a')+AcInfo+'&name='+urllib.quote_plus(NAME); 
		PageE=zCoDeSz('us2b')+DoD+zCoDeSz('pb1b')+AcInfo+'&name='+urllib.quote_plus(NAME); 
		##
		if Testing==True:  ##F#O#R##T#E#S#T#I#N#G##
			deb("Stream URL",url); 
		try: ADDON.resolve_url(url)
		except: pass
		#html=nolines(getURL(PageS)); 
		#debob({'url':url})
		try: play.play(url)
		except: pass
		#html=nolines(getURL(PageE)); 
		##
	#except: pass
#############################################################################
#############################################################################
### F # O # R ### T # E # S # T # I # N # G ### O # N # L # Y ###############
#a1=""; a2=EncodeUrlB64(a1); print [a1,a2]; 
#a1=""; a2=EncodeUrlB64(a1); print [a1,a2]; 
#for a in ['','','']: print [a]; a2=EncodeUrlB64(a); print [a2]
#############################################################################
#############################################################################
def zModeCheck(mode='',url=''):
	#deb('mode',mode); 
	if (mode=='') or (mode=='main'): Menu0()
	elif mode=='Browse': Browse('ch',addpr('page'))
	elif mode=='Search': Browse('sh',addpr('page'))
	elif mode=='SearchMovie': Browse('sh-movie',addpr('page'))
	elif mode=='SearchTV': Browse('sh-tv',addpr('page'))
	elif mode=='SearchSong': Browse('sh-song',addpr('page'))
	elif mode=='Quality': ChooseQuality(addpr('name'),addpr('img'),addpr('res'),addpr('ressd'),addpr('reshd'))
	elif mode=='Play': PlayStream(addpr('channel'),addpr('name'))
	##
zModeCheck(addpr('mode'),addpr('url'))
#############################################################################
#############################################################################
