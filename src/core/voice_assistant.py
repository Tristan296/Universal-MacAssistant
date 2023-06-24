import numpy as np
import openai
import sounddevice as sd
from scipy.io import wavfile
import tempfile
import subprocess
from gtts import gTTS
import os, sys
from dotenv import load_dotenv

from langchain.agents import initialize_agent
from langchain.llms import OpenAIChat
from langchain.agents import load_tools, AgentType, initialize_agent
from langchain.llms import OpenAI
from src.core.commands import (
    chrome_click_on_link,
    chrome_get_the_links_on_the_page,
    chrome_open_url,
    chrome_read_the_page,
    computer_applescript_action,
)

# load environment variables
load_dotenv()


class VoiceAssistant:
    def __init__(self):
        llm = OpenAIChat(openai_api_key="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", model="gpt-3.5-turbo-0613", temperature=0.5)  # type: ignore
        self.tools = load_tools(
            ["serpapi", "llm-math"],
            llm=llm,
            serpapi_api_key="your_serpapi_api_key_here",
        )

        self.history = [
            {
                "role": "system",
                "content": "You are a helpful assistant. The user is English. Only speak English.",
            }
        ]
        tools = [
            computer_applescript_action,
            chrome_open_url,
            chrome_get_the_links_on_the_page,
            chrome_read_the_page,
            chrome_click_on_link,
        ]
        self.agent = initialize_agent(
            tools, llm=llm, initialize_agent="zero-shot-react-description", verbose=True
        )

        self.commands = {
            "open chrome": self.open_chrome,
            "get links": self.get_links,
            "read page": self.read_page,
            "click link": self.click_link,
        }

    def listen(self):
        """
        Records audio from the user and transcribes it.
        """
        print("Listening...")
        # Record the audio
        duration = 3  # Record for 3 seconds
        fs = 44100  # Sample rate

        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
        sd.wait()

        # Save the NumPy array to a temporary wav file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
            wavfile.write(temp_wav_file.name, fs, audio)

            # Use the temporary wav file in the OpenAI API
            transcript = openai.Audio.transcribe("whisper-1", temp_wav_file)

        print(f"User: {transcript['text']}")
        return transcript["text"]

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
        # Convert text to speech using the appropriate text-to-speech functionality
        tts = gTTS(text=text, lang="en", slow=False)

        # Save the speech as a temporary audio file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            tts.save(temp_audio.name)

        # Play the audio file through the speakers
        subprocess.run(["afplay", temp_audio.name])

    def open_chrome(self, args):
        # Extract the URL from the arguments
        url = args.strip()
        self.agent.run(chrome_open_url, url)

    def get_links(self, args):
        self.agent.run(chrome_get_the_links_on_the_page)

    def read_page(self, args):
        self.agent.run(chrome_read_the_page)

    def click_link(self, args):
        # Extract the link index from the arguments
        index = int(args)
        self.agent.run(chrome_click_on_link, index)

    def run(self):
        while True:
            print("""Initialising ChatGPT and Text-To-Speech...\n""")
            print("Welcome to IntelliVoiceAI! How can I assist you? If unsure say help")

            text = self.listen()
            formattedText = text.strip().lower()

            if "open chrome" in formattedText:
                self.commands["open chrome"](
                    formattedText.replace("open chrome", "").strip()
                )
                return

            if "get links" in formattedText:
                self.commands["get links"]("")
                return

            if "read page" in formattedText:
                self.commands["read page"]("")
                return

            if "click link" in formattedText:
                link_index = formattedText.replace("click link", "").strip()
                self.commands["click link"](link_index)
                return
            if "goodbye" in formattedText or "bye" in formattedText:
                print("Assistant: Goodbye! Have a great day!")
                self.speak("Goodbye! Have a great day!")
                break

            if "list" in formattedText or "note" in formattedText:
                from src.skills.todo_list import todoList

                todolist = todoList(self)
                todolist.create_todo_list()
                break

            if "reminder" in formattedText:
                from src.skills.reminder import Reminder

                reminder = Reminder(self)
                reminder.set_reminder()
                break

            if "speed" in formattedText or "internet speed" in formattedText:
                from src.skills.internet_test import InternetSpeed, SpeedHistory

                history_file_path = "speed_history.json"
                speed_history = SpeedHistory(history_file_path)
                speed = InternetSpeed(self, speed_history)
                speed.run()

            if "weather" in formattedText:
                from src.skills.weather import Weather
            if "exit" in formattedText or "quit" in formattedText:
                print("Goodbye")
                break

            response = self.think(text)
            self.speak(response)
