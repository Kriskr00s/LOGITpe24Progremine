from urllib.request import urlopen
from webbrowser import *

failVeebis = urlopen("https://jurivaitmaa21.thkit.ee/palmisaargame.txt")
baidid = failVeebis.read()
tekst = baidid.decode()
tekstridadena = tekst.splitlines()
failVeebis.close()
print(tekstridadena[9][16])

filenamefromsite = input("millisstfaili avada tahad")
open("https://jurivaitmaa21.thkit.ee/"+filenamefromsite+".txt")