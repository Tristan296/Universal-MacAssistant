import speedtest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from extras.loading_logo import Loader
from core.voice_assistant import VoiceAssistant

class InternetSpeed:
    def __init__(self, voice_assistant):
        self.voice_assistant = voice_assistant
      
    def download(self):
        loader = Loader("Testing download...").start()
        internet = speedtest.Speedtest()
        download_speed = internet.download()
        download_mbs = round(download_speed / (10**6), 2)
        loader.stop()
        self.voice_assistant.speak(f"Your download speed is {download_mbs} megabits per second.")
        
    def upload(self):
        loader = Loader("Testing upload...").start()
        internet = speedtest.Speedtest()
        upload_speed = internet.upload()
        upload_mbs = round(upload_speed / (10**6), 2)
        loader.stop()
        self.voice_assistant.speak(f"Your upload speed is {upload_mbs} megabits per second.")
        
    def ping(self):
        loader = Loader("Testing latency...").start()
        internet = speedtest.Speedtest()
        servernames = []
        internet.get_servers(servernames)  
        ping = internet.results.ping
        loader.stop()
        self.voice_assistant.speak(f"Your latency is {ping} milliseconds")
        
    def run(self):
        while True:
            self.voice_assistant.speak("Did you want to test download speed, upload speed, or ping?")
            choice = self.voice_assistant.listen().lower()
            if "download" in choice: 
                self.download()
                break
            elif "upload" in choice:
                self.upload()
                break
            elif "ping" in choice:
                self.ping()
                break
            else:
                print("It seems that you haven't picked one of the choices. Please try again.")


if __name__ == "__main__": 
    voice_assistant = VoiceAssistant()
    speed_test = InternetSpeed(voice_assistant)
    speed_test.run()