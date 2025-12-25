from gtts import gTTS
import pygame
import os
import time

def speak(text):
    filename = "voice.mp3"
    
    try:
        #  Generate Speech
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filename)

        #  Initialize Mixer with standard frequency (44100Hz)
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        
        #  Load and Play
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        #  Wait for it to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.05) # Smaller sleep for better responsiveness
        
        pygame.mixer.music.unload() 
        pygame.mixer.quit()

        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        print(f"Error in TTS: {e}")

if __name__ == "__main__":
    print("[Alexa] Speaking...")
    speak("System online. All modules are functional.")
    print("[System] Done!")