# IntelliVoiceGPT

A Personal Assistant for Linux, MacOS and Windows

IntelliVoiceGPT is a simple voice assistant developed using Python. It uses OpenAI's GPT-3 API for language understanding and response generation, SoundDevice for recording audio, and gTTS for text-to-speech conversion. IntelliVoiceAI incorporates integration with various applications such as creating reminders in the Reminders app and generating to-do lists in the Notes app. 


## Features
* **Voice Recognition**: Listens to user's voice commands and transcribes them to text.
* **AI Conversation**: Communicates with users in natural language using OpenAI's GPT-3 model.
* 
* **Text-to-Speech**: Converts the assistant's text responses into voice and speaks them out.
* **Reminders**: Create reminders in the reminders app
* **To-do-list**: Create to do lists in the notes app
* **Internet Statistics**: Check internet speed and ping
* **Internet History**: Check previous internet results
* **Weather**: Get several weather metrics in chosen city

## Requirements
### Install the dependencies 
```

# Windows and Linux:
pip install numpy openai sounddevice scipy gtts

# MacOS
sudo pip3 install numpy openai sounddevice scipy gtts

```

## Usage
1. Download Repository folder or git clone https://github.com/Tristan296/IntelliVoiceGPT
2. replace `openai.api_key = "your_api_key_here"` with API key
3. Open terminal and run `python3 main.py`
4. Choose from the available prompts or talk to ChatGPT

### NOTE: Using the Weather function (OpenWeather API):
1. Create an account https://home.openweathermap.org/users/sign_in
2. Visit https://home.openweathermap.org/api_keys and generate an API key
3. Copy key and add your unique key```openweather_api_key = "API_key_here"```

The way the default prompt works is that if the user says something that starts with the trigger words, IntelliVoiceGPT will act as an Assistant to perform various functions. If the user says something that does not contain the trigger words, the assistant will ask LangChain agent to handle user commands. 


https://github.com/Tristan296/IntelliVoiceGPT/assets/109927879/8878e476-83a5-4a6c-8c65-63289f3c1c5a


## Contribution
Feel free to fork this project, make some changes, and submit a pull request. All contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
