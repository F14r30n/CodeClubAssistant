from gtts import gTTS
from playsound import playsound
def say(phrase):
    tts = gTTS(phrase)
    tts.save('audio.mp3')
    playsound('audio.mp3')
