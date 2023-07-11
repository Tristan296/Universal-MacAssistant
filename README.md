# Universal Assistant for MacOS

[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/Tristan296/82e0272a21bddb472fb3feebea622050/raw/clone.json&logo=github)](https://github.com/MShawon/github-clone-count-badge)
[![CodeQL](https://github.com/Tristan296/Universal-MacAssistant/workflows/CodeQL/badge.svg)](https://github.com/Tristan296/Universal-MacAssistant/actions?query=workflow%3ACodeQL)

![alt text](https://github.com/Tristan296/LangChain-GPT-Voice-Assistant/blob/main/assistant_logo.png)

The Universal Assistant for macOS is a powerful voice-enabled assistant that provides a range of features to enhance your productivity and accessibility on your Mac. With voice recognition, text-to-speech capabilities, and integration with Siri, this assistant aims to make your daily tasks more efficient and convenient.

## Features

* **Voice Recognition**: Listens to user's voice commands and transcribes them to text.
* **Text-to-Speech**: Converts the assistant's text responses into voice and speaks them out.
* **Reminders**: Create reminders in the reminders app
* **To-do-list**: Create to do lists in the notes app
* **Internet Statistics**: Check internet speed and ping
* **Internet History**: Check previous internet results
* **Weather**: Get real-time weather information and forecasts for your chosen city.
* **File Management**: Open any file or folder without need for manual search
* **Siri Integration**: Seamlessly integrate with Siri to perform various actions such as creating reminders, opening applications, adjusting brightness and volume, enabling or disabling Wi-Fi and Bluetooth, and searching the web.

## Usage

1. Clone this repository using git clone https://github.com/Tristan296/Universal-MacAssistant.git
2. Run python setup.py install in the terminal to install the required dependencies.
3. Open the terminal and run python3 main.py to start the assistant.
4. Choose from the available prompts to interact with the assistant and utilize its features.

## Additional Features:

**OpenWeatherMap API**: To utilize weather information, create an OpenWeatherMap account and generate an API key. Add the API key to the .env file using the format OPENWEATHER_API_KEY=your_key_here.

**Siri Integration**: Enable "Type to Siri" in the system preferences to allow Siri integration with the assistant.
 
## Example Prompts:
- "Open Safari" or "Open setup.py" to launch applications or files.
- "What is my internet speed?" to perform a speed test and obtain metrics.
- "Where is the nearest cafe?" to use Siri to find the nearest cafe.

## Contribution
Contributions to this project are welcome! Feel free to fork the project, make changes, and submit a pull request. Please refer to the CONTRIBUTING.md file for guidelines on contributing.


## TODO:

- [ ] Integrate File system tools in MacOS
- [ ] Create more AppleScripts
 - In progress

## License

This project is licensed under the MIT License - see the LICENSE file for details.
