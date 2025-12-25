import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv
import time


load_dotenv()
api_key =os.getenv("OPENAI_API_KEY")
# --- INITIALIZE OPENAI ---
client = OpenAI(api_key= api_key)

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Fastest and cheapest for voice
            messages=[
                {"role": "system", "content": "You are a helpful assistant named Alexa. Keep your answers concise for voice interaction."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I'm having trouble thinking right now. {e}"

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
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()
    except:
        return ""

if __name__ == "__main__":
    speak("GPT Brain activated. I am ready.")
    
    while True:
        command = listen()

        if "alexa" in command:
            # If you say "stop", it exits
            if "stop" in command or "exit" in command:
                speak("Goodbye!")
                break
            
            # For everything else, ask GPT!
            answer = ask_gpt(command)
            print(f"Alexa: {answer}")
            speak(answer)