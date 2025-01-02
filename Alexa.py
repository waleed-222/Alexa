import playsound
import os
import webbrowser
from gtts import gTTS
import speech_recognition as sr
import datetime
import pyautogui
from time import sleep

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")  # 24-hour format

    # Arabic time message
    time_message = f"الوقت الحالي هو {current_time}"
    alexia.speak(time_message)
    

def close_vs_code():
    pyautogui.click(1455,132)
def Exit_vs_code():
    location = None

    # Locate the image and click it
    while location is None:
        location = pyautogui.locateOnScreen('Exit.png', confidence=0.9)
        sleep(2)  # Sleep to avoid excessive CPU usage

    pyautogui.click(location)  # Click on the located image



class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()  # Use self.recognizer to make it accessible in all methods

    def record_audio(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)  # Dynamically adjust for noise
            try:
                # Set a timeout for listening and a phrase limit for processing
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=8)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for speech.")
                return None
        return audio

    def recognize_speech(self, audio):
        if audio is None:
            return ""
        try:
            text = self.recognizer.recognize_google(audio, language="ar-EG")
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that!")
        except sr.RequestError:
            print("Sorry, there was an error processing your request")
        return ""

    def speak(self, audios):
        tts = gTTS(text=audios, lang="ar", slow=False)
        audio_file = "audio.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audios)
        os.remove(audio_file)


def search_words_in_string(word_list, text):
    # Find words from word_list in the string
    found_words = [word for word in word_list if word in text]
    return len(found_words) != 0


def respond(voice_data, alexia):
    if search_words_in_string(["اسمى", "اسم", "الاسم"], voice_data):
        alexia.speak("مرحبا بك بشمهندس وليد")

    if search_words_in_string(["افتح جوجل", "افتح جوجل"], voice_data):
        webbrowser.open("https://www.google.com")

    if search_words_in_string(["افتح فيجوال ستديو", "افتح فيجوال ستوديو"], voice_data):
        os.system("code")

    if search_words_in_string(["افتح ويكيبيديا", "افتح ويكيبديا"], voice_data): 
        webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")
    
    if search_words_in_string(["االساعه كام","الساعه كام","الساعه كم"],voice_data):
        tell_time()
    
    if search_words_in_string(["شكرا","شوكرن","شكرن"],voice_data):
        alexia.speak("عفواّ")

    

    if search_words_in_string(["اقفل فيجوال ستوديو", "اقفلل فيجوال ستوديو"], voice_data):
        alexia.speak("حسناّ")
        close_vs_code()

    elif search_words_in_string(["اقفل جوجل", "اقفل جوجل"], voice_data):
        alexia.speak("حسناّ")
        Exit_vs_code()
       
        close_vs_code()
    elif search_words_in_string(["اقفل"," اقفل","اقفلل"],voice_data):
        alexia.speak("وداعاّ")
        Exit_vs_code()

    


if __name__ == "__main__":
    os.system("chcp 65001")  # Set UTF-8 encoding for CMD
    alexia = VoiceAssistant()
    while True:
        voice_note = alexia.record_audio()
        recognized_text = alexia.recognize_speech(voice_note)
        if recognized_text:
            respond(recognized_text, alexia)
