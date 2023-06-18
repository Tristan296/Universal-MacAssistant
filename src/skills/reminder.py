import subprocess
from datetime import datetime, timedelta

import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.voice_assistant import VoiceAssistant

class Reminder:
    def __init__(self, voice_assistant):
        self.voice_assistant = voice_assistant
    
    def create_reminder_in_app(self, reminder_text):
        script = f'tell application "Reminders" to make new reminder with properties {{name:"{reminder_text}"}}'
        subprocess.run(["osascript", "-e", script])
        
    def set_reminder(self):
        print("What should I remind you about?")
        reminder = self.voice_assistant.listen()

        self.voice_assistant.speak("Alright, I will create a reminder for that.")

        # Execute the script via shell to create a new reminder in the Apple Reminders app
        self.create_reminder_in_app(reminder)

if __name__ == "__main__": 
    voice_assistant = VoiceAssistant()
    reminder = Reminder(voice_assistant)
    reminder.set_reminder()
