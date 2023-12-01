
import requests
import random
import threading
E = '\x1b[1;31m'
Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
C1 = '\x1b[2;35m'
G = '\x1b[1;35m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
M = '\x1b[1;37m'
S = '\x1b[1;33m'
U = '\x1b[1;37m'
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
import requests
import sys
import os
import time

from contextlib import contextmanager, redirect_stdout
from io import StringIO
from time import sleep

""",أداة صيد متاحات تيكتوك النسخة التجريبية 
كل ماعليك ضع توكن بوتك والأيدي """
#print('—'*60)

#print(B + '⋘────━⚜️ 𝑹𝑴dddddddd𝑨𝑫 ⚜️━────⋙')

#print(B + '⋘────━𓆩HACKER𓆪━────⋙')

#print(B + '⋘────━⚜️ 𝑹𝑴𝑨𝑫 HeroKo ⚜️────⋙')

import requests

def sui():
  try:
    user = '1234567890asdfghjklqwertyuiopzxcvbnm'
    num = ('Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley', 'Jennifer', 'Joshua', 'Amanda', 'David', 'Daniel', 'James', 'Robert', 'John', 'Joseph', 'Andrew', 'Ryan', 'Brandon', 'Jason', 'Justin', 'Sarah', 'William', 'Jonathan', 'Stephanie', 'Brian', 'Nicole', 'Nicholas', 'Anthony', 'Heather', 'Elizabeth', 'Megan', 'Adam', 'Eric', 'Melissa', 'Kevin', 'Steven', 'Thomas'); 
    rang = ''.join(random.choice(num) for i in range(1))
    name = ''.join(random.choice(user) for i in range(6))
    username = name
    email = name + '@gmail.com'
    res = requests.get(f'''https://GmailandTiktokandzaid.zaidbot.repl.co/2/email={email}''').text
    groupChatId = ('@N_1_N_6')
    if '"Dev":"@t_7_55","Email":"Good"' in res:
        print(f'''{F}Good Email : {email}''')
    api = requests.get(f'''https://api.dlyar-dev.tk/info-tiktok.json?user={username}''').json()
    useire = ('6413387021:AAHamlt1m_Jbs7j92SvPqclDaeZnIiiu0HA')
    if api['status'] == True:
        name = api['name']
        followers = api['followers']
        following = api['following']
        like = api['likes']
        id = api['id']
        code = api['code-country']
        country = api['country']
        tlg = f'''
𝑇𝐼𝐾𝑇𝑂𝐾 𖤍
⋘─────━⚜️ 𝑹𝑴𝑨𝑫 HeroKo HeroKo⚜️━─────⋙

★ ＮＡＭＥ ★ : {name}
 
★ ＵＳＥＲＮＡＭＥ ★ : @{username}
 
★ ＥＭＡＩＬ ★ : {email}

★  𝐈𝐃 ★ : {id}
   
★ ＵＲＬ ★ : https://www.tiktok.com/@{username}
 
⋘─────━⚜️ 𝑹𝑴𝑨𝑫 HeroKo ⚜️━─────⋙

PY : @N_9_N_6 || @R_M_D
		'''
        tlg = f'''
𝑇𝐼𝐾𝑇𝑂𝐾 𖤍
⋘─────━⚜️ 𝑹𝑴𝑨𝑫 HeroKo ⚜️━─────⋙

★ ＮＡＭＥ ★ : {name}
 
★ ＵＳＥＲＮＡＭＥ ★ : @{username}
 
★ ＥＭＡＩＬ ★ : {email}

★  𝐈𝐃 ★ : {id}
   
★ ＵＲＬ ★ : https://www.tiktok.com/@{username}
 
⋘─────━⚜️ 𝑹𝑴𝑨𝑫 HeroKo ⚜️━─────⋙

PY : @N_9_N_6 || @R_M_D
		'''
        requests.get('https://api.telegram.org/bot' + str(useire) + '/sendMessage?chat_id=' + str(groupChatId) + '&text=' + str(tlg))
        
        print(tlg)
    else:
      print(f''' Bad Gmail : {email}''')
  except:
    print(f''' Bad Gmail : {email}''')
while True:

    sui()
