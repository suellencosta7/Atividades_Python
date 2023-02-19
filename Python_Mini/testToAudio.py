#Aplicação, transforma texto em audio.
#Para funcionamento, é necessário a instalçao das bibliotecas

# pip install gtts  e  #pip install playsound

from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(
    text= 'Teste primeiro audio',
    lang = language
)

sp.save (audio)
playsound(audio)


