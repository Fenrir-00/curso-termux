import os, sys, time, io
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")
while True:
 try:
  import requests
  break
 except ModuleNotFoundError:
  os.system("pip install requests")

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

r= requests.get("https://raw.githubusercontent.com/Fenrir-00/curso-termux/main/version.txt")
r=r.text
print(r)
if r != "version=1.2\n":
 os.system("clear")
 print(f"""{color.rojo}HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO""")
 time.sleep(5)
def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""")
 print(f"{color.fin}")
def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝


██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()
def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  1.2                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)
def cabecera():
 os.system("clear")
 print(f"""{color.cyan}

████████╗██╗██████╗░████████╗███████╗███╗   ███╗██╗   ██╗██╗  ██╗
╚══██╔══╝██║██╔══██╗╚══██╔══╝██╔════╝████╗ ████║██║   ██║╚██╗██╔╝
   ██║   ██║██████╔╝   ██║   █████╗  ██╔████╔██║██║   ██║ ╚███╔╝
   ██║   ██║██╔═══╝    ██║   ██╔══╝  ██║╚██╔╝██║██║   ██║ ██╔██╗
   ██║   ██║██║        ██║   ███████╗██║ ╚═╝ ██║╚██████╔╝██╔╝╚██╗
   ╚═╝   ╚═╝╚═╝        ╚═╝   ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝""")
def menu():
    os.system("clear")
    cabecera()
    version()
    print()
    print(f"{color.verde}    QUE TE GUSTARIA APRENDER")
    print(f"""{color.verde}
[1]LISTAR CONTENIDO              LS
[2]VER UBICACION                 PWD
[3]LIMPIAR CONSOLA               CLEAR
[4]PAQUETES                      PKG
[5]HERRQMIENTAS                  PT
[6]BORRA ARCHIVOS                RM                                                       
[7]ENTRAR EN UNA CARPETA         CD                                       
[8]COPIAR UN ARCHIVO             CP
[9]CREAR UN ARCHIVO              TOUCH
[10]LEER UN ARCHIVO              CAT
[11]SALIR                        EXIT
[12]PERMISO CARPETAS TELEFONO    TERMUX-SETUP-STORAGE
[13]CREAR CARPETAS               MKDIR
{color.rojo}[0]SALIR{color.fin}
""")                                                                                                          
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
        banner()
    elif eleccion == "2" :
      banner()
    elif eleccion == "3" :
     banner()
    elif eleccion == "4" :
     banner()
    elif eleccion == "5" :
     banner()
    elif eleccion == "6" :
     banner()
    elif eleccion == "7" :
     banner()
    elif eleccion == "8" :
     banner()
    elif eleccion == "9" :
     banner()
    elif eleccion == "10" :
     banner()
    elif eleccion == "11" :
     banner()
    elif eleccion == "12" :
     banner()
    elif eleccion == "13" :
     banner()
    elif eleccion == "14" :
     banner()
    elif eleccion == "15" :
     banner()
    elif eleccion == "16" :
     banner()
    elif eleccion == "17" :
     banner()
    elif eleccion == "18" :
     banner()
    elif eleccion == "19" :
     banner()
    elif eleccion == "20" :
     banner()
    elif eleccion == "21" :
     banner()
    elif eleccion == "22" :
     banner()
    elif eleccion == "23" :
     banner()
    elif eleccion == "24" :
     banner()
    elif eleccion == "25" :
     banner()
    elif eleccion == "0" :
     banner()
     exit()
    elif eleccion == "99" :
     banner()
    else:
     incorrecto()
menu()
