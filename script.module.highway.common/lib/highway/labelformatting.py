### ############################################################################################################
###	#	
### # Project: 			#		Label Formatting Handler - by The Highway 2014.
### # Author: 			#		The Highway
### # Version:			#		v0.0.2
### # Date:					#		[Y-M-D] [2014-01-14]
### # Description: 	#		Fetch a Proxy Address (Address,IP,Port,Percent/Speed) and be able to catch/update it from multiple addons.
###	#	
### ############################################################################################################
### ############################################################################################################

### ### Example:
### ### To Import:
### from common.labelformatting import LabelFormatting as LF
### ### To Use:
### LF("Do you ever sleep?").B()	>>	[B]Do you ever sleep?[/B]
### LF("Do you ever sleep?").I()	>>	[I]Do you ever sleep?[/I]
### LF("Do you ever sleep?").UC()	>>	[UPPERCASE]Do you ever sleep?[/UPPERCASE]
### LF("Do you ever sleep?").LC()	>>	[LOWERCASE]Do you ever sleep?[/LOWERCASE]
### LF("Do you ever sleep?").COLOR("red")	>>	[COLOR red]Do you ever sleep?[/COLOR]

##### Imports #####
import xbmc,xbmcaddon,xbmcgui,xbmcplugin
import re,os,sys,string,StringIO,logging,random,array,time,datetime
import urllib,urllib2

##### Settings #####
UserAgent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
addon_id="script.module.highway.common"
addon=xbmcaddon.Addon(id=addon_id)

##### Functions #####
def SettingSet(id,value=''): ## Save Settings
	try: addon.setSetting(id=id,value=value)
	except: pass
def SettingGet(r,s=''): ## Get Settings
	try: return addon.getSetting(r)
	except: return s

##### Class #####
class LabelFormatting:
	msg=""
	def __init__(self,message=""):
		self.msg=message
	def B(self,o="B"): #[B]bold[/B] - bold text.
		try: 		return "[%s]%s[/%s]" % (o,str(self.msg),o)
		except: return self.msg
	def I(self,o="I"): #[I]italics[/I] - italic text. 
		try: 		return "[%s]%s[/%s]" % (o,str(self.msg),o)
		except: return self.msg
	def UC(self,o="UPPERCASE"): #[UPPERCASE]force text uppercase[/UPPERCASE] - force text to uppercase 
		try: 		return "[%s]%s[/%s]" % (o,str(self.msg),o)
		except: return self.msg
	def LC(self,o="LOWERCASE"): #[LOWERCASE]Force Text Lowercase[/LOWERCASE] - force text to lowercase 
		try: 		return "[%s]%s[/%s]" % (o,str(self.msg),o)
		except: return self.msg
	def CR(self,o="CR"): #[CR] - carriage return (line break). 
		try: 		return "%s[%s]" % (str(self.msg),o)
		except: return self.msg
	def COLOR(self,color,o="COLOR"): #
		if len(color)==0: return self.msg
		try: 		return "[%s %s]%s[/%s]" % (o,color.lower(),str(self.msg),o)
		except: return self.msg
	def C(self,color,o="COLOR"): return self.COLOR(color)
	def LOWERCASE(self): return self.LC()
	def UPPERCASE(self): return self.UC()
	def CP(self,color,start=0,length=1,o="COLOR"): #Color text start at a Given Position for a Given Length.
		if len(color)==0: return self.msg
		if len(color)==1: return "[%s %s]%s[/%s]" % (o,color.lower(),str(self.msg),o)
		else: return "[%s %s]%s[/%s]%s" % (o,color.lower(),str(self.msg[int(start):int(length)]),o,self.msg[(int(start)+int(length)):])
	def Notify(self,title="",delay=5000,image=""): xbmc.executebuiltin('XBMC.Notification("%s","%s",%d,"%s")' % (title,self.msg,delay,image))
	def FileSAVE(self,path): file=open(path,'w'); file.write(self.msg); file.close()
	def FileLOAD(self,path,default=""): 
		try:
			if os.path.isfile(path): ## File found.
				file=open(path,'r'); contents=file.read(); file.close(); return contents
			else: return default ## File not found.
		except: return default
	def isFile(self):
		try: return os.path.isfile(self.msg)
		except: return False
	def noLines(self): #Removes line breaks from a string.
		try:
			t=self.msg
			it=t.splitlines(); t=''
			for L in it: t=t+L
			return t.replace("\r","").replace("\n","")
		except: return self.msg
	def RemoveLines(self): #Removes line breaks from a string.
		return self.RemoveLines()
	def UrlFetch(self,UA=UserAgent,default="[ERROR]"):
		try: req=urllib2.Request(self.msg); req.add_header('User-Agent',UA); response=urllib2.urlopen(req); link=response.read(); response.close(); return link
		except: return default
	def isPath(self): 
		try: return os.path.exists(self.msg)
		except: return False
	def FileExtension(self,default=""):
		try:
			if "." in self.msg: return self.msg.split(".")[-1]
			else: return default
		except: default
	def log(self): print self.msg
	def log2(self,title=""): print title+":  "+str(self.msg)
	def GetOS(self,default=""):
		try: return os.environ.get('OS')
		except: return default
	def GetVersion(self,default=""):
		try: return xbmc.getInfoLabel('System.BuildVersion')
		except: return default
	def TP(self): return xbmc.translatePath(self.msg)
	def TranslatePath(self): return self.TP()
	def popOK(title="",line2="",line3=""):
		try: dialog=xbmcgui.Dialog(); dialog.ok(title,self.msg,line2,line3)
		except: pass
	def popYN(title='',line2='',line3='',n='',y=''):
		try:
			diag=xbmcgui.Dialog(); r=diag.yesno(title,self.msg,line2,line3,n,y)
			if r: return r
			else: return False
		except: return False
	def BusyAnimationShow(): xbmc.executebuiltin('ActivateWindow(busydialog)')
	def BusyAnimationHide(): xbmc.executebuiltin('Dialog.Close(busydialog,true)')
	def CloseAllDialogs():   xbmc.executebuiltin('Dialog.Close(all, true)') 
	def AddSortMethod(self,h=int(sys.argv[1])): xbmcplugin.addSortMethod(handle=h,sortMethod=self.msg)
	def SetContent(self,h=int(sys.argv[1])): xbmcplugin.setContent(h,self.msg)
	def SetViewMode(self): xbmc.executebuiltin("Container.SetViewMode(%s)" % str(self.msg))
	def showkeyboard(default="",passwordField=False): #LF(title).showkeyboard("DefaultText",False)
		try: #("text to show","header text", True="password field"/False="show text")
			keyboard=xbmc.Keyboard(default,self.msg,passwordField); keyboard.doModal()
			if keyboard.isConfirmed(): return keyboard.getText()
			else: return default
		except: return default
	def askSelection(option_list=[],default=False):
		try:
			if option_list==[]: return default
			dialogSelect=xbmcgui.Dialog(); return dialogSelect.select(self.msg,option_list)
		except: return default
	def XBMC_RefreshRSS(self): 						xbmc.executebuiltin("XBMC.RefreshRSS()")
	def XBMC_EjectTray(self): 						xbmc.executebuiltin("XBMC.EjectTray()")
	def XBMC_Mute(self): 									xbmc.executebuiltin("XBMC.Mute()")
	def XBMC_System_Exec(self): 					xbmc.executebuiltin("XBMC.System.Exec(%s)" % self.msg)
	def XBMC_System_ExecWait(self): 			xbmc.executebuiltin("XBMC.System.ExecWait(%s)" % self.msg)
	def XBMC_PlayDVD(self): 							xbmc.executebuiltin("XBMC.PlayDVD()")
	def XBMC_ReloadSkin(self): 						xbmc.executebuiltin("XBMC.ReloadSkin()")
	def XBMC_UpdateAddonRepos(self): 			xbmc.executebuiltin("XBMC.UpdateAddonRepos()")
	def XBMC_UpdateLocalAddons(self): 		xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
	def XBMC_Weather_Refresh(self): 			xbmc.executebuiltin("XBMC.Weather.Refresh()")
	def XBMC_ToggleDebug(self): 					xbmc.executebuiltin("XBMC.ToggleDebug()")
	def XBMC_Minimize(self): 							xbmc.executebuiltin("XBMC.Minimize()")
	def XBMC_ActivateScreensaver(self): 	xbmc.executebuiltin("XBMC.ActivateScreensaver()")
	def RunPlugin(self): xbmc.executebuiltin("XBMC.RunPlugin(%s)" % self.msg)
	def ContainerUpdate(self): xbmc.executebuiltin("XBMC.Container.Update(%s)" % self.msg)
	def RefreshList(): xbmc.executebuiltin("XBMC.Container.Refresh")
	def ContainerRefresh(): xbmc.executebuiltin("XBMC.Container.Refresh")
	def QP(self): return urllib.quote_plus(self.msg)
	def uQP(self): return urllib.unquote_plus(self.msg)
	def quote(self): return QP
	def unquote(self): return uQP
	
	
	
	#
