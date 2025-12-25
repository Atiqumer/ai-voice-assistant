import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv
import time

# --- INITIALIZATION ---
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"))

# Initialize pygame mixer ONCE at the start to save time
pygame.mixer.init()

def ask_gpt(prompt):
    try:
        # Optimization: Added a more specific system instruction
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {"role": "system", "content": "You are Alexa, a helpful AI. Keep responses brief and friendly for voice interaction. Avoid using markdown like bold or bullet points in your text."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I'm having trouble connecting to my brain. Error: {e}"

def speak(text):
    filename = "response.mp3"
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)
            
        pygame.mixer.music.unload() # Critical for file deletion
        if os.path.exists(filename):
            os.remove(filename)
    except Exception as e:
        print(f"TTS Error: {e}")

def listen():
    r = sr.Recognizer()
    # Optimization: Speed up the listening phase
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
            # Clean the command so it doesn't send "Alexa" to GPT
            clean_command = command.replace("alexa", "").strip()
            
            if not clean_command:
                speak("Yes? I'm listening.")
                clean_command = listen()

            if "stop" in clean_command or "exit" in clean_command:
                speak("Goodbye!")
                break
            
            if clean_command:
                answer = ask_gpt(clean_command)
                print(f"Alexa: {answer}")
                speak(answer)