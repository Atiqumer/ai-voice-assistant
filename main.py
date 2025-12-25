import speech_recognition as sr
import webbrowser
from gtts import gTTS
import pygame
import os
import time
from datetime import datetime

# --- FUNCTION: SPEAK ---
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()
    if os.path.exists(filename):
        os.remove(filename)

# --- FUNCTION: LISTEN ---
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n(Waiting for command...)")
        r.pause_threshold = 1 # Wait for 1 second of silence before finishing
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        return ""

# --- MAIN LOOP ---
if __name__ == "__main__":
    speak("System online.")
    
    while True:
        command = listen()

        # 1. WAKE WORD LOGIC: Only proceed if "Alexa" is mentioned
        if "alexa" in command:
            
            if "hello" in command:
                speak("Hello! I am your assistant. How can I help you?")

            elif "time" in command:
                current_time = datetime.now().strftime("%I:%M %p")
                speak(f"The time is {current_time}")

            elif "open youtube" in command:
                speak("Opening YouTube.")
                webbrowser.open("https://www.youtube.com")

            elif "search google for" in command:
                # Extracts the part after 'search google for'
                search_term = command.split("search google for")[-1]
                speak(f"Searching Google for {search_term}")
                webbrowser.open(f"https://www.google.com/search?q={search_term}")

            elif "stop" in command or "exit" in command:
                speak("Goodbye, shutting down.")
                break

            else:
                speak("I heard the wake word, but I'm not sure what you want me to do.")