import datetime
import speedtest
import os
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from extras.loading_logo import Loader
from core.voice_assistant import VoiceAssistant


class InternetSpeed:
    def __init__(self, voice_assistant, speed_history):
        self.voice_assistant = voice_assistant
        self.speed_history = speed_history
        self.speed_history.load_history()

    def download(self):
        loader = Loader("Testing download...").start()
        internet = speedtest.Speedtest()
        download_speed = internet.download()
        download_mbs = round(download_speed / (10**6), 2)
        loader.stop()
        output = f"Your download speed is {download_mbs} megabits per second."
        print(output)
        self.voice_assistant.speak(output)
        result = SpeedResult(datetime.datetime.now(), download_mbs, 0, 0)
        self.speed_history.add_result(result)

    def upload(self):
        loader = Loader("Testing upload...").start()
        internet = speedtest.Speedtest()
        upload_speed = internet.upload()
        upload_mbs = round(upload_speed / (10**6), 2)
        loader.stop()
        output = f"Your upload speed is {upload_mbs} megabits per second."
        print(output)
        self.voice_assistant.speak(output)
        result = SpeedResult(datetime.datetime.now(), 0, upload_mbs, 0)
        self.speed_history.add_result(result)

    def ping(self):
        loader = Loader("Testing latency...").start()
        internet = speedtest.Speedtest()
        servernames = []
        internet.get_servers(servernames)
        ping = internet.results.ping
        loader.stop()
        output = f"Your latency is {ping} milliseconds."
        print(output)
        self.voice_assistant.speak(output)
        result = SpeedResult(datetime.datetime.now(), 0, 0, ping)
        self.speed_history.add_result(result)

    def run(self):
        while True:
            prompt =  "Do you want to check your latency, download speed, upload speed or view past results?"
            print(prompt)
            self.voice_assistant.speak(prompt)
            choice = self.voice_assistant.listen().lower()
            if "download" in choice:
                self.download()
            elif "upload" in choice:
                self.upload()
            elif "ping" in choice or "latency" in choice:
                self.ping()
            elif "history" in choice or "results" in choice:
                self.speed_history.load_history()
                self.speed_history.display_history()
            else:
                print(
                    "It seems that you haven't picked one of the choices. Please try again."
                )


class SpeedHistory:
    def __init__(self, file_path):
        self.file_path = file_path
        self.history = []
        self.load_history()

    def add_result(self, result):
        self.history.append(result)
        self.save_history()

    def save_history(self):
        with open(self.file_path, "w") as file:
            json.dump(
                self.history,
                file,
                default=lambda o: o.__str__() if isinstance(o, datetime.datetime) else o.__dict__,
                indent=4,
            )
    def load_history(self):
        try:
            with open(self.file_path, 'r') as file:
                contents = file.read()
                if contents:
                    self.history = json.loads(contents, object_hook=self._deserialize_result)
                else:
                    self.history = []
        except (FileNotFoundError, json.JSONDecodeError):
            self.history = []

    @staticmethod
    def _deserialize_result(json_obj):
        if "timestamp" in json_obj:
            timestamp = datetime.datetime.strptime(
                json_obj["timestamp"], "%Y-%m-%d %H:%M:%S.%f"
            )
            return SpeedResult(
                timestamp, json_obj["download_speed"], json_obj["upload_speed"], json_obj["ping_latency"]
            )
        return json_obj
    
    def display_history(self):
        if self.history:
            print("Speed Test History:")
            for result in self.history:
                print(f"Timestamp: {result.timestamp}")
                print(f"Download Speed: {result.download_speed} Mbps")
                print(f"Upload Speed: {result.upload_speed} Mbps")
                print(f"Ping Latency: {result.ping_latency} ms")
                print("------------------------")
        else:
            print("No speed test history available.")


class SpeedResult:
    def __init__(self, timestamp, download_speed, upload_speed, ping_latency):
        self.timestamp = timestamp
        self.download_speed = download_speed
        self.upload_speed = upload_speed
        self.ping_latency = ping_latency


if __name__ == "__main__":
    voice_assistant = VoiceAssistant()
    history_file_path = "speed_history.json"
    speed_history = SpeedHistory(history_file_path)
    speed_test = InternetSpeed(voice_assistant, speed_history)
    speed_test.run()
