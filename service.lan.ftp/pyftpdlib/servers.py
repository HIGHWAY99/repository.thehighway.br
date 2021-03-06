#!/usr/bin/env python
# $Id: servers.py 1230 2013-07-16 16:07:08Z btimby $
#  ======================================================================
#  Copyright (C) 2007-2013 Giampaolo Rodola' <g.rodola@gmail.com>
#                         All Rights Reserved
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#  ======================================================================
"""This module contains the main FTPServer class which listens on a host:port and dispatches the incoming connections to a handler.
The concurrency is handled asynchronously by the main process thread, meaning the handler cannot block otherwise the whole server will hang.

Other than that we have 2 subclasses changing the asynchronous concurrency model using multiple threads or processes.

You might be interested in these in case your code contains blocking parts which cannot be adapted to the base async model or if the underlying filesystem is particularly slow, see:
https://code.google.com/p/pyftpdlib/issues/detail?id=197
https://code.google.com/p/pyftpdlib/issues/detail?id=212

Two classes are provided:
 - ThreadingFTPServer
 - MultiprocessFTPServer
...spawning a new thread or process every time a client connects.

The main thread will be async-based and be used only to accept new
connections.
Every time a new connection comes in that will be dispatched to a
separate thread/process which internally will run its own IO loop.
This way the handler handling that connections will be free to block
without hanging the whole FTP server. """
import os,sys,time,socket,traceback,errno,select,logging,signal; from log import logger; from ioloop import Acceptor,IOLoop
__all__=['FTPServer']
_BSD='bsd' in sys.platform
# ===================================================================
# --- Additions for Addon Workings.
# ===================================================================
import xbmcaddon
addon_id="service.lan.ftp"; addon=xbmcaddon.Addon(id=addon_id)
def getAddonSetting(setting,default=""): 
	try: return addon.getSetting(setting)
	except: return default
	#getAddonSetting("","")
	#def IsServerOn(self): return tfalse(getAddonSetting("server_enable","false"))
def setAddonSetting(setting,value=""): 
	try: addon.setSetting(id=setting,value=value)
	except: pass
def tfalse(r,d=False): ## Get True / False
	if   (r.lower()=='true' ) or (r.lower()=='t') or (r.lower()=='y') or (r.lower()=='1') or (r.lower()=='yes'): return True
	elif (r.lower()=='false') or (r.lower()=='f') or (r.lower()=='n') or (r.lower()=='0') or (r.lower()=='no'): return False
	else: return d
# ===================================================================
# --- base class
# ===================================================================
class FTPServer(Acceptor):
    """Creates a socket listening on <address>, dispatching the requests to a <handler> (typically FTPHandler class).
    Depending on the type of address specified IPv4 or IPv6 connections (or both, depending from the underlying system) will be accepted.
    All relevant session information is stored in class attributes  described below.
     - (int) max_cons:
        number of maximum simultaneous connections accepted (defaults to 512). 
        Can be set to 0 for unlimited but it is recommended to always have a limit to avoid running out of file descriptors (DoS).
     - (int) max_cons_per_ip:
        number of maximum connections accepted for the same IP address (defaults to 0 == unlimited). """
    max_cons=512; max_cons_per_ip=0
    def __init__(self,address_or_socket,handler,ioloop=None,backlog=5):
        """Creates a socket listening on 'address' dispatching connections to a 'handler'.
         - (tuple) address_or_socket: the (host, port) pair on which
           the command channel will listen for incoming connections or an existent socket object.
         - (instance) handler: the handler class to use.
         - (instance) ioloop: a ioloop.IOLoop instance
         - (int) backlog: the maximum number of queued connections passed to listen(). 
           If a connection request arrives when the queue is full the client may raise ECONNRESET. Defaults to 5. """
        Acceptor.__init__(self,ioloop=ioloop); self.handler=handler; self.backlog=backlog; self.ip_map=[]
        # in case of FTPS class not properly configured we want errors # to be raised here rather than later, when client connects
        if hasattr(handler,'get_ssl_context'): handler.get_ssl_context()
        if callable(getattr(address_or_socket,'listen',None)):
        	sock=address_or_socket; sock.setblocking(0); self.set_socket(sock)
        	if hasattr(sock,'family'): self._af=sock.family
        	else: # python 2.4
        		ip,port=self.socket.getsockname()[:2]; self._af=socket.getaddrinfo(ip,port,socket.AF_UNSPEC,socket.SOCK_STREAM)[0][0]
        else: self._af=self.bind_af_unspecified(address_or_socket)
        self.listen(backlog)
    @property
    def address(self): return self.socket.getsockname()[:2]
    def _map_len(self): return len(self.ioloop.socket_map)
    def IsServerOn(self): return tfalse(getAddonSetting("server_enable","false"))
    def _accept_new_cons(self): #"""Return True if the server is willing to accept new connections."""
        if self.IsServerOn()==False: 
        	try: self.socket.close(); 
        	except: pass
        	try: self._exit.set()
        	except: pass
        	return False
        elif not self.max_cons: return True
        else: return self._map_len() <= self.max_cons
    def _log_start(self):
        if not logging.getLogger().handlers:
        	# If we get to this point it means the user hasn't # configured logger. We want to log by default so
        	# we configure logging ourselves so that it will # print to stderr.
        	from ioloop import _config_logging; _config_logging()
        if self.handler.passive_ports: pasv_ports="%s->%s" % (self.handler.passive_ports[0], self.handler.passive_ports[-1])
        else: pasv_ports=None
        addr=self.address
        logger.info(">>> starting FTP server on %s:%s, pid=%i <<<" % (addr[0],addr[1],os.getpid()))
        try: setAddonSetting("server-pid",str(os.getpid()))
        except: print "failed to save server-pid to settings."
        logger.info("poller: %r",self.ioloop.__class__)
        logger.info("masquerade (NAT) address: %s",self.handler.masquerade_address)
        logger.info("passive ports: %s",pasv_ports)
        if os.name=='posix': logger.info("use sendfile(2): %s",self.handler.use_sendfile)
    def serve_forever(self,timeout=None,blocking=True,handle_exit=True):
        """Start serving.
         - (float) timeout: the timeout passed to the underlying IO
           loop expressed in seconds (default 1.0).
         - (bool) blocking: if False loop once and then return the
           timeout of the next scheduled call next to expire soonest
           (if any).
         - (bool) handle_exit: when True catches KeyboardInterrupt and
           SystemExit exceptions (generally caused by SIGTERM / SIGINT
           signals) and gracefully exits after cleaning up resources.
           Also, logs server start and stop. """
        if handle_exit:
        	log=handle_exit and blocking==True
        	if log: self._log_start()
        	try: self.ioloop.loop(timeout,blocking)
        	#except (self.IsServerOn==False): self.close_all(); return
        	except (KeyboardInterrupt,SystemExit): pass #sys.exit(); raise #pass
        	if blocking:
        		if log: logger.info(">>> shutting down FTP server (%s active fds) <<<",self._map_len())
        		self.close_all()
        else: self.ioloop.loop(timeout,blocking)
    def handle_accepted(self,sock,addr): #"""Called when remote client initiates a connection."""
        handler=None; ip=None
        try:
            handler=self.handler(sock,self,ioloop=self.ioloop)
            if not handler.connected: return
            ip=addr[0]; self.ip_map.append(ip)
            # For performance and security reasons we should always set a limit for the number of file 
            # descriptors that socket_map should contain.  When we're running out of such limit we'll
            # use the last available channel for sending a 421 response to the client before disconnecting it.
            if not self._accept_new_cons(): handler.handle_max_cons(); return
            # accept only a limited number of connections from the same source address.
            if self.max_cons_per_ip:
            	if self.ip_map.count(ip) > self.max_cons_per_ip: handler.handle_max_cons_per_ip(); return
            try: handler.handle()
            except: handler.handle_error()
            else: return handler
        except Exception:
            # This is supposed to be an application bug that should be fixed. We do not want to tear down the 
            # server though (DoS). We just log the exception, hoping that someone will eventually file a bug. 
            # References:
            # - http://code.google.com/p/pyftpdlib/issues/detail?id=143
            # - http://code.google.com/p/pyftpdlib/issues/detail?id=166
            # - https://groups.google.com/forum/#!topic/pyftpdlib/h7pPybzAx14
            logger.error(traceback.format_exc())
            if handler is not None: handler.close()
            else:
            	if ip is not None and ip in self.ip_map: self.ip_map.remove(ip)
    def handle_error(self): #"""Called to handle any uncaught exceptions."""
    	try: raise
    	except Exception: logger.error(traceback.format_exc())
    	self.close()
    def close_all(self): 
    	try: self.socket.close(); 
    	except: pass
    	try: self.close()
    	except: print "self.close() in .close_all() has failed."; pass
    	#try: sys.exit()
    	#except: print "sys.exit() in .close_all() has failed."; pass
    	return self.ioloop.close() #"""Stop serving and also disconnects all currently connected clients. """
    def turn_off(self): 
    	try: self.socket.close(); 
    	except: pass
    	#try: os.kill(os.getpid,signal.SIGKILL)
    	#except: pass
    	#try: sys.exit() #"""Stop serving and also disconnects all currently connected clients. """
    	#except: pass
# ===================================================================
# --- extra implementations
# ===================================================================
class _SpawnerBase(FTPServer): #"""Base class shared by multiple threads/process dispatcher. Not supposed to be used. """
    # how many seconds to wait when join()ing parent's threads or processes
    join_timeout=5; _lock=None; _exit=None
    def __init__(self,address,handler,ioloop=None): FTPServer.__init__(self,address,handler,ioloop); self._active_tasks=[]
    def _start_task(self,*args,**kwargs): raise NotImplementedError('must be implemented in subclass')
    def _current_task(self): raise NotImplementedError('must be implemented in subclass')
    def _map_len(self): raise NotImplementedError('must be implemented in subclass')
    def IsServerOn(self): return tfalse(getAddonSetting("server_enable","false"))
    def _loop(self,handler): #"""Serve handler's IO loop in a separate thread or process."""
        ioloop=IOLoop()
        try:
            handler.ioloop=ioloop
            try: handler.add_channel()
            except EnvironmentError:
            	err=sys.exc_info()[1]
            	if err.errno==errno.EBADF: return # we might get here in case the other end quickly disconnected (see test_quick_connect())
            	else: raise
            # Here we localize variable access to minimize overhead.
            poll=ioloop.poll; sched_poll=ioloop.sched.poll; poll_timeout=getattr(self,'poll_timeout',None); soonest_timeout=poll_timeout
            while (ioloop.socket_map or ioloop.sched._tasks) and not self._exit.is_set():
                if (self.IsServerOn()==False): 
                	#try: ioloop.close()
                	#except: print "ioloop.close() in servers.py ioloop while statement failed."; pass
                	#try: handler.del_channel()
                	#except: pass
                	#try: self.close_all()
                	#except: pass
                	#sys.exit()
                	try: self.socket.close(); 
                	except: pass
                	self._exit.set()
                	return
                try:
                	if ioloop.socket_map: poll(timeout=soonest_timeout)
                	if ioloop.sched._tasks:
                		soonest_timeout=sched_poll()
                		# Handle the case where socket_map is emty but some cancelled scheduled calls are still around causing
                		# this while loop to hog CPU resources. In theory this should never happen as all the sched
                		# functions are supposed to be cancel()ed on close() but by using threads we can incur into
                		# synchronization issues such as this one.  https://code.google.com/p/pyftpdlib/issues/detail?id=245
                		if not ioloop.socket_map:
                			ioloop.sched.reheapify() # get rid of cancel()led calls
                			soonest_timeout=sched_poll()
                			if soonest_timeout: time.sleep(min(soonest_timeout,1))
                	else: soonest_timeout=None
                except (KeyboardInterrupt,SystemExit): self._exit.set(); sys.exit();   # note: these two exceptions are raised in all sub processes
                except select.error: 
                	err=sys.exc_info()[1] # on Windows we can get WSAENOTSOCK if the client rapidly connect and disconnects
                	if os.name=='nt' and err.args[0]==10038:
                		for fd in list(ioloop.socket_map.keys()):
                			try: select.select([fd],[],[],0)
                			except select.error:
                				try: logger.info("discarding broken socket %r",ioloop.socket_map[fd]); del ioloop.socket_map[fd]
                				except KeyError: pass # dict changed during iteration
                	else: raise
                else:
                	if poll_timeout:
                		if soonest_timeout is None or soonest_timeout > poll_timeout: soonest_timeout=poll_timeout
        finally: ioloop.close()
    def handle_accepted(self,sock,addr):
        handler = FTPServer.handle_accepted(self,sock,addr)
        if handler is not None:
            self.ioloop.unregister(handler._fileno) # unregister the handler from the main IOLoop used by the main thread to accept connections
            t=self._start_task(target=self._loop,args=(handler,)); t.name=repr(addr); t.start()
            # it is a different process so free resources here
            if hasattr(t,'pid'): handler.close()
            self._lock.acquire()
            try:
            	for task in self._active_tasks[:]: # clean finished tasks
            		if not task.is_alive(): self._active_tasks.remove(task)
            	self._active_tasks.append(t) # add the new task
            finally: self._lock.release()
    def _log_start(self): FTPServer._log_start(self); logger.info("dispatcher: %r",self.__class__)
    def serve_forever(self,timeout=None,blocking=True,handle_exit=True):
    	self._exit.clear()
    	if handle_exit:
    		log=handle_exit and blocking == True
    		if log: self._log_start()
    		try: self.ioloop.loop(timeout,blocking)
    		except (KeyboardInterrupt,SystemExit): pass #sys.exit(); raise #pass
    		if blocking:
    			if log: logger.info(">>> shutting down FTP server (%s active workers) <<<", self._map_len())
    			self.close_all()
    	else: self.ioloop.loop(timeout,blocking)
    def close_all(self):
        tasks=self._active_tasks[:]
        self._exit.set() # this must be set after getting active tasks as it causes thread objects to get out of the list too soon
        if tasks and hasattr(tasks[0],'terminate'):
        	for t in tasks: # we're dealing with subprocesses
        		try:
        			if not _BSD: t.terminate()
        			else: 
        				try: print t.pid
        				except:
        					try: print str(t.pid)
        					except: pass
        				try: print signal.SIGKILL
        				except:
        					try: print str(signal.SIGKILL)
        					except: pass
        				os.kill(t.pid,signal.SIGKILL) # XXX - On FreeBSD using SIGTERM doesn't work as the process hangs on kqueue.control() or select.select(). Use SIGKILL instead.
        		except OSError:
        			err=sys.exc_info()[1]
        			if err.errno != errno.ESRCH: raise
        self._wait_for_tasks(tasks)
        del self._active_tasks[:]
        FTPServer.close_all(self)
    def _wait_for_tasks(self,tasks): #"""Wait for threads or subprocesses to terminate."""
    	warn=logger.warning
    	for t in tasks:
    		t.join(self.join_timeout)
    		if t.is_alive():
    			# Thread or process is still alive. If it's a process attempt to send SIGKILL as last resort.
    			# Set timeout to None so that we will exit immediately in case also other threads/processes are hanging.
    			self.join_timeout=None
    			if hasattr(t,'terminate'):
    				msg="could not terminate process %r" % t
    				if not _BSD:
    					warn(msg+"; sending SIGKILL as last resort")
    					try: os.kill(t.pid,signal.SIGKILL)
    					except OSError:
    						err=sys.exc_info()[1]
    						if err.errno != errno.ESRCH: raise
    				else: warn(msg)
    			else: warn("thread %r didn't terminate; ignoring it", t)
try: import threading
except ImportError: pass
else:
	__all__ +=['ThreadedFTPServer']
	# compatibility with python <= 2.6
	if not hasattr(threading.Thread,'is_alive'): threading.Thread.is_alive=threading.Thread.isAlive
	class ThreadedFTPServer(_SpawnerBase): #"""A modified version of base FTPServer class which spawns a thread every time a new connection is established."""
		# The timeout passed to thread's IOLoop.poll() call on every loop. Necessary since threads ignore KeyboardInterrupt.
		poll_timeout=1.0; _lock=threading.Lock(); _exit=threading.Event()
		# compatibility with python <= 2.6
		if not hasattr(_exit,'is_set'): _exit.is_set=_exit.isSet
		def _start_task(self,*args,**kwargs): return threading.Thread(*args,**kwargs)
		def _current_task(self): return threading.currentThread()
		def _map_len(self): return threading.activeCount()
if os.name=='posix':
	try: import multiprocessing
	except ImportError: pass
	else:
		__all__ +=['MultiprocessFTPServer']
		class MultiprocessFTPServer(_SpawnerBase): #"""A modified version of base FTPServer class which spawns a process every time a new connection is established."""
			_lock=multiprocessing.Lock(); _exit=multiprocessing.Event()
			def _start_task(self,*args,**kwargs): return multiprocessing.Process(*args,**kwargs)
			def _current_task(self): return multiprocessing.current_process()
			def _map_len(self): return len(multiprocessing.active_children())
