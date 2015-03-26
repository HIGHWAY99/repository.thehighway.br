### ############################################################################################################
###	#	
### # Project: 			#		Proxies Handler - by The Highway 2014.
### # Author: 			#		The Highway
### # Version:			#		v0.0.2
### # Date:					#		[Y-M-D] [2014-01-14]
### # Description: 	#		Fetch a Proxy Address (Address,IP,Port,Percent/Speed) and be able to catch/update it from multiple addons.
###	#	
### ############################################################################################################
### ############################################################################################################

### ### Example:
### ### To Import:
### from common.proxies import Proxies
### ### To Return a Proxy Addres:
### proxyaddress=Proxies().catchNewProxy(path="country-us",percentbetterthan=75)
### i.e.: http://#.#.#.#:8080
### default: percentbetterthan=75
### Note: You can set percentbetterthan=0 for all proxies.
### default: path=""
### Example: path="country-us"
### Example: path="port-8080"
### ### To Return an array of [ip,port,percent]:  percent=Proxy Speed on proxynova.com.
### results=Proxies().getProxyList(path="country-us",percentbetterthan=75)
### ### To Return Current Saved Proxy Address or New Proxy Address if there is not a current one.
### proxyaddress=Proxies().getSavedProxyOrNew(path="country-us",percentbetterthan=75,default="")
### ### To Return Current Saved Proxy Address.
### proxyaddress=Proxies().getSavedProxy(default="")

##### Imports #####
import xbmc,xbmcaddon,xbmcgui,xbmcplugin
import re,os,sys,string,StringIO,logging,random,array,time,datetime
import urllib,urllib2

##### Settings #####
UserAgent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
ProxyList_Domain="http://www.proxynova.com/proxy-server-list/"
addon_id="script.module.highway.common"
addon=xbmcaddon.Addon(id=addon_id)

##### Functions #####
def SettingSet(id,value=''): ## Save Settings
	try: addon.setSetting(id=id,value=value)
	except: pass
def SettingGet(r,s=''): ## Get Settings
	try: return addon.getSetting(r)
	except: return s
def fetchUrl(url): #Function to fetch a url. To save some time and writing you can just call: link=fetchUrl(url)
	try:
		req=urllib2.Request(url); req.add_header('User-Agent',UserAgent)
		response=urllib2.urlopen(req); link=response.read(); response.close()
		return link
	except: return "[ERROR]"
def nolines(t): #Removes line breaks from a string.
	it=t.splitlines(); t=''
	for L in it: t=t+L
	return t.replace("\r","").replace("\n","")

##### Class #####
class Proxies:
	def __init__(self):
		return
	def getSavedProxy(self,default=""):
		### Gets the information from settings of this module.
		### This is so that you can use the same proxy on multiple addons.
		try: return SettingGet("CurrentProxy")
		except: return default
	def getSavedProxyOrNew(self,path="",percentbetterthan=75,default=""):
		### Gets the information from settings of this module.
		### This is so that you can use the same proxy on multiple addons.
		### If returned value is "" and default is "" then it'll Catch a new ProxyAddress.
		try: t=SettingGet("CurrentProxy")
		except: t=default
		if t=="": t=self.catchNewProxy(path=path,percentbetterthan=percentbetterthan)
		return t
	def getSavedProxyIp(self,default=""):
		try: return SettingGet("CurrentProxyIp")
		except: return default
	def getSavedProxyPort(self,default=""):
		try: return SettingGet("CurrentProxyPort")
		except: return default
	def getSavedProxyPercent(self,default=""):
		try: return SettingGet("CurrentProxyPercent")
		except: return default
	def setSavedProxy(self,proxy="",ip="",port="",percent=""):
		### Saves the information into settings of this module.
		SettingSet("CurrentProxy",proxy)
		SettingSet("CurrentProxyIp",ip)
		SettingSet("CurrentProxyPort",port)
		SettingSet("CurrentProxyPercent",percent)
	def catchNewProxy(self,path="",percentbetterthan=75):
		### Returns a random Proxy Addres from among a list.
		results=self.getProxyList(path=path,percentbetterthan=percentbetterthan)
		result=results[random.randint(0,len(results))]
		print result
		prox="http://"+result[0]+":"+result[1]+""
		self.setSavedProxy(proxy=prox,ip=result[0],port=result[1],percent=result[2])
		return prox
	def getProxyList(self,path="",percentbetterthan=75):
		#country-us/
		PL_Url=ProxyList_Domain
		if len(path) > 0: PL_Url+=path+"/"
		PL_HTML=fetchUrl(PL_Url)
		print "lenth of html for proxy list:  "+str(len(PL_HTML))
		#print PL_HTML
		s1='<span class="row_proxy_ip">\s*<script>document.write\("(\d+\.\d+\.\d+\.\d+)"\);</script>'+'\s*</span></td>\s*<td align="left">\s*(.+?)\s*</td>'+'\s*<td align="left">\s*<time class=".+?" datetime=".+?">.+?</time>\s*</td>\s*<td align="left">\s*<div class="progress-bar" data-value="(\d+)" title="\d+"></div>'
		try: results=re.compile(s1).findall(nolines(PL_HTML))
		except: results=""
		print results
		#return results
		results2=[]
		if len(results) > 0:
			for (ip,port,percent) in results:
				if '</a>' in port: port=port.split('</a>')[0].split('>')[-1]
				if int(percent) > int(percentbetterthan):
					results2.append((ip,port,percent))
		print results2
		return results2
	def getProxyList_FreeProxyList(self,country="US",uptime="80"):
		#PL_Url=ProxyList_Domain+"/?c="+country+"&u="+uptime+"&pt=&pr=&a[]=0&a[]=1&a[]=2"
		PL_Url=ProxyList_Domain+"/?c="+country+"&u="+uptime
		PL_HTML=fetchUrl(PL_Url)
		print "lenth of html for proxy list:  "+str(len(PL_HTML))
		print PL_HTML
		s1='<tr class="\D+"><td><script type="text/javascript">IPDecode\("([0-9\%]+)"\)</script></td><td align="center">([0-9]+)</td><td align="center">(HTTP[S]*)</td><td align="center">([A-Za-z]+)</td><td><img src="(img/[A-Za-z]+\.[A-Za-z]+)" title="[A-Za-z0-9\s]+ Proxy">\s*([A-Za-z0-9\s]+)\s*</td><td>\s*([A-Za-z0-9\s]+)\s*</td><td>\s*([A-Za-z0-9\s]+)\s*</td><td align="center">([0-9\.]+)%</td><td><div class="graph"><span class="bar" style="width:[0-9\.]+%;background:#\d+;"></span></div></td><td><div class="graph"><span class="bar" style="width:[0-9\.]+%;background:#\d+;"></span></div></td></tr>'
		try: results=re.compile(s1).findall(PL_HTML)
		except: results=""
		print results
		return results
		#if len(results) > 0:
		#	for () in results:
		#		t=""
		#		#
		#
	
	
	
	
	
	
	
	#




#<a href="http://www.proxynova.com/proxy-server-list/country-ar/" title="Argentinian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-az/" title="Azerbaijani, Azeri Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-bd/" title="Bangladeshi Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-br/" title="Brazilian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-bn/" title="Bruneian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-bg/" title="Bulgarian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-kh/" title="Cambodian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-cl/" title="Chilean Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-cn/" title="Chinese Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-co/" title="Colombian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-cz/" title="Czech Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ec/" title="Ecuadorian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-eg/" title="Egyptian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-fr/" title="French Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-de/" title="German Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-hk/" title="Hong Konger Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-in/" title="Indian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-id/" title="Indonesian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ir/" title="Iranian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-iq/" title="Iraqi Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-jp/" title="Japanese Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ke/" title="Kenyan Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-my/" title="Malaysian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-np/" title="Nepali Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-nl/" title="Dutch Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ng/" title="Nigerian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-pk/" title="Pakistani Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ps/" title="Palestinian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-pe/" title="Peruvian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-pl/" title="Polish Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ru/" title="Russian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-rs/" title="Serbian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-kr/" title="South Korean Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-tw/" title="Taiwanese Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-th/" title="Thai Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-tr/" title="Turkish Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ua/" title="Ukrainian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ae/" title="Emirati, Emirian Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-gb/" title="British Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-us/" title="American Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-ve/" title="Venezuelan Proxy List"> 
#<a href="http://www.proxynova.com/proxy-server-list/country-vn/" title="Vietnamese Proxy List"> 



