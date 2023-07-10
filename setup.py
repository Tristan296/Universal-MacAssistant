from setuptools import setup

setup(
    name='IntelliVoiceGPT',
    version='1.0',
    description='IntelliVoiceGPT project',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['src'],
    install_requires=[
        'numpy',
        'sounddevice',
        'scipy',
        'gTTS',
        'tempfile',
        'python-dotenv',
        'pyaudio',
        'SpeechRecognition'
    ],
)
