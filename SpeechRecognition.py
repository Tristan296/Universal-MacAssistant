import time
import speech_recognition as sr
import os
import subprocess
import platform
from datetime import datetime, timedelta
import pyautogui
import openai
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import tempfile
from gtts import gTTS

mic = sr.Microphone()
r = sr.Recognizer()

class VoiceAssistant:
    """
    This class represents a voice assistant.

    Attributes:
        history (list): A list of dictionaries representing the assistant's history.

    Methods:
        listen: Records audio from the user and transcribes it.
        think: Generates a response to the user's input.
        speak: Converts text to speech and plays it.
    """

    def __init__(self):
        # Set your OpenAI API key
        openai.api_key = "your_api_key_here"
        # Initialize the assistant's history
        self.history = [
            {
                "role": "system",
                "content": "You are a helpful assistant. The user is english. Only speak english.",
            }
        ]

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
        # Send the conversation to the GPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.history, temperature=0.5
        )
        # Extract the assistant's response from the API response
        message = dict(response.choices[0])["message"]["content"]
        self.history.append({"role": "system", "content": message})
        print("Assistant: ", message)
        return message

    def speak(self, text):
         # Convert text to speech using gTTS
        tts = gTTS(text=text, lang='en')
        
        # Save the speech as a temporary audio file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            tts.save(temp_audio.name)
        
        # Play the audio file through the speakers
        subprocess.run(["afplay", temp_audio.name])
    

def create_reminder_in_app(reminder_text, reminder_datetime):
    script = f'tell application "Reminders" to make new reminder with properties {{name:"{reminder_text}", due date: date ("{reminder_datetime.strftime("%Y-%m-%dT%H:%M:%S")}"), remind me date: date ("{reminder_datetime.strftime("%Y-%m-%dT%H:%M:%S")}")}}'
    subprocess.run(["osascript", "-e", script])


def set_reminder():
    assistant.speak("What should I remind you about?")
    reminder = recognize_speech_from_mic(r, mic)

    assistant.speak("When did you want to be reminded?")
    reminder_time = recognize_speech_from_mic(r, mic)

    try:
        time_str = reminder_time.lower()  # Convert to lowercase for case insensitivity
        time_str = time_str.replace(".", "")  # Remove periods in the time string

        if "p.m." in time_str or "pm" in time_str:
            hour, minute = map(int, time_str.split()[0].split(":"))
            if hour != 12:
                hour += 12
        elif "a.m." in time_str or "am" in time_str:
            hour, minute = map(int, time_str.split()[0].split(":"))
            if hour == 12:
                hour = 0
        else:
            raise ValueError("Invalid time format")

        now = datetime.now()
        reminder_datetime = now.replace(
            hour=hour, minute=minute, second=0, microsecond=0
        )
        if now > reminder_datetime:
            reminder_datetime = reminder_datetime + timedelta(
                days=1
            )  # Adjust the reminder time

        print(
            f"Alright, I will remind you about '{reminder}' at {hour:02d}:{minute:02d}."
        )

        # Execute the script via shell to create a new reminder in the Apple Reminders app
        create_reminder_in_app(reminder, reminder_datetime)

    except ValueError:
        print("Sorry, I couldn't understand the time you provided. Please try again.")


def create_todo_list():
    todo_list = []
    assistant.speak("Let's create a to-do list. Please say the tasks one by one. Say 'done' when you're finished.")

    while True:
        task = assistant.listen()
        
        if "done" in task.strip().lower():
            break

        todo_list.append(task)
        print(f"Added: {task}")

    print("Saving to notes app...")
    subprocess.call(["open", "-b", "com.apple.Notes"])  # open Apple Notes app
    time.sleep(1.5)
    pyautogui.hotkey("command", "n")
    pyautogui.hotkey("command", "shift", "l")
    for task in todo_list:
        if platform.system() == "Darwin":  # macOS
            pyautogui.write(task, interval=0.1)
            pyautogui.hotkey("return")
        elif platform.system() == "Windows":
            os.system("notepad")

def search_web():
    # Implement your web search functionality here
    pass


def show_help():
    # Implement your help functionality here
    pass

if __name__ == "__main__":
    assistant = VoiceAssistant()

    while True:
        text = assistant.listen()

        if "goodbye" in text.strip().lower() or "bye" in text.strip().lower():
            print("Assistant: Goodbye! Have a great day!")
            assistant.speak("Goodbye! Have a great day!")
            break
        
        if "reminder" in text.strip().lower():
            set_reminder()
        elif "to-do" in text.strip().lower() or "todo" in text.strip().lower() or "list" in text.strip().lower():
            create_todo_list()
        elif "search" in text.strip().lower():
            search_web()
        elif "help" in text.strip().lower():
            show_help()
        elif "exit" in text.strip().lower() or "quit" in text.strip().lower():
            print("Goodbye")
            break
        
        response = assistant.think(text)
        assistant.speak(response)
