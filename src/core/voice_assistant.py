import numpy as np
import openai
import sounddevice as sd
from scipy.io import wavfile
import tempfile
import subprocess
from gtts import gTTS


class VoiceAssistant:
    def __init__(self):
        # Set your OpenAI API key
        openai.api_key = "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"
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

    def run(self):
        while True:
            user_input = self.listen()
            response = self.think(user_input)
            self.speak(response)

