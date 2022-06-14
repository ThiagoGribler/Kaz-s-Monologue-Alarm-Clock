from pygame import mixer
import time

#Definir Variável do Tempo Atual
#Define Actual Time Variable
tagr=time.localtime()
timestring=time.strftime("%H:%M", tagr)

#Input do Usuário
#User's Input
myhour=input("Hours: ")
myminute=input("Minutes: ")
mytime=myhour+":"+myminute

#Loop
while mytime != timestring:
    tagr=time.localtime()
    timestring=time.strftime("%H:%M", tagr)

#Tocar o Alarme
#Play Alarm Sound
mixer.init()
mixer.music.load("C:/Users/thiag/Desktop/My Python Workspace/1-Projetos/Kaz Alarm Clock/KAZ.mp3")
mixer.music.play()
while mixer.music.get_busy():  
    time.sleep(1)

print("Hang in there Kaz, just 5 more minutes")
