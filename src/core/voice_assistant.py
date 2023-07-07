import re
import time
import numpy as np
import openai
import sounddevice as sd
from scipy.io import wavfile
import tempfile
import subprocess
from gtts import gTTS
import os, sys
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.agents import load_tools
import speech_recognition as sr


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from skills.apple_scripts import ask_siri
from core.commands import (computer_applescript_action,
            chrome_open_url,
            chrome_get_the_links_on_the_page,
            chrome_read_the_page,
            chrome_click_on_link)

# load environment variables
load_dotenv()
class VoiceAssistant:
    def __init__(self):
        # Set your OpenAI API key
        api_key = os.environ['OPENAI_API_KEY']
        openai.api_key = api_key
        # Initialize the assistant's history
        self.history = [
            {
                "role": "system",
                "content": "You are a helpful assistant. The user is English. Only speak English.",
            }
        ]
        llm = OpenAI(temperature=0, openai_api_key=api_key) # type: ignore 
        tools = [
            computer_applescript_action,
            chrome_open_url,
            chrome_get_the_links_on_the_page,
            chrome_read_the_page,
            chrome_click_on_link
        ]
        self.agent = initialize_agent(tools, llm, initialize_agent="zero-shot-react-description", verbose=True)

    def listen(self):
        """
        Records audio from the user and transcribes it.
        """
        self.print_typing("Listening...")
        # Create a recognizer object
        recognizer = sr.Recognizer()

        # Record the audio
        duration = 5  # Record for 5 seconds

        with sr.Microphone() as source:
            audio = recognizer.record(source, duration=duration)

        try:
            # Perform speech recognition
            transcript = recognizer.recognize_google(audio)
            print(f"User: {transcript}")
            return transcript
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""

    def think(self, text):
        """
        Generates a response to the user's input.
        """
        # Add the user's input to the assistant's history
        self.history.append({"role": "user", "content": text})

        # Use the agent to generate a response
        response = self.agent.run(text)

        if isinstance(response, str):
            # Handle the case when the response is a string
            message = response
        else:
            # Extract the assistant's response from the agent output
            message = response["content"]

        self.history.append({"role": "system", "content": message})
        print("Assistant:", message)
        return message


    def speak(self, text):
        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang='en', slow=False)

        # Save the speech as a temporary audio file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            tts.save(temp_audio.name)

        # Play the audio file through the speakers
        subprocess.run(["afplay", temp_audio.name])

    
    def print_typing(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)  # Adjust the delay time as desired
        print()

    def run(self):
        while True:
            print("""Initialising ChatGPT, Text-To-Speech and LangChain...\n""")
            print("How can I assist you? If unsure say help")

            text = self.listen()
            formattedText = text.strip().lower() if isinstance(text, str) else ""

            if "goodbye" in formattedText or "bye" in formattedText:
                print("Assistant: Goodbye! Have a great day!")
                self.speak("Goodbye! Have a great day!")
                break

            elif "list" in formattedText or "note" in formattedText: 
                from src.skills.todo_list import todoList
                todolist = todoList(self)
                todolist.create_todo_list()
                break

            elif "speed" in formattedText or "internet speed" in formattedText: 
                from src.skills.internet_test import InternetSpeed, SpeedHistory
                history_file_path = "speed_history.json"
                speed_history = SpeedHistory(history_file_path)
                speed = InternetSpeed(self, speed_history)
                speed.run()
                            
            elif "weather" in formattedText:
                from src.skills.weather import Weather
                weather = Weather(self, None)
                weather.run()
            
            elif ("open" in formattedText or "reminder" in formattedText):
                ask_siri(formattedText)
            
            elif re.search(r"(increase|decrease|reduce) brightness", formattedText) or re.search(r"(increase|decrease|reduce) volume", formattedText):
                ask_siri(formattedText)
            
            elif re.search(r"(wifi|bluetooth|settings)", formattedText):
                ask_siri(formattedText)
                
            elif "exit" in formattedText or "quit" in formattedText:
                print("Goodbye")
                break

            response = self.think(text)
            self.speak(response)

