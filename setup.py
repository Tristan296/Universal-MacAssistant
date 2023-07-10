from setuptools import setup

setup(
    name='Universal-MacAssistant',
    version='1.0',
    description='MacAssistant project',
    author='Tristan Norbury',
    author_email='tristannorbury123@gmail.com',
    packages=['src'],
    install_requires=[
        'numpy',
        'sounddevice',
        'scipy',
        'gTTS',
        'python-dotenv',
        'pyaudio',
        'SpeechRecognition'
    ],
)
