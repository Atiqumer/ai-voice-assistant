import speech_recognition as sr

def listen():
    #  Initialize the recognizer
    r = sr.Recognizer()
    
    # OPTIMIZATION: Fine-tune sensitivity
    r.energy_threshold = 300 
    r.dynamic_energy_threshold = True 
    r.pause_threshold = 0.8  

    with sr.Microphone() as source:
        print("\n[Alexa] Listening...")
        
        # Calibration (Essential for accuracy)
        r.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            # 3. Listen with a timeout so it doesn't wait forever
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("[Alexa] Recognizing...")
            
            # 4. Transcription
            # Changed language to 'en-in' for better Indian accent support if needed
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query.lower() # Return lowercase for easier 'if' checks later

        except sr.WaitTimeoutError:
            print("[System] Listening timed out. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("[System] Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"[System] API error; {e}")
            return None
        except Exception as e:
            print(f"[System] Unexpected error: {e}")
            return None

if __name__ == "__main__":
    result = listen()
    if result:
        print(f"Final Output: {result}")