# IntelliVoiceAI

A Personal Assistant for Linux, MacOS and Windows

IntelliVoiceAI is a simple voice assistant developed using Python. It uses OpenAI's GPT-3 API for language understanding and response generation, SoundDevice for recording audio, and gTTS for text-to-speech conversion. IntelliVoiceAI incorporates integration with various applications such as creating reminders in the Reminders app and generating to-do lists in the Notes app. 


## Features
* Voice Recognition: Listens to user's voice commands and transcribes them to text.
* AI Conversation: Communicates with users in natural language using OpenAI's GPT-3 model.
* Text-to-Speech: Converts the assistant's text responses into voice and speaks them out.
* Reminders: Create reminders in the reminders app
* To-do-list: Create to do lists in the notes app
* Check internet speed and ping

## Requirements
### Install the dependencies 
```

# Windows and Linux:
pip install numpy openai sounddevice scipy gtts

# MacOS
sudo pip3 install numpy openai sounddevice scipy gtts

```

## Usage
1. Download Repository folder or git clone https://github.com/Tristan296/IntelliVoiceAI.git
2. replace `openai.api_key = "your_api_key_here"` with API key
3. Open terminal and run `python3 main.py`
4. Choose from the available prompts or talk to ChatGPT

## Contribution
Feel free to fork this project, make some changes, and submit a pull request. All contributions are welcome!
