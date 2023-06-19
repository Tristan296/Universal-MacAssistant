import speedtest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.voice_assistant import VoiceAssistant

class InternetSpeed:
    def __init__(self, voice_assistant):
        self.voice_assistant = voice_assistant
      
    def download(self):
        st = speedtest.Speedtest()
        self.voice_assistant.speak(st.download())
    
    def upload(self):
        st = speedtest.Speedtest()
        self.voice_assistant.speak(st.upload())
        
    def ping(self):
        st = speedtest.Speedtest()
        servernames = []  
        st.get_servers(servernames)  
        self.voice_assistant.speak(st.results.ping())
        
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