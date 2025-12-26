# AI Voice Assistant 🎙️

A lightweight, Python-based voice assistant that uses OpenAI's GPT models (via OpenRouter) for intelligence, Google Speech-to-Text for listening, and offline/online TTS engines for speaking.

## ✨ Features
- **Wake Word Detection:** Responds when it hears "Alexa".
- **AI Brain:** Powered by `Gemini 2.0 Flash` (via OpenRouter) for fast, intelligent responses.
- **Dynamic Listening:** Calibrates for ambient noise to work in different environments.
- **Fast Responses:** Optimized to provide concise, voice-friendly answers.
- **Secure:** Uses environment variables (`.env`) to keep API keys safe.

## 🛠️ Built With
- **Python 3.13+**
- [OpenRouter API](https://openrouter.ai/) - Access to various LLMs (Gemini, Llama, etc.)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - For capturing audio input
- [gTTS](https://pypi.org/project/gTTS/) / [pyttsx3](https://pypi.org/project/pyttsx3/) - For text-to-speech output
- [Pygame](https://www.pygame.org/) - For audio management

## 🚀 Getting Started

### Prerequisites
- Python installed on your system.
- An API key from [OpenRouter](https://openrouter.ai/).

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Atiqumer/ai-voice-assistant.git](https://github.com/Atiqumer/ai-voice-assistant.git)
   cd ai-voice-assistant

2. **Create and activate a virtual environment:**
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


2. **install dependencies**
pip install -r requirements.txt


## 🚀 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
