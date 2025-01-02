# Alexa Voice Assistant in Python

A simple Python-based voice assistant that responds to Arabic voice commands and can perform actions like telling the time, opening applications, and browsing websites.

## Features
- **Voice Recognition**: Uses Google Speech Recognition to understand Arabic voice commands.
- **Text-to-Speech**: Responds using Arabic audio generated with Google Text-to-Speech (gTTS).
- **Perform Actions**:
  - Tell the current time in Arabic.
  - Open and close applications like Google Chrome and Visual Studio Code.
  - Search Wikipedia and Google.

## Requirements
- Python 3.6 or higher
- Libraries:
  - `playsound`
  - `os`
  - `webbrowser`
  - `gTTS`
  - `speech_recognition`
  - `pyautogui`
  - `time`

Install the required libraries using pip:
```bash
pip install playsound gtts SpeechRecognition pyautogui

