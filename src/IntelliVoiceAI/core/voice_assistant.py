import time
import subprocess
import platform
from datetime import datetime, timedelta

from voice_operations import VoiceOperations
from reminder import set_reminder
import help
import web_searcher 

if __name__ == "__main__":
    assistant = VoiceOperations()

    while True:
        text = assistant.listen()

        if "goodbye" in text.strip().lower() or "bye" in text.strip().lower():
            print("Assistant: Goodbye! Have a great day!")
            assistant.speak("Goodbye! Have a great day!")
            break

        if "reminder" in text.strip().lower():
            set_reminder()
        elif "search" in text.strip().lower():
            search_web() #TODO 
        elif "help" in text.strip().lower():
            show_help() #TODO
        elif "exit" in text.strip().lower() or "quit" in text.strip().lower():
            print("Goodbye")
            break
        else:
            response = assistant.think(text)
            assistant.speak(response)