import speech_recognition as sr
from openai import OpenAI
import pygame
import os
from dotenv import load_dotenv
import time
import pyttsx3
from AppOpener import open as open_app, close as close_app
import webbrowser

# --- INITIALIZATION ---
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"))

pygame.mixer.init()

def process_command(query):
    query = query.lower()
    
    if "open" in query:
        app_name = query.replace("open", "").strip()
        print(f"Opening {app_name}...")
        open_app(app_name, match_closest=True) # match_closest handles typos
        return f"Opening {app_name} for you."
    
    elif "close" in query:
        app_name = query.replace("close", "").strip()
        print(f"Closing {app_name}...")
        # close_app can close multiple apps if comma-separated, 
        # but here we handle one at a time for simplicity
        close_app(app_name, match_closest=True)
        return f"Closing {app_name}."
    
    # Feature: Open Websites
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    
    return None # Return None if it's not a system command

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo", # Fixed model name for stability
            messages=[
                {"role": "system", "content": "You are Alexa, a helpful AI. Keep responses brief and friendly for voice interaction."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "I'm having trouble connecting to my brain."

def speak(text):
    try:
        engine = pyttsx3.init() 
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) 
        print(f"Alexa: {text}")
        engine.say(text)
        engine.runAndWait()
        engine.stop() 
    except Exception as e:
        print(f"Pyttsx3 Error: {e}")

def listen():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8 
    
    with sr.Microphone() as source:
        print("\n[Status] Waiting for 'Alexa'...")
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()
    except:
        return ""

if __name__ == "__main__":
    speak("System online.")
    
    while True:
        command = listen()

        if "alexa" in command:
            clean_command = command.replace("alexa", "").strip()
            
            if not clean_command:
                speak("Yes? I'm listening.")
                clean_command = listen()

            if "stop" in clean_command or "exit" in clean_command:
                speak("Goodbye!")
                break
            
            if clean_command:
                # 1. CHECK FOR SYSTEM COMMANDS FIRST
                system_response = process_command(clean_command)
                
                if system_response:
                    speak(system_response)
                else:
                    # 2. IF NOT SYSTEM, ASK GPT
                    answer = ask_gpt(clean_command)
                    speak(answer)