import subprocess
import time 
import pyautogui
import platform
import os, sys
from core.voice_assistant import assistant

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class todoList:
    def __init__(self):
        pass
    
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
