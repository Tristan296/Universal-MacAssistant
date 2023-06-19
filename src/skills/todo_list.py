import subprocess
import time 
import pyautogui
import platform
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.voice_assistant import VoiceAssistant 

class todoList:
    def __init__(self, voice_assistant):
        self.voice_assistant = voice_assistant
    
    def create_todo_list(self):
        todo_list = []
        self.voice_assistant.speak("Let's create a to-do list. Please say the tasks one by one. Say 'done' when you're finished.")

        while True:
            task = self.voice_assistant.listen()
            
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
                
if __name__ == "__main__": 
    voice_assistant = VoiceAssistant()
    reminder = todoList(voice_assistant)
    reminder.create_todo_list()