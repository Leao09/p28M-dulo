import os
import sys
import speech_recognition as sr
from gtts import gTTS
import playsound
# Função para converter texto em fala e reproduzir
def speak_text(text):
    tts = gTTS(text=text, lang='pt-BR')
    tts.save("videoplayback.mp3")
    playsound.playsound("videoplayback.mp3")
    os.remove("videoplayback.mp3")  # Remove o arquivo de áudio após reprodução


if __name__ == "__main__":
 frase = str(input("Digite algo para ser falado"))
 speak_text(frase)
