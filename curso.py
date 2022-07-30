import os, sys, time, io

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

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

def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()
banner()
carga()
print(f"{color.azul}telegram del curso : https://t.me/termuxhispano{color.fin}")
print()
print(f"{color.cyan}       CURSO DE INICIACION TERMUX")
print()
print(f"{color.cyan}           ACTULIZAR TERMUX{color.fin}")
print()
print(f"{color.verde}PARA BAJAR LA ACTULIZACION PONDREMOS : {color.amarillo}pkg update")
print(f"{color.verde}PARA INSTALAR LA ACTULIZACION PONDREMOS : {color.amarillo}pkg upgrade")
print(f"{color.morado}ES MUY IMPORTANTE TENER SIEMPRE ACTUALIZADO NUESTRO TERMUX{color.fin}")
print()
print(f"{color.cyan}QUIERES CONTINUAR CON EL CURSO{color.fin}")
print(f"{color.verde}[1] SI")
print(f"{color.rojo}[1] NO")
valor = input(f"{color.cyan}ELIJE EL NUMERO QUE QUIERAS >> {color.fin}")
if valor == "1":
 banner()
 print(f"{color.azul}telegram del curso : https://t.me/termuxhispano{color.fin}")
 print()
 print(f"{color.cyan}       CURSO DE INICIACION TERMUX")                                                                           
 print()
 print(f"{color.cyan}       VER LAS CARPETAS Y ARCHIVOS{color.fin}")
 print()
 print(f"{color.verde}PARA VER CARPETAS Y ARCHIVOS  PONDREMOS :{color.amarillo} ls {color.fin}")
 print(f"{color.morado}LAS CARPETAS SALDRAN EN COLOR AZUL Y PODREMOS ENTRAR")
 print(f"LOS ARCHIVOS SALDRAN EN BLANCO {color.fin}")
 print()
 print(f"{color.cyan}QUIERES CONTINUAR CON EL CURSO{color.fin}")
 print(f"{color.verde}[1] SI")
 print(f"{color.rojo}[1] NO")
 valor = input(f"{color.cyan}ELIJE EL NUMERO QUE QUIERAS >> {color.fin}")
 if valor == "1":
  banner()
  print(f"{color.azul}telegram del curso : https://t.me/termuxhispano{color.fin}")
  print()
  print(f"{color.cyan}       CURSO DE INICIACION TERMUX")
  print()
  print(f"{color.cyan}         ENTRAR EN CARPETAS{color.fin}")
  print()
  print(f"{color.verde}PARA ENTRAR EN UNA CARPETA  PONDREMOS : {color.amarillo}cd nombre de la carpeta")
  print(f"{color.verde}PARA RETROCEDER UNA CARPETA PONDREMOS : {color.amarillo}cd ..")
  print(f"{color.verde}PARA RETROCEDER AL INICIO PONDREMOS : {color.amarillo}cd ")
  print(f"{color.morado}UNA VEZ DENTRO DE LA CARPETA MIRAREMOS QUE HAY CON ls{color.fin}")
  print()
  print(f"{color.cyan}QUIERES CONTINUAR CON EL CURSO{color.fin}")
  print(f"{color.verde}[1] SI")
  print(f"{color.rojo}[1] NO")
  valor = input(f"{color.cyan}ELIJE EL NUMERO QUE QUIERAS >> {color.fin}")
  if valor == "1":
   banner()
   print(f"{color.azul}telegram del curso : https://t.me/termuxhispano{color.fin}")
   print()
   print(f"{color.cyan}       CURSO DE INICIACION TERMUX")
   print()
   print(f"{color.cyan}          BORRAR ARCHIVOS{color.fin}")
   print()
   print(f"{color.verde}PARA BORRAR UN ARCHIVO PONDREMOS : {color.amarillo}rm nombre del archivo")
   print(f"{color.verde}PARA BORRAR UNA CARPETA PONDREMOS : {color.amarillo}rm -rf nombre de la carpeta")
   print(f"{color.morado}PODEMOS COMPROBAR QUE YA NO ESTA  CON ls{color.fin}")
   print()
   print(f"{color.cyan}QUIERES CONTINUAR CON EL CURSO{color.fin}")
   print(f"{color.verde}[1] SI")
   print(f"{color.rojo}[1] NO")
   valor = input(f"{color.cyan}ELIJE EL NUMERO QUE QUIERAS >> {color.fin}")
   if valor == "1":
    banner()
    print(f"{color.azul}telegram del curso : https://t.me/termuxhispano{color.fin}")
    print()
    print(f"{color.cyan}       CURSO DE INICIACION TERMUX")
    print()
    print(f"{color.cyan}         VER RUTA ACTUAL{color.fin}")
    print()
    print(f"{color.verde}PARA VER LA RUTA  PONDREMOS : {color.amarillo}pwd")
    print(f"{color.morado}LA RUTA QUIERE DECIR DENTRO DE QUE CARPETAS NOS ENCONTRAMOS{color.fin}")
    print()
    print(f"{color.cyan}QUIERES CONTINUAR CON EL CURSO{color.fin}")
    print(f"{color.verde}[1] SI")
    print(f"{color.rojo}[1] NO")
    valor = input(f"{color.cyan}ELIJE EL NUMERO QUE QUIERAS >> {color.fin}")
    if valor == "1":
     banner()
     print(f"{color.azul}telegram del curso : https://t.me/termuxhispano{color.fin}")
     print()
     print(f"{color.cyan}       CURSO DE INICIACION TERMUX")
     print()
     print(f"{color.cyan}         EJECUTAR ARCHIVOS{color.fin}")
     print()
     print(f"{color.verde}EJECUTAR LOS ARHCIVOS QUE TERMINEN EN .SH PONDREMOS : {color.amarillo}bash nombre del archivo")
     print(f"{color.verde}EJECUTAR LOS ARHCIVOS QUE TERMINEN EN .py PONDREMOS : {color.amarillo}python3 nombre del archivo")
     print(f"{color.morado}SI NO SE EJECUTA PUEDE QUE NOS FALTE ALGUN MODULO {color.fin}")
     print()
     print(f"{color.cyan}QUIERES CONTINUAR CON EL CURSO{color.fin}")
     print(f"{color.verde}[1] SI")
     print(f"{color.rojo}[1] NO")
     valor = input(f"{color.cyan}ELIJE EL NUMERO QUE QUIERAS >> {color.fin}")
     if valor == "1":
      banner()
      print(f"{color.azul}telegram del curso : https://t.me/termuxhispano{color.fin}")
      print()
      print(f"{color.cyan}       CURSO DE INICIACION TERMUX")
      print()
      print(f"{color.cyan}           MODULOS TERMUX{color.fin}")
      print()
      print(f"{color.verde}PARA VER TODOS LOS MODULOS PONDREMOS : {color.amarillo}apt list")
      print(f"{color.verde}PARA INSTALAR UN MODULO PONDREMOS : {color.amarillo}apt install nombre del modulo")
      print()
      print(f"{color.morado}SI TENEMOS CLAROS ESTOS COMANDOS PODREMOS EMPEZAR ESPERO QUE OS AYUDE {color.fin}")
    else:
     exit()
   else:
    exit
  else:
   exit
 else:
  exit()
else:
 exit()
