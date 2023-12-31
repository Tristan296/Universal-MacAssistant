import time
import os
import sys
import subprocess
import tempfile
import re
import speech_recognition as sr
from gtts import gTTS
from dotenv import load_dotenv


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from skills.apple_scripts import ask_siri, open_file
from skills.help import help
load_dotenv()

class VoiceAssistant:
    def __init__(self):
      pass

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
            transcript = recognizer.recognize_sphinx(audio)
            print(f"User: {transcript}")
            return transcript
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""

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
            print("\n" * 30, """Initialising MacAssistant...\n""")
            print("How can I assist you? If unsure, say help")

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

            elif "help" in formattedText:
                help()

            elif (("open" in formattedText and "app" in formattedText) or "reminder" in formattedText):
                ask_siri(formattedText)

            elif re.search(r"(increase|decrease|reduce) brightness", formattedText) or re.search(
                    r"(increase|decrease|reduce) volume", formattedText):
                ask_siri(formattedText)

            elif re.search(r"(wifi|bluetooth|settings)", formattedText):
                ask_siri(formattedText)

            elif "open" in formattedText and "file" in formattedText:
                open_file(formattedText)

            elif "exit" in formattedText or "quit" in formattedText:
                print("Goodbye")
                break
