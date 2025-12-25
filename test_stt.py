import speech_recognition as sr

def listen():
    # Initialize the recognizer
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... say something!")
        # Adjust for ambient noise to make it more accurate
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # We use Google's free web search API for the transcription
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        return query
    except Exception as e:
        print("Sorry, I didn't catch that. Could you repeat?")
        return None

if __name__ == "__main__":
    listen()