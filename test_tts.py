from gtts import gTTS
import pygame
import os
import time

def speak(text):
    # Create the audio file
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)

    # Initialize and play
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait for the sound to finish
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    # Shut down mixer so we can delete the file
    pygame.mixer.quit()
    os.remove(filename)

if __name__ == "__main__":
    print("Alexa is speaking...")
    speak("Your System is online. Hello, I am your custom assistant. How can I help you today?")
    print("Done!")